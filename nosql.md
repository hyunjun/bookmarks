NoSQL
=====
* [Cassandra vs MongoDB vs CouchDB vs Redis vs Riak vs HBase vs Couchbase vs OrientDB vs Aerospike vs Neo4j vs Hypertable vs ElasticSearch vs Accumulo vs VoltDB vs Scalaris comparison](http://kkovacs.eu/cassandra-vs-mongodb-vs-couchdb-vs-redis)
* [Acquisition of Seismic, Hydroacoustic, and Infrasonic Data with Hadoop and Accumulo](http://srl.geoscienceworld.org/content/88/6/1553)
  * 미국 국립 데이터 센터가 시계열 데이터를 수집하기 위해 HDFS, Apache Accumulo, Apache NiFi 및 Apache Zeppelin을 기반으로 하는 새로운 시스템을 어떻게 사용하고 있는지 설명
  * 현재 200 센서에서 거의 500,000 event/sec을 처리
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
* [2016: The Year in Big Data](https://dzone.com/articles/2016-the-year-in-big-data)
* [Shasta: Interactive reporting at scale](https://blog.acolyer.org/2017/01/10/shasta-interactive-reporting-at-scale/) Shastr 논문 요약
  * Shasta는 구글의 F1이라고 불리는 RDBMS 및 데이터 시스템의 꼭대기에 위치한 OLTP/OLAP 시스템
  * Shasta의 핵심은 SQL보다 유연한 관계형 뷰 언어(Relational View Languase)라는 점
* [Distributed Algorithms in NoSQL Databases](https://highlyscalable.wordpress.com/2012/09/18/distributed-algorithms-in-nosql-databases)
  * NoSQL 데이터베이스 분산 오퍼레이션과 관련 기술에 대해 설명
* [Introduction to: Triplestores](http://www.dataversity.net/introduction-to-triplestores/)
* [How to Create a Stream System with Tens of Millions of Feeds?](https://medium.com/@alitech_2017/how-to-create-a-stream-system-with-tens-of-millions-of-feeds-6df06e302c78)

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
* [NoSQL Performance Benchmark 2018 – MongoDB, PostgreSQL, OrientDB, Neo4j and ArangoDB](https://www.arangodb.com/2018/02/nosql-performance-benchmark-2018-mongodb-postgresql-orientdb-neo4j-arangodb)

# [Aerospike](http://www.aerospike.com/) High performance NoSQL database delivering speed at scale
* [Call me maybe: Aerospike](https://aphyr.com/posts/324-call-me-maybe-aerospike)

# [AtlasDB is a transactional layer on top of a key value store](https://github.com/palantir/atlasdb)

# Azure DocumentDB
* [NoSQL database service Azure DocumentDB now Generally Available](http://azure.microsoft.com/blog/2015/04/08/nosql-database-service-azure-documentdb-now-generally-available)

# Benchmark
* **[Yahoo! Cloud System Benchmark (YCSB)](https://github.com/brianfrankcooper/YCSB)**

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
* [복합 기본 키(compound primary key)](http://knight76.tistory.com/entry/cassandra3-%EB%B3%B5%ED%95%A9-%EA%B8%B0%EB%B3%B8-%ED%82%A4)
* [cassandra의 라이브러리를 사용한 UUID version1 테스트](http://knight76.tistory.com/entry/cassandra%EC%9D%98-%EB%9D%BC%EC%9D%B4%EB%B8%8C%EB%9F%AC%EB%A6%AC%EB%A5%BC-%EC%82%AC%EC%9A%A9%ED%95%9C-UUID-version1-%ED%85%8C%EC%8A%A4%ED%8A%B8)
* [null의 개념(http://knight76.tistory.com/entry/cassandra-null%EC%9D%98-%EA%B0%9C%EB%85%90)
* Phantom - Reactive type-safe Scala driver for Apache Cassandra/Datastax Enterprise
  * [Getting Started With Phantom](https://blog.knoldus.com/2017/09/24/getting-started-with-phantom/)
* [Store Semantic Web Triples into Cassandra](https://blog.knoldus.com/2017/11/22/store-semantic-web-triples-into-cassandra/)

# [ceph](http://ceph.com/)
* [처음 만난 ceph](http://knight76.tistory.com/entry/%ED%8E%8C%EC%A7%88-%EC%B2%98%EC%9D%8C-%EB%A7%8C%EB%82%9C-ceph)

# [CockroachDB](https://github.com/cockroachdb/cockroach)
* [How CockroachDB Does Distributed, Atomic Transactions](http://www.cockroachlabs.com/blog/how-cockroachdb-distributes-atomic-transactions/)
* [SQL in CockroachDB: Mapping Table Data to Key-Value Storage](http://www.cockroachlabs.com/blog/sql-in-cockroachdb-mapping-table-data-to-key-value-storage/)
* [Why Go Was the Right Choice for CockroachDB](http://www.cockroachlabs.com/blog/why-go-was-the-right-choice-for-cockroachdb/)
* [CockroachDB beta-20160829](https://jepsen.io/analyses/cockroachdb-beta-20160829) Google Spanner와 유사한 디자인이 목표
* [Handling Contention with CockroachDB](https://medium.com/learning-with-diagrams/handling-contention-with-cockroachdb-aee872771412)
  * Multiversion concurrency, 트랜잭션 큐(동시 트랜잭션에 대한 추가 기능)을 다이어그램을 통해 설명

# CouchBase
* [QUERY TRANSLATOR - SQL TO COUCHBASE N1QL](http://www.querycouchbase.com/#/query)
* [Couchbase Spring data repository 적용기(1)](http://tmondev.blog.me/221016955783)
* [Couchbase Spring data repository 적용기(2)](http://tmondev.blog.me/221022211160)
* [Couchbase Spring data repository 적용기(3)](http://tmondev.blog.me/221024529817)

# CouchDB
* [Let’s learn Erlang and fix a bug on a CouchDB Cluster #1](http://robert-kowalski.de/blog/lets-learn-erlang-and-fix-a-bug-on-a-couchdb-cluster/)
* [Open-Sourcing IBM Cloudant’s CouchDB Search Integration with Lucene](https://cloudant.com/blog/open-sourcing-cloudant-search)

# CryptDB
* [CryptDB - A database system that can process SQL queries over encrypted data](https://github.com/CryptDB/cryptdb)

# [Datomic](http://www.datomic.com/)

# [Ehcache: Java's Most Widely-Used Cache](http://ehcache.org/)

# [EnnoDB](http://twigtechnology.com/blog/2015/06/11/announcing-ennodb/)

# [FiloDB](http://velvia.github.io/Introducing-FiloDB/)
* [2017 High Performance Database with Scala, Akka, Spark](https://www.slideshare.net/EvanChan2/2017-high-performance-database-with-scala-akka-spark)

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
  * [구글 클라우드 빅데이터 분석 서비스를 활용한 아이폰7 SNS 메시지 반응 분석](http://whitechoi.tistory.com/33)
  * [대용량 로그분석 Bigquery로 간단히 사용하기](https://www.slideshare.net/secret/nrUbS8uh6Bs3H0)
  * [빅쿼리 Streaming Insert - go lang 샘플](http://whitechoi.tistory.com/47)
  * [BigQuery 데이터 로드시에 분할해서 로드하기 - #1](https://jungwoon.github.io/bigquery/2017/09/28/BigQuery-Partitioning-1/)
  * [BigQuery 데이터 로드시에 분할해서 로드하기 - #2](https://jungwoon.github.io/bigquery/2017/09/29/BigQuery-Partitioning-2/)
  * [BigQuery 기본 사용법](https://jungwoon.github.io/bigquery/2017/10/31/BigQuery-Syntax/)
  * [빅쿼리 대쉬 보드를 위한 오픈소스 메타 베이스](http://bcho.tistory.com/1232)
* [Cloud Bigtable](https://cloud.google.com/bigtable/)
  * [Announcing Google Cloud Bigtable: The same database that powers Google Search, Gmail and Analytics is now available on Google Cloud Platform](http://googlecloudplatform.blogspot.kr/2015/05/introducing-Google-Cloud-Bigtable.html)
  * [Cloud Launcher](https://cloud.google.com/launcher/explore)
  * [Google Cloud Next '17에서 발표된 100가지 소식!](https://developers-kr.googleblog.com/2017/04/100-announcements-google-cloud-next-17.html)
  * [Data Loss Prevention API 사용하기](http://whitechoi.tistory.com/46)
  * [jybaek.tistory.com/m/category/개발/Cloud(GCP)](http://jybaek.tistory.com/m/category/%EA%B0%9C%EB%B0%9C/Cloud%20%28GCP%29)
* [Firebase](https://firebase.google.com/)
  * [Introducing Cloud Firestore: Google's New Document Database for Apps](https://firebase.googleblog.com/2017/10/introducing-cloud-firestore.html)
    * 모바일 및 웹앱 개발을 위한 docuemnt database
    * Documents and collections with powerful querying
    * iOS, Android, and Web SDKs with offline data access
    * Real-time data synchronization
    * Automatic, multi-region data replication with strong consistency
    * Node, Python, Go, and Java server SDKs
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
  * [Google Cloud Platform for Mobile Backend](https://www.youtube.com/watch?v=fz5n4l6K6gk)
  * [Mobile App Development using Firebase](https://www.youtube.com/watch?v=IIA_gGyk14g)
  * [Mobile Data Analysis using Firebase Analytics and BigQuery](https://www.youtube.com/watch?v=xCK9ChQVmho)
  * [유다시티, ‘파이어베이스’ 무료 온라인 강의 공개](http://www.bloter.net/archives/267282)
  * [파이어베이스를 이용한 유니티 게임 로그 분석](http://bcho.tistory.com/1145)
  * [Gcp event firebase 20161214](https://www.slideshare.net/secret/2N2CpAMPzEcbIn)
  * [FIREBASE AUTHENTICATION을 이용한 FACEBOOK 로그인 연동하기](https://jungwoon.github.io/jungwoon.github.io/Firebase-Authentication-Facebook/)
  * [FIREBASE AUTHENTICATION을 이용한 GOOGLE LOGIN API 연동하기](https://jungwoon.github.io/jungwoon.github.io/Firebase-Authentication-Google-Login-API/)
  * [FIREBASE AUTHENTICATION을 이용한 로그인 및 회원가입 연동하기](https://jungwoon.github.io/jungwoon.github.io/Firebase-Authentication/)
  * Firebase를 활용한 App 개발
    * [#1 안드로이드 스튜디오 설치 (mac 기준)](http://gomcine.tistory.com/entry/firebase%EB%A5%BC-%ED%99%9C%EC%9A%A9%ED%95%9C-App-%EA%B0%9C%EB%B0%9C-1-%EC%95%88%EB%93%9C%EB%A1%9C%EC%9D%B4%EB%93%9C-%EC%8A%A4%ED%8A%9C%EB%94%94%EC%98%A4-%EC%84%A4%EC%B9%98)
    * [#2 Firebase 프로젝트 생성](http://gomcine.tistory.com/entry/Firebase%EB%A5%BC-%ED%99%9C%EC%9A%A9%ED%95%9C-App-%EA%B0%9C%EB%B0%9C-2-Firebase-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EC%83%9D%EC%84%B1)
  * [파이어베이스를 이용한 간단한 웹 어플리케이션 만들기](https://www.inflearn.com/course/%ED%8C%8C%EC%9D%B4%EC%96%B4%EB%B2%A0%EC%9D%B4%EC%8A%A4-%EA%B0%95%EC%A2%8C-%EC%9B%B9-%EC%96%B4%ED%94%8C%EB%A6%AC%EC%BC%80%EC%9D%B4%EC%85%98/)
  * [Firebase 실시간 데이터베이스 성능 프로파일링](https://developers-kr.googleblog.com/2017/04/profiling-your-realtime-database.html)
  * [Firebase를 위한 Cloud Functions을 소개합니다](https://developers-kr.googleblog.com/2017/04/introducing-cloud-functions-for-firebase.html)
  * [Back-End (BaaS)/Firebase - Hosting 카테고리](http://namhoon.kim/category/Back-End%20%28BaaS%29/Firebase%20-%20Hosting)
  * [Google I/O 2017에서 선보인 Firebase의 새로운 기능을 소개합니다](https://developers-kr.googleblog.com/2017/05/whats-new-from-firebase-at-google-io.html)
  * [Zero to App: Live coding a Firebase app in JavaScript, Kotlin, and Swift (Google I/O '17)](https://www.youtube.com/watch?v=01M_hZav9Gw)
  * [Cloud Functions for Firebase를 사용할 때 Promise도 함께 사용하는 방법을 확인해 보세요](https://developers-kr.googleblog.com/2017/07/keep-your-promises-when-using-cloud.html)
  * [Python Admin SDK에서 데이터베이스 액세스하는 방법을 확인해 보세요](https://developers-kr.googleblog.com/2017/07/accessing-database-from-python-admin-sdk.html)
  * [Cloud Functions 셸을 통한 로컬에서의 함수 테스트에 대해 알아보세요](https://developers-kr.googleblog.com/2017/10/testing-functions-locally-with-cloud-functions-for-firebase.html)
  * [Google Firebase Cloud Messaging 사용하기 (iOS) — 1부](https://medium.com/@zida.papa/google-firebase-cloud-messaging-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0-ios-1%EB%B6%80-b739f7c87d50)
  * [안드로이드 & 아이폰 푸시 알람 영상](https://www.youtube.com/watch?v=gOaPrmYrMAs)
* [The Google Stack](http://malteschwarzkopf.de/research/assets/google-stack.pdf)
  * [What is the open source version of Google Cloud Dataflow?](http://www.quora.com/What-is-the-open-source-version-of-Google-Cloud-Dataflow)
  * [Google Dataflow A Unified Model for Batch and Streaming Data Processing](https://www.youtube.com/watch?v=3UfZN59Nsk8)
  * [한시간에 만드는 대용량 로그 수집 시스템](http://bcho.tistory.com/1158)
  * [Firebase Admin SDK for Go를 소개합니다](https://developers-kr.googleblog.com/2017/09/introducing-firebase-admin-sdk-for-go.html)
  * [Google Cloud에서 Dataflow 정리](https://jungwoon.github.io/google%20cloud/2017/12/13/Google-Dataflow/)

# [Greenplum Database (GPDB)](https://github.com/greenplum-db/gpdb)

# [H2 Database Engine](http://www.h2database.com/)

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

# MapD; C++로 구현, GPU 기반의 In-Memory Columnar SQL DB
* [MapD: Massive Throughput Database Queries with LLVM on GPUs](http://devblogs.nvidia.com/parallelforall/mapd-massive-throughput-database-queries-llvm-gpus/)
* [MapD Open Sources GPU-Powered Database](https://www.mapd.com/blog/2017/05/08/mapd-open-sources-gpu-powered-database/)

# Memcached
* [MONITORING GROWING MEMCACHED](http://engineering.vinted.com/2015/06/09/monitoring-growing-memcached/)
* [libmc - Fast and light-weight memcached client for C++/Python https://pypi.python.org/pypi/libmc/](https://github.com/douban/libmc)
* [memcache internals](https://www.adayinthelifeof.nl/2011/02/06/memcache-internals/)
* [입 개발 아는 사람은 알지만 모르는 사람은 모르는 memcached expire 이슈…](http://www.popit.kr/%EC%9E%85-%EA%B0%9C%EB%B0%9C-%EC%95%84%EB%8A%94-%EC%82%AC%EB%9E%8C%EC%9D%80-%EC%95%8C%EC%A7%80%EB%A7%8C-%EB%AA%A8%EB%A5%B4%EB%8A%94-%EC%82%AC%EB%9E%8C%EC%9D%80-%EB%AA%A8%EB%A5%B4%EB%8A%94-memcached/)

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
* [Episode 1 - Mongo DB Is Web Scale](https://www.youtube.com/watch?v=b2F-DItXtZs)
* [zerocho.com/category/MongoDB](https://www.zerocho.com/category/MongoDB)
* [MongoDB 스키마 디자인을 위한 6가지 규칙 요약](http://www.haruair.com/blog/3055)
* [Motor: Asynchronous Python driver for MongoDB](https://motor.readthedocs.io/)
* [MongoDB에서 쉽게 데이터 옮기기](http://blog.kazikai.net/?p=188)
* [MultiThread로 RabbitMQ에서 메세지를 읽어서 MongoDB에 쓰는 예제 (Python)](http://bcho.tistory.com/category/%ED%81%B4%EB%9D%BC%EC%9A%B0%EB%93%9C%20%EC%BB%B4%ED%93%A8%ED%8C%85%20%26%20NoSQL/MongoDB)
* [Mongoose(몽구스) 쿼리 빌더](https://www.zerocho.com/category/MongoDB/post/59bd148b1474c800194b695a)
* [MongoDB gets support for multi-document ACID transactions](https://techcrunch.com/2018/02/15/mongodb-gets-support-for-multi-document-acid-transactions/)
* [How to set up a database if you’re a front-end developer](https://medium.freecodecamp.org/how-to-set-up-a-database-if-youre-a-front-end-developer-3ed945221219)

# [PipelineDB](http://www.pipelinedb.com/)
* [파이프라인DB, 오픈소스 스트리밍 SQL DB 출시](http://www.bloter.net/archives/231952)

# [Pyro: A Spatial-Temporal Big-Data Storage System](https://www.usenix.org/conference/atc15/technical-session/presentation/li_shen)

# Realm
* [Between 사용 사례: APT를 활용한 Realm 마이그레이션](https://realm.io/kr/news/realm-meetup-vcnc-between-case-study/)
* **[실시간 데이터베이스 비교: Realm 모바일 플랫폼 vs. Firebase](https://realm.io/kr/news/welcome-to-reactive-world/)**
* [좌충우돌 Realm 모바일 플랫폼 사용기](https://realm.io/kr/news/develop-app-in-3-days-with-rmp/)
* [데모와 함께 하는 Realm 모바일 플랫폼 따라잡기: Scanner, RealmPop 예제](https://realm.io/kr/news/realm-mobile-platform-demos/)
* [Realm Java 3.1: 객체 알림, 백업 복구, 역 관계](https://realm.io/kr/news/realm-java-3-1/)
* [프알못의 Realm 사용기 + 라이브 코딩 데모](https://realm.io/kr/news/realm-swift-live-coding-beginner/)
* [Realm 내부 구조와 동작 원리 자세히 살펴보기](https://realm.io/kr/news/anatomy-of-realm/)
* [OrangeRealm helps you safety multithreading and UI integration using Realm](https://github.com/pisces/OrangeRealm)
* [Realm의 서버리스 로직: Realm Functions를 소개합니다](https://news.realm.io/kr/news/serverless-logic-with-realm-introducing-realm-functions/)
* [Realm SDK로 관심사별 로직을 간단명료하게 분리하세요](https://news.realm.io/kr/news/realm-sdk-clean-easy-separation-of-concerns/)
* [라이브 오브젝트와 정밀한 알림: Realm 업데이트 기능](http://news.realm.io/kr/news/live-objects-fine-grained-notifications-realm-update/)
* [최신 모바일 애플리케이션을 위한 데이터베이스, Realm의 개발 전략](http://news.realm.io/kr/news/modern-development-strategies-realm/)
* [Realm 모바일 데이터베이스부터 플랫폼까지, Realm 사용자 모임의 발표를 공유합니다](http://news.realm.io/kr/news/realm-world-tour-seoul/)
* [동기 Realm 마이그레이션 가이드](http://news.realm.io/kr/news/migrations-with-synced-realms/)
* [학습 경로: Realm 이해하기](https://academy.realm.io/kr/posts/learning-path-understanding-realm/)
* [골치아픈 REST API에서 벗어나 효율적인 모바일 네트워크를 구성하는 방법](https://academy.realm.io/kr/posts/best-practices-pain-points-mobile-networking-rest-api-failures/)
* **[데이터베이스를 설계하며 배운것들:Realm 스레드 깊게 들여보기](https://academy.realm.io/kr/posts/threading-deep-dive/)**

# RethinkDB
* [Building better Node.js apps with RethinkDB](https://nodecraft.com/blog/dev/building-better-node-js-apps-with-rethinkdb)
* [Render realtime RethinkDB results in React](https://github.com/mikemintz/react-rethinkdb)
* [Rethinking temperature, sensors, and Raspberry Pi](http://rethinkdb.com/blog/temperature-sensors-and-a-side-of-pi/)
* [Optimizing a Big RethinkDB Query, and a Correction](http://rob.conery.io/2015/04/18/optimizing-a-big-rethinkdb-query-and-a-correction/)
* [The 3REE Stack: React + Redux + RethinkDB + Express.js](http://blog.workshape.io/the-3ree-stack-react-redux-rethinkdb-express-js/)
* [RethinkDB 시작하기](http://mobicon.tistory.com/502)
* [RethinkDB: why we failed](http://www.defmacro.org/2017/01/18/why-rethinkdb-failed.html)

# Riak
* [Dynamiq - A simple implimentation of a queue on top of riak](https://github.com/Tapjoy/dynamiq)

# [RocketDB](http://rocketdb.io/)

# RYE
* [rye, 샤딩을 지원하는 오픈소스 관계형 dbms](https://www.slideshare.net/deview/223rye-dbms)

# Spanner
* [글로벌 분산 데이터베이스 Spanner](http://d2.naver.com/helloworld/216593)
* [Spanner, TrueTime & The CAP Theorem](https://cloud.google.com/spanner/docs/whitepapers/SpannerAndCap.pdf)
* [Introducing Cloud Spanner: a global database service for mission-critical applications](https://cloudplatform.googleblog.com/2017/02/introducing-Cloud-Spanner-a-global-database-service-for-mission-critical-applications.html)
* [CLOUD SPANNER - The first horizontally scalable, globally consistent, relational database service](https://cloud.google.com/spanner)
* ['구글 스패너'···막 오르는 SQL 데이터베이스 새 시대](http://www.ciokorea.com/news/34274)
* [How we built a brand new bank on GCP and Cloud Spanner: Shine](https://cloudplatform.googleblog.com/2017/09/how-shine-built-bank-on-gcp-and-cloud-spanner.html)
* [Google Cloud’s Distributed Relational Database Spanner Goes Global](https://thenewstack.io/google-takes-cloud-spanner-global)
  * 올해 초 regional offering으로 출시된 Google의 분산 관계형 데이터 저장소인 Google Cloud Spanner가 글로벌로 확대
  * Google은 MySQL 구현에 필요한 수동 샤딩이 지나치게 다루기 힘들어서 10년 전부터 AdWords나 Google Play에 Cloud Spanner를 적용해서 사용하다가 출시
* [Why you should pick strong consistency, whenever possible](https://cloudplatform.googleblog.com/2018/01/why-you-should-pick-strong-consistency-whenever-possible.html)
  * Google Cloud Spanner가 multi-master replication과 다른점을 포함한 external consistency를 보장

# Splunk
* [Falkonry for Splunk](https://www.youtube.com/watch?v=zJ7NWNel80c)

# Scylla
* [ScyllaDB: world's fastest NoSQL column store database Fully compatible with Apache Cassandra at 10x the throughput and jaw dropping low latency](http://www.scylladb.com/)
* [Supporting 4 Million transactions per second and 7 TB of data per node with Scylla on Oracle Cloud Infrastructure](https://blogs.oracle.com/cloud-infrastructure/scylla-on-oracle-cloud-infrastructure)
* [Scylla Summit 2017: Running a Soft Real-time Service at One Million QPS](https://youtu.be/HhGvA75F1xM)

# [Tarantool - Get your data in RAM. Get compute close to data. Enjoy the performance](http://tarantool.org/)

# [Terracotta](http://terracotta.org/products/bigmemory)

# [TileDB](http://tiledb.io/)
* [TileDB](http://tiledb.io/)
  * 고밀도 다차원 배열을 지원하도록 설계된 새로운 데이터베이스
  * 현재 HDFS, S3, GFS 등 다양한 백엔드와 결합 가능

# Time Series DB
* IRONdb; Circonus에서 개발 한 상업용 시계열 데이터베이스
  * [Fred Moyer: Solving the Technical Challenges of Time Series Databases at Scale](https://www.youtube.com/watch?v=QBatpIFii7M&feature=youtu.be)
    * 시계열 데이터베이스는 시간별로 인덱싱된 데이터 집합을 처리하도록 최적화
    * 데이터 저장, 데이터 안전 및 IOPS 문제는 모든 TSDB가 직면한 문제
    * Fred는 IRONdb가 이러한 기술적 문제를 해결하거나 완전히 피하는 방법에 대해 설명

# [TiDB is a distributed SQL database](https://github.com/pingcap/tidb)
* [TiDB introduction](https://www.pingcap.com/docs/overview/#tidb-introduction)
* [Running TiDB on Kubernetes](https://banzaicloud.com/blog/tidb-kubernetes/) Kubernetes에서 TiDB를 실행하는 방법

# Trafodion Hadoop/HBase에서 Transaction SQL을 구현
* [The Apache Software Foundation Announces Apache® Trafodion™ as a Top-Level Project](https://blogs.apache.org/foundation/entry/the-apache-software-foundation-announces27)

# Venice; Linkedin 에서 사용하고 있는 분산 Key-Value 데이터베이스 
* [Venice Hybrid: Doing Lambda Better](https://engineering.linkedin.com/blog/2017/12/venice-hybrid--doing-lambda-better) Venice를 통해 Lambda 아키텍처를 구현하는 것을 설명

# [ZeroDB, an end-to-end encrypted database, is open source!](http://blog.zerodb.io/zerodb-open-source-announcement/)
