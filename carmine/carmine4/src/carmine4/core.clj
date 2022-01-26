(ns carmine4.core
  (:require [taoensso.carmine :as carmine :refer (wcar)]))


(def redis-connection {
  :pool {}
  :spec {
    :uri "redis://localhost@127.0.0.1:6379"}})


(defmacro wcar*
  [& body]
  `(carmine/wcar redis-connection ~@body))


(defn -main
  [& args]
  (println "Storing data")
  (println
    (wcar*
      (carmine/set "klíč" "hodnota")))
  (println "Done")
  (println "Retrieving data")
  (println
    (wcar*
      (carmine/get "klíč")))
  (println "Done"))
