(ns produce-messages-2.core
  (:require [jackdaw.client :as jc]
            [clojure.pprint :as pp]))

(def producer-config
  {"bootstrap.servers" "localhost:9092"
   "key.serializer" "org.apache.kafka.common.serialization.StringSerializer"
   "value.serializer" "org.apache.kafka.common.serialization.StringSerializer"
   "acks" "all"
   "client.id" "foo"})

(defn -main
  [& args]
  (with-open [producer (jc/producer producer-config)]
    (doseq [i (range 1 101)]
      (let [key (str i)
            value (str "Message #" i)]
        (println "Publishing message with key '" key "' and value '" value "'")
        (let [record-metadata (jc/produce! producer {:topic-name "test2"} key value)]
          (pp/pprint @record-metadata)))
      )))
