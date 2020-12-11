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

(ns durable-queue-1.core
  (:gen-class))

(require '[durable-queue :refer :all])

(defn -main
  "I don't do a whole lot ... yet."
  [& args]
  (let [q (queues "/tmp" {})]
       (println q)
       (println (stats q))))
