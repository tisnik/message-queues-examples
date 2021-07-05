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

(ns describe-topics.core
  (:require [jackdaw.admin :as ja]
            [clojure.pprint :as pp]))

(defn -main
  [& args]
  (let [client (ja/->AdminClient {"bootstrap.servers" "localhost:9092"})]
    (pp/pprint (ja/describe-topics client))))
