(ns carmineF.core
  (:require [taoensso.carmine.message-queue :as car-mq]))


(def redis-connection {
  :pool {}
  :spec {
    :uri "redis://localhost@127.0.0.1:6379"}})


(defmacro wcar*
  [& body]
  `(carmine/wcar redis-connection ~@body))

(defn -main
  [& args]
  (println "Worker")

  (car-mq/worker {:spec redis-connection} "task-queue"
   {:handler (fn [{:keys [message attempt]}]
               (println "Received" message)
               {:status :success})})

  ;(car-mq/stop my-worker)
)
