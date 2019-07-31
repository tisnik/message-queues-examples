(ns durable-queue-5.core
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
  (let [q (queues "/tmp" {})]
       (pprint (stats q))
       (put! q :queue-1 "task #A")
       (put! q :queue-1 "task #B")
       (put! q :queue-2 "task #C")
       (pprint (stats q))
       (println "Získávám dvě zprávy z front queue-1 a queue-2, které budou uloženy zpět")
       (deque-and-retry-message q :queue-1)
       (deque-and-retry-message q :queue-2)
       (pprint (stats q))
       (println "Získávám další dvě zprávy z front queue-1 a queue-2, které budou uloženy zpět")
       (deque-and-retry-message q :queue-1)
       (deque-and-retry-message q :queue-2)
       (pprint (stats q))))
