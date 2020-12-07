(ns consume-messages-2.core
  (:require [jackdaw.client :as jc]
            [jackdaw.client.log :as jl]
            [clojure.pprint :as pp]))

(def consumer-config
  {"bootstrap.servers" "localhost:9092"
   "key.deserializer" "org.apache.kafka.common.serialization.StringDeserializer"
   "value.deserializer" "org.apache.kafka.common.serialization.StringDeserializer"
   "auto.offset.reset" "earliest"
   "group.id"  "group-A"})

(defn -main
  [& args]
  (with-open [consumer (-> (jc/consumer consumer-config)
                           (jc/subscribe [{:topic-name "test1"}]))]
    (doseq [{:keys [key value partition timestamp offset]} (jl/log consumer 10)]
      (println "key: " key)
      (println "value: " value)
      (println "partition: " partition)
      (println "timestamp: " timestamp)
      (println "offset: " offset))))
