(defproject durable-queue-1 "0.1.0-SNAPSHOT"
  :description "FIXME: write description"
  :url "http://example.com/FIXME"
  :license {:name "Eclipse Public License"
            :url "http://www.eclipse.org/legal/epl-v10.html"}
  :dependencies [[org.clojure/clojure "1.8.0"]
                 [factual/durable-queue "0.1.5"]]
  :main ^:skip-aot durable-queue-8.core
  :target-path "target/%s"
  :profiles {:uberjar {:aot :all}})
