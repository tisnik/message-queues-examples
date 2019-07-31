(ns durable-queue-2.core
  (:gen-class))

(require '[durable-queue :refer :all])
(require '[clojure.pprint :refer :all])

(defn -main
  [& args]
  (let [q (queues "/tmp" {})]
       (pprint (stats q))
       (put! q :queue-1 "task #A")
       (put! q :queue-1 "task #B")
       (pprint (stats q))
       (-> (take! q :queue-1) println)
       (pprint (stats q))
       (-> (take! q :queue-1) println)
       (pprint (stats q))))
