(ns durable-queue-6.core
  (:gen-class))

(require '[durable-queue :refer :all])
(require '[clojure.pprint :refer :all])

(defn deque-and-retry-message
  [q queue-name]
  (let [message (take! q queue-name)]
       (println "Message dequeued" message)
       (retry! message)
       (println "Message completed" message)))

(defn -main
  [& args]
  (let [q (queues "/tmp" {:max-queue-size 10})]
       (pprint (stats q))
       (doseq [i (range 20)]
           (put! q :queue-1 (str "task #" i))
           (pprint (stats q)))))
