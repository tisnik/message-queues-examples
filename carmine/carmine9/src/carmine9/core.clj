(ns carmine9.core
  (:require [taoensso.carmine :as carmine :refer (wcar)]))


(def redis-connection {
  :pool {}
  :spec {
    :uri "redis://localhost@127.0.0.1:6379"}})


(defmacro wcar*
  [& body]
  `(carmine/wcar redis-connection ~@body))


(defn -main
  [& args]
  (println "Working with two sets")
  (println "Fill in sets s1 and s2")

  (println
    (wcar*
      (carmine/srem :s1 :a :b :c :d :e :f)
      (carmine/srem :s2 :a :b :c :d :e :f)
      (carmine/sadd :s1 :a :b :c :d)
      (carmine/sadd :s2 :c :d :e :f)
      (carmine/smembers :s1)
      (carmine/smembers :s2)))

  (println "Set operations")

  (println "union")
  (println
    (wcar*
      (carmine/sunionstore :s3 :s1 :s2)
      (carmine/smembers :s3)))

  (println "intersection")
  (println
    (wcar*
      (carmine/sinterstore :s4 :s1 :s2)
      (carmine/smembers :s4)))

  (println "diff")
  (println
    (wcar*
      (carmine/sdiffstore :s5 :s1 :s2)
      (carmine/smembers :s5)
      (carmine/sdiffstore :s6 :s2 :s1)
      (carmine/smembers :s6)))

  (println "Done"))
