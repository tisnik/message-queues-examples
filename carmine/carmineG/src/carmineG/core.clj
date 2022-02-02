(ns carmineG.core
  (:require [taoensso.carmine :as carmine :refer (wcar)]
            [taoensso.carmine.message-queue :as car-mq]))


(def redis-connection {
  :pool {}
  :spec {
    :uri "redis://localhost@127.0.0.1:6379"}})


(defmacro wcar*
  [& body]
  `(carmine/wcar redis-connection ~@body))

(defn -main
  [& args]
  (println "")

  (doseq [i (range 100)]
    (println i)
    (println (wcar* (car-mq/enqueue "task-queue" (* i 100))))))
