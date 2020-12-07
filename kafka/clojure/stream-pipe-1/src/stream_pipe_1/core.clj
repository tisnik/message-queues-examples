(ns stream-pipe-1.core
  (:require [jackdaw.admin :as ja]
            [jackdaw.client :as jc]
            [jackdaw.client.log :as jl]
            [jackdaw.serdes.json]
            [jackdaw.streams :as j]
            [clojure.pprint :as pp]))


;; konfigurace temat
(def topic-config
  {:input
   {:topic-name "input"
    :partition-count 1
    :replication-factor 1
    :key-serde (jackdaw.serdes.json/serde)
    :value-serde (jackdaw.serdes.json/serde)}
   :output
   {:topic-name "output"
    :partition-count 1
    :replication-factor 1
    :key-serde (jackdaw.serdes.json/serde)
    :value-serde (jackdaw.serdes.json/serde)}})


;; konfigurace aplikace
(def app-config
  {"application.id" "pipe"
   "bootstrap.servers" "localhost:9092"
   "cache.max.bytes.buffering" "0"})


(defn delete-topic
  [broker-config topic]
  (try
    (let [client (ja/->AdminClient broker-config)]
      (ja/delete-topics! client [topic]))
    (catch Exception e (str "caught exception: " (.getMessage e)))))


(defn new-topic
  [broker-config topic]
  (try
    (let [client (ja/->AdminClient broker-config)]
      (ja/create-topics! client [topic]))
      (catch Exception e (str "caught exception: " (.getMessage e)))))


;; transformacni funkce
(defn etl
  [[k v]]
  [k {:result (+ (:x v) (:y v))}])


;; cela pipeline (kolona)
(defn build-topology
  [builder topic-config]
  (-> (j/kstream builder (:input topic-config))
      (j/peek (fn [[k v]]
                (println "Received message with key:   " k " and value:" v)))
      (j/map etl)
      (j/peek (fn [[k v]]
                (println "Transformed message with key:" k " and value:" v)))
      (j/to (:output topic-config)))
  builder)


;; spusteni aplikace
(defn start-app
  "Starts the stream processing application."
  [app-config topic-config]
  (let [builder (j/streams-builder)
        topology (build-topology builder topic-config)
        app (j/kafka-streams topology app-config)]
    (j/start app)
    (println "pipe is up")
    app))


;; zastaveni aplikace
(defn stop-app
  "Stops the stream processing application."
  [app]
  (j/close app)
  (println "pipe is down"))


(defn -main
  [& args]
  (let [broker-config {"bootstrap.servers" "localhost:9092"}]

    ;; na zacatku pro jistotu vymazeme temata pouzivane pipou
    (delete-topic broker-config (:input topic-config))
    (delete-topic broker-config (:output topic-config))

    ;; vytvoreni novych tamat akceptujiciho zpravy ve formatu JSON
    (new-topic broker-config (:input topic-config))
    (new-topic broker-config (:output topic-config))

    ;; spusteni kolony
    (println "Starting pipe")
    (let [app (start-app app-config topic-config)]
      (println "App:" app))))
