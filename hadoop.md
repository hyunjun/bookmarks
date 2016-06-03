Hadoop
======
* [Hadoop Interview Questions – MapReduce](https://intellipaat.com/blog/hadoop-interview-questions-mapreduce/)
* [Quick Line Count - Hadoop](http://dronamk.blogspot.kr/2012/10/quick-line-count-hadoop.html)
* [Hadoop Programming with Arbitrary Languages](https://rcc.fsu.edu/docs/hadoop-programming-arbitrary-languages) word count + hadoop streaming in c/c++/python/shell script
* [Nobody ever got fired for using Hadoop on a cluster](http://research.microsoft.com/pubs/163083/hotcbp12%20final.pdf)
* [The Improved Job Scheduling Algorithm of Hadoop Platform](http://arxiv.org/abs/1506.03004)
* [Streaming](https://hadoop.apache.org/docs/r1.2.1/streaming.html)
  * [python example](https://github.com/hyunjun/practice/tree/master/hadoop/Streaming)
  * [perl example](https://github.com/hyunjun/practice/tree/master/hadoop/Streaming_perl)
  * [Hadoop streaming - remove trailing tab from reducer output](http://stackoverflow.com/questions/18133290/hadoop-streaming-remove-trailing-tab-from-reducer-output)
  * [hadoop streaming map.output.key.field.separator](http://blog.sina.com.cn/s/blog_5357c0af0101mgak.html)
  * [Hadoop Streaming the order of reducer output files is messed up when sorting](http://stackoverflow.com/questions/33310987/hadoop-streaming-the-order-of-reducer-output-files-is-messed-up-when-sorting)
* [피보탈, 아파치재단에 분석엔진·머신러닝 기술 제공](http://www.bloter.net/archives/240300)
* [mapr hadoop training](https://www.mapr.com/services/mapr-academy/big-data-hadoop-online-training)
* [Secure Hadoop in Real Time](http://goeagle.io/)
* [Introduction to Big Data and Hadoop for Beginners | Big Data Tutorial Training Video](https://www.youtube.com/watch?v=pg3f1ftPlZU)
* balancer
  * [Running HDFS Balancer fail, report namenode.LeaseExpiredException](https://community.cloudera.com/t5/Storage-Random-Access-HDFS/Running-HDFS-Balancer-fail-report-namenode-LeaseExpiredException/td-p/14052)
* hadoop streaming with jar
  * cluster의 모든 local directory에 필요한 파일을 모두 복사하지 않고, library를 hdfs에 올려서 참조
  * 필요한 파일을 jar로 묶어 hdfs에 올리고, -archives option으로 참조
  * ref
  * https://hadoop.apache.org/docs/r2.5.2/hadoop-mapreduce-client/hadoop-mapreduce-client-core/HadoopStreaming.html
  * zipimport; local에서는 잘 동작하지만, streaming은 실패함
    * [hadoop-how-to-include-third-party-library-in-python-mapreduce](http://stackoverflow.com/questions/15352981/hadoop-how-to-include-third-party-library-in-python-mapreduce) 
    * [how-can-i-include-a-python-package-with-hadoop-streaming-job](http://stackoverflow.com/questions/6811549/how-can-i-include-a-python-package-with-hadoop-streaming-job)
    * [running-extrnal-python-lib-like-nltk-with-hadoop-streaming](http://stackoverflow.com/questions/24167933/running-extrnal-python-lib-like-nltk-with-hadoop-streaming/32135850#32135850)
  * troubleshooting
    * `Error: java.lang.RuntimeException: PipeMapRed.waitOutputThreads(): subprocess failed with code 1`
      * local script를 실행시켜서 정상 동작하는지부터 확인
    * `ERROR streaming.StreamJob: Error Launching job : Input path does not exist`
      * hdfs directory와 local directory의 이름이 같은 경우 발생할 때가 있음
      * -input/-output에 `hdfs://[name node]/path/to/directory`처럼 절대 경로를 사용하거나 directory 이름을 unique하게 변경
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
        * [[Java 8] Over usage of virtual memory](https://issues.apache.org/jira/browse/HADOOP-11364)
        * [Hadoop Yarn memory settings in HDInsight](http://blogs.msdn.com/b/shanyu/archive/2014/07/31/hadoop-yarn-memory-settings-in-hdinsigh.aspx)
        * [Container is running beyond memory limits](http://www.chinabtp.com/container-is-running-beyond-memory-limits/)
        * [Container is running beyond memory limits](http://www.hitmaroc.net/191849-4083-container-running-beyond-memory-limits.html)
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

# Cloudera
* [cloudera.daumkakao.io](http://cloudera.daumkakao.io/)
* installation
  * [CDH 5.4.x](https://gist.github.com/hyunjun/8c6f702e73e3f94d559e)
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
* [How-to: Build a Real-Time Search System using StreamSets, Apache Kafka, and Cloudera Search](http://blog.cloudera.com/blog/2016/02/how-to-build-a-real-time-search-system-using-streamsets-apache-kafka-and-cloudera-search/)
  * [StreamSets Data Collector](https://streamsets.com/product/)
* [How-to: Include Third-Party Libraries in Your MapReduce Job](https://blog.cloudera.com/blog/2011/01/how-to-include-third-party-libraries-in-your-map-reduce-job/)

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

# [Hue](http://gethue.com/)
* [Hadoop Tutorial: the new beta Notebook app for Spark & SQL](https://vimeo.com/125792752)

# Library
* [CLOUD DATAPROC - Google Cloud Dataproc is a managed Spark and Hadoop service that is fast, easy to use, and low cost](https://cloud.google.com/dataproc/)
  * [구글, 스파크·하둡 관리 클라우드 서비스 공개](http://www.bloter.net/archives/239483)
* [CloumonELK is a monitoring solution package based on the popular ELK (ElasticSearch, Logstash and Kibana) stack](http://gruter.github.io/cloumon-elk/)
* [Dr. Elephant Self-Serve Performance Tuning for Hadoop and Spark](https://engineering.linkedin.com/blog/2016/04/dr-elephant-open-source-self-serve-performance-tuning-hadoop-spark)
* [Falcon - Simplifying Managing Data Jobs on Hadoop](http://www.slideshare.net/Hadoop_Summit/apache-falcon-simplifying-managing-data-jobs-on-hadoop)
* [Hadoop filesystem at Twitter](https://blog.twitter.com/2015/hadoop-filesystem-at-twitter)
* [Snakebite is a python library that provides a pure python HDFS client and a wrapper around Hadoops minicluster](https://github.com/spotify/snakebite)
* [Spring XD is a unified, distributed, and extensible system for data ingestion, real time analytics, batch processing, and data export](http://projects.spring.io/spring-xd/)
  * [SpringXD Lab](https://github.com/Pivotal-Open-Source-Hub/StockInference-Spark/blob/master/SpringXD.md)
* [StreamSets - Performance Management for Data Flows Harness the value of your data in motion with control, efficiency and agility](https://streamsets.com/)
  * [Ingest and Stream Processing What will you choose](https://www.youtube.com/watch?v=LTONR-L40Xg&feature=player_embedded)
* [Terrapin - Pinterest open-sources Terrapin, a tool for serving data from Hadoop](http://venturebeat.com/2015/09/14/pinterest-open-sources-terrapin-a-tool-for-serving-data-from-hadoop/)

# Presto
* [프레스토 소개 (facebook presto)](http://knight76.tistory.com/m/post/2497)

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
