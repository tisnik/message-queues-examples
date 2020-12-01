(ns describe-cluster.core
  (:require [jackdaw.admin :as ja]
            [clojure.pprint :as pp]))

(defn -main
  [& args]
  (let [client (ja/->AdminClient {"bootstrap.servers" "localhost:9092"})]
    (pp/pprint (ja/describe-cluster client))))
