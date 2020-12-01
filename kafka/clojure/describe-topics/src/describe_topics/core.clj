(ns describe-topics.core
  (:require [jackdaw.admin :as ja]
            [clojure.pprint :as pp]))

(defn -main
  [& args]
  (let [client (ja/->AdminClient {"bootstrap.servers" "localhost:9092"})]
    (pp/pprint (ja/describe-topics client [{:topic-name "test1"}
                                           {:topic-name "test3"}]))))
