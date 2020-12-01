(ns topic-constructor.core
  (:require [jackdaw.admin :as ja]))

(defn -main
  []
  (let [client (ja/->AdminClient {"bootstrap.servers" "localhost:9092"})]
    (ja/create-topics! client [{:topic-name "test1"
                                :partition-count 1
                                :replication-factor 1
                                :topic-config {"cleanup.policy" "compact"}}])))

