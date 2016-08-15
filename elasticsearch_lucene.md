ElasticSearch - Lucene
======================

# ElasticSearch
* [시작하세요! 엘라스틱서치](https://github.com/wikibook/elasticsearch)
* [엘라스틱서치 이해하기 20160612](http://www.slideshare.net/dahlmoon/20160612)
* [엘라스틱서치 이해하기 20160613](http://www.slideshare.net/dahlmoon/20160613)
* [엘라스틱서치 분석 이해하기 20160623](http://www.slideshare.net/dahlmoon/20160623)
* [엘라스틱서치 적합성 이해하기 20160630](http://www.slideshare.net/dahlmoon/20160630)
* [Elasticsearch 2.3.2 released](https://www.elastic.co/blog/elasticsearch-2-3-2-released)
* [Configuration](https://www.elastic.co/guide/en/elasticsearch/reference/1.7/setup-configuration.html)
  * [Heap: Sizing and Swapping](https://www.elastic.co/guide/en/elasticsearch/guide/1.x/heap-sizing.html)
* example
  * [installation, example json, and delete - create index - search - search all](https://gist.github.com/hyunjun/c3c0dbd13f50d5242ffb)
    * [Analyzers in elasticsearch](http://stackoverflow.com/questions/12836642/analyzers-in-elasticsearch)
    * [Match Query](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-match-query.html)
    * [Wildcard Query](https://www.elastic.co/guide/en/elasticsearch/reference/1.4/query-dsl-wildcard-query.html)
    * **[ElasticSearch for Logging](http://edgeofsanity.net/article/2012/12/26/elasticsearch-for-logging.html)** configuration
    * [Centralized Log Server 를 위한 기본 세팅 (EC2 + ElasticSearch + Logstash + filebeat + kibana)](http://knphouse.tistory.com/85)
    * [mlockall: false despite being configured](https://github.com/elastic/elasticsearch/issues/9357)
  * Bulk
    * [Bulk API](https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-bulk.html)
    * [Cheaper in Bulk](https://www.elastic.co/guide/en/elasticsearch/guide/current/bulk.html)
  * Count
    * [1.7/search-count.html](https://www.elastic.co/guide/en/elasticsearch/reference/1.7/search-count.html)
  * Index
    * **[Elasticsearch Indexing Performance Cheatsheet](https://blog.codecentric.de/en/2014/05/elasticsearch-indexing-performance-cheatsheet/)**
    * [Multiple analyzers and query fields in Elasticsearch for auto-completion](https://gist.github.com/karmi/4526141)
    * [1.7/indices-stats.html](https://www.elastic.co/guide/en/elasticsearch/reference/1.7/indices-stats.html)
    * [Elasticsearch 인덱싱에 대한 성능 고려 사항](https://www.elastic.co/kr/blog/performance-considerations-elasticsearch-indexing)
  * Mapping
    * [ElasticSearch – nested mappings and filters](http://joelabrahamsson.com/elasticsearch-nested-mapping-and-filter/)
  * Optimize
    * **[Optimizing Elasticsearch Searches](https://www.elastic.co/blog/found-optimizing-elasticsearch-searches)**
    * **[9 Tips on ElasticSearch Configuration for High Performance](https://www.loggly.com/blog/nine-tips-configuring-elasticsearch-for-high-performance/)**
    * [indices optimize](https://www.elastic.co/guide/en/elasticsearch/reference/current/indices-optimize.html)
  * Query
    * [Nested Query](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-nested-query.html)
    * [SEARCHING MULTIPLE INDICES AND TYPES IN ELASTICSEARCH](https://damienbod.com/2015/02/10/searching-multiple-indices-and-types-in-elasticsearch/)
  * Shard
    * [Testing the limits of elasticsearch](https://speakerdeck.com/bm_dumitrescu/testing-the-limits-of-elasticsearch)
    * **[Optimizing Elasticsearch: How Many Shards per Index?](https://qbox.io/blog/optimizing-elasticsearch-how-many-shards-per-index)**
    * [Every Shard Deserves a Home - Deep Dive into Shard Allocation in Elasticsearch](https://speakerdeck.com/elastic/every-shard-deserves-a-home-deep-dive-into-shard-allocation-in-elasticsearch)
    * [Stack Overflow: The Architecture - 2016 Edition](http://nickcraver.com/blog/2016/02/17/stack-overflow-the-architecture-2016-edition/) index마다 별도의 cluster를 설정했다는 뜻일까?
* [github.com/elastic/elasticsearch](https://github.com/elastic/elasticsearch)
  * [Aggregations](https://www.elastic.co/guide/en/elasticsearch/reference/current/search-aggregations.html#search-aggregations)
    * [Multiple group-by in Elasticsearch](http://stackoverflow.com/questions/14181674/multiple-group-by-in-elasticsearch)
  * [Combining Filters](https://www.elastic.co/guide/en/elasticsearch/guide/current/combining-filters.html)
  * [Term Filters](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-terms-filter.html)
  * [How to get max _id from elastic search](http://stackoverflow.com/questions/28811744/how-to-get-max-id-from-elastic-search)
* [get started with elasticsearch](https://www.elastic.co/webinars/get-started-with-elasticsearch)
* [Elasticsearch: The Definitive Guide The Definitive Guide](https://www.elastic.co/guide/en/elasticsearch/guide/current/index.html)
* [The Definitive Guide to Elasticsearch https://www.elastic.co/guide/en/elasticsearch/guide/current/index.html](https://github.com/elastic/elasticsearch-definitive-guide)
* [Riak, Elasticsearch and Numad Walk Into a Red Hat](http://underthehood.meltwater.com/blog/2015/04/14/riak-elasticsearch-and-numad-walk-into-a-red-hat/)
* [Collaborate Apache Tajo + Elasticsearch](https://github.com/gruter/tajo-elasticsearch)
* [Packetbeat - the open source data shipper that integrates with Elasticsearch and Kibana to provide real-time analytics for web, database, and other network protocols](https://www.elastic.co/products/beats/packetbeat)
* [Remote Code Execution in Elasticsearch - CVE-2015-1427](http://jordan-wright.com/blog/2015/03/08/elasticsearch-rce-vulnerability-cve-2015-1427/)
* [potential-happiness - A dashboard for the terminal, for use with riemann and/or elasticsearch](https://github.com/algernon/potential-happiness)
* [Balancing an Elasticsearch Cluster by Shard Size](http://engineering.datarank.com/2015/07/08/balancing-elasticsearch-cluster-by-shard-size.html)
* [Quantitative Cluster Sizing](https://speakerdeck.com/elastic/quantitative-cluster-sizing?slide=16)
* [엘라스틱 “오픈소스 검색 기술로 기업 혁신 돕고파”](http://www.bloter.net/archives/234528)
* [Logasuarus: A CLI Utility for Elasticsearch / Logstash](http://www.jeffmalnick.com/blog/2015/08/28/elasticsearch-logstash-cli-utility/)
* [[번역] Solr vs ElasticSearch - Part 1 : Overview](http://jeen.github.io/2013/07/15/solr-vs-elasticsearch-part-1/)
* [[번역] Solr vs. ElasticSearch: Part 2 - Indexing and Language Handling](http://jeen.github.io/2013/07/16/solr-vs-elasticsearch-part-2-indexing-and-language-handling/)
* [[번역] Solr vs. ElasticSearch - Part 3 : Searching](http://jeen.github.io/2013/07/16/solr-vs-elasticsearch-part-3-searching/)
* [[번역] Solr vs ElasticSearch Part 4 - Faceting](http://jeen.github.io/2013/07/17/solr-vs-elasticsearch-part-4-faceting/)
* [[번역] Solr vs ElasticSearch: Part 5 – Management API Capabilities](http://jeen.github.io/2013/07/17/solr-vs-elasticsearch-part-5-management-api-capabilities/)
* [[번역] Solr vs. ElasticSearch: Part 6 – User & Dev Communities Compared](http://jeen.github.io/2013/07/17/solr-vs-elasticsearch-part-6-user-and-dev-communities-compared/)
* [ElasticSearch 이해하기 #1](https://evilimp79.wordpress.com/2014/10/27/elasticsearch-%EC%9D%B4%ED%95%B4%ED%95%98%EA%B8%B0-1/)
* [Amazon Elasticsearch Service](https://aws.amazon.com/ko/blogs/aws/new-amazon-elasticsearch-service/)
* [Supercharging the Elasticsearch Percolator](http://underthehood.meltwater.com/blog/2015/09/29/supercharging-the-elasticsearch-percolator/)
* [[Filebeat] 가볍게 사용해 볼까요?](http://jjeong.tistory.com/1059)
* [Elasticsearch as a Time Series Data Store](https://www.elastic.co/blog/elasticsearch-as-a-time-series-data-store)
* [Building a Streaming Analytics Data Stack](https://medium.com/@henridf/building-a-streaming-analytics-data-stack-ea0641048661)
* [Beyond the basics with Elasticsearch](https://speakerdeck.com/elasticsearch/beyond-the-basics-with-elasticsearch)
  * [Honza Král - Beyond the basics with Elasticsearch](https://www.youtube.com/watch?v=yIixWzjTNog)
* [[자모분석기] 초성, 중성, 종성 남의 코드 가져다 구현해 보기](http://jjeong.tistory.com/1067)
* [elasticsearch로 로그 검색 시스템 만들기](http://d2.naver.com/helloworld/273788)
* troubleshooting
  * `Action/metadata line contains an unknown parameter`
  * [HOW TO FIX YOUR ELASTICSEARCH CLUSTER STUCK IN INITIALIZING SHARDS MODE?](https://t37.net/how-to-fix-your-elasticsearch-cluster-stuck-in-initializing-shards-mode.html)
* [How To Configure Elasticsearch on Hadoop with HDP](http://ko.hortonworks.com/blog/configure-elastic-search-hadoop-hdp-2-0/)
* [Using Elasticsearch with Apache Hadoop](http://p.brightact.com/p/1406323195390438?e=agapelover4u@yahoo.co.kr&rep=SteveLi&mkt_tok=3RkMMJWWfF9wsRovuaTOZKXonjHpfsX%2F6uglWq%2BxlMI%2F0ER3fOvrPUfGjI4HSsZmI%2BSLDwEYGJlv6SgFQrHGMa1h17gOUhM%3D)
* [ElasticSearch 성능 최적화](http://deview.kr/2014/session?seq=43)
* [aws 기반의 ELK](https://www.youtube.com/playlist?list=PLDMPhWe3CfpZqZ91BUo5udpdgXB2MWxy7)
* [EMOCON 2015 F/W ELK 스택을 사용한 서울시 지하철 대시보드 만들기](https://www.youtube.com/watch?v=ec-XzM6_CgU)
* [Elasticsearch 1.x에서 2.x로 업그레이드할 때 알아야 할 주요 사항](https://www.elastic.co/kr/blog/key-point-to-be-aware-of-when-upgrading-from-elasticsearch-1-to-2)
* [Elastic Stack 그리고 X-Pack 이 왔습니다](https://www.elastic.co/kr/blog/heya-elastic-stack-and-x-pack)
* [MySQL Audit using Percona audit plugin and ELK](http://www.slideshare.net/YoungHeonKim1/mysql-audit-using-percona-audit-plugin-and-elk)
* [Elasticsearch 2.0 Releases and Webinars Pack](http://p.brightact.com/p/1446045743545361?e=agapelover4u@yahoo.co.kr&rep=AndrewDuong&mkt_tok=3RkMMJWWfF9wsRovsqzNZKXonjHpfsX%2F6uglWq%2BxlMI%2F0ER3fOvrPUfGjI4GSsphI%2BSLDwEYGJlv6SgFQrHGMa1h17gOUhM%3D)
* [[Elasticsearch] ElasticON'16 - Stories from Support](http://jjeong.tistory.com/1139)
* [How to effectively use the Elasticsearch data source in Grafana and solutions to common pitfalls](https://blog.raintank.io/how-to-effectively-use-the-elasticsearch-data-source-and-solutions-to-common-pitfalls/)
* [Lessons Learned From A Year Of Elasticsearch In Production](https://tech.scrunch.com/blog/lessons-learned-from-a-year-of-running-elasticsearch-in-production/)
* [Spring Data Elasticsearch](http://docs.spring.io/spring-data/elasticsearch/docs/current/reference/html/)
* [ELK Stack (Elasticsearch, Logstash and Kibana) on FreeBSD - Part 3](https://blog.gufi.org/2016/03/16/elk-stack-elasticsearch-logstash-and-kibana-on-freebsd-part-3/)
  * [Hackers & Painters: Kibana](https://www.youtube.com/watch?v=DeOSy37R1sc)
  * [Visualizing Logs Using ElasticSearch, Logstash and Kibana](https://www.youtube.com/watch?v=Kqs7UcCJquM)
* [데이터 분석 오픈소스 도구 ELK install](https://www.youtube.com/watch?v=ZLuGfwKUvdg)
* [Elasticsearch Farm 만들기](https://brunch.co.kr/@alden/20)
* [How To Use Elasticsearch With Python and Django (Part 1)](https://qbox.io/blog/how-to-elasticsearch-python-django-part1)
* [How To Use Elasticsearch With Python and Django (Part 2)](https://qbox.io/blog/elasticsearch-python-django-database)
* [Elastic Stack을 이용한 서울시 지하철 대시보드](https://www.elastic.co/kr/blog/seoul-metro-2014)
* [Setting up a Secure Single Node Elasticsearch server behind Nginx](http://www.minvolai.com/blog/2014/08/Setting-up-a-Secure-Single-Node-Elasticsearch-server-behind-Nginx/Setting-up-a-Secure-Single-Node-Elasticsearch-server-behind-Nginx/)
* [How-to: Monitor Your Elasticsearch Cluster Performance](http://stackify.com/monitoring-elasticsearch-getting-right/)
* [Just Enough Kafka for the Elastic Stack, Part 1](https://www.elastic.co/blog/just-enough-kafka-for-the-elastic-stack-part1)
  * [Elastic Stack에는 Kafka면 충분합니다 - 1부](https://www.elastic.co/kr/blog/just-enough-kafka-for-the-elastic-stack-part1)
* [How scoring works in Elasticsearch](https://www.compose.io/articles/how-scoring-works-in-elasticsearch/)
* [엘라스틱서치로 검색 전문가가 되자! 01. 시작](http://lemonism.net/258)
* [And the big one said "Rollover" — Managing Elasticsearch time-based indices efficiently](https://www.elastic.co/kr/blog/managing-time-based-indices-efficiently)
* [ElasticSearch Data Exploration and Analytics](https://www.youtube.com/watch?v=d9l2-3QeDTs)
* [Geospatial Data Structures in Elasticsearch and Apache Lucene](https://www.elastic.co/elasticon/conf/2016/sf/geospatial-data-structures-in-elasticsearch-and-apache-lucene)

## Docker
* Dockerfile
  * [docker-library/elasticsearch/1.7/Dockerfile](https://github.com/docker-library/elasticsearch/blob/master/1.7/Dockerfile)
  * [example](https://github.com/rutesun/dockerfiles/blob/c3bc90e93e1c4e8d46ffda6dffc81f99343935fa/elasticsearch/1.7.3/Dockerfile)
* [Docker Networking](https://www.elastic.co/kr/blog/docker-networking)
* [What's differ dockerfile/elasticsearch](https://github.com/seapy/dockerfiles/tree/master/elasticsearch)
* elasticsearch server status 503, discovery fails
  * `sudo docker run -d -p 9200:9200 -p 9300:9300 [image] --network.publish_host=$(hostname -i)`

## Library
* [은전한닢 프로젝트](http://eunjeon.blogspot.com/)
* Beats
  * [Community Beats](https://www.elastic.co/guide/en/beats/libbeat/current/community-beats.html)
  * [나만의 Beats 만들기](http://kimjmin.net/2016/06/create-own-beats/)
  * [나만의 Beats 만들기](https://www.youtube.com/watch?v=N3NbYQgiUn0&feature=youtu.be)
  * [MySQL Slow Query log Monitoring using Beats & ELK](http://www.slideshare.net/YoungHeonKim1/mysql-slow-query-log-monitoring-using-beats-elk)
* [CloumonELK is a monitoring solution package based on the popular ELK (ElasticSearch, Logstash and Kibana) stack](http://gruter.github.io/cloumon-elk/)
* [Curator: Tending your time-series indices](https://www.elastic.co/kr/blog/curator-tending-your-time-series-indices)
* Elastic Graph
  * [Elastic Graph와 Kibana를 사용하여 파나마 페이퍼스(Panama Papers) 분석](https://www.elastic.co/kr/blog/using-elastic-graph-and-kibana-to-analyze-panama-papers)
* [elasticsearch-analysis-hangueljamo](https://github.com/HowookJeong/elasticsearch-analysis-hangueljamo)
* [Elasticsearch Hadoop](https://github.com/elastic/elasticsearch-hadoop)
  * [spark packages elasticsearch-hadoop](http://spark-packages.org/package/elastic/elasticsearch-hadoop)
  * [Configuration](https://www.elastic.co/guide/en/elasticsearch/hadoop/current/configuration.html)
  * [Adding Spark (and Security) to Elasticsearch for Hadoop](https://www.elastic.co/webinars/adding-spark-and-security-to-elasticsearch-for-hadoop/?baymax=rtp&elektra=docs&iesrc=ctr)
  * [Apache Spark support](https://www.elastic.co/guide/en/elasticsearch/hadoop/current/spark.html)
  * [[elasticsearch] [Hadoop][Spark] Exclude metadata fields from _source](http://grokbase.com/t/gg/elasticsearch/152ctjtsdw/hadoop-spark-exclude-metadata-fields-from-source)
  * Bulk
    * [elasticsearch-hadoop: bulk indexing JSON](https://groups.google.com/forum/#!msg/elasticsearch/jlAioYzsDGM/IO7oS6eEBUMJ)
    * Upsert
      * [How to upsert an initial value into elasticsearch using spark?](https://discuss.elastic.co/t/how-to-upsert-an-initial-value-into-elasticsearch-using-spark/29450) cannot use upsert yet
      * [Considering bulk upserts from hadoop](https://groups.google.com/forum/#!topic/elasticsearch/8s25zRo-3Lk) no upsert yet
      * [How to upsert into elasticsearch in spark?](http://stackoverflow.com/questions/32605883/how-to-upsert-into-elasticsearch-in-spark)
  * [sparkes - Spark ↔ ElasticSearch Build Status ElasticSearch integration for Apache Spark](https://github.com/SHSE/spark-es)
  * troubleshooting
    * `org.elasticsearch.hadoop.EsHadoopException: Could not write all entries [.../...] (maybe ES was overloaded?). Bailing out` [Pushback to hadoop from es on bulk load](https://discuss.elastic.co/t/pushback-to-hadoop-from-es-on-bulk-load/1535)
  * [Hadoop Map/Reduce runtime options](https://www.elastic.co/guide/en/elasticsearch/hadoop/current/configuration-runtime.html)
* [elasticsearch-jaso-analyzer - EJ Analyzer](https://github.com/netcrazy/elasticsearch-jaso-analyzer)
* [Elasticsearch Langdetect Plugin](https://github.com/jprante/elasticsearch-langdetect)
* [elasticsearch-py](https://elasticsearch-py.readthedocs.org)
  * [elasticsearch-py](https://github.com/elastic/elasticsearch-py)
  * [How to Query Elasticsearch with Python](http://marcobonzanini.com/2015/02/02/how-to-query-elasticsearch-with-python/)
  * [Having Fun: Python and Elasticsearch, Part 1](http://bitquabit.com/post/having-fun-python-and-elasticsearch-part-1/)
* [Embulk - open-source bulk data loader that helps data transfer between various databases, storages, file formats, and cloud services](http://www.embulk.org/)
* [es-swapi-test](https://github.com/ernestorx/es-swapi-test/blob/master/ES%20notebook.ipynb?__hstc=62641971.0135eefa3bdff6b723c411e4c9086d2d.1448241371111.1448241371111.1448241371111.1&__hssc=62641971.1.1448241371112&__hsfp=2294634674)
* [Fess is very powerful and easily deployable Enterprise Search Server. http://fess.codelibs.org/](https://github.com/nocode2k/fess)
* [fluent-plugin-beats at Elasticsearch meetup](http://www.slideshare.net/repeatedly/fluentpluginbeats-at-elasticsearch-meetup-14)
* [fluent-plugin-mysql-replicator](https://github.com/y-ken/fluent-plugin-mysql-replicator)
* [Hierarchical filtering](http://demo.searchkit.co/taxonomy)
* [Komoran](https://github.com/shin285/KOMORAN)
  * [KOMORAN 3.0 beta](http://shineware.tistory.com/entry/KOMORAN-30-beta)
* logstash
  * [[Logstash] logstash slack chat output plugin 만들기](http://jjeong.tistory.com/1161)
* [match - Scalable reverse image search built on Kubernetes and Elasticsearch](https://github.com/pavlovml/match)
* [packetbeat - real-time network packet analytics](https://www.elastic.co/products/beats/packetbeat)
* [pyes - Python connector for ElasticSearch - the pythonic way to use ElasticSearch](https://github.com/aparo/pyes)
* [Raigad - Co-Process for backup/recovery, Auto Deployments and Centralized Configuration management for ElasticSearch](https://github.com/Netflix/Raigad)
* Rally
  * [Announcing Rally: Our benchmarking tool for Elasticsearch](https://www.elastic.co/blog/announcing-rally-benchmarking-for-elasticsearch)
* [Requests is an elegant and simple HTTP library for Python, built for human beings](http://docs.python-requests.org/)
  * [Elasticsearch/Python test](https://gist.github.com/bonzanini/fe2ff32116f16e3009be)
  * [How to Query Elasticsearch with Python](http://marcobonzanini.com/2015/02/02/how-to-query-elasticsearch-with-python/)
  * [How to use Bulk API to store the keywords in ES by using Python](http://stackoverflow.com/questions/20288770/how-to-use-bulk-api-to-store-the-keywords-in-es-by-using-python)
  * [Python POST binary data](http://stackoverflow.com/questions/14365027/python-post-binary-data) post bulk --data-binary
  * [python-requests equivalent to curl's --data-binary?](http://stackoverflow.com/questions/17680688/python-requests-equivalent-to-curls-data-binary)
  * [elasticsearch bulk indexing using python](http://stackoverflow.com/questions/19271943/elasticsearch-bulk-indexing-using-python)
* [Search Guard for Elasticsearch 2.3.1 BETA 1](https://github.com/floragunncom/search-guard)
* [subitolabs - ElasticSearch TestR, filters - tokenizers - analyzers](http://es.subitolabs.com/#/)
* [Timelion: The time series composer for Kibana](https://www.elastic.co/kr/blog/timelion-timeline)
* [VOYAGER : 검색 엔진 기반 실시간 이슈 감지 시스템](http://engineering.riotgames.com/news/voyager-original-korean)

## Plugin
* [Plugins - site 플러그인과 custom analyzer 플러그인 만들기](http://jjeong.tistory.com/818)
* [Plugin development for elasticsearch](https://speakerdeck.com/salyh/plugin-development-for-elasticsearch)
* [elasticsearch-analysis-arirang - korean analyzer (lucene analyzer kr arirang)](https://github.com/HowookJeong/elasticsearch-analysis-arirang/)
  * [Arirang analyzer 버전 올렸습니다.](http://jjeong.tistory.com/1142)
  * [Elasticsearch에 Arirang 외부 사전 등록하기](http://jjeong.tistory.com/1143)
* [Effective Elasticsearch Plugin Management with Docker](https://www.elastic.co/blog/elasticsearch-docker-plugin-management)
* [youtube.com/results?search_query=elasticsearch+plugin](https://www.youtube.com/results?search_query=elasticsearch+plugin)
* [Running site plugins with Elasticsearch 5.0](https://www.elastic.co/blog/running-site-plugins-with-elasticsearch-5-0)

## REST API
* status

  ```
  curl -XGET 'http://localhost:9200/_cluster/state
  curl -XGET 'http://localhost:9200/_status
  curl -XGET 'http://localhost:9200/_nodes/stats?all=true
  curl -XGET 'http://localhost:9200/_nodes
  ```

# Lucene
* [Search Engine (내용기반 검색 기술 : FTR) ](https://docs.com/sunnykwak/3330)
* [http://lucene.apache.org/](http://lucene.apache.org/)
  * [http://lucene.apache.org/core/4_10_3/](http://lucene.apache.org/core/4_10_3/)
* [http://lucenekorean.svn.sourceforge.net/](http://lucenekorean.svn.sourceforge.net/)
* [Lucene and MySQL](http://www.vikasing.com/2009/07/lucene-and-mysql.html)
  * [Lucene and MySQL (Correction!)](http://www.vikasing.com/2009/10/lucene-and-mysql-correction.html)
* [Exploiting CSRF against search with Lucene](https://www.idontplaydarts.com/2015/09/cross-domain-timing-attacks-against-lucene/)
* [BM25 The Next Generation of Lucene Relevance](http://opensourceconnections.com/blog/2015/10/16/bm25-the-next-generation-of-lucene-relevation/)
