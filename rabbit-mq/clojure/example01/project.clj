(defproject example-01 "0.1.0-SNAPSHOT"
  :description "FIXME: write description"
  :url "http://example.com/FIXME"
  :license {:name "Eclipse Public License"
            :url "http://www.eclipse.org/legal/epl-v10.html"}
  :dependencies [[org.clojure/clojure "1.8.0"]
                 [com.novemberain/langohr "5.0.0"]]
  :plugins [[lein-codox "0.10.7"]
            [test2junit "1.1.0"]
            ]
  :main ^:skip-aot example-01.core
  :target-path "target/%s"
  :project-edn {:output-file "doc/details.clj"}
  :profiles {:uberjar {:aot :all}})
