HBase
=====
* [World's 10 Big HBase Database Cluster Details](http://blog.bizosys.com/2014/05/worlds-10-big-hbase-database-cluster.html)
* [The HBase Request Throttling Feature](https://blogs.apache.org/hbase/entry/the_hbase_request_throttling_feature)
* [Scalable Distributed Transactional Queues on HBase](http://blog.cask.co/2015/05/scalable-distributed-transactional-queues/)
* [hbasecon](http://hbasecon.com/)
  * [HBaseCon 2017](https://easychair.org/cfp/hbasecon2017)
  * [agenda](http://www.hbasecon.com/#agenda)
    * [HBase Conf 2016 - Cloudera Youtube](https://www.youtube.com/playlist?list=PLe-h9HrA9qfDVOeNh1l_T5HvwvkO9raWy)
* [Make Endpoint Coprocessors Available from Thrift](https://issues.apache.org/jira/browse/HBASE-5600)
* [Apache HBase Application Archetypes](http://www.slideshare.net/cloudera/141120-hbasearchetypesstratahw142)
* [HBase at Xiaomi](http://www.slideshare.net/HBaseCon/features-session-4)
* [HbaseCon](http://www.slideshare.net/HBaseCon)
* examples
  * [from hbase to graph DB](https://gist.github.com/hyunjun/55f83bfd91e2b1e24f46) read hbase using pig, java
* [Apache Spark Comes to Apache HBase with HBase-Spark Module](http://blog.cloudera.com/blog/2015/08/apache-spark-comes-to-apache-hbase-with-hbase-spark-module/?elq=b8eb31d395f14250a2c264604a98ed0e&elqCampaignId=987&elqaid=2217&elqat=1&elqTrackId=8472a26fbfcb4511b1a86953234a7bed)
* [Introduction to HBase Schema Design](http://0b4af6cdc2f0c5998459-c0245c5c937c5dedcca3f1764ecc9b2f.r43.cf2.rackcdn.com/9353-login1210_khurana.pdf)
* [발 번역 HBase I/O – HFile](https://charsyam.wordpress.com/2012/07/01/발-번역-hbase-io-hfile/)
* [HBase shell commands](https://learnhbase.wordpress.com/2013/03/02/hbase-shell-commands/)
* [Hadoop Summit San Jose 2016](https://www.youtube.com/playlist?list=PLKnYDs_-dq16K1NH83Bke2dGGUO3YKZ5b)
* [Monitoring HBase with Prometheus](https://blog.godatadriven.com/hbase-prometheus-monitoring)
  * 오픈 소스 모니터링 시스템인 Prometheus에 HBase 메트릭을 연결하는 방법
* [Offheap Read-Path in Production – The Alibaba story](http://blog.cloudera.com/blog/2017/03/offheap-read-path-in-production-the-alibaba-story/) 알리바바에서 Off-heap Cache를 사용한 예
* [Accordion: HBase Breathes with In-Memory Compaction](https://blogs.apache.org/hbase/entry/accordion-hbase-breathes-with-in)
* [Accordion: Developer View of In-Memory Compaction](https://blogs.apache.org/hbase/entry/accordion-developer-view-of-in)
* [Tips for Migrating to Apache HBase on Amazon S3 from HDFS](https://aws.amazon.com/blogs/big-data/tips-for-migrating-to-apache-hbase-on-amazon-s3-from-hdfs/)
  * HBase 클러스터를 S3로 마이그레이션하기 위한 다양한 옵션 소개
* [HBase 로컬 설치와 연동](http://astrod.github.io/2017/05/29/HBase-%EB%A1%9C%EC%BB%AC-%EC%84%A4%EC%B9%98%EC%99%80-%EC%97%B0%EB%8F%99.html)
* [Upgrading Pinterest to HBase 1.2 from 0.94](https://medium.com/@Pinterest_Engineering/upgrading-pinterest-to-hbase-1-2-from-0-94-e6e34c157783)
  * Thrift 기반의 복제를 이용한 HBase 마이그레이션
  * dual-client 기능을 구현하기 위해 클라이언트는 asynchbase 사용
* [Introducing Apache HBase Medium Object Storage (MOB) compaction partition policies](http://blog.cloudera.com/blog/2017/06/introducing-apache-hbase-medium-object-storage-mob-compaction-partition-policies/)
  * Apache HBase는 "Medium Object Storage" MOB 지원
  * MOB는 값이 특정 크기보다 클 경우 별도로 파일을 저장
  * 이 게시물에서는 생성 될 수 있는 MOB 파일의 수 때문에 NameNode의 메모리 문제를 해결하는 디자인의 향상된 기능 (주간 및 월간 파티셔닝 지원)을 설명
* [Measuring HBase cluster replication overhead](https://github.daumkakao.com/jg-choi/hbase-replication-test)
* [HBASE APPLICATION ARCHETYPES REDUX2 (Part 2 of 2)](https://blogs.apache.org/hbase/entry/hbase-application-archetypes-redux2-part)
  * HBase 응용 프로그램의 아키텍처 타입에서 설명하고 있는 Apache Software Foundation 게시물
  * 문서, 그래프, 대기열 및 메트릭의 저장을 포함하여 네 가지 사용 사례에 대해 설명
* [BENCHMARK APACHE HBASE VS APACHE CASSANDRA ON SSD IN A CLOUD ENVIRONMENT](https://hortonworks.com/blog/hbase-cassandra-benchmark/)
  * HBase가 읽기 성능이 빠름, 작업 흐름이 무거울 때 Cassandra가 더 빠름
* [Database Comparison: An In-Depth Look at How MapR-DB Does What Cassandra, HBase, and Others Can't](https://mapr.com/blog/database-comparison-an-in-depth-look-at-mapr-db/)
  * MapR과 Apache HBase 및 Apache Cassandra와의 아키텍처를 비교
* [AMBARI KERBEROS SUPPORT FOR HBASE PART 1](https://ko.hortonworks.com/blog/ambari-kerberos-support-hbase-1/)
  * Ambari를 사용하여 Kerberos Hadoop 및 HBase 클러스터를 설정하기 위한 자습서
* HBase 와 구글의 빅테이블
  * [#1 아키텍쳐](http://bcho.tistory.com/1217)
  * [#2 - 설치 및 기본 사용 방법](http://bcho.tistory.com/1219)

# Library
* kakao의 오픈소스
  * [HBase Region Inspector](http://tech.kakao.com/2016/03/11/opensource-3-hri/)
  * [HBase Tools](http://tech.kakao.com/2016/03/24/opensource-4-hbase-tools/)
  * [hbase-packet-inspector](https://github.com/kakao/hbase-packet-inspector)
    * [hbase-packet-inspector](http://tech.kakao.com/2017/09/22/opensource-8-hbase-packet-inspector/)
* [Omid reloaded: scalable and highly-available transaction processing](https://blog.acolyer.org/2017/03/17/omid-reloaded-scalable-and-highly-available-transaction-processing/) Yahoo에서 개발한 Apache HBase 상단의 트랜잭션 계층
* [Secondary index on HBase http://tristartom.github.io/docs/ccgrid15.pdf](https://github.com/tristartom/nosql-indexing)

# Python
* [happybase](https://happybase.readthedocs.org/en/latest/user.html)
  * [miscellaneous](https://gist.github.com/hyunjun/0f5f21b45d7d2c02c564) troubleshooting
