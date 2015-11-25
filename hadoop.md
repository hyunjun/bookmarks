Hadoop
======
* [Hadoop Interview Questions – MapReduce](https://intellipaat.com/blog/hadoop-interview-questions-mapreduce/)
* [Quick Line Count - Hadoop](http://dronamk.blogspot.kr/2012/10/quick-line-count-hadoop.html)
* [Hadoop Programming with Arbitrary Languages](https://rcc.fsu.edu/docs/hadoop-programming-arbitrary-languages) word count + hadoop streaming in c/c++/python/shell script
* [Nobody ever got fired for using Hadoop on a cluster](http://research.microsoft.com/pubs/163083/hotcbp12%20final.pdf)
* [The Improved Job Scheduling Algorithm of Hadoop Platform](http://arxiv.org/abs/1506.03004)
* Streaming
  * [python example](https://github.com/hyunjun/practice/tree/master/hadoop/Streaming)
  * [perl example](https://github.com/hyunjun/practice/tree/master/hadoop/Streaming_perl)
* [피보탈, 아파치재단에 분석엔진·머신러닝 기술 제공](http://www.bloter.net/archives/240300)
* [mapr hadoop training](https://www.mapr.com/services/mapr-academy/big-data-hadoop-online-training)
* [Secure Hadoop in Real Time](http://goeagle.io/)
* [Introduction to Big Data and Hadoop for Beginners | Big Data Tutorial Training Video](https://www.youtube.com/watch?v=pg3f1ftPlZU)
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

# Cloudera
* installation
  * [CDH 5.4.x](https://gist.github.com/hyunjun/8c6f702e73e3f94d559e)
* [Cloudera Korea](https://www.facebook.com/groups/1446013985717499)
* [CDH 4.5.0](http://www.cloudera.com/content/cloudera/en/downloads/cdh/cdh-4-5-0.html)
* [Strata NY 2014 - Architectural considerations for Hadoop applications tutorial](http://www.slideshare.net/hadooparchbook/strata-ny-2014-architectural-considerations-for-hadoop-applications-tutorial)
* [Taming Operations in the Hadoop Ecosystem](http://www.slideshare.net/cloudera/taming-operations-in-the-hadoop-ecosystem)
* [How-to: Install Apache Zeppelin on CDH](http://blog.cloudera.com/blog/2015/07/how-to-install-apache-zeppelin-on-cdh/)
* [Architectural Patterns for Near Real-Time Data Processing with Apache Hadoop](http://blog.cloudera.com/blog/2015/06/architectural-patterns-for-near-real-time-data-processing-with-apache-hadoop/)
* [How-to: Build a Complex Event Processing App on Apache Spark and Drools](http://blog.cloudera.com/blog/2015/11/how-to-build-a-complex-event-processing-app-on-apache-spark-and-drools/)

## Impala
* [Contributing to Impala](http://www.slideshare.net/cloudera/contributing-to-impala)
* [The Impala Cookbook](http://www.slideshare.net/cloudera/the-impala-cookbook-42530186)
* [What’s Next for Impala: More Reliability, Usability, and Performance at Even Greater Scale](http://blog.cloudera.com/blog/2015/07/whats-next-for-impala-more-reliability-usability-and-performance-at-even-greater-scale/)
* [How-to: Prepare Unstructured Data in Impala for Analysis](http://blog.cloudera.com/blog/2015/09/how-to-prepare-unstructured-data-in-impala-for-analysis/)

## [Kudu](http://blog.cloudera.com/blog/2015/09/kudu-new-apache-hadoop-storage-for-fast-analytics-on-fast-data/)
* [getkudu.io](http://getkudu.io/)
* [Kudu: New Hadoop Storage for Fast Analytics on Fast Data](http://www.slideshare.net/cloudera/kudu-new-hadoop-storage-for-fast-analytics-on-fast-data)

# [Hue](http://gethue.com/)
* [Hadoop Tutorial: the new beta Notebook app for Spark & SQL](https://vimeo.com/125792752)

# Library
* [CLOUD DATAPROC - Google Cloud Dataproc is a managed Spark and Hadoop service that is fast, easy to use, and low cost](https://cloud.google.com/dataproc/)
  * [구글, 스파크·하둡 관리 클라우드 서비스 공개](http://www.bloter.net/archives/239483)
* [Falcon - Simplifying Managing Data Jobs on Hadoop](http://www.slideshare.net/Hadoop_Summit/apache-falcon-simplifying-managing-data-jobs-on-hadoop)
* [Hadoop filesystem at Twitter](https://blog.twitter.com/2015/hadoop-filesystem-at-twitter)
* [Terrapin - Pinterest open-sources Terrapin, a tool for serving data from Hadoop](http://venturebeat.com/2015/09/14/pinterest-open-sources-terrapin-a-tool-for-serving-data-from-hadoop/)

# Python
* [A Guide to Python Frameworks for Hadoop](https://blog.cloudera.com/blog/2013/01/a-guide-to-python-frameworks-for-hadoop/)
