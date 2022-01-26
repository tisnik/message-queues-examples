(ns carmine6.core
  (:require [taoensso.carmine :as carmine :refer (wcar)]
            [clojure.pprint :as pprint]))


(def redis-connection {
  :pool {}
  :spec {
    :uri "redis://localhost@127.0.0.1:6379"}})


(defmacro wcar*
  [& body]
  `(carmine/wcar redis-connection ~@body))


(def data {
           :boolean   true
           :nil-value nil
           :text      "Hello world!"
           :list      '(1 2 3)
           :vector    [1 2 3]
           :a-set     #{1 2 3 4}
           :map {:name    "foo"
                 :surname "bar"
                 }})

(defn -main
  [& args]
  (println "Storing data structure")
  (println
    (wcar*
      (carmine/set "value" data)))
  (println "Done")
  (println "Retrieving data structure")
  (pprint/pprint
    (wcar*
      (carmine/get "value")))
  (println "Done"))
