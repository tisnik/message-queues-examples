(ns durable-queue-7.core
  (:gen-class))

(require '[durable-queue :refer :all])
(require '[clojure.pprint :refer :all])

(defn sleep
  [amount]
  (Thread/sleep amount))

(defn worker
  [q queue-name]
  (println "Worker started")
  (while true
     (let [message (take! q queue-name)]
        (println "Worker received message" (deref message))
        (complete! message)
        (sleep 2000)
        (println "Worker completed message" (deref message)))))

(defn -main
  [& args]
  (let [q (queues "/tmp" {:max-queue-size 10})]
       (pprint (stats q))
       (println "Starting worker")
       (.start (Thread. (fn [] (worker q :queue-1))))
       (doseq [i (range 10)]
           (println "Enqueuing task #" i)
           (put! q :queue-1 (str "task #" i))
           (pprint (stats q))
           (sleep 1000))))
