(ns carmineB.core
  (:require [taoensso.carmine :as carmine :refer (wcar)]
            [clojure.pprint :as pprint]))


(def redis-connection {
  :pool {}
  :spec {
    :uri "redis://localhost@127.0.0.1:6379"}})


(defmacro wcar*
  [& body]
  `(carmine/wcar redis-connection ~@body))


(defn -main
  [& args]
  (println "Working with maps")

  (println "hset operation")
  (println
    (wcar*
      (carmine/hset :m1 :foo :bar)
      (carmine/hset :m1 :bar :baz)
      (carmine/hset :m1 "result" 1/3)
      (carmine/hset :m1 "more-complicated" [1 2 3])
      (carmine/hset :m1 :boolean   true)
      (carmine/hset :m1 :nil-value nil)
      (carmine/hset :m1 :text      "Hello world!")
      (carmine/hset :m1 :list      '(1 2 3))
      (carmine/hset :m1 :vector    [1 2 3])
      (carmine/hset :m1 :a-set     #{1 2 3 4})
      (carmine/hset :m1 :map {:name    "foo"
                              :surname "bar"
                         })))

  (println "hget operation")
  (println
    (wcar*
      (carmine/hget :m1 :foo)
      (carmine/hget :m1 :bar)
      (carmine/hget :m1 :baz)
      (carmine/hget :m1 "result")
      (carmine/hget :m1 "more-complicated")
      (carmine/hget :m1 :unknown)))


  (println "hgetall operation")
  (pprint/pprint
    (wcar*
      (carmine/hgetall :m1)))

  (println "Done"))
