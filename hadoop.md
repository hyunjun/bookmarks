Hadoop
======

* [Hadoop Interview Questions – MapReduce](https://intellipaat.com/blog/hadoop-interview-questions-mapreduce/)
* [Quick Line Count - Hadoop](http://dronamk.blogspot.kr/2012/10/quick-line-count-hadoop.html)
* [Hadoop Programming with Arbitrary Languages](https://acct.rcc.fsu.edu/docs/hadoop-programming-arbitrary-languages) word count + hadoop streaming in c/c++/python/shell script
* [Nobody ever got fired for using Hadoop on a cluster](http://research.microsoft.com/pubs/163083/hotcbp12%20final.pdf)
* [The Improved Job Scheduling Algorithm of Hadoop Platform](http://arxiv.org/abs/1506.03004)
* Test
  * [Testing the Installation](https://www.cloudera.com/documentation/enterprise/5-4-x/topics/cm_ig_testing_the_install.html)
  * [The "Getting Started with Hadoop" Tutorial](https://www.cloudera.com/developers/get-started-with-hadoop-tutorial/data-governance-and-compliance.html)
* [Streaming](https://hadoop.apache.org/docs/r1.2.1/streaming.html)
  * [python example](https://github.com/hyunjun/practice/tree/master/hadoop/Streaming)
  * [perl example](https://github.com/hyunjun/practice/tree/master/hadoop/Streaming_perl)
  * [Hadoop streaming - remove trailing tab from reducer output](http://stackoverflow.com/questions/18133290/hadoop-streaming-remove-trailing-tab-from-reducer-output)
  * [hadoop streaming map.output.key.field.separator](http://blog.sina.com.cn/s/blog_5357c0af0101mgak.html)
  * [Hadoop Streaming the order of reducer output files is messed up when sorting](http://stackoverflow.com/questions/33310987/hadoop-streaming-the-order-of-reducer-output-files-is-messed-up-when-sorting)
* [피보탈, 아파치재단에 분석엔진·머신러닝 기술 제공](http://www.bloter.net/archives/240300)
* [mapr hadoop training](https://www.mapr.com/services/mapr-academy/big-data-hadoop-online-training)
* [Introduction to Big Data and Hadoop for Beginners | Big Data Tutorial Training Video](https://www.youtube.com/watch?v=pg3f1ftPlZU)
* [learn hadoop spark by examples](https://www.java-success.com/category/tutorial/hadoop-tutorials/learn-hadoop-spark-by-examples/)
* balancer `sudo hdfs balancer [-threshold n]`
  * [Running HDFS Balancer fail, report namenode.LeaseExpiredException](https://community.cloudera.com/t5/Storage-Random-Access-HDFS/Running-HDFS-Balancer-fail-report-namenode-LeaseExpiredException/td-p/14052)
  * [HDFS Commands, HDFS Permissions and HDFS Storage](http://www.informit.com/articles/article.aspx?p=2755708)
* [`hadoop fs -test -[defsz]`](http://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-common/FileSystemShell.html#test)
  * [hadoop fs -test example](http://jugnu-life.blogspot.com/2012/10/hadoop-fs-test-example.html)
  * [practice hadoop fs -test](https://gist.github.com/hyunjun/35700e8e8dc4a7be2a97f24f7144be4e)
* hadoop streaming with jar
  * cluster의 모든 local directory에 필요한 파일을 모두 복사하지 않고, library를 hdfs에 올려서 참조
  * 필요한 파일을 jar로 묶어 hdfs에 올리고, -archives option으로 참조
  * ref
    * [Specifying the Number of Reducers](http://hadoop.apache.org/docs/stable/hadoop-streaming/HadoopStreaming.html#Specifying_the_Number_of_Reducers) 당연히 결과는 reducer 개수만큼 출력
  * zipimport; local에서는 잘 동작하지만, streaming은 실패함
    * [hadoop-how-to-include-third-party-library-in-python-mapreduce](http://stackoverflow.com/questions/15352981/hadoop-how-to-include-third-party-library-in-python-mapreduce) 
    * [how-can-i-include-a-python-package-with-hadoop-streaming-job](http://stackoverflow.com/questions/6811549/how-can-i-include-a-python-package-with-hadoop-streaming-job)
    * [running-extrnal-python-lib-like-nltk-with-hadoop-streaming](http://stackoverflow.com/questions/24167933/running-extrnal-python-lib-like-nltk-with-hadoop-streaming/32135850#32135850)
  * [Using multiple mapper inputs in one streaming job on hadoop?](http://stackoverflow.com/questions/12180791/using-multiple-mapper-inputs-in-one-streaming-job-on-hadoop) -input을 원하는 개수만큼 사용
  * troubleshooting
    * python에서 mapper들의 공통 모듈이 있어서 별도의 file로 만들고(e.g. commons.py) `-files commons.py,mapper[n].py ... -mapper mapper[n].py`로 실행했더니 오류가 발생
      * 아마 path 문제로 mapper.py가 commons.py를 참조하지 못했을 가능성이 매우 크다
      * 해결책이 있겠지만, 일단 공통 모듈이 별로 크지 않으면 각 mapper[n].py에 넣어줘서 해결 -_-;;
    * `Container ... is running beyond physical memory limits`
      * `yarn.app.mapreduce.am.resource.mb` 1 > 2
      * `mapreduce.reduce.memory.mb` 1 > 2
      * `mapreduce.map.memory.mb` 1 > 2
      * `mapreduce.map.java.opts.max.heap` .768 > 1.5
      * `mapreduce.reduce.java.opts.max.heap` .768 > 1.5
      * `yarn.app.mapreduce.am.command-opts` -Xmx2048m
      * `mapreduce.map.java.opts` -Xmx1024m
      * `mapreduce.reduce.java.opts` -Xmx2048m
      * ref
        * [How to change memory in EMR hadoop streaming job](http://stackoverflow.com/questions/24091973/how-to-change-memory-in-emr-hadoop-streaming-job)
        * [Hadoop 2.2.0 Streaming Memory Limitation](http://stackoverflow.com/questions/21933937/hadoop-2-2-0-streaming-memory-limitation)
        * [Container is running beyond memory limits](http://stackoverflow.com/questions/21005643/container-is-running-beyond-memory-limits)
        * [How/Where to set limits to avoid error container running beyond physical memory limits](http://stackoverflow.com/questions/28571623/how-where-to-set-limits-to-avoid-error-container-running-beyond-physical-memory)
        * [Java 8 Over usage of virtual memory](https://issues.apache.org/jira/browse/HADOOP-11364)
        * [Hadoop Yarn memory settings in HDInsight](http://blogs.msdn.com/b/shanyu/archive/2014/07/31/hadoop-yarn-memory-settings-in-hdinsigh.aspx)
        * [Container is running beyond memory limits](http://www.chinabtp.com/container-is-running-beyond-memory-limits/)
        * [Container is running beyond memory limits](http://www.hitmaroc.net/191849-4083-container-running-beyond-memory-limits.html)
    * `Error: java.lang.RuntimeException: PipeMapRed.waitOutputThreads(): subprocess failed with code 1`
      * local script를 실행시켜서 정상 동작하는지부터 확인
      * 예를 들어 다음과 같이 some.jar를 사용하는 경우 jar file name에 -(dash)와 같은 character가 있으면 발생
        * ERROR

          ```hadoop jar /path/to/hadoop-streaming-*.jar -archives "hdfs://namenode/path/to/some-0.1.jar#library" -files [mapper] -input [input] -output [output] -mapper [mapper] -numReduceTasks 0```
        * OK

          ```hadoop jar /path/to/hadoop-streaming-*.jar -archives "hdfs://namenode/path/to/some.jar#library" -files [mapper] -input [input] -output [output] -mapper [mapper] -numReduceTasks 0```
      * mapper_a.py에서 other.py의 function foo를 호출하려고 import other; foo(...)을 한 경우. 아마 path 문제일 것으로 짐작
    * `ERROR streaming.StreamJob: Error Launching job : Input path does not exist`
      * hdfs directory와 local directory의 이름이 같은 경우 발생할 때가 있음
      * -input/-output에 `hdfs://[name node]/path/to/directory`처럼 절대 경로를 사용하거나 directory 이름을 unique하게 변경
    * [`java.lang.OutOfMemoryError: GC overhead limit exceeded`](http://stackoverflow.com/questions/10109572/gc-overhead-limit-exceeded-on-hadoop-20-datanode)
      * [datanode java option](_hadoop/datanode_java_opts.png) `http://x.y.z.w:port/cmf/services/16/config?q=datanode_java_opts`
    * Exit code 143; cannot find path(s) or file(s) in `-files` option on hdfs
    * performance problem
      * 별로 큰 문제가 아닌데도 성능이 이상하게 느린 경우, 환경 설정 문제일 수 있음
        * 문제; 12억 entry의 query count(disk에서 32GB)에서 bigram count를 구하는데, 몇 시간씩 소요
        * 원인; 실행하는 서버의 HADOOP_CONF_DIR에 yarn-site.xml이 없어서, yarn resource manager에 적절하게 할당이 되지 않았고, cloudera manager의 애플리케이션 탭에서 워크로드 요약도 볼 수 없었음
        * 해결; 실행하는 서버에 환경 설정 문제가 있어, 다른 서버에서 실행하니 resource manager에도 잘 등록되었고, (별다른 tuning 없이) 한 번 실행하는 데 대략 15m 정도 소요
* [7 Tips for Improving MapReduce Performance](http://blog.cloudera.com/blog/2009/12/7-tips-for-improving-mapreduce-performance/)
* [Hadoop Performance Tuning Best Practices](http://www.idryman.org/blog/2014/03/05/hadoop-performance-tuning-best-practices/)
* [Sparse matrix computations in MapReduce](http://www.slideshare.net/dgleich/sparse-matrix-computations-in-mapreduce)
* [A MapReduce Algorithm for Matrix Multiplication](http://www.norstad.org/matrix-multiply/)
* [Database Access with Apache Hadoop](https://archanaschangale.wordpress.com/2013/09/26/database-access-with-apache-hadoop/)
* [mapred-default](https://hadoop.apache.org/docs/stable/hadoop-mapreduce-client/hadoop-mapreduce-client-core/mapred-default.xml)
* [What is the maximum container(s) in a single-node cluster (hadoop)?](http://stackoverflow.com/questions/26540507/what-is-the-maximum-containers-in-a-single-node-cluster-hadoop)
* [How to sort reducer input values in hadoop](https://sites.google.com/site/hadoopandhive/home/ewewe)
* [Secondary sorting flags for Hadoop 0.20.2 streaming](http://blog.tomhennigan.co.uk/post/46330524717/secondary-sorting-flags-for-hadoop-0202)
* [쉽게 배우는 하둡 에코 시스템 2.0 (Hadoop ECO system 2.0)](http://blrunner.com/m/post/99)
* [Spark HDFS Integration](http://0x0fff.com/spark-hdfs-integration/)
* [Module 5: Advanced MapReduce Features](https://developer.yahoo.com/hadoop/tutorial/module5.html)
* **[Hadoop Streaming Made Simple using Joins and Keys with Python](https://allthingshadoop.com/2011/12/16/simple-hadoop-streaming-tutorial-using-joins-and-keys-with-python/)**
  * [Python Streaming Sample](https://github.com/joestein/amaunet)

    ```
$ cat countries.dat
United States|US
Canada|CA
United Kingdom|UK
Italy|IT

$ cat customers.dat
Alice Bob|not bad|US
Sam Sneed|valued|CA
Jon Sneed|valued|CA
Arnold Wesise|not so good|UK
Henry Bob|not bad|US
Yo Yo Ma|not so good|CA
Jon York|valued|CA
Alex Ball|valued|UK
Jim Davis|not so bad|JA

$ cat countries.dat
customers.dat | ./smplMapper.py | sort | ./smplReducer.py
Canada  not so good     1
Canada  valued  3
JA - Unkown Country     not so bad      1
not bad - Unkown Country        ITAlice Bob     1
United Kingdom  not so good     1
United Kingdom  valued  1
United States   not bad 1
    ```
* [Memory Storage Support in HDFS](https://hadoop.apache.org/docs/r2.7.1/hadoop-project-dist/hadoop-hdfs/MemoryStorage.html)
* [SK텔레콤, Hadoop DW 와 데이터 분석환경 구축사례](http://www.popit.kr/sk%ED%85%94%EB%A0%88%EC%BD%A4-hadoop-dw-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EB%B6%84%EC%84%9D%ED%99%98%EA%B2%BD-%EA%B5%AC%EC%B6%95%EC%82%AC%EB%A1%80/)
* [Hadoop NameNode 이중화 시 fencing의 역할](http://www.popit.kr/hadoop-namenode-%EC%9D%B4%EC%A4%91%ED%99%94-%EC%8B%9C-fencing-%EC%97%AD%ED%95%A0/)
* 하둡 인사이드
  * [1. Hadoop RPC](http://hamait.tistory.com/175)
  * [2. Hadoop Streamming](http://hamait.tistory.com/187)
  * [3. 하둡과 보안](http://hamait.tistory.com/184)
* [하둡 쉘 스크립트 실행 순서도](http://hamait.tistory.com/180)
* [업그레이드를 부르는 Hadoop 3.0 신규 기능 살펴보기](http://www.popit.kr/%EC%97%85%EA%B7%B8%EB%A0%88%EC%9D%B4%EB%93%9C%EB%A5%BC-%EB%B6%80%EB%A5%B4%EB%8A%94-hadoop-3-0-%EC%8B%A0%EA%B7%9C-%EA%B8%B0%EB%8A%A5-%EC%82%B4%ED%8E%B4%EB%B3%B4%EA%B8%B0/)
* [Hadoop 3.0 Ships, But What Does the Roadmap Reveal?](https://www.datanami.com/2017/12/15/hadoop-3-0-ships-roadmap-reveal/) 새로운 GPU 리소스 유형, Docker 지원, Long-running 서비스 지원, FPGAS 지원 S3-compatable blob store 등
* [HDFS Erasure Coding](http://hadoop.apache.org/docs/r3.0.0-alpha3/hadoop-project-dist/hadoop-hdfs/HDFSErasureCoding.html)
  * [Hadoop-3.0과 Erasure Coding 편집증](http://www.popit.kr/hadoop-3-0%EA%B3%BC-erasure-coding-%ED%8E%B8%EC%A7%91%EC%A6%9D/)
* [멀티테넌트 Hadoop 클러스터 운영 경험기](http://d2.naver.com/helloworld/0475200)
* [Performance comparison of different file formats and storage engines in the Hadoop ecosystem](https://db-blog.web.cern.ch/blog/zbigniew-baranowski/2017-01-performance-comparison-different-file-formats-and-storage-engines)
  * CERN에서 실행한 Apache Avro, Apache Parquet, Apache Kudu, Apache HBase benchmark (공간효율성, 수집속도, Scan속도, Random Access 속도)
  * 하둡 에코시스템에서 사용가능한 스토리지 엔진들 (Apache Avro, Apache Parquet, Apache HBase, Apache Kudu)을 비교분석한 기사
  * 패턴, 저장 구조 설계에 따라 그 때 그 때 성능이 달라지므로 참고만
  * space utilization, ingestion rate, random lookup latency, data scan rates
  * [A  STUDY OF  DATA  REPRESENTATION  IN  HADOOP  TO  OPTIMIZE  DATA  STORAGE AND SEARCH  PERFORMANCE FOR THE ATLAS EVENTINDEX](https://indico.cern.ch/event/505613/contributions/2230964/attachments/1346598/2039265/highlights_-200.pdf)
  * [A STUDY OF DATA REPRESENTATION IN HADOOP TO OPTIMIZE DATA STORAGE AND SEARCH PERFORMANCE FOR THE ATLAS EVENTINDEX](https://indico.cern.ch/event/505613/contributions/2230964/attachments/1346598/2039266/poster-200.pdf)
  * parquet와 kudu같은 column store가 빠른 데이터 처리, 빠른 random access와 확장성 있는 데이터 분석을 모두 잘 지원(하지만 Kudu는 update, delete 지원)
* [Hadoop cluster os_tuning_v1.0_20170106_mobile](https://www.slideshare.net/ssuser39d504/hadoop-cluster-ostuningv1020170106mobile)
* [Hadoop을 이용한 빅데이터 분석 전파교육](https://prezi.com/gu7ihbi5geja/hadoop/)
* [Hadoop에서 FileSystem 객체에 대한 Tip 몇가지](http://www.popit.kr/hadoop%EC%97%90%EC%84%9C-filesystem-%EA%B0%9D%EC%B2%B4%EC%97%90-%EB%8C%80%ED%95%9C-tip-%EB%AA%87%EA%B0%80%EC%A7%80/)
* [DB 데이터를 Hadoop에 저장 시 삽질 두가지](http://www.popit.kr/db-%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%A5%BC-hadoop%EC%97%90-%EC%A0%80%EC%9E%A5-%EC%8B%9C-%EC%82%BD%EC%A7%88-%EB%91%90%EA%B0%80%EC%A7%80/)
* [Troubleshooting Hadoop psuedo distributed mode Issues](https://medium.com/@anmol.ganju81/troubleshooting-hadoop-psuedo-distributed-mode-issues-becd37d1f14e)
* [Running A MapReduce job on a Psuedo Distributed Mode](https://medium.com/@anmol.ganju81/running-a-mapreduce-job-on-a-psuedo-distributed-mode-b935966ade09)
* [Reducing MapReduce](https://medium.com/@pavanraju023/reducing-mapreduce-8ffe653f7907)
* [MapReduce Architecture and Components](https://medium.com/@ananthis740/mapreduce-architecture-and-components-37be52af157e)
* [Reduce](https://medium.com/@gregheo/reduce-a83c85f07960)
* [Configuring Hadoop on Linux(RHEL 7/Cent OS/Fedora 23) Machine](https://medium.com/@anmol.ganju81/configuring-hadoop-on-linux-rhel-7-cent-os-fedora-23-machine-3dc8caf57ec9)
* [Hadoop Cluster Architecture and Core Components](https://medium.com/@ananthis740/hadoop-cluster-architecture-and-core-components-d5d56ddafb53)
* [Architecture and Components of Hadoop](Architecture and Components of Hadoop)
* [CAP Theorem in Hadoop](https://medium.com/@ananthis740/cap-theorem-in-hadoop-e0ef8b1b07d9)
* [Hadoop Ecosystem Tutorial](https://medium.com/@ananthis740/hadoop-ecosystem-tutorial-501d95c083ca)
* [PART 1: HORTONWORKS THOUGHTS ON BUILDING A SUCCESSFUL STREAMING ANALYTICS PLATFORM](https://ko.hortonworks.com/blog/part-1-hortonworks-building-successful-streaming-analytics-platforms/)
* [PART 2 OF HDF BLOG SERIES: A SHARED SCHEMA REGISTRY: WHAT IS IT AND WHY IS IT IMPORTANT?](https://ko.hortonworks.com/blog/part-2-hdf-blog-series-shared-schema-registry-important/)
  * Hortonworks 에서 구상하고 있는 스트리밍 분석 플랫폼에서 스트리밍 응용 프로그램 간의 공유 스키마 레지스트리에 대한 필요성을 설명
  * 차기 HDF 플랫폼에서 Apache Kafka, Apache Atlas, Apache Ranger, Apache NiFi를 통합하는 자체 스키마 레지스트리를 포함할 예정
* [change IP address for cloudera manager](https://medium.com/@strncpy/change-ip-address-for-cloudera-manager-14e22b43d893)
* [Change IP address for cloudera manager](https://hyunjun.github.io/change-ip-address-for-cm/)
* [Fastest track to Apache Hadoop and Spark success: using job-scoped clusters on cloud-native architecture](https://cloud.google.com/blog/big-data/2017/06/fastest-track-to-apache-hadoop-and-spark-success-using-job-scoped-clusters-on-cloud-native-architecture)
  * 클러스터 당 하나의 작업이 Hadoop에 올바른 접근 방식이라는 주장
  * Google Cloud에서는 클러스터 시작에 대한 패널티가 2분 미만으로 낮기 때문에 장기 실행 Hadoop 클러스터와 같이 멀티 테넌시를 최적화 할 필요가 없음
* [Hadoop and Spark on Docker: Ten Things You Need to Know](https://www.bluedata.com/blog/2017/08/hadoop-spark-docker-ten-things-to-know/)
  * Hadoop, Spark용 배포 도구를 만드는 것이 좋지 않은 10가지 이유
* [Introducing S3Guard: S3 Consistency for Apache Hadoop](http://blog.cloudera.com/blog/2017/08/introducing-s3guard-s3-consistency-for-apache-hadoop/)
  * S3Guard  개요; S3Guard는 Hadoop S3A 파일 시스템이 메타데이터 저장소를 사용하여 S3에 저장된 데이터에 일관된 뷰를 추가하는 새로운 기능
* [Secure Hadoop in Real Time](http://goeagle.io/)
* [Accessing Secure Cluster from Web Applications](http://blog.cloudera.com/blog/2017/08/accessing-secure-cluster-from-web-applications/)
  * Kerberos constrained delegation를 설정하고 사용하는 방법, Secure Hadoop Cluster에 쿼리를 실행하도록 웹 응용 프로그램을 구성하는 방법에 대해 설명
* distcp
  * [Copying Data between two Clusters Using distcp](https://www.cloudera.com/documentation/enterprise/5-4-x/topics/cdh_admin_distcp_data_cluster_migrate.html)
* [Dynamometer: Scale Testing HDFS on Minimal Hardware with Maximum Fidelity](https://engineering.linkedin.com/blog/2018/02/dynamometer--scale-testing-hdfs-on-minimal-hardware-with-maximum)
  * Dynamometer라는 로드 테스트 도구를 사용하여 버전을 업그레이드하기 전에 Apache Hadoop DFS 성능을 테스트하는 방법 소개
* [Hadoop legacy](https://virtuslab.com/blog/hadoop-legacy/)

# Cloudera
* [cloudera.daumkakao.io](http://cloudera.daumkakao.io/)
* installation
  * [practice - cloudera manager 5.13.0](https://gist.github.com/hyunjun/8c6f702e73e3f94d559e#file-5-13-0-md)
  * [practice - cloudera manager 5.4.x](https://gist.github.com/hyunjun/8c6f702e73e3f94d559e#file-installation-md)
* [Cloudera Korea](https://www.facebook.com/groups/1446013985717499)
* [CDH 4.5.0](http://www.cloudera.com/content/cloudera/en/downloads/cdh/cdh-4-5-0.html)
* [Strata NY 2014 - Architectural considerations for Hadoop applications tutorial](http://www.slideshare.net/hadooparchbook/strata-ny-2014-architectural-considerations-for-hadoop-applications-tutorial)
* [Taming Operations in the Hadoop Ecosystem](http://www.slideshare.net/cloudera/taming-operations-in-the-hadoop-ecosystem)
* [How-to: Install Apache Zeppelin on CDH](http://blog.cloudera.com/blog/2015/07/how-to-install-apache-zeppelin-on-cdh/)
* [Architectural Patterns for Near Real-Time Data Processing with Apache Hadoop](http://blog.cloudera.com/blog/2015/06/architectural-patterns-for-near-real-time-data-processing-with-apache-hadoop/)
* [How-to: Build a Complex Event Processing App on Apache Spark and Drools](http://blog.cloudera.com/blog/2015/11/how-to-build-a-complex-event-processing-app-on-apache-spark-and-drools/)
* [Cloudera Manager Demo 1: Automated Deployment and Configuration](https://www.youtube.com/watch?v=1KEwGcPJW_I&index=1&list=PLe-h9HrA9qfDkH8RCxHGMzSAzL7x73T-Q)
* [How-To: Run a MapReduce Job in CDH4 using Advanced Features](https://blog.cloudera.com/blog/2013/02/how-to-run-a-mapreduce-job-in-cdh4-using-advanced-features/)
* [Autoconfiguration](http://www.cloudera.com/content/www/en-us/documentation/enterprise/latest/topics/cm_mc_autoconfig.html)
* [Progress Report: Bringing Erasure Coding to Apache Hadoop](http://blog.cloudera.com/blog/2016/02/progress-report-bringing-erasure-coding-to-apache-hadoop/)
  * [Erasure Code and Intel® Intelligent Storage Acceleration Library](http://www.intel.com/content/www/us/en/storage/erasure-code-isa-l-solution-video.html)
  * [스토리지 데이터 보존 및 복제기법 : 이레이저코딩(Erasure Coding)](http://blog.naver.com/PostView.nhn?blogId=limoremo&logNo=220553762165)
  * [Debunking the Myths of HDFS Erasure Coding Performance](https://www.slideshare.net/HadoopSummit/debunking-the-myths-of-hdfs-erasure-coding-performance)
  * [Introduction to HDFS Erasure Coding in Apache Hadoop](https://blog.cloudera.com/blog/2015/09/introduction-to-hdfs-erasure-coding-in-apache-hadoop/)
* [How-to: Build a Real-Time Search System using StreamSets, Apache Kafka, and Cloudera Search](http://blog.cloudera.com/blog/2016/02/how-to-build-a-real-time-search-system-using-streamsets-apache-kafka-and-cloudera-search/)
  * [StreamSets Data Collector](https://streamsets.com/product/)
* [Replicating Relational Databases with StreamSets Data Collector](https://streamsets.com/blog/blogreplicating-relational-databases-with-streamsets-data-collector/)
  * MySQL 데이터베이스의 변경 내용을 스트림으로 캡처하기 위해 StreamSets을 이용
  * StreamSets은 JDBC를 이용하여 폴링 기반의 스트림 데이터 캡처가 가능
  * 본문에서 MySQL 데이터베이스의 변경 사항을 캡처하고 HDFS/Hive/Impala로 streaming 하는 과정을 설명
* [August 2016 HUG: Open Source Big Data Ingest with StreamSets Data Collector](https://www.slideshare.net/ydn/august-2016-hug-open-source-big-data-ingest-with-streamsets-data-collector?ref=http%3A%2F%2Fyahoohadoop.tumblr.com%2Ftagged%2FHadoop)
* [How-to: Include Third-Party Libraries in Your MapReduce Job](https://blog.cloudera.com/blog/2011/01/how-to-include-third-party-libraries-in-your-map-reduce-job/)
* [Ibis Project Blog](http://www.ibis-project.org/)
  * [ibis-demo Demo program of Ibis for "Spark + Python + Dita science Festival"](https://github.com/chezou/ibis-demo)
  * [Ibis: Scaling Python Analytics on Hadoop and Impala](http://www.slideshare.net/wesm/ibis-scaling-python-analytics-on-hadoop-and-impala)
  * Ibis
    * Python이 Big Data 처리를 하는데 있어 보다 손쉬운 방법을 제공하는 라이브러리
    * 2016.07.29 현재 Apache Impala, SQLite, PostgreSQL과의 연결을 지원
    * pandas를 처음 설립한 Wes Mckinney가 만든 Python <> Big Data 라이브러리
    * Ibis Demo 준비사항
      * Impala cluster
      * CDH 5.7 with Cloudera Director 2.1
      * require port impalad node's 21050 port NN's 50070 port
      * table is created with parquet on S3
      * Python 3.5 using wheel and virtualenv, don't need conda
    * FAQ on Ibis
      * PySpark와의 차이점은?
        * 쉬운 셋업. DB 연결과 같이 간단
        * 속도가 약 10배 이상 빠름
      * Ibis + scikit-learn vs Spark + MLlib?
        * 데이터 크기에 따라 알맞은 프레임워크 활용
        * Netflix의 경우 Spark와 R을 예측 모델 빌딩에 활용. R은 필터링을 마친 나라 또는 지역에 국한된 데이터 모델링시, Spark의 경우는 전체 글로벌 모델 빌딩시 활용
* [Running Spark 2.x.x on Cloudera Hadoop Distro (CDH)](https://www.linkedin.com/pulse/running-spark-2xx-cloudera-hadoop-distro-cdh-deenar-toraskar-cfa)
* [YCSB 0.10.0 Now in Cloudera Labs](http://blog.cloudera.com/blog/2016/11/ycsb-0-10-0-now-in-cloudera-labs/)
* [imp51.tistory.com/category/Big DATA](http://imp51.tistory.com/category/Big%20DATA)
* [클라우데라 엔터프라이즈 (Cloudera & Open Source)](https://www.facebook.com/TalkIT/videos/1653248424689274/)
* [Part 1: Introducing the Cloudera Data Science Workbench](https://www.slideshare.net/cloudera/part-1-introducing-the-cloudera-data-science-workbench)
* [HDFS Maintenance State](http://blog.cloudera.com/blog/2017/05/hdfs-maintenance-state/)
  * 새로운 기능 "Maintenace State"
  * replication storm을 일으키지 않고 클러스터에서 노드를 일시적으로 제거하는 메커니즘 제공
  * 예를 들어 전체 랙을 한 번에 패치하는 경우 유용
  * 사용하려면 dfs.hosts 파일로는 충분하지 않아서 JSON 형태의 "maintenance" 파일 필요
* [Deploy Cloudera EDH Clusters Like a Boss Revamped – Part 1](https://blog.cloudera.com/blog/2017/11/deploy-cloudera-edh-clusters-like-a-boss-revamped-part-1/)
* [Deploy Cloudera EDH Clusters Like a Boss Revamped – Part 2](http://blog.cloudera.com/blog/2018/01/deploy-cloudera-edh-clusters-like-a-boss-revamped-part-2/)
* [What’s New in Cloudera Director 2.7?](http://blog.cloudera.com/blog/2018/01/whats-new-in-cloudera-director-2-7/)
* [Cloudera Altus Analytic DB (Beta)](https://www.cloudera.com/products/altus/altus-analytic-db.html)
  * [A Technical Overview of Cloudera Altus Analytic DB](http://blog.cloudera.com/blog/2018/02/a-technical-overview-of-cloudera-altus-analytic-db/)

# Combiner
* [Combiner in Mapreduce](http://hadooptutorial.info/combiner-in-mapreduce/#Combiner_Output)
* [Combiner function in python hadoop streaming](http://stackoverflow.com/questions/4269355/combiner-function-in-python-hadoop-streaming)

# Command
* find
  * [HdfsFindTool](http://www.cloudera.com/documentation/archive/search/1-3-0/Cloudera-Search-User-Guide/csug_hdfsfindtool.html)
    * `hadoop jar /opt/cloudera/parcels/CDH-5.5.1-1.cdh5.5.1.p0.11/lib/solr/contrib/mr/search-mr-job.jar org.apache.solr.hadoop.HdfsFindTool -find [path] -type f -size 0` size 28인 file도 결과에 나왔음
* webhdfs
  * [Enabling WebHDFS](http://www.cloudera.com/documentation/manager/5-0-x/Cloudera-Manager-Managing-Clusters/cm5mc_hdfs_enable_webhdfs.html)
  * [Open and Read a File](http://archive.cloudera.com/cdh5/cdh/5/hadoop/hadoop-project-dist/hadoop-hdfs/WebHDFS.html#Open_and_Read_a_File)
    * `curl -L "http://[name node]:50070/webhdfs/v1/path/to/file_name?op=OPEN" > file_name`

# Hive
* [Hive Query 의 Hadoop Job Id (YARN) 알아내기](http://www.popit.kr/hive-query-%EC%9D%98-hadoop-job-id-yarn-%EC%95%8C%EC%95%84%EB%82%B4%EA%B8%B0/)
* [Hive 메타 및 데이터 플로우 탐색 도구](http://readme.skplanet.com/?p=13565)
* [장치에 남은 공간이 없음 에러..](http://knight76.tistory.com/entry/hive-%EC%9E%A5%EC%B9%98%EC%97%90-%EB%82%A8%EC%9D%80-%EA%B3%B5%EA%B0%84%EC%9D%B4-%EC%97%86%EC%9D%8C)
* [ULTRA-FAST OLAP ANALYTICS WITH APACHE HIVE AND DRUID – PART 1 OF 3](https://hortonworks.com/blog/apache-hive-druid-part-1-3/)
  * Hive-Druid 통합에 대한 정보와 향후 계획
  * Druid; 대용량 실시간 분석 시스템
  * 특정 질의에 대해 월등한 응답 성능을 보장하지만, 데이터 셋의 많은 부분을 스캔해야 하는 쿼리 또는 조인 미지원
  * 이러한 유형의 쿼리의 경우, Apache Hive에서 Druid에 저장된 데이터를 조회 가능
* [Ultra-Fast OLAP Analytics With Apache Hive and Druid (Part 1)](https://dzone.com/articles/ultra-fast-olap-analytics-with-apache-hive-and-dru)
* [Ultra-Fast OLAP Analytics With Apache Hive and Druid (Part 2)](https://dzone.com/articles/ultra-fast-olap-analytics-with-apache-hive-and-dru-1)
* [BENCHMARK: SUB-SECOND ANALYTICS WITH APACHE HIVE AND DRUID](https://hortonworks.com/blog/sub-second-analytics-hive-druid/)
* [Hive 와 Druid로 울트라-빠른 OLAP 분석하기](http://www.popit.kr/ultra-fast_olap_druid/)
* [reducer에 메모리 할당하기](http://knight76.tistory.com/entry/hive-reducer%EC%97%90-%EB%A9%94%EB%AA%A8%EB%A6%AC-%ED%95%A0%EB%8B%B9%ED%95%98%EA%B8%B0)
* [Turbocharge your Apache Hive Queries on Amazon EMR using LLAP](https://aws.amazon.com/blogs/big-data/turbocharge-your-apache-hive-queries-on-amazon-emr-using-llap/)
  * Hive의 LLAP을 사용하여 Hive 쿼리 성능을 향상시키는 방법
* [UPDATE HIVE TABLES THE EASY WAY](https://hortonworks.com/blog/update-hive-tables-easy-way/)
  * Apache Hive의 transaction update 기능, 특히 MERGE 문에 대해 설명
* [UPDATE HIVE TABLES THE EASY WAY PART 2](https://hortonworks.com/blog/update-hive-tables-easy-way-2/)
  * Hive에서 천천히 변화하는 디맨전을 유지하기 위해 MERGE문을 사용하는 방법 또는 전략에 대해 설명
* [3X FASTER INTERACTIVE QUERY WITH APACHE HIVE LLAP](https://ko.hortonworks.com/blog/3x-faster-interactive-query-hive-llap/)
  * Hortonworks의 HDP 2.5와 2.6에서 하이브의 성능을 비교하는 벤치마크
* [Optimizing ORC and Parquet files for Big SQL queries performance](https://developer.ibm.com/hadoop/2018/01/19/optimizing-orc-and-parquet-files-for-big-sql-queries-performance/)
  * HDFS 파일 시스템에서 작은 파일을 사용하면 큰 데이터를 처리하는데 성능 문제가 발생. 가장 현대적인 파일 포맷인 ORC, Parquet도 마찬가지
  * 이 문제를 해결하기 위해 Hive에서는 'concatenate' 명령어, parquet 에서는 병합툴을 제공

# [Hue](http://gethue.com/)
* [Hadoop Tutorial: the new beta Notebook app for Spark & SQL](https://vimeo.com/125792752)
* [Get Started with Hue](http://www.cloudera.com/documentation/enterprise/latest/topics/hue.html)
* [Hadoop Tutorial - Hue: Execute Hive queries and schedule them with Oozie](https://www.youtube.com/watch?v=Tu1IM4rph6w)
* Hue 4
  * [The Hue 4 user interface in detail](http://gethue.com/the-hue-4-user-interface-in-detail/)
  * [Hue 4 SQL Editor improvements](http://gethue.com/hue-4-sql-editor-improvements/)
* [Importing data from traditional databases into HDFS/Hive in just a few clicks](http://gethue.com/importing-data-from-traditional-databases-into-hdfshive-in-just-a-few-clicks/)
  * 최신 버전 HUE에서 Apache Sqoop1을 실행하여 UI를 통해 HDFS와 Hive에 데이터를 가져오는 방법을 설명
* [Import data to be queried via the Self Service Drag & Drop Create Table Wizard](http://gethue.com/import-data-to-be-queried-via-the-self-service-drag-drop-create-table-wizard/)
  * 테이블 생성 마법사를 통해 파일 내용을 분석하여 새로운 테이블의 메타 데이터를 생성
* [Using Sentry to Manage Table Access in Hue](https://www.youtube.com/watch?v=bcDpWcL6H8c&feature=youtu.be)

# Library
* [CLOUD DATAPROC - Google Cloud Dataproc is a managed Spark and Hadoop service that is fast, easy to use, and low cost](https://cloud.google.com/dataproc/)
  * [구글, 스파크·하둡 관리 클라우드 서비스 공개](http://www.bloter.net/archives/239483)
  * [Google Cloud Dataproc 사용하기(http://whitechoi.tistory.com/48)
* [CloumonELK is a monitoring solution package based on the popular ELK (ElasticSearch, Logstash and Kibana) stack](http://gruter.github.io/cloumon-elk/)
* [CMUX](https://github.com/kakao/cmux)
  * [kakao의 오픈소스 Ep7 - CMUX: CLI에 날개를 달자!](http://tech.kakao.com/2017/07/12/opensource-7-cmux/)
* [Dr. Elephant Self-Serve Performance Tuning for Hadoop and Spark](https://engineering.linkedin.com/blog/2016/04/dr-elephant-open-source-self-serve-performance-tuning-hadoop-spark)
* [Falcon - Simplifying Managing Data Jobs on Hadoop](http://www.slideshare.net/Hadoop_Summit/apache-falcon-simplifying-managing-data-jobs-on-hadoop)
* [Hadoop filesystem at Twitter](https://blog.twitter.com/2015/hadoop-filesystem-at-twitter)
* [HDFS Shell - a HDFS manipulation tool](https://github.com/avast/hdfs-shell) hbase-shell처럼 HDFS 작업을 할 수 있는 CLI interface
* [Snakebite is a python library that provides a pure python HDFS client and a wrapper around Hadoops minicluster](https://github.com/spotify/snakebite)
* [Spring XD is a unified, distributed, and extensible system for data ingestion, real time analytics, batch processing, and data export](http://projects.spring.io/spring-xd/)
  * [SpringXD Lab](https://github.com/Pivotal-Open-Source-Hub/StockInference-Spark/blob/master/SpringXD.md)
* [StreamSets - Performance Management for Data Flows Harness the value of your data in motion with control, efficiency and agility](https://streamsets.com/)
  * [Ingest and Stream Processing What will you choose](https://www.youtube.com/watch?v=LTONR-L40Xg&feature=player_embedded)
* [Terrapin - Pinterest open-sources Terrapin, a tool for serving data from Hadoop](http://venturebeat.com/2015/09/14/pinterest-open-sources-terrapin-a-tool-for-serving-data-from-hadoop/)

# Presto
* [프레스토 소개 (facebook presto)](http://knight76.tistory.com/m/post/2497)
* [Presto, Zeppelin을 이용한 초간단 BI 구축 사례](http://www.slideshare.net/babokim/presto-zeppelin-bi)
* [Presto, Zeppelin을 이용한 초간단 BI 시스템 구축 사례(1)](http://www.popit.kr/presto-zeppelin%EC%9D%84-%EC%9D%B4%EC%9A%A9%ED%95%9C-%EC%B4%88%EA%B0%84%EB%8B%A8-bi-%EC%8B%9C%EC%8A%A4%ED%85%9C-%EA%B5%AC%EC%B6%95-%EC%82%AC%EB%A1%80-1/)
* [Presto SQL을 이용하여 Kafka topic 데이터 조회하기](http://www.popit.kr/presto-sql%EC%9D%84-%EC%9D%B4%EC%9A%A9%ED%95%98%EC%97%AC-kafka-topic-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EC%A1%B0%ED%9A%8C%ED%95%98%EA%B8%B0/)
* [Presto Kafka connector 개선 실패기](http://www.popit.kr/presto-kafka-connector-%EA%B0%9C%EC%84%A0-%EC%8B%A4%ED%8C%A8%EA%B8%B0/)
* [Presto 쿼리 실행계획 겉핥기](https://cojette.github.io/prestoquery/)

# Python
* [A Guide to Python Frameworks for Hadoop](https://blog.cloudera.com/blog/2013/01/a-guide-to-python-frameworks-for-hadoop/)
* [Writing an Hadoop MapReduce Program in Python](http://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python)
* [Making Python on Apache Hadoop Easier with Anaconda and CDH](http://blog.cloudera.com/blog/2016/02/making-python-on-apache-hadoop-easier-with-anaconda-and-cdh/)

# Troubleshooting
* [out of Memory Error in Hadoop](http://stackoverflow.com/questions/8464048/out-of-memory-error-in-hadoop)

# YARN
* [Best Practices for YARN Resource Management](https://www.mapr.com/blog/best-practices-yarn-resource-management)
* [Tuning the Cluster for MapReduce v2 (YARN)](http://www.cloudera.com/content/www/en-us/documentation/enterprise/5-3-x/topics/cdh_ig_yarn_tuning.html)
  * 실행해봤지만, i, j, k값에 따른 실행 시간 편차가 별로 크지 않아 어느 값이 최적인지 알 수 없었음
* [Yarn Commands](https://hadoop.apache.org/docs/r2.6.0/hadoop-yarn/hadoop-yarn-site/YarnCommands.html)
* [How to increase the number of containers in nodemanager in YARN](http://stackoverflow.com/questions/20021566/how-to-increase-the-number-of-containers-in-nodemanager-in-yarn)
* [Hadoop YARN how to determine the number of containers](http://stackoverflow.com/questions/22317198/hadoop-yarn-how-to-determine-the-number-of-containers)
* [Configuring memory for MapReduce running on YARN](http://grepalex.com/2016/12/07/mapreduce-yarn-memory/)
  * YARN 관련 메모리 설정과 MapReduce 작업에서 메모리를 소모하는 주요 원인 설명
* [Apache Hadoop YARN: Yet another resource negotiator](https://blog.acolyer.org/2017/01/09/apache-hadoop-yarn-yet-another-resource-negotiator/)
* [Untangling Apache Hadoop YARN, Part 5: Using FairScheduler queue properties](http://blog.cloudera.com/blog/2017/02/untangling-apache-hadoop-yarn-part-5-using-fairscheduler-queue-properties/)
  * YARN FairScheduler에 대한 내용
  * 효과적이이고 지연 시간이 적은 큐 구성과 리소스 할당, ad-hoc 쿼리의 크기 제한에 대한 예제
* [PART 5 OF DATA LAKE 3.0: YARN AND CONTAINERIZATION: SUPPORTING DOCKER AND BEYOND](https://ko.hortonworks.com/blog/part-5-of-data-lake-3-0-yarn-and-containerization-supporting-docker-and-beyond/)
  * LinuxContainerExecutor를 통해 Docker 컨테이터를 실행하는 YARN에 대한 이야기
* [PART 6 OF DATA LAKE 3.0: A SELF-DIAGNOSING DATA LAKE](https://ko.hortonworks.com/blog/part-6-of-data-lake-3-0-a-self-diagnosing-data-lake/)
  * 느린 데이터 노드와 느린 디스크를 감지하기 위해 HDFS에 추가되는 몇 가지 새로운 기능에 대해 소개
* [YARN – THE CAPACITY SCHEDULER](https://ko.hortonworks.com/blog/yarn-capacity-scheduler/)
