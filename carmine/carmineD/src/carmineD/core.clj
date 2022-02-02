(ns carmineD.core
  (:require [taoensso.carmine :as carmine :refer (wcar)]
            [clojure.pprint :as pprint]))


(def redis-connection {
  :pool {}
  :spec {
    :uri "redis://localhost@127.0.0.1:6379"}})


(defmacro wcar*
  [& body]
  `(carmine/wcar redis-connection ~@body))

(defn -main
  [& args]
  (println "Listener to given channel")

  (carmine/with-new-pubsub-listener
    (:spec redis-connection)
    {"events" (fn f [event] (println "Received event" event))}
    (carmine/subscribe "events")))
