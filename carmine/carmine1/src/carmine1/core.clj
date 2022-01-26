(ns carmine1.core
  (:require [taoensso.carmine :as carmine :refer (wcar)]))


(def redis-connection {
  :pool {}
  :spec {
    :host "127.0.0.1"
    :port 6379}})


(defn -main
  [& args]
  (println "Pinging Redis")
  (println (carmine/wcar redis-connection (carmine/ping)))
  (println "Done"))
