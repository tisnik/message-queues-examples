;
;  (C) Copyright 2019, 2020  Pavel Tisnovsky
;
;  All rights reserved. This program and the accompanying materials
;  are made available under the terms of the Eclipse Public License v1.0
;  which accompanies this distribution, and is available at
;  http://www.eclipse.org/legal/epl-v10.html
;
;  Contributors:
;      Pavel Tisnovsky
;

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
