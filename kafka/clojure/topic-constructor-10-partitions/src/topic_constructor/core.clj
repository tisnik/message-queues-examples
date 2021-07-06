;
;  (C) Copyright 2021  Pavel Tisnovsky
;
;  All rights reserved. This program and the accompanying materials
;  are made available under the terms of the Eclipse Public License v1.0
;  which accompanies this distribution, and is available at
;  http://www.eclipse.org/legal/epl-v10.html
;
;  Contributors:
;      Pavel Tisnovsky
;

(ns topic-constructor.core
  (:require [jackdaw.admin :as ja]))

(defn -main
  []
  (let [client (ja/->AdminClient {"bootstrap.servers" "localhost:9092"})]
    (ja/create-topics! client [{:topic-name "test3"
                                :partition-count 10
                                :replication-factor 1
                                :topic-config {"cleanup.policy" "compact"}}])))

