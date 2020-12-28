(ns stream-pipe-3.core
  (:require [jackdaw.admin :as ja]
            [jackdaw.client :as jc]
            [jackdaw.client.log :as jl]
            [jackdaw.serdes.json]
            [jackdaw.streams :as j]
            [clojure.pprint :as pp]
            [clojure.tools.logging :as log]))


(def topic-config
  "Konfigurace témat - vstupního i výstupního."
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


(def app-config
  "Konfigurace aplikace (ve smyslu knihovny Jackdaw)."
  {"application.id" "pipe"
   "bootstrap.servers" "localhost:9092"
   "cache.max.bytes.buffering" "0"
   "default.deserialization.exception.handler" "org.apache.kafka.streams.errors.LogAndContinueExceptionHandler"})


(defn delete-topic
  "Pomocná funkce pro smazání vybraného tématu."
  [broker-config topic]
  (try
    (log/warn "Deleting topic" (:topic-name topic))
    (let [client (ja/->AdminClient broker-config)]
      (ja/delete-topics! client [topic]))
    (catch Exception e (str "caught exception: " (.getMessage e)))))


(defn new-topic
  "Pomocná funkce pro vytvoření nového tématu."
  [broker-config topic]
  (try
    (log/warn "Creating topic" (:topic-name topic))
    (let [client (ja/->AdminClient broker-config)]
      (ja/create-topics! client [topic]))
      (catch Exception e (str "caught exception: " (.getMessage e)))))


(defn etl-1
  "Transformační funkce."
  [[k v]]
  [k {:result (+ (:x v) (:y v))}])


(defn etl-2
  "Transformační funkce."
  [[k v]]
  [k (assoc v :timestamp (str (new java.util.Date)))])


(defn build-topology
  "Definice celé pipeliny (kolony) - základ aplikace."
  [builder topic-config]
  (-> (j/kstream builder (:input topic-config))
      (j/peek (fn [[k v]]
                (log/warn "Received message with key:   " k " and value:" v)))
      (j/map etl-1)
      (j/peek (fn [[k v]]
                (log/warn "Transformed message with key:" k " and value:" v)))
      (j/map etl-2)
      (j/peek (fn [[k v]]
                (log/warn "Transformed message with key:" k " and value:" v)))
      (j/to (:output topic-config)))
  builder)


(defn start-app
  "Spuštění aplikace."
  [app-config topic-config]
  (let [builder (j/streams-builder)
        topology (build-topology builder topic-config)
        app (j/kafka-streams topology app-config)]
    (log/warn "Starting pipe")
    (j/start app)
    (log/warn "Pipe is up")
    app))


(defn stop-app
  "Zastavení aplikace."
  [app]
  (log/warn "Stopping pipe")
  (j/close app)
  (log/warn "Pipe is down"))


(defn -main
  [& args]
  (let [broker-config {"bootstrap.servers" "localhost:9092"}]

    ;; na začátku pro jistotu vymažeme témata používaná pipou
    (delete-topic broker-config (:input topic-config))
    (delete-topic broker-config (:output topic-config))

    ;; vytvoření nových témat akceptujících zprávy ve formátu JSON
    (new-topic broker-config (:input topic-config))
    (new-topic broker-config (:output topic-config))

    ;; spuštění kolony
    (log/warn "Starting application")
    (let [app (start-app app-config topic-config)]
      (log/warn "App created:" app))))
