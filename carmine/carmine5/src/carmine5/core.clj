(ns carmine5.core
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
  (println "Storing integer value")
  (println
    (wcar*
      (carmine/set "counter" 1)))
  (println "Done")
  (println "Retrieving integer value")
  (println
    (wcar*
      (carmine/get "counter")))
  (println "Done")
  (println "Increasing and retrieving new integer value")
  (println
    (wcar*
      (carmine/incr "counter")
      (carmine/get "counter")))
  (println "Done"))
