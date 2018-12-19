(ns example-01.core
    (:gen-class))

(require '[langohr.core      :as rabbit-mq])
(require '[langohr.channel   :as l-channel])
(require '[langohr.queue     :as l-queue])
(require '[langohr.consumers :as l-consumers])


(defn message-handler
    [ch {:keys [content-type delivery-tag type] :as meta} ^bytes payload]
    (println (format "Received a message: %s" (String. payload "UTF-8"))))


(defn -main
    [& args]
    (let [conn  (rabbit-mq/connect)
          ch    (l-channel/open conn)]
      (l-queue/declare ch "test" {:exclusive false :auto-delete false})
      (l-consumers/subscribe ch "test" message-handler {:auto-ack true})
      (println (format "Connected to channel id: %d" (.getChannelNumber ch)))
      (Thread/sleep 10000)
      (println "Disconnecting...")
      (rabbit-mq/close ch)
      (rabbit-mq/close conn)))
