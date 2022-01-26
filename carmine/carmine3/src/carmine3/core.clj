(ns carmine3.core
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
  (println "Pinging Redis")
  (println
    (wcar*
      (carmine/ping)))
  (println "Done"))
