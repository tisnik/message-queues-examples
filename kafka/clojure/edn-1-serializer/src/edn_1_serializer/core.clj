(ns edn-1-serializer.core
  (:require [jackdaw.admin :as ja]
            [jackdaw.client :as jc]
            [clojure.pprint :as pp]))

(require '[jackdaw.serdes.edn])

(defn delete-topic
  [broker-config topic-name]
  (try
    (let [client (ja/->AdminClient broker-config)]
      (ja/delete-topics! client [{:topic-name topic-name}]))
    (catch Exception e (str "caught exception: " (.getMessage e)))))

(defn new-topic
  [broker-config topic-name]
  (try
    (let [client (ja/->AdminClient broker-config)
          topic-config {:topic-name topic-name
                        :partition-count 1
                        :replication-factor 1
                        :key-serde (jackdaw.serdes.edn/serde)
                        :value-serde (jackdaw.serdes.edn/serde)
                        :topic-config {"cleanup.policy" "compact"}}]
      (ja/create-topics! client [topic-config]))
      (catch Exception e (str "caught exception: " (.getMessage e)))))

(defn produce-messages
  [broker-config topic-name messages]
  ;; konfigurace producenta zprav ve formatu EDN
  (let [producer-config (merge broker-config {"acks" "all"
                                              "client.id" "foo"})
        ; specifikace zpusobu serializace klicu i obsahu zpravy
        producer-serde-config {:key-serde   (jackdaw.serdes.edn/serde)
                               :value-serde (jackdaw.serdes.edn/serde)}]

    ;; poslani 100 zprav se serializaci klice i hodnoty
    (with-open [producer (jc/producer producer-config producer-serde-config)]
      (doseq [i (range 0 messages)]
        (let [topic {:topic-name topic-name}
              ; posilany klic
              message-key {:n i
                           :foo "foo"}
              ; posilany obsah zpravy
              message-value {:bar "bar"
                             :value i
                             :recip (/ 1 (inc i))
                             :factorial (reduce * (range 1M (inc i)))
                             :values (range i) }
              record-metadata (jc/produce! producer topic message-key message-value)]
          (pp/pprint @record-metadata))))))

(defn -main
  [& args]
  (let [broker-config {"bootstrap.servers" "localhost:9092"}
        topic-name "edn"]

    ;; na zacatku pro jistotu vymazeme tema "edn"
    (delete-topic broker-config topic-name)

    ;; vytvoreni noveho tematu akceptujiciho zpravy ve formatu EDN
    (new-topic broker-config topic-name)

    ;; poslani 100 zprav se serializaci klice i hodnoty
    (produce-messages broker-config topic-name 100)))
