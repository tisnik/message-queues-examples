;
;  (C) Copyright 2020  Pavel Tisnovsky
;
;  All rights reserved. This program and the accompanying materials
;  are made available under the terms of the Eclipse Public License v1.0
;  which accompanies this distribution, and is available at
;  http://www.eclipse.org/legal/epl-v10.html
;
;  Contributors:
;      Pavel Tisnovsky
;

(ns kafka-repl.core
  (:gen-class))

(defn -main
  [& args]
  (println "Hello, World!"))

;(comment


;; vsechny potrebne jmenne prostory
(require '[jackdaw.admin :as ja])
(require '[jackdaw.client :as jc])
(require '[jackdaw.client.log :as jl])
(require '[clojure.pprint :as pp])


;; -----------------------------------------------------------------------------
;; manipulace s tematy - vytvoreni, smazani, informace, konfigurace
;; -----------------------------------------------------------------------------

;; vytvoreni noveho tematu s jednim oddilem
(let [client (ja/->AdminClient {"bootstrap.servers" "localhost:9092"})]
  (ja/create-topics! client [{:topic-name "test1"
                              :partition-count 1
                              :replication-factor 1
                              :topic-config {"cleanup.policy" "compact"}}]))


;; -----------------------------------------------------------------------------

;; vytvoreni dalsiho tematu s jednim oddilem
(let [client (ja/->AdminClient {"bootstrap.servers" "localhost:9092"})]
  (ja/create-topics! client [{:topic-name "test2"
                              :partition-count 1
                              :replication-factor 1
                              :topic-config {"cleanup.policy" "compact"}}]))


;; -----------------------------------------------------------------------------

;; vytvoreni tematu s deseti oddily
(let [client (ja/->AdminClient {"bootstrap.servers" "localhost:9092"})]
  (ja/create-topics! client [{:topic-name "test3"
                              :partition-count 10
                              :replication-factor 1
                              :topic-config {"cleanup.policy" "compact"}}]))


;; -----------------------------------------------------------------------------

;; vymazani temat test1, test2 a test3
(let [client (ja/->AdminClient {"bootstrap.servers" "localhost:9092"})]
  (ja/delete-topics! client [{:topic-name "test1"}
                             {:topic-name "test2"}
                             {:topic-name "test3"}]))


;; -----------------------------------------------------------------------------

;; vypis konfigurace brokera
(let [client (ja/->AdminClient {"bootstrap.servers" "localhost:9092"})
      configs (ja/describe-cluster client)
      id      (->> configs :controller :id)]
  (pp/pprint (ja/get-broker-config client id)))


;; -----------------------------------------------------------------------------

;; vypis konfigurace clusteru
(let [client (ja/->AdminClient {"bootstrap.servers" "localhost:9092"})]
  (pp/pprint (ja/describe-cluster client)))


;; -----------------------------------------------------------------------------

;; vypis informaci o vybranych tematech
(let [client (ja/->AdminClient {"bootstrap.servers" "localhost:9092"})]
  (pp/pprint (ja/describe-topics client [{:topic-name "test1"}
                                         {:topic-name "test2"}
                                         {:topic-name "test3"}])))


;; vypis informaci o vsech tematech
(let [client (ja/->AdminClient {"bootstrap.servers" "localhost:9092"})]
  (pp/pprint (ja/describe-topics client)))


;; -----------------------------------------------------------------------------

;; vypis konfiguraci o jednom tematu
(let [client (ja/->AdminClient {"bootstrap.servers" "localhost:9092"})]
  (pp/pprint (ja/describe-topics-configs client [{:topic-name "test1"}])))


;; vypis konfiguraci vybranych temat
(let [client (ja/->AdminClient {"bootstrap.servers" "localhost:9092"})]
  (pp/pprint (ja/describe-topics-configs client [{:topic-name "test1"}
                                                 {:topic-name "test2"}
                                                 {:topic-name "test3"}])))


;; -----------------------------------------------------------------------------
;; producent zprav
;; -----------------------------------------------------------------------------

;; konfigurace producenta zprav
(def producer-config
  {"bootstrap.servers" "localhost:9092"
   "key.serializer" "org.apache.kafka.common.serialization.StringSerializer"
   "value.serializer" "org.apache.kafka.common.serialization.StringSerializer"
   "acks" "all"
   "client.id" "foo"})


;; poslani jedine zpravy
(with-open [producer (jc/producer producer-config)]
  (let [record-metadata (jc/produce! producer {:topic-name "test1"} "1" "Hello, Kafka!")]
    (pp/pprint @record-metadata)))


;; poslani 100 zprav
(with-open [producer (jc/producer producer-config)]
  (doseq [i (range 1 101)]
    (let [key (str i)
          value (str "Message #" i)]
      (println "Publishing message with key '" key "' and value '" value "'")
      (let [record-metadata (jc/produce! producer {:topic-name "test1"} key value)]
        (pp/pprint @record-metadata)))))


;; -----------------------------------------------------------------------------
;; konzument zprav
;; -----------------------------------------------------------------------------

;; konfigurace konzumenta zprav
(def consumer-config
  {"bootstrap.servers" "localhost:9092"
   "key.deserializer" "org.apache.kafka.common.serialization.StringDeserializer"
   "value.deserializer" "org.apache.kafka.common.serialization.StringDeserializer"
   "auto.offset.reset" "earliest"
   "group.id"  "group-A"})

   #"auto.offset.reset" "none"


;; start konzumenta
(with-open [consumer (-> (jc/consumer consumer-config)
                         (jc/subscribe [{:topic-name "test1"}]))]
  (doseq [{:keys [key value partition timestamp offset]} (jl/log consumer 10)]
    (println "key: " key)
    (println "value: " value)
    (println "partition: " partition)
    (println "timestamp: " timestamp)
    (println "offset: " offset)))


;; -----------------------------------------------------------------------------
;; zpravy s daty ve formatu EDN
;; -----------------------------------------------------------------------------

(require '[jackdaw.serdes.edn])
(require '[jackdaw.serdes.edn2])

;; na zacatku pro jistotu vymazeme tema "edn"
(let [client (ja/->AdminClient {"bootstrap.servers" "localhost:9092"})]
  (ja/delete-topics! client [{:topic-name "edn"}]))


;; vytvoreni noveho tematu akceptujiciho zpravy ve formatu EDN
(let [client (ja/->AdminClient {"bootstrap.servers" "localhost:9092"})
      input-topic {:topic-name "edn"
                   :partition-count 1
                   :replication-factor 1
                   :key-serde (jackdaw.serdes.edn/serde)
                   :value-serde (jackdaw.serdes.edn/serde)
                   :topic-config {"cleanup.policy" "compact"}}]
  (ja/create-topics! client [input-topic]))


;; konfigurace producenta zprav ve formatu EDN
(def producer-config
  {"bootstrap.servers" "localhost:9092"
   ;"default.key.serde" "jackdaw.serdes.EdnSerde"
   ;"default.value.serde" "jackdaw.serdes.EdnSerde"
   ;"key.serializer" "org.apache.kafka.common.serialization.StringSerializer"
   ;"value.serializer" "org.apache.kafka.common.serialization.StringSerializer"
   "acks" "all"
   "client.id" "foo"})


;; konfigurace serializatoru a deserializatoru
(def producer-serde-config
  {:key-serde   (jackdaw.serdes.edn/serde)
   :value-serde (jackdaw.serdes.edn/serde)})


;; poslani jedine zpravy
(with-open [producer (jc/producer producer-config producer-serde-config)]
  (let [topic {:topic-name "edn"}
        message-key {:id 0
                     :foo "foo"}
        message-value {:foo "foo"
                       :bar :bar
                       :baz 42
                       :values (range 10) }
        record-metadata (jc/produce! producer topic message-key message-value)]
    (pp/pprint @record-metadata)))


;; poslani 100 zprav
(with-open [producer (jc/producer producer-config producer-serde-config)]
  (doseq [i (range 1 101)]
    (let [topic {:topic-name "edn"}
          message-key {:id i
                       :foo "foo"}
          message-value {:foo "foo"
                         :bar (/ 1 i)
                         :baz i
                         :values (range i) }
          record-metadata (jc/produce! producer topic message-key message-value)]
        (pp/pprint @record-metadata))))


;; -----------------------------------------------------------------------------
;; zpravy s daty ve formatu EDN, alternativni pristup
;; -----------------------------------------------------------------------------

(require '[jackdaw.serdes])

;; na zacatku pro jistotu vymazeme tema "edn2"
(let [client (ja/->AdminClient {"bootstrap.servers" "localhost:9092"})]
  (ja/delete-topics! client [{:topic-name "edn2"}]))


;; vytvoreni noveho tematu akceptujiciho zpravy ve formatu EDN
(let [client (ja/->AdminClient {"bootstrap.servers" "localhost:9092"})
      input-topic {:topic-name "edn2"
                   :partition-count 1
                   :replication-factor 1
                   :key-serde (jackdaw.serdes/edn-serde)
                   :value-serde (jackdaw.serdes/edn-serde)
                   :topic-config {"cleanup.policy" "compact"}}]
  (ja/create-topics! client [input-topic]))


;; konfigurace producenta zprav ve formatu JSON
(def producer-config
  {"bootstrap.servers" "localhost:9092"
   "acks" "all"
   "client.id" "foo"})


;; konfigurace serializatoru a deserializatoru
(def producer-serde-config
  {:key-serde   (jackdaw.serdes/edn-serde)
   :value-serde (jackdaw.serdes/edn-serde)})


;; poslani jedine zpravy
(with-open [producer (jc/producer producer-config producer-serde-config)]
  (let [topic {:topic-name "edn2"}
        message-key {:id 0
                     :foo "foo"}
        message-value {:foo "foo"
                       :bar :bar
                       :baz 42
                       :values (range 10) }
        record-metadata (jc/produce! producer topic message-key message-value)]
    (pp/pprint @record-metadata)))


;; poslani 100 zprav
(with-open [producer (jc/producer producer-config producer-serde-config)]
  (doseq [i (range 1 101)]
    (let [topic {:topic-name "edn2"}
          message-key {:id i
                       :foo "foo"}
          message-value {:foo "foo"
                         :bar (/ 1 i)
                         :baz i
                         :values (range i) }
          record-metadata (jc/produce! producer topic message-key message-value)]
        (pp/pprint @record-metadata))))


;; -----------------------------------------------------------------------------
;; zpravy s daty ve formatu JSON
;; -----------------------------------------------------------------------------

(require '[jackdaw.serdes.json])

;; na zacatku pro jistotu vymazeme tema "json"
(let [client (ja/->AdminClient {"bootstrap.servers" "localhost:9092"})]
  (ja/delete-topics! client [{:topic-name "json"}]))


;; vytvoreni noveho tematu akceptujiciho zpravy ve formatu JSON
(let [client (ja/->AdminClient {"bootstrap.servers" "localhost:9092"})
      input-topic {:topic-name "json"
                   :partition-count 1
                   :replication-factor 1
                   :key-serde (jackdaw.serdes.json/serde)
                   :value-serde (jackdaw.serdes.json/serde)
                   :topic-config {"cleanup.policy" "compact"}}]
  (ja/create-topics! client [input-topic]))


;; konfigurace producenta zprav v JSONu
(def producer-config
  {"bootstrap.servers" "localhost:9092"
   "acks" "all"
   "client.id" "foo"})


;; konfigurace serializatoru a deserializatoru
(def producer-serde-config
  {:key-serde   (jackdaw.serdes.json/serde)
   :value-serde (jackdaw.serdes.json/serde)})


;; poslani jedine zpravy
(with-open [producer (jc/producer producer-config producer-serde-config)]
  (let [topic {:topic-name "json"}
        message-key {:id 0
                     :foo "foo"}
        message-value {:foo "foo"
                       :bar :bar
                       :baz 42
                       :values (range 10) }
        record-metadata (jc/produce! producer topic message-key message-value)]
    (pp/pprint @record-metadata)))


;; poslani 100 zprav
(with-open [producer (jc/producer producer-config producer-serde-config)]
  (doseq [i (range 1 101)]
    (let [topic {:topic-name "edn2"}
          message-key {:id i
                       :foo "foo"}
          message-value {:foo "foo"
                         :bar (/ 1 i)
                         :baz i
                         :values (range i) }
          record-metadata (jc/produce! producer topic message-key message-value)]
        (pp/pprint @record-metadata))))


;; -----------------------------------------------------------------------------
;; ETL (jednoducha kolona)
;; -----------------------------------------------------------------------------

(require '[jackdaw.serdes.json])

;; na zacatku pro jistotu vymazeme temata "input" i "output"
(let [client (ja/->AdminClient {"bootstrap.servers" "localhost:9092"})]
  (ja/delete-topics! client [{:topic-name "input"}
                             {:topic-name "output"}]))


;; vytvoreni noveho tematu "input" akceptujiciho zpravy ve formatu JSON
(let [client (ja/->AdminClient {"bootstrap.servers" "localhost:9092"})
      input-topic {:topic-name "input"
                   :partition-count 1
                   :replication-factor 1
                   :key-serde (jackdaw.serdes.json/serde)
                   :value-serde (jackdaw.serdes.json/serde)
                   :topic-config {"cleanup.policy" "compact"}}]
  (ja/create-topics! client [input-topic]))


;; vytvoreni noveho tematu "output" akceptujiciho zpravy ve formatu JSON
(let [client (ja/->AdminClient {"bootstrap.servers" "localhost:9092"})
      input-topic {:topic-name "output"
                   :partition-count 1
                   :replication-factor 1
                   :key-serde (jackdaw.serdes.json/serde)
                   :value-serde (jackdaw.serdes.json/serde)
                   :topic-config {"cleanup.policy" "compact"}}]
  (ja/create-topics! client [input-topic]))


;; konfigurace konzumenta zprav
(def consumer-config
  {"bootstrap.servers" "localhost:9092"
   "key.deserializer" "org.apache.kafka.common.serialization.StringDeserializer"
   "value.deserializer" "org.apache.kafka.common.serialization.StringDeserializer"
   "auto.offset.reset" "earliest"
   "group.id"  "group-A"})


;; konfigurace producenta zprav
(def producer-config
  {"bootstrap.servers" "localhost:9092"
   "acks" "all"
   "client.id" "foo"})


;; konfigurace serializatoru a deserializatoru
(def consumer-serde-config
  {:key-serde   (jackdaw.serdes.json/serde)
   :value-serde (jackdaw.serdes.json/serde)})


;; konfigurace serializatoru a deserializatoru
(def producer-serde-config
  {:key-serde   (jackdaw.serdes.json/serde)
   :value-serde (jackdaw.serdes.json/serde)})


;; pouze test: poslani jedine zpravy na vystup
(with-open [producer (jc/producer producer-config producer-serde-config)]
  (let [topic {:topic-name "output"}
        message-key {:id (.toString (java.util.UUID/randomUUID))}
        message-value {:result 3}
        record-metadata (jc/produce! producer topic message-key message-value)]
    (pp/pprint @record-metadata)))


;; start jednoduche pipeline
(with-open [consumer (-> (jc/consumer consumer-config consumer-serde-config)
                         (jc/subscribe [{:topic-name "input"}]))]
  (with-open [producer (jc/producer producer-config producer-serde-config)]
    (doseq [{:keys [key value partition timestamp offset]} (jl/log consumer 10)]
      (println "Incomming message:")
      (println "key: " key)
      (println "value: " value)
      (println "partition: " partition)
      (println "timestamp: " timestamp)
      (println "offset: " offset)
      (let [result (+ (:x value) (:y value)) ; vypocet vysledku
            message-key {:id (.toString (java.util.UUID/randomUUID))}
            message-value {:result result}
            record-metadata (jc/produce! producer {:topic-name "output"} message-key message-value)]
        (println "Outgoing message:")
        (pp/pprint @record-metadata)
        (println "------------------")))))


;; -----------------------------------------------------------------------------
;; ETL (jednoducha kolona se specifikovanou transformacni funkci)
;; -----------------------------------------------------------------------------

(require '[jackdaw.serdes.json])

;; na zacatku pro jistotu vymazeme temata "input" i "output"
(let [client (ja/->AdminClient {"bootstrap.servers" "localhost:9092"})]
  (ja/delete-topics! client [{:topic-name "input"}
                             {:topic-name "output"}]))


;; vytvoreni noveho tematu "input" akceptujiciho zpravy ve formatu JSON
(let [client (ja/->AdminClient {"bootstrap.servers" "localhost:9092"})
      input-topic {:topic-name "input"
                   :partition-count 1
                   :replication-factor 1
                   :key-serde (jackdaw.serdes.json/serde)
                   :value-serde (jackdaw.serdes.json/serde)
                   :topic-config {"cleanup.policy" "compact"}}]
  (ja/create-topics! client [input-topic]))


;; vytvoreni noveho tematu "output" akceptujiciho zpravy ve formatu JSON
(let [client (ja/->AdminClient {"bootstrap.servers" "localhost:9092"})
      input-topic {:topic-name "output"
                   :partition-count 1
                   :replication-factor 1
                   :key-serde (jackdaw.serdes.json/serde)
                   :value-serde (jackdaw.serdes.json/serde)
                   :topic-config {"cleanup.policy" "compact"}}]
  (ja/create-topics! client [input-topic]))


;; konfigurace konzumenta zprav
(def consumer-config
  {"bootstrap.servers" "localhost:9092"
   "key.deserializer" "org.apache.kafka.common.serialization.StringDeserializer"
   "value.deserializer" "org.apache.kafka.common.serialization.StringDeserializer"
   "auto.offset.reset" "earliest"
   "group.id"  "group-A"})


;; konfigurace producenta zprav
(def producer-config
  {"bootstrap.servers" "localhost:9092"
   "acks" "all"
   "client.id" "foo"})


;; konfigurace serializatoru a deserializatoru
(def consumer-serde-config
  {:key-serde   (jackdaw.serdes.json/serde)
   :value-serde (jackdaw.serdes.json/serde)})


;; konfigurace serializatoru a deserializatoru
(def producer-serde-config
  {:key-serde   (jackdaw.serdes.json/serde)
   :value-serde (jackdaw.serdes.json/serde)})


;; pouze test: poslani jedine zpravy na vystup
(with-open [producer (jc/producer producer-config producer-serde-config)]
  (let [topic {:topic-name "output"}
        message-key {:id (.toString (java.util.UUID/randomUUID))}
        message-value {:result 3}
        record-metadata (jc/produce! producer topic message-key message-value)]
    (pp/pprint @record-metadata)))


(defn etl
  [input-value]
  {:key {:id (.toString (java.util.UUID/randomUUID))}
   :value (* (:x input-value) (:y input-value))})


;; start jednoduche pipeline
(with-open [consumer (-> (jc/consumer consumer-config consumer-serde-config)
                         (jc/subscribe [{:topic-name "input"}]))]
  (with-open [producer (jc/producer producer-config producer-serde-config)]
    (doseq [{:keys [key value partition timestamp offset]} (jl/log consumer 10)]
      (println "Incomming message:")
      (println "key: " key)
      (println "value: " value)
      (println "partition: " partition)
      (println "timestamp: " timestamp)
      (println "offset: " offset)
      (println)
      ; vypocet vysledku s jeho poslanim do vystupniho tematu
      (let [message (etl value)
            record-metadata (jc/produce! producer {:topic-name "output"} (:key message) (:value message))]
        (println "Result:")
        (println "message" message)
        (println)
        (println "Outgoing message:")
        (pp/pprint @record-metadata)
        (println "------------------")))))


;; -----------------------------------------------------------------------------
;; ETL (streaming API)
;; -----------------------------------------------------------------------------

(require '[jackdaw.serdes.json])
(require '[jackdaw.streams :as j])

;; na zacatku pro jistotu vymazeme temata "input" i "output"
(let [client (ja/->AdminClient {"bootstrap.servers" "localhost:9092"})]
  (ja/delete-topics! client [{:topic-name "input"}
                             {:topic-name "output"}]))


;; vytvoreni noveho tematu "input" akceptujiciho zpravy ve formatu JSON
(let [client (ja/->AdminClient {"bootstrap.servers" "localhost:9092"})
      input-topic {:topic-name "input"
                   :partition-count 1
                   :replication-factor 1
                   :key-serde (jackdaw.serdes.json/serde)
                   :value-serde (jackdaw.serdes.json/serde)
                   :topic-config {"cleanup.policy" "compact"}}]
  (ja/create-topics! client [input-topic]))


;; vytvoreni noveho tematu "output" akceptujiciho zpravy ve formatu JSON
(let [client (ja/->AdminClient {"bootstrap.servers" "localhost:9092"})
      input-topic {:topic-name "output"
                   :partition-count 1
                   :replication-factor 1
                   :key-serde (jackdaw.serdes.json/serde)
                   :value-serde (jackdaw.serdes.json/serde)
                   :topic-config {"cleanup.policy" "compact"}}]
  (ja/create-topics! client [input-topic]))


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


;; transformacni funkce
(defn etl
  [[k v]]
  [k {:result (+ (:x v) (:y v))}])


;; cela pipeline (kolona)
(defn build-topology
  [builder]
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
  [app-config]
  (let [builder (j/streams-builder)
        topology (build-topology builder)
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


;; zkusime aplikaci spustit
(def app (start-app app-config))

;; a zastavit
(stop-app app)


;) ; comment
