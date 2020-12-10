{[ch.qos.logback/logback-classic "1.1.3"]
 {[ch.qos.logback/logback-core "1.1.3"] nil,
  [org.slf4j/slf4j-api "1.7.7"] nil},
 [clojure-complete "0.2.5" :exclusions [[org.clojure/clojure]]] nil,
 [fundingcircle/jackdaw "0.7.6"]
 {[aleph "0.4.6"]
  {[byte-streams "0.2.4"]
   {[clj-tuple "0.2.2"] nil, [primitive-math "0.1.6"] nil},
   [io.netty/netty-codec-http "4.1.25.Final"] nil,
   [io.netty/netty-codec "4.1.25.Final"] nil,
   [io.netty/netty-handler-proxy "4.1.25.Final"]
   {[io.netty/netty-codec-socks "4.1.25.Final"] nil},
   [io.netty/netty-handler "4.1.25.Final"] nil,
   [io.netty/netty-resolver-dns "4.1.25.Final"]
   {[io.netty/netty-codec-dns "4.1.25.Final"] nil},
   [io.netty/netty-resolver "4.1.25.Final"] nil,
   [io.netty/netty-transport-native-epoll "4.1.25.Final"]
   {[io.netty/netty-common "4.1.25.Final"] nil,
    [io.netty/netty-transport-native-unix-common "4.1.25.Final"] nil},
   [io.netty/netty-transport "4.1.25.Final"]
   {[io.netty/netty-buffer "4.1.25.Final"] nil},
   [manifold "0.1.8"]
   {[io.aleph/dirigiste "0.1.5"] nil, [riddley "0.1.14"] nil},
   [potemkin "0.4.5"] nil},
  [clj-time "0.15.1"] {[joda-time "2.10"] nil},
  [danlentz/clj-uuid "0.1.9" :exclusions [[primitive-math]]] nil,
  [io.confluent/kafka-avro-serializer "5.3.1"] nil,
  [io.confluent/kafka-schema-registry-client
   "5.3.1"
   :exclusions
   [[com.fasterxml.jackson.core/jackson-databind]]]
  {[io.confluent/common-config "5.3.1"] nil,
   [io.confluent/common-utils "5.3.1"]
   {[com.101tec/zkclient
     "0.10"
     :exclusions
     [[org.slf4j/slf4j-log4j12] [log4j]]]
    nil,
    [org.apache.zookeeper/zookeeper
     "3.4.14"
     :exclusions
     [[org.slf4j/slf4j-log4j12] [log4j]]]
    {[com.github.spotbugs/spotbugs-annotations "3.1.9"]
     {[com.google.code.findbugs/jsr305 "3.0.2"] nil},
     [io.netty/netty "3.10.6.Final"] nil,
     [jline "0.9.94" :exclusions [[*]]] nil,
     [org.apache.yetus/audience-annotations "0.5.0"] nil}},
   [org.apache.avro/avro "1.8.1"]
   {[com.thoughtworks.paranamer/paranamer "2.7"] nil,
    [org.apache.commons/commons-compress "1.8.1"] nil,
    [org.codehaus.jackson/jackson-core-asl "1.9.13"] nil,
    [org.codehaus.jackson/jackson-mapper-asl "1.9.13"] nil,
    [org.tukaani/xz "1.5"] nil}},
  [org.apache.kafka/kafka-clients "2.3.1"]
  {[com.github.luben/zstd-jni "1.4.0-1"] nil,
   [org.lz4/lz4-java "1.6.0"] nil,
   [org.xerial.snappy/snappy-java "1.1.7.3"] nil},
  [org.apache.kafka/kafka-streams "2.3.1"]
  {[org.apache.kafka/connect-json
    "2.3.1"
    :exclusions
    [[*/javax.ws.rs-api]]]
   {[com.fasterxml.jackson.core/jackson-databind "2.10.0"]
    {[com.fasterxml.jackson.core/jackson-annotations "2.10.0"] nil,
     [com.fasterxml.jackson.core/jackson-core "2.10.0"] nil},
    [com.fasterxml.jackson.datatype/jackson-datatype-jdk8 "2.10.0"]
    nil,
    [org.apache.kafka/connect-api "2.3.1"] nil},
   [org.rocksdb/rocksdbjni "5.18.3"] nil},
  [org.clojure/core.cache "0.7.2"]
  {[org.clojure/data.priority-map "0.0.7"] nil},
  [org.clojure/data.fressian "0.2.1"]
  {[org.fressian/fressian "0.6.6"] nil},
  [org.clojure/data.json "0.2.6"] nil,
  [org.clojure/tools.logging "0.4.1"] nil},
 [nrepl "0.7.0" :exclusions [[org.clojure/clojure]]] nil,
 [org.clojure/clojure "1.10.1"]
 {[org.clojure/core.specs.alpha "0.2.44"] nil,
  [org.clojure/spec.alpha "0.2.176"] nil},
 [venantius/ultra "0.6.0"]
 {[grimradical/clj-semver "0.3.0" :exclusions [[org.clojure/clojure]]]
  nil,
  [io.aviso/pretty "0.1.35"] nil,
  [mvxcvi/puget "1.1.0"]
  {[fipp "0.6.14"] {[org.clojure/core.rrb-vector "0.0.13"] nil},
   [mvxcvi/arrangement "1.1.1"] nil},
  [mvxcvi/whidbey "2.1.0"] {[org.clojure/data.codec "0.1.1"] nil},
  [org.clojars.brenton/google-diff-match-patch "0.1"] nil,
  [robert/hooke "1.3.0"] nil,
  [venantius/glow "0.1.5" :exclusions [[hiccup] [garden]]]
  {[clj-antlr "0.2.3"]
   {[org.antlr/antlr4-runtime "4.5.3"] nil,
    [org.antlr/antlr4 "4.5.3"] nil},
   [instaparse "1.4.1"] nil}}}
