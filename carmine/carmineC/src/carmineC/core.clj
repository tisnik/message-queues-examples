(ns carmineC.core
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
  (println "Working with sorted sets")

  (println "Fill in sorted set s1")
  (println
    (wcar*
      (carmine/zadd :s1 0.9 :a)
      (carmine/zadd :s1 0.8 :b)
      (carmine/zadd :s1 0.7 :c)
      (carmine/zadd :s1 0.6 :d)))

  (println "Retrieving items from sorted set s1")
  (println
    (wcar*
      (carmine/zcard :s1)
      (carmine/zrangebyscore :s1 0 100)
      (carmine/zrangebyscore :s1 0.65 0.85)))

  (println "Done"))
