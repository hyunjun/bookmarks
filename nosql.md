NoSQL
=====
* [Cassandra vs MongoDB vs CouchDB vs Redis vs Riak vs HBase vs Couchbase vs OrientDB vs Aerospike vs Neo4j vs Hypertable vs ElasticSearch vs Accumulo vs VoltDB vs Scalaris comparison](http://kkovacs.eu/cassandra-vs-mongodb-vs-couchdb-vs-redis)
* [Building a Distributed Fault-Tolerant Key-Value Store](http://blog.fourthbit.com/2015/04/12/building-a-distributed-fault-tolerant-key-value-store)
* [Implementing a Key-Value Store](http://codecapsule.com/2012/11/07/ikvs-implementing-a-key-value-store-table-of-contents/)
* [Indeed LSM Tree](https://github.com/indeedeng/lsmtree)
* [ToroDB: A MongoDB-compatible, document-oriented database on top of PostgreSQL](http://www.8kdata.com/torodb/)
* [Please stop calling databases CP or AP](https://martin.kleppmann.com/2015/05/11/please-stop-calling-databases-cp-or-ap.html)
* [Basho Relaunches To Deliver A Cohesive Big Data Platform](http://www.forbes.com/sites/benkepes/2015/05/27/basho-relaunches-to-deliver-a-cohesive-big-data-platform/)
* [hyperfs - A content-addressable union file system build on top of fuse, hyperlog, leveldb and node](https://github.com/mafintosh/hyperfs)
* [2015년 4월 9일자 오픈소스 임베디드 DB 리스트](http://blog.hazard.kr/archives/412)
* [NewSQL vs. NoSQL for New OLTP](https://www.youtube.com/watch?v=uhDM4fcI2aI)
* [Database expert on why NoSQL mattered — and SQL still matters](https://medium.com/s-c-a-l-e/database-guru-on-why-nosql-matters-and-sql-still-matters-c64239fe84fd)
* [The CAP FAQ](The CAP FAQ)
* [TIMESERIES DATASTORES](http://abhishekkr.github.io/slides/2015.ggn.geeknight.timeseriesdb.htm#/)
  * [시계열 DB (OpenTSDB , 인플럭스 DB , Graphite ) 정리](http://hamait.tistory.com/440)
* [Why MongoDB, Cassandra, HBase, DynamoDB, and Riak will only let you perform transactions on a single data item](http://dbmsmusings.blogspot.kr/2015/10/why-mongodb-cassandra-hbase-dynamodb_28.html)
* [NoSQL 간단한 소개](http://www.slideshare.net/WonchangSong1/no-sqlsimpleintro)
* [A Survey of Query Execution Engines (from Volcano to Vectorized Processing)](https://chatwithengineers.com/2016/08/29/a-survey-of-query-execution-engines-from-volcano-to-vectorized-processing/)

# Amazon

## AWS
* [Uploading to S3 in 18 lines of Shell (used to upload builds for http://soltrader.net)](https://gist.github.com/chrismdp/6c6b6c825b07f680e710)
* [Intro to Node on AWS Lambda for S3 and Kinesis](http://eng.localytics.com/taming-aws-lambda-for-s3-and-kinesis-at-localytics/)

## DynamoDB
* [Deep Dive: Amazon DynamoDB](http://www.slideshare.net/AmazonWebServices/deep-dive-amazon-dynamodb)
* [bloop - Object Mapper for DynamoDB http://bloop.readthedocs.org](https://github.com/numberoverzero/bloop/)
* [Dynomite, inspired by Dynamo whitepaper, is a thin, distributed dynamo layer for different storage engines and protocols](https://github.com/Netflix/dynomite)
  * [Getting Started](https://github.com/Netflix/dynomite/wiki/Getting-Started)
  * [Introducing Dynomite - Making Non-Distributed Databases, Distributed](http://techblog.netflix.com/2014/11/introducing-dynomite.html?m=1)

# ArangoDB
* [Performance comparison between ArangoDB, MongoDB, Neo4j and OrientDB](https://www.arangodb.com/2015/06/performance-comparison-between-arangodb-mongodb-neo4j-and-orientdb/)
* [Benchmark: PostgreSQL, MongoDB, Neo4j, OrientDB and ArangoDB](https://www.arangodb.com/2015/10/benchmark-postgresql-mongodb-arangodb/)
* [Data modeling with multi-model databases](http://radar.oreilly.com/2015/07/data-modeling-with-multi-model-databases.html)

# [Aerospike](http://www.aerospike.com/) High performance NoSQL database delivering speed at scale
* [Call me maybe: Aerospike](https://aphyr.com/posts/324-call-me-maybe-aerospike)

# [AtlasDB is a transactional layer on top of a key value store](https://github.com/palantir/atlasdb)

# Azure DocumentDB
* [NoSQL database service Azure DocumentDB now Generally Available](http://azure.microsoft.com/blog/2015/04/08/nosql-database-service-azure-documentdb-now-generally-available)

# [Blazing GPU Database](http://blazingdb.com/)

# Cassandra
* [Performance doubling with message coalescing](http://www.datastax.com/dev/blog/performance-doubling-with-message-coalescing)
* [Cassandra: Daughter of Dynamo and BigTable](http://www.insightdataengineering.com/blog/cass.html)
* [Cassandra on ContainerShip](https://medium.com/containership-articles/cassandra-on-containership-84ca90b8e1b9)
* [This Team Used Apache Cassandra… You Won’t Believe What Happened Next](http://blog.parsely.com/post/1928/cass/)
* [Cassandra From a Relational World](https://medium.com/@mustwin/cassandra-from-a-relational-world-7bbdb0a9f1d)
* [legacy - A light weight Cassandra backup utility](https://github.com/iamthemovie/legacy)
* [New in Cassandra 3.0: Materialized Views](http://www.datastax.com/dev/blog/new-in-cassandra-3-0-materialized-views)
* [Understanding the Impact of Cassandra Compact Storage](http://blog.librato.com/posts/cassandra-compact-storage)
* [Doradus is a REST service that extends a Cassandra NoSQL database with a graph-based data model](https://github.com/dell-oss/Doradus)
* [Apple's secret NoSQL sauce includes a hefty dose of Cassandra](http://www.techrepublic.com/article/apples-secret-nosql-sauce-includes-a-hefty-dose-of-cassandra/)
* [ScyllaDB: world's fastest NoSQL column store database Fully compatible with Apache Cassandra at 10x the throughput and jaw dropping low latency](http://www.scylladb.com/)

# [CockroachDB](https://github.com/cockroachdb/cockroach)
* [How CockroachDB Does Distributed, Atomic Transactions](http://www.cockroachlabs.com/blog/how-cockroachdb-distributes-atomic-transactions/)
* [SQL in CockroachDB: Mapping Table Data to Key-Value Storage](http://www.cockroachlabs.com/blog/sql-in-cockroachdb-mapping-table-data-to-key-value-storage/)
* [Why Go Was the Right Choice for CockroachDB](http://www.cockroachlabs.com/blog/why-go-was-the-right-choice-for-cockroachdb/)

# CouchBase
* [QUERY TRANSLATOR - SQL TO COUCHBASE N1QL](http://www.querycouchbase.com/#/query)

# CouchDB
* [Let’s learn Erlang and fix a bug on a CouchDB Cluster #1](http://robert-kowalski.de/blog/lets-learn-erlang-and-fix-a-bug-on-a-couchdb-cluster/)
* [Open-Sourcing IBM Cloudant’s CouchDB Search Integration with Lucene](https://cloudant.com/blog/open-sourcing-cloudant-search)

# CryptDB
* [CryptDB - A database system that can process SQL queries over encrypted data](https://github.com/CryptDB/cryptdb)

# [Ehcache: Java's Most Widely-Used Cache](http://ehcache.org/)

# [EnnoDB](http://twigtechnology.com/blog/2015/06/11/announcing-ennodb/)

# [FiloDB](http://velvia.github.io/Introducing-FiloDB/)

# [Geode - an open source, distributed, in-memory database for scale-out applications](http://geode.incubator.apache.org/)

# Google
* BigQuery
  * [구글 빅데이타 플랫폼 빅쿼리(BIGQUERY)에 소개](http://bcho.tistory.com/1116)
  * [Google BigQuery Now Allows to Query All Open-Source Projects on GitHub](https://www.infoq.com/news/2016/07/google-github-bigquery)
  * [구글 빅쿼리 데이터 로딩하기](http://whitechoi.tistory.com/25)
  * [BigQuery at WePay](https://wecode.wepay.com/posts/bigquery-wepay)
  * [Building WePay's data warehouse using BigQuery and Airflow](https://wecode.wepay.com/posts/wepays-data-warehouse-bigquery-airflow)
  * [빅데이타 수집을 위한 데이타 수집 솔루션 Embulk 소개](http://bcho.tistory.com/1126)
  * [In-memory query execution in Google BigQuery 빅쿼리의 In-memory query 실행](http://whitechoi.tistory.com/29)
  * [빅쿼리 Query Plan을 이용한 쿼리 실행 분석](http://whitechoi.tistory.com/32)
  * [구글 빅쿼리와 데이타 플로우를 이용한 노트7 소셜 반응 분석](http://bcho.tistory.com/1136)
  * [노트7의 소셜 반응을 분석해 보았다. #2 구현하기](http://bcho.tistory.com/1137)
* [Cloud Bigtable](https://cloud.google.com/bigtable/)
  * [Announcing Google Cloud Bigtable: The same database that powers Google Search, Gmail and Analytics is now available on Google Cloud Platform](http://googlecloudplatform.blogspot.kr/2015/05/introducing-Google-Cloud-Bigtable.html)
  * [Cloud Launcher](https://cloud.google.com/launcher/explore)
* [Firebase](https://firebase.google.com/)
  * [Firecasts (Firebase + Screencasts)](https://www.youtube.com/playlist?list=PLOU2XLYxmsIKkg55tSHz0Xc8ZMVS1GJQL)
  * [Firebase, 통합 앱 플랫폼으로 확장](http://googledevkr.blogspot.com/2016/05/firebase-8-firebase-google43.html)
  * [Migrate to Firebase - Google I/O 2016](https://www.youtube.com/watch?v=RWM9J6Mvu-4)
  * [Firebase Android Codelab](https://codelabs.developers.google.com/codelabs/firebase-android/index.html)
  * [Firebase Analytics 소개](http://googledevkr.blogspot.com/2016/06/introducing-firebase-analytics.html)
  * [Android Firebase 설정하기](https://www.evernote.com/shard/s181/sh/3a664964-38db-4a4b-82b6-6485e25d389d/2622252d5d9272ac)
  * [Firebase 강의에 관하여...](http://jetalog.net/43)
  * [Google Firebase로 레고블럭 조립하기 - IO Extended 2016](http://www.slideshare.net/ChiungChoi/google-firebase-io-extended-2016)
  * [firebase-unity](https://github.com/firebase/Firebase-Unity)
  * [Firebase Hosting 신청 및 배포](http://jetalog.net/47)
  * [Saving data - Firebase Database REST API](http://eojji.blogspot.com/2016/08/saving-data-firebase-database-rest-api.html)
  * [파이어베이스 애널러틱스를 이용한 모바일 데이타 분석 #1-Hello Firebase](http://bcho.tistory.com/1131)
  * [파이어베이스 애널러틱스를 이용한 모바일 데이타 분석 #2-분석 지표 이해하기](http://bcho.tistory.com/1132)
  * [파이어베이스 애널러틱스를 이용한 모바일 데이타 분석- #3 빅쿼리에 연동하여 모든 데이타를 분석하기](http://bcho.tistory.com/1133)
  * [Speakers Bureau](https://github.com/google/gde-speakersbureau/tree/master/speakersbureau)
* [The Google Stack](http://malteschwarzkopf.de/research/assets/google-stack.pdf)
  * [What is the open source version of Google Cloud Dataflow?](http://www.quora.com/What-is-the-open-source-version-of-Google-Cloud-Dataflow)
  * [Google Dataflow A Unified Model for Batch and Streaming Data Processing](https://www.youtube.com/watch?v=3UfZN59Nsk8)

# [Greenplum Database (GPDB)](https://github.com/greenplum-db/gpdb)

# [HazelCast](http://hazelcast.org/)

# [Infinispan](http://infinispan.org/) Distributed in-memory key/value data grid and cache
* [Infinispan Spark connector 0.1 released!](http://blog.infinispan.org/2015/08/infinispan-spark-connector-01-released.html)

# IndexedDB
* [IndexedDB is an asynchronous, transactional, key-value object store](https://dev.opera.com/articles/introduction-to-indexeddb/)

# InfluxDB
* [Influxdb - Scalable datastore for metrics, events, and real-time analytics](https://github.com/influxdb/influxdb)
* [Announcing Telegraf, a metrics collector for InfluxDB](https://influxdb.com/blog/2015/06/19/Announcing-Telegraf-a-metrics-collector-for-InfluxDB.html)
  * [The plugin-driven server agent for reporting metrics into InfluxDB](https://github.com/influxdb/telegraf)
* [Time-Series Database with InfluxDB CEO Paul Dix](http://softwareengineeringdaily.com/2015/08/21/time-series-database-with-influxdb-ceo-paul-dix/)
* [Scouter와 influx db – grafana 연동 가이드](http://www.slideshare.net/ienvyou/scouter-influx-db-grafana)
* [MONITORING APACHE KAFKA WITH GRAFANA / INFLUXDB VIA JMX](https://softwaremill.com/monitoring-apache-kafka-with-influxdb-grafana/)

# In-memory In memory
* [A K/V Store For In-Memory Analytics: Part 1](http://0xdata.com/blog/2014/02/kv-store-memory-analytics/)
* [A K/V Store For In-Memory Analytics, Part 2](http://0xdata.com/blog/2014/05/kv-store-memory-analytics-part-2-2/)
* [Gorilla: A Fast, Scalable, In-Memory Time Series Database](http://www.vldb.org/pvldb/vol8/p1816-teller.pdf)
* [How To Choose An In-Memory NoSQL Solution: Performance Measuring](http://highscalability.com/blog/2015/12/30/how-to-choose-an-in-memory-nosql-solution-performance-measur.html) comparison of redis, tarantool, couchbase, and memcached
* [인-메모리 데이터 기술을 활용한 실시간 빅데이터 분석](https://www.youtube.com/watch?v=PuA6qplF0Gk)

# [Irmin - a distributed database that follows the same design principles as Git](https://github.com/mirage/irmin)
* [Introducing Irmin: Git-like distributed, branchable storage](https://mirage.io/blog/introducing-irmin)

# [Khronus - A reactive time series database](https://github.com/Searchlight/khronus)

# LevelDB
* [Transaction manager for Node.js LevelDB: two-phase locking, snapshot isolation, atomic commits](https://github.com/cshum/level-transactions)
* [A blazing fast geo database with LevelDB, Go and Geohashes](http://blog.nobugware.com/post/2015/leveldb_geohash_golang/)
* [levi - Streaming full-text search for Node.js and browsers. Built on LevelDB](https://github.com/cshum/levi)
* [Siberite is a simple leveldb backed message queue server](https://github.com/bogdanovich/siberite)

# [LMDB - Lightning Memory-Mapped Database Manager](http://symas.com/mdb/doc/)

# Manhattan
* [Manhattan, our real-time, multi-tenant distributed database for Twitter scale](https://blog.twitter.com/2014/manhattan-our-real-time-multi-tenant-distributed-database-for-twitter-scale)
* [Building DistributedLog: Twitter’s high-performance replicated log service](https://blog.twitter.com/2015/building-distributedlog-twitter-s-high-performance-replicated-log-service)

# MapD
* [MapD: Massive Throughput Database Queries with LLVM on GPUs](http://devblogs.nvidia.com/parallelforall/mapd-massive-throughput-database-queries-llvm-gpus/)

# Memcached
* [MONITORING GROWING MEMCACHED](http://engineering.vinted.com/2015/06/09/monitoring-growing-memcached/)
* [libmc - Fast and light-weight memcached client for C++/Python https://pypi.python.org/pypi/libmc/](https://github.com/douban/libmc)
* [memcache internals](https://www.adayinthelifeof.nl/2011/02/06/memcache-internals/)

# MemSQL
* [Launching Our Community Edition](http://blog.memsql.com/memsql-community-edition/)
* [Customer Guest Post: Learning the MemSQL JSON Column Type](http://blog.memsql.com/json-column-type/)
* [MemSQL Community Edition Available on AWS and Azure Marketplaces](http://blog.memsql.com/memsql-on-aws-and-azure/)
* [Using MemSQL and Spark for Machine Learning](https://dzone.com/articles/using-memsql-and-spark-for-machine-learning-memsql)

# [MICA: A Holistic Approach to Fast In-Memory Key-Value Storage](https://www.cs.cmu.edu/~hl/papers/mica-nsdi2014.pdf)

# MongoDB
* [M101P: MONGODB FOR DEVELOPERS](https://university.mongodb.com/courses/M101P/about?_ga=1.191685481.23006852.1438307238)
* [Separating Collections to Improve MongoDB Measurability](https://blog.compose.io/separating-collections-to-improve-mongodb-measurability/)
* [MongoDB + RocksDB at Parse](http://blog.parse.com/announcements/mongodb-rocksdb-parse/)
* [Call me maybe: MongoDB stale reads](https://www.aphyr.com/posts/322-call-me-maybe-mongodb-stale-reads)
* [A proof of concept MongoDB clone built on Postgres](https://github.com/JerrySievert/mongolike)
* [mgfs - Mount a MongoDb database as a filesystem](https://github.com/amsa/mgfs)
* [Managing schema changes with MongoDB](http://derickrethans.nl/managing-schema-changes.html)
* [Mongo BSON Injection: Ruby Regexps Strike Again](http://sakurity.com/blog/2015/06/04/mongo_ruby_regexp.html?)
* [MongoDB for Beginners Tutorials](https://www.youtube.com/playlist?list=PL6gx4Cwl9DGDQ5DrbIl20Zu9hx1IjeVhO)
* [A new way to store your data with MongoDB](https://codepicnic.com/posts/feature-friday-a-new-way-to-store-your-data-with-mongodb-045117b0e0a11a242b9765e79cbf113f/)
* [Apache Spark and MongoDB – Turning Analytics into Real-Time Action](https://www.mongodb.com/collateral/apache-spark-and-mongodb-turning-analytics-into-real-time-action)
* [Why you should never, ever, ever use MongoDB](http://cryto.net/~joepie91/blog/2015/07/19/why-you-should-never-ever-ever-use-mongodb/)
* [mongeez allows you to manage changes of your mongo documents and propagate these changes in sync with your code changes when you perform deployments](http://secondmarket.github.io/mongeez/)
* [MemDB - Distributed Transactional In-Memory Database](https://github.com/rain1017/memdb)
* [NSP로 구현한 API 예제](https://github.com/Hanul/nsp-sample-restful)
* [MongoDB를 쓰면서 알게 된 것들](http://bigmatch.i-um.net/2013/12/mongodb%EB%A5%BC-%EC%93%B0%EB%A9%B4%EC%84%9C-%EC%95%8C%EA%B2%8C-%EB%90%9C-%EA%B2%83%EB%93%A4/)

# [PipelineDB](http://www.pipelinedb.com/)
* [파이프라인DB, 오픈소스 스트리밍 SQL DB 출시](http://www.bloter.net/archives/231952)

# [Pyro: A Spatial-Temporal Big-Data Storage System](https://www.usenix.org/conference/atc15/technical-session/presentation/li_shen)

# Realm
* [Between 사용 사례: APT를 활용한 Realm 마이그레이션](https://realm.io/kr/news/realm-meetup-vcnc-between-case-study/)

# RethinkDB
* [Building better Node.js apps with RethinkDB](https://nodecraft.com/blog/dev/building-better-node-js-apps-with-rethinkdb)
* [Render realtime RethinkDB results in React](https://github.com/mikemintz/react-rethinkdb)
* [Rethinking temperature, sensors, and Raspberry Pi](http://rethinkdb.com/blog/temperature-sensors-and-a-side-of-pi/)
* [Optimizing a Big RethinkDB Query, and a Correction](http://rob.conery.io/2015/04/18/optimizing-a-big-rethinkdb-query-and-a-correction/)
* [The 3REE Stack: React + Redux + RethinkDB + Express.js](http://blog.workshape.io/the-3ree-stack-react-redux-rethinkdb-express-js/)

# Riak
* [Dynamiq - A simple implimentation of a queue on top of riak](https://github.com/Tapjoy/dynamiq)

# [RocketDB](http://rocketdb.io/)

# Spanner
* [글로벌 분산 데이터베이스 Spanner](http://d2.naver.com/helloworld/216593)

# [Tarantool - Get your data in RAM. Get compute close to data. Enjoy the performance](http://tarantool.org/)

# [Terracotta](http://terracotta.org/products/bigmemory)

# [TiDB is a distributed SQL database](https://github.com/pingcap/tidb)

# [ZeroDB, an end-to-end encrypted database, is open source!](http://blog.zerodb.io/zerodb-open-source-announcement/)
