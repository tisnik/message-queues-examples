(ns kafka-repl.core
  (:gen-class))

(defn -main
  [& args]
  (println "Hello, World!"))

(comment


;; vsechny potrebne jmenne prostory
(require '[jackdaw.admin :as ja])
(require '[jackdaw.client :as jc])
(require '[jackdaw.client.log :as jl])
(require '[clojure.pprint :as pp])


;; vytvoreni noveho tematu s jednim oddilem
(let [client (ja/->AdminClient {"bootstrap.servers" "localhost:9092"})]
  (ja/create-topics! client [{:topic-name "test1"
                              :partition-count 1
                              :replication-factor 1
                              :topic-config {"cleanup.policy" "compact"}}]))


;; vytvoreni dalsiho tematu s jednim oddilem
(let [client (ja/->AdminClient {"bootstrap.servers" "localhost:9092"})]
  (ja/create-topics! client [{:topic-name "test2"
                              :partition-count 1
                              :replication-factor 1
                              :topic-config {"cleanup.policy" "compact"}}]))


;; vytvoreni tematu s deseti oddily
(let [client (ja/->AdminClient {"bootstrap.servers" "localhost:9092"})]
  (ja/create-topics! client [{:topic-name "test3"
                              :partition-count 10
                              :replication-factor 1
                              :topic-config {"cleanup.policy" "compact"}}]))


;; vymazani temat test1, test2 a test3
(let [client (ja/->AdminClient {"bootstrap.servers" "localhost:9092"})]
  (ja/delete-topics! client [{:topic-name "test1"}
                             {:topic-name "test2"}
                             {:topic-name "test3"}]))


;; vypis konfigurace brokera
(let [client (ja/->AdminClient {"bootstrap.servers" "localhost:9092"})
      configs (ja/describe-cluster client)
      id      (->> configs :controller :id)]
  (pp/pprint (ja/get-broker-config client id)))


;; vypis konfigurace clusteru
(let [client (ja/->AdminClient {"bootstrap.servers" "localhost:9092"})]
  (pp/pprint (ja/describe-cluster client)))


;; vypis informaci o vybranych tematech
(let [client (ja/->AdminClient {"bootstrap.servers" "localhost:9092"})]
  (pp/pprint (ja/describe-topics client [{:topic-name "test1"}
                                         {:topic-name "test2"}
                                         {:topic-name "test3"}])))


;; vypis informaci o vsech tematech
(let [client (ja/->AdminClient {"bootstrap.servers" "localhost:9092"})]
  (pp/pprint (ja/describe-topics client)))


;; vypis konfiguraci o jednom tematu
(let [client (ja/->AdminClient {"bootstrap.servers" "localhost:9092"})]
  (pp/pprint (ja/describe-topics-configs client [{:topic-name "test1"}])))


;; vypis konfiguraci vybranych temat
(let [client (ja/->AdminClient {"bootstrap.servers" "localhost:9092"})]
  (pp/pprint (ja/describe-topics-configs client [{:topic-name "test1"}
                                                 {:topic-name "test2"}
                                                 {:topic-name "test3"}])))


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


) ; comment
