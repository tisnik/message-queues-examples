(ns get-broker-config.core
  (:require [jackdaw.admin :as ja])
  (:require [clojure.pprint :as pp]))

(defn -main
  [& args]
  (let [client (ja/->AdminClient {"bootstrap.servers" "localhost:9092"})
        configs (ja/describe-cluster client)
        id      (->> configs :controller :id)]
    (pp/pprint (ja/get-broker-config client id))))
