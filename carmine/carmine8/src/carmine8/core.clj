(ns carmine8.core
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

  (println "Set s1")
  (println
    (wcar*
      (carmine/sadd :s1 :a)
      (carmine/sadd :s1 :b)
      (carmine/sadd :s1 :c)
      (carmine/sadd :s1 :d)
      (carmine/smembers :s1)
      (carmine/scard :s1)))

  (println "Set s2")
  (println
    (wcar*
      (carmine/sadd :s2 :c :d :e :f)
      (carmine/smembers :s2)
      (carmine/scard :s1)))

  (println "Done"))
