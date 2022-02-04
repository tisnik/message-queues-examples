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

(defproject durable-queue-1 "0.1.0-SNAPSHOT"
  :description "FIXME: write description"
  :url "http://example.com/FIXME"
  :license {:name "Eclipse Public License"
            :url "http://www.eclipse.org/legal/epl-v10.html"}
  :dependencies [[org.clojure/clojure "1.10.1"]
                 [factual/durable-queue "0.1.5"]]
  :plugins [[lein-codox "0.10.7"]
            ]
  :main ^:skip-aot durable-queue-4.core
  :project-edn {:output-file "doc/details.clj"}
  :target-path "target/%s"
  :profiles {:uberjar {:aot :all}})
