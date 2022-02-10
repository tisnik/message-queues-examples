(defproject carmineB "0.1.0-SNAPSHOT"
  :description "FIXME: write description"
  :url "http://example.com/FIXME"
  :license {:name "EPL-2.0 OR GPL-2.0-or-later WITH Classpath-exception-2.0"
            :url "https://www.eclipse.org/legal/epl-2.0/"}
  :dependencies [[org.clojure/clojure "1.10.1"]
                 [com.taoensso/carmine "3.1.0"]]
  :plugins [[lein-codox "0.10.7"]
            [test2junit "1.1.0"]
            [lein-cloverage "1.0.7-SNAPSHOT"]
            [lein-kibit "0.1.8"]
            [lein-clean-m2 "0.1.2"]
            ]
  :main ^:skip-aot carmineB.core
  :target-path "target/%s"
  :project-edn {:output-file "doc/details.clj"}
  :profiles {:uberjar {:aot :all
                       :jvm-opts ["-Dclojure.compiler.direct-linking=true"]}})
