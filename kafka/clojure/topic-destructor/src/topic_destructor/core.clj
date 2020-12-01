(ns topic-destructor.core
  (:require [jackdaw.admin :as ja]))

(defn -main
  []
  (let [client (ja/->AdminClient {"bootstrap.servers" "localhost:9092"})]
    (ja/delete-topics! client [{:topic-name "test1"}
                               {:topic-name "test3"}])))
