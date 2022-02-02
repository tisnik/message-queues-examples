(ns carmineA.core
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
      (carmine/sunion :s1 :s2)))

  (println "intersection")
  (println
    (wcar*
      (carmine/sinter :s1 :s2)))

  (println "diff")
  (println
    (wcar*
      (carmine/sdiff :s1 :s2)
      (carmine/sdiff :s2 :s1)))

  (println "Done"))
