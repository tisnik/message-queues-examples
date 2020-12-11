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
