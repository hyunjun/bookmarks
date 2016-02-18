Apache
======
* [Using Apache Parquet at AppNexus](http://blog.cloudera.com/blog/2015/04/using-apache-parquet-at-appnexus/)
* [지금 핫한 Real-time In-memory Stream Processing 이야기](http://www.slideshare.net/tedwon/realtimeinmemorystreamprocessingbytedwon) KaVa, Storm, Spark streaming
* [SuperChief: From Apache Storm to In-House Distributed Stream Processing](http://blog.librato.com/posts/superchief)
* [apache bigdata europe](http://events.linuxfoundation.org/events/apache-big-data-europe/program/schedule)

# [Arrow](http://arrow.apache.org/)
* [Apache Arrow - Powering Columnar In-Memory Analytics - Arrow is a set of technologies that enable big-data systems to process and move data fast](https://github.com/apache/arrow)

# Beam (Former [DataFlow](https://wiki.apache.org/incubator/DataflowProposal))

* [Comparing the Dataflow/Beam and Spark Programming Models](https://cloud.google.com/blog/big-data/2016/02/comparing-the-dataflowbeam-and-spark-programming-models#closeImage)
  
# [Commons](https://commons.apache.org/)

# Cordova
* [Apache Cordova: after 10 months, I won't be using it anymore](http://geekcoder.org/apache-cordova-after-10-months-i-wont-using-it-anymore/)
* [Cordova 환경 구성 & Git Ignore 설정](http://brantiffy.axisj.com/archives/377)

# [Crunch](https://crunch.apache.org/)

# [Drill](http://drill.apache.org/)

# [Falcon - Simplifying Managing Data Jobs on Hadoop](http://www.slideshare.net/Hadoop_Summit/apache-falcon-simplifying-managing-data-jobs-on-hadoop)

# [Flink](https://flink.apache.org/)
* [Apache Flink Training](http://dataartisans.github.io/flink-training/)
* [Juggling with Bits and Bytes](http://flink.apache.org/news/2015/05/11/Juggling-with-Bits-and-Bytes.html)
* [스사모 테크톡 - Apache Flink 둘러보기](http://www.slideshare.net/sangwookimme/apache-flink-48832827)
* [Off-heap Memory in Apache Flink and the curious JIT compiler](http://flink.apache.org/news/2015/09/16/off-heap-memory.html)
* [Stream Processing with Apache Flink](http://blog.brakmic.com/stream-processing-with-apache-flink/)

# [Geode - an open source, distributed, in-memory database for scale-out applications](http://geode.incubator.apache.org/)

# [Ignite](https://ignite.apache.org/features/igniterdd.html) - Spark Shared RDDs

# [Imapala](http://impala.io/)
* [Apache Impala (Incubating)](http://www.cloudera.com/products/apache-hadoop/impala.html)
* [Contributing to Impala](http://www.slideshare.net/cloudera/contributing-to-impala)
* [The Impala Cookbook](http://www.slideshare.net/cloudera/the-impala-cookbook-42530186)
* [What’s Next for Impala: More Reliability, Usability, and Performance at Even Greater Scale](http://blog.cloudera.com/blog/2015/07/whats-next-for-impala-more-reliability-usability-and-performance-at-even-greater-scale/)
* [How-to: Prepare Unstructured Data in Impala for Analysis](http://blog.cloudera.com/blog/2015/09/how-to-prepare-unstructured-data-in-impala-for-analysis/)
* [New SQL Benchmarks: Apache Impala (incubating) Uniquely Delivers Analytic Database Performance](http://blog.cloudera.com/blog/2016/02/new-sql-benchmarks-apache-impala-incubating-2-3-uniquely-delivers-analytic-database-performance/)

# [Jena](http://jena.apache.org)

# [Kafka](http://kafka.apache.org/)
* [Kafka in a Nutshell](http://sookocheff.com/post/kafka/kafka-in-a-nutshell/)
* [REACTIVE STREAMS FOR APACHE KAFKA](https://softwaremill.com/reactive-kafka/)
* [HANDS-FREE KAFKA REPLICATION: A LESSON IN OPERATIONAL SIMPLICITY](http://blog.confluent.io/2015/04/07/hands-free-kafka-replication-a-lesson-in-operational-simplicity/)
* [Bottled Water: Real-time integration of PostgreSQL and Kafka](http://blog.confluent.io/2015/04/23/bottled-water-real-time-integration-of-postgresql-and-kafka/)
* [REACTIVE STREAMS FOR APACHE KAFKA](https://softwaremill.com/reactive-kafka/)
* [Recent Evolution of Zero Data Loss Guarantee in Spark Streaming With Kafka](http://getindata.com/blog/post/recent-evolution-of-zero-data-loss-guarantee-in-spark-streaming-with-kafka/)
* [Apache Kafka, Samza, and the Unix Philosophy of Distributed Data](http://www.confluent.io/blog/apache-kafka-samza-and-the-unix-philosophy-of-distributed-data)
* [Apache Kafka: Case of Large Messages, Many Partitions, Few Consumers](https://olnrao.wordpress.com/2015/03/24/apache-kafka-case-of-large-messages-many-partitions-few-consumers/)
* [Distributed Consensus Reloaded: Apache ZooKeeper and Replication in Apache Kafka](http://www.confluent.io/blog/distributed-consensus-reloaded-apache-zookeeper-and-replication-in-kafka)
* [From Kafka to ZeroMQ for real-time log aggregation](http://tomasz.janczuk.org/2015/09/from-kafka-to-zeromq-for-log-aggregation.html)
* [SQL on Kafka](https://www.pipelinedb.com/blog/sql-on-kafka)
* [This is a Kafka-Storm-Esper example on vagrant](https://github.com/doohee323/tzstorm)
  1. kafka를 사용할 때 Producer.send 해서 stream을 전달하던데, legacy시스템에서 별도의 코딩을 통해서 구현해야 하는 것인지 => kafka를 사용할 때 보통 producer, consumer를 구현한다. kafka - storm을 사용할 때 kafkaspout는 consumer 역할은 한다.
  2. KafkaSpout에서 생성된 stream이 storm의 Bolt로 들어올 때 어떻게 디버깅이 가능한 지 => 원격 디버깅은 없고 -Dstorm.log.dir를 통한 로그파일로 디버깅한다.
  3. bolt로 넘어온 중복된 stream을 어떻게 unique한 데이터로 처리 가능한 지 => unique한 데이터 처리를 위해서 trident를 사용하며, trident는 storm의 구현을 지원하는 (aggregation 등) 역할을 한다. -> esper로 group by 등의 쿼리문을 만들 수 있는데 trident와 역할 충돌이 있지 않을까 싶지만, trident를 통해 unique한 데이터를 받아 esper로 쿼리문을 돌릴 수 있지 않을까 싶다.
  4. kafka 대신에 zmq로 연동할 때 예상되는 문제점이 있는지. zmq와 kafka 모두 큐 역할을 하므로 특별한 이유가 없다면 zmqspout를 활용하는 것이 좋겠다.
* [Kafka at HubSpot: Critical Consumer Metrics](http://product.hubspot.com/blog/kafka-at-hubspot-part-1-critical-consumer-metrics)
* [Bottled Water: Real-time integration of PostgreSQL and Kafka](http://www.confluent.io/blog/bottled-water-real-time-integration-of-postgresql-and-kafka/)
* [빅데이터 윤활유 '아파치 카프카', 왜 주목받나](http://www.ciokorea.com/news/27214)
* [Flafka: Apache Flume Meets Apache Kafka for Event Processing](http://blog.cloudera.com/blog/2014/11/flafka-apache-flume-meets-apache-kafka-for-event-processing/)
* [Why I am not a fan of Apache Kafka](https://gist.github.com/markrendle/26e423b6597685757732)
* [주니어 개발자의 storm kafka 시작하기](http://blog.embian.com/m/post/108)

# [Mesos](http://mesos.apache.org/)
* [Advanced Mesos Course](http://open.mesosphere.com/intro-course/)
* [Spark(1.2.1 -> 1.3.1) 을 위한 Mesos(0.18 -> 0.22.rc) - Upgrade](http://hoondongkim.blogspot.kr/2015/05/spark121-131-mesos018-021-upgrade.html)
* [mesos, omega, borg: a survey](http://www.umbrant.com/blog/2015/mesos_omega_borg_survey.html)
* [Mesos: A Platform for Fine-Grained Resource Sharing in the Data Center](http://people.csail.mit.edu/matei/papers/2011/nsdi_mesos.pdf)
* [minmesos - Testing infrastructure for Mesos frameworks](http://minimesos.org/)

# [Nifi](https://nifi.apache.org/) Apache nifi is an easy to use, powerful, and reliable system to process and distribute data

# [Nutch](http://nutch.apache.org/)
* [Apache Nutch - 오픈소스 웹 검색 엔진](http://jsonlee.tistory.com/entry/Apache-Nutch-%EC%98%A4%ED%94%88%EC%86%8C%EC%8A%A4-%EC%9B%B9-%EA%B2%80%EC%83%89-%EC%97%94%EC%A7%84)

# [Oozie](http://oozie.apache.org/)

# [Parquet](https://parquet.apache.org/)
* [Dremel made simple with Parquet](https://blog.twitter.com/2013/dremel-made-simple-with-parquet)

# [Pig](http://pig.apache.org/)
* [A Simple Explanation of COGROUP in Apache Pig](http://joshualande.com/cogroup-in-pig/)
* examples
  * [https://gist.github.com/hyunjun/55f83bfd91e2b1e24f46](https://gist.github.com/hyunjun/55f83bfd91e2b1e24f46)
* [[pig] hug number of part files](https://github.com/dsindex/blog/wiki/%5Bpig%5D-hug-number-of-part-files)
* [Hadoop Tutorial: Pig Part 2 -- Joining Data Sets and Other Advanced Topics](http://www.slideshare.net/martyhall/hadoop-tutorial-pig-part-2-joining-data-sets-and-other-advanced-topics)

# [Phoenix](http://phoenix.apache.org/) High performance relational database layer over HBase for low latency applications
* [Apache Phoenix Joins Cloudera Labs](http://blog.cloudera.com/blog/2015/05/apache-phoenix-joins-cloudera-labs/)

# [River](https://river.apache.org/)

# Samza
* [REAL-TIME FULL-TEXT SEARCH WITH LUWAK AND SAMZA](http://blog.confluent.io/2015/04/13/real-time-full-text-search-with-luwak-and-samza/)
* [Apache Kafka, Samza, and the Unix Philosophy of Distributed Data](http://www.confluent.io/blog/apache-kafka-samza-and-the-unix-philosophy-of-distributed-data)

# [SINGA](http://singa.apache.org/docs/overview.html) a general distributed deep learning platform for training big deep learning models over large datasets

# Solr
* [gooper.com/검색엔진-solr](http://www.gooper.com/ss/index.php?mid=bigdata&category=270441)

# [SystemML](http://systemml.apache.org/)
* [IBM's SystemML Machine Learning - Now Apache SystemML](https://github.com/SparkTC/systemml)

# [Tajo](http://tajo.apache.org/)
* [Introduction to Apache Tajo](http://www.slideshare.net/gruter/introduction-to-apache-tajo)
* [Collaborate Apache Tajo + Elasticsearch](https://github.com/gruter/tajo-elasticsearch)
* [아파치 타조(Apache Tajo)를 이용한 코호트(Cohort) 분석](http://blrunner.com/80)
* [아파치 타조 (Apache Tajo) 한글 문서 프로젝트 리소스 및 진행 공유](http://diveintodata.org/2015/01/01/%EC%95%84%ED%8C%8C%EC%B9%98-%ED%83%80%EC%A1%B0-apache-tajo-%ED%95%9C%EA%B8%80-%EB%AC%B8%EC%84%9C-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EB%A6%AC%EC%86%8C%EC%8A%A4-%EB%B0%8F-%EC%A7%84%ED%96%89/)
* [Big data analysis with R and Apache Tajo (in Korean)](http://www.slideshare.net/gruter/ruck2015-gruter-public)
* [Tajo Seoul Meetup July 2015 - What's New Tajo 0.11](http://www.slideshare.net/hyunsikchoi/tajo-meetup-0716)
* [[Apache Tajo] Apache Tajo 데스크탑 + Zeppelin 연동 하기](http://jjeong.tistory.com/1031)
* [Expanding Your Data Warehouse with Tajo](http://www.slideshare.net/blrunner/expanding-your-data-warehouse-with-tajo)
* [AWS + Tajo를 이용한 '테라 렉 로그 분석 이야기'](http://www.slideshare.net/zenos2408/aws-tajo)
* [Python 에서 Tajo 사용하기](http://linewalks.com/archives/1085)

# [Zookeeper](http://zookeeper.apache.org/)
* [Zoom: Reactive Programming with Zookeeper](http://blog.midonet.org/zoom-reactive-programming-zookeeper/)
* [The Discovery of Apache ZooKeeper’s Poison Packet](http://www.pagerduty.com/blog/the-discovery-of-apache-zookeepers-poison-packet/)
* [Mining Zookeeper’s transaction log to track down bugs](https://medium.com/@ivankelly/mining-zookeeper-s-transaction-log-to-track-down-bugs-63b4c653bb6)
