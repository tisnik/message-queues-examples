(ns carmine7.core
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
  (println "Working with list")
  (println
    (wcar*
      (carmine/llen "a-list")
      (carmine/lpush "a-list" "first")
      (carmine/llen "a-list")
      (carmine/lpush "a-list" "second")
      (carmine/llen "a-list")
      (carmine/lpop "a-list")
      (carmine/llen "a-list")
      (carmine/lpop "a-list")
      (carmine/llen "a-list")
      (carmine/lpop "a-list")
      (carmine/llen "a-list")))
  (println "Done"))
