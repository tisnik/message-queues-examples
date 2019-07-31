(ns durable-queue-1.core
  (:gen-class))

(require '[durable-queue :refer :all])

(defn -main
  "I don't do a whole lot ... yet."
  [& args]
  (let [q (queues "/tmp" {})]
       (println q)
       (println (stats q))))
