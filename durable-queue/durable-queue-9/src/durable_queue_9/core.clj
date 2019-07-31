(ns durable-queue-9.core
  (:gen-class))

(require '[durable-queue :refer :all])
(require '[clojure.pprint :refer :all])

(defn sleep
  [amount]
  (Thread/sleep amount))

(defn worker
  [q queue-name]
  (println "Worker started, using queue" queue-name)
  (loop []
    (let [message (take! q queue-name)
          value   (deref message)]
        (if (=  value :exit)
            (println "Stopping worker that use queue" (name queue-name))
            (do
                (println "Worker received message" value "from queue" (name queue-name))
                (complete! message)
                (sleep 2000)
                (println "Worker completed message" value "from queue" (name queue-name))
                (recur))))))

(def queue-names
    [:queue-1 :queue-2 :queue-3])

(defn -main
  [& args]
  (let [q (queues "/tmp" {:max-queue-size 10})]
       (pprint (stats q))

       (println "Starting workers")
       (doseq [queue queue-names]
           (.start (Thread. (fn [] (worker q queue)))))

       (doseq [queue queue-names]
           (doseq [i (range 10)]
               (println "Enqueuing task #" i)
               (put! q queue (str "task #" i))
               (pprint (stats q))
               (sleep 500))
           (println "Enqueuing task to stop worker subscribed to queue" (name queue))
           (put! q queue :exit))

       (println "All tasks has been scheduled")))
