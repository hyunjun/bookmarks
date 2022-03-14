Logging
=======

* function/method의 시작과 끝 부분에 log를 넣자
  * 너무 많은 log를 남기는 게 보기 힘들 수는 있지만, 확인이 어려운 거 보다는 좋다
  * 최소한 해당 function/method 내부가 문제인지 외부가 문제인지는 확인이 가능하다
* 같은 API server를 여러 개의 section으로 나눠서 운영할 때 좋은 logging은 뭘까?
  * 서로 호출하는 동작이 있는데, logging을 나눠서 각각 저장하는 게 좋은가, 한 곳에 모아서 구분해서 보는 게 좋은가?
* [로그 기깔나게 잘 디자인하는 법](https://www.slideshare.net/jeongsangbaek/ss-80795259)
* [LoggingThe Ultimate Guide - your open-source resource for understanding, analyzing, and troubleshooting system logs](https://www.loggly.com/ultimate-guide/)
* [Centralized Logging at Signal](http://www.signal.co/dev-log/centralized-logging/)
* [DESIGNING A SEARCH SYSTEM FOR LOG DATA — PART 2](http://www.philipotoole.com/designing-a-search-system-for-log-data-part-2/)
* [Logging을 System.out으로 하면 안되는 이유](http://silentsoft.tistory.com/13)
* [Centralized Log Server 를 위한 기본 세팅 (EC2 + ElasticSearch + Logstash + filebeat + kibana)](http://knphouse.tistory.com/85)
* [log 생성하기](http://downman.tistory.com/155)
* [How-to: Log Analytics with Solr, Spark, OpenTSDB and Grafana](http://blog.cloudera.com/blog/2017/03/how-to-log-analytics-with-solr-spark-opentsdb-and-grafana/)
* [#review AWS + Tajo를 이용한 '테라 렉 로그 분석 이야기'](http://ohyecloudy.com/pnotes/archives/aws-tajo-tera-lag-log/)
* [**#ndc_15 #review 쿠키런 로그 시스템 - 바쁘고 가난한 개발자를 위해**](http://ohyecloudy.com/pnotes/archives/ndc15-cookie-run-log-system/)
* [Conetix Network Operations Centre Build Part 3 - Metrics and Monitoring](https://www.conetix.com.au/blog/conetix-network-operations-centre-build-part-3)
* [정적 기록자는 이제 그만](https://justhackem.wordpress.com/2017/07/07/no-more-static-logger/)
* [로그 데이터로 유저 이해하기](http://woowabros.github.io/woowabros/2017/07/30/logdata.html)
* [로그를 잘 남기기](https://ash84.net/2017/09/29/how-do-you-keep-your-logs/)
* [구글 스택드라이버를 이용한 애플리케이션 로그 모니터링](http://bcho.tistory.com/1214)
* [The Architecture of the Next CERN Accelerator Logging Service](https://databricks.com/blog/2017/12/14/the-architecture-of-the-next-cern-accelerator-logging-service.html)
* Building a Distributed Log from Scratch
  * [Part 1: Storage Mechanics](https://bravenewgeek.com/building-a-distributed-log-from-scratch-part-1-storage-mechanics/)
  * [Part 2: Data Replication](https://bravenewgeek.com/building-a-distributed-log-from-scratch-part-2-data-replication/)
  * [Part 3: Scaling Message Delivery](https://bravenewgeek.com/building-a-distributed-log-from-scratch-part-3-scaling-message-delivery/)
  * [Part 4: Trade-Offs and Lessons Learned](https://bravenewgeek.com/building-a-distributed-log-from-scratch-part-4-trade-offs-and-lessons-learned/)
  * [Part 5: Sketching a New System](https://bravenewgeek.com/building-a-distributed-log-from-scratch-part-5-sketching-a-new-system/)
* [Part 1: Building a Centralized Logging Application](https://medium.com/eulercoder/part-1-building-a-centralized-logging-application-5a537033da0a)
* [Logging in Android](https://android.jlelse.eu/logging-in-android-cfcd50cdc1ae)
* **NDC18 〈야생의 땅: 듀랑고〉의 데이터 엔지니어링 이야기: 로그 시스템 구축 경험 공유**
  * [1부](https://www.slideshare.net/ssuser380e9c/ndc18-95524337)
  * [2부](https://www.slideshare.net/ssuser380e9c/ndc18-2-95522893)
* [How To Write Error Messages That Don’t Suck](https://medium.freecodecamp.org/how-to-write-error-messages-that-dont-suck-f31c53b64c3e)
* [**로그 파일은 좋다**](https://libsora.so/posts/log-file-is-good/) 실제 구현에서 겪을 수 있는 상황에 대한 이야기라 좋음
* [더 나은 개발자로 성장합는 팁, " 로그를 잘 남기세요."](https://www.youtube.com/watch?v=HxzlJWMcHng)
* [로그 시스템의 개념과, 구글 스택드라이버 그리고 삼성전자 사례](https://bcho.tistory.com/1330)
* [멀티클라우드를 이용한 로그 분석 플랫폼 개발하기](https://medium.com/watcha/%EB%A9%80%ED%8B%B0%ED%81%B4%EB%9D%BC%EC%9A%B0%EB%93%9C%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%9C-%EB%A1%9C%EA%B7%B8-%EB%B6%84%EC%84%9D-%ED%94%8C%EB%9E%AB%ED%8F%BC-%EA%B0%9C%EB%B0%9C%ED%95%98%EA%B8%B0-8c5f671df559)
* [How to Write Log Files That Save You Hours of Time](https://medium.com/better-programming/how-to-write-log-files-that-save-you-hours-of-time-1ff0cd9ae2ed)
* [Code Walked Out of a Spaghetti Bar… | by Nduka Anthony Okocha | Capital One Tech | Jun, 2020 | Medium](https://medium.com/capital-one-tech/code-walked-out-of-a-spaghetti-bar-2dcc1750789a)
* [Logging Like a Pro. Theories and best practices on… | by Neal Hu | ITNEXT](https://itnext.io/logging-like-a-pro-8cc6ad09e415)
* [쏘카에서 로그 파이프라인을 구축](https://www.linkedin.com/posts/mssqldba-joo_%EB%A1%9C%EA%B7%B8-%ED%8C%8C%EC%9D%B4%ED%94%84%EB%9D%BC%EC%9D%B8-%EA%B5%AC%EC%B6%95-ugcPost-6772078735547097088-Ghfd/)
* [1주차-로그관리 어떻게 할 것인가? - SLiPP 스터디 - SLiPP::위키](https://www.slipp.net/wiki/pages/viewpage.action?pageId=18350094)
* [Why you shouldn’t log into db. From time to time, I see systems… | by Márton Waszlavik | Medium](https://medium.com/@marton.waszlavik/why-you-shouldnt-log-into-db-e700c2cb0c8c)
* [What the Fastly outage can teach us about writing error messages | OnlineOrNot](https://onlineornot.com/what-fastly-outage-can-teach-about-writing-error-messages)
* [**데이터 로그 설계, 데이터 로깅, 이벤트 로그 설계, 데이터 QA의 모든 것 · 어쩐지 오늘은**](https://zzsza.github.io/data/2021/06/13/data-event-log-definition/)
  * 서비스에서 데이터 추적을 위해 많은 로그를 쌓게 되는데 이 데이터 로그의 설계부터 QA까지 기획자, PM, 마케터들이 이해할 수 있게 정리한 글
  * 데이터 로깅을 하기 위해 필요한 상식, 사용할 수 있는 플랫폼들 정리. 서버 로그와 클라이언트 로그의 차이, 웹이나 앱의 로깅 특성도 잘 정리
  * 이벤트 로그를 어떻게 설계하는 방법과 예시도 잘 나와 있어서 데이터 추적에 대한 이해도를 높이거나 서비스에 로깅 설계를 할 때 참고
* [유저를 이해하는 단서, 이벤트 로그 | 하조은의 블로그](https://hajoeun.blog/event-log-is-a-clue-to-understand-user)
* [29CM 로그 수집 시스템 소개. 29CM에서는 기존의 로그 시스템, 신규 구축한 로그 시스템 두가지를… | by 29CM | 29CM 기술블로그 | Jul, 2021 | Medium](https://medium.com/29cm/29cm-%EB%A1%9C%EA%B7%B8-%EC%88%98%EC%A7%91-%EC%8B%9C%EC%8A%A4%ED%85%9C-%EC%86%8C%EA%B0%9C-e7955d7deec6)
  * 29CM에서 기존에는 Fluentd와 Elasticsearch로 로그 수집, 관리의 어려움과 로그 유실을 막기 위해 새 로그 수집 시스템 구축
  * 새 시스템은 로그 수집 단계에 Kafka를 두어 ES에 문제가 생겨도 Kafka가 데이터 유실 방지, Kafka 플러그인을 기본으로 제공하는 Logstash로 변경
* [Logging at Twitter: Updated](https://blog.twitter.com/engineering/en_us/topics/infrastructure/2021/logging-at-twitter-updated)
* [Who is the winner — Comparing Vector, Fluent Bit, Fluentd performance | by Ajay Gupta | IBM Cloud | Medium](https://medium.com/ibm-cloud/log-collectors-performance-benchmarking-8c5218a08fea)
* [What's in a Good Error Message? - Gunnar Morling](https://www.morling.dev/blog/whats-in-a-good-error-message/)
* [5 new sudo features sysadmins need to know in 2022 | Opensource.com](https://opensource.com/article/22/2/new-sudo-features-2022)

# Fluentd
* [Fluentd](http://www.fluentd.org/)
* [분산 로그 & 데이타 수집기 Fluentd](http://bcho.tistory.com/1115)
* [Personal Logging으로 삽질하기 #1](https://medium.com/@HatusneMiku3939/personal-logging%EC%9C%BC%EB%A1%9C-%EC%82%BD%EC%A7%88%ED%95%98%EA%B8%B0-1-d40ae348ac5e)
* [Personal Logging으로 삽질하기 #2](https://medium.com/@HatusneMiku3939/personal-logging%EC%9C%BC%EB%A1%9C-%EC%82%BD%EC%A7%88%ED%95%98%EA%B8%B0-2-36677466b8b8)
* [fluentd와 함께하는 검색 데이터 수집](https://dailyhotel.io/fluentd%EC%99%80-%ED%95%A8%EA%BB%98%ED%95%98%EB%8A%94-%EA%B2%80%EC%83%89-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EC%88%98%EC%A7%91-b76932a8dc2a)
* [Fluentd에서 PubSub로 데이터 보내기](https://jungwoon.github.io/bigquery/2017/11/13/BigQuery-Lecture-1/)
* [CNCF, Fluentd 프로젝트 졸업을 발표](https://www.44bits.io/ko/post/news--fluentd-has-graduated-cncf)
* [Fluentd vs. Logstash: A Comparison of Log Collectors](http://logz.io/blog/fluentd-logstash)
* [Fluentd로 데이터파이프라인 구축하기 kafka→kafka→s3](https://blog.voidmainvoid.net/261)
* [Fluentd? 나만의 에이전트 패키징! – gywndi's database](https://gywn.net/2021/09/package-own-fluentd-agent/)

# Library
* [angle-grinder: Slice and dice logs on the command line](https://github.com/rcoh/angle-grinder)
  * [Angle-grinder - 실시간 로그 뷰어 | GeekNews](https://news.hada.io/topic?id=4694)
* [Apache logging services](https://logging.apache.org)
* [Apex Logs — Structured log management](https://apex.sh/logs/)
  * [Apex Logs public beta. My latest product Apex Logs is now in… | by TJ Holowaychuk | Aug, 2020 | Medium](https://medium.com/@tjholowaychuk/apex-logs-public-beta-48c683464054)
* lnav [The Logfile Navigator | The Logfile Navigator, lnav for short, is an advanced log file viewer for the small-scale](https://lnav.org/)
  * [The Logfile Navigator | GeekNews](https://news.hada.io/topic?id=4606)
* [LOGAI – AUTOMATED LOG ANALYTICS FOR VALIDATION](https://ko.hortonworks.com/blog/logai-automated-log-analytics-validation/)
  * Hortonworks의 HDP 테스트에서 나온 로그를 분석하는 도구
  * 시스템에서 빈도(frequency), 동시 발생(co-occurence), 기타 상관 모델을 사용하여 에러를 하이라이트하고, trace와 기타 내용
  * Web UI 제공
* [logbook: An extensible Java library for HTTP request and response logging](https://github.com/zalando/logbook)
* [LogDevice - a scalable and fault tolerant distributed log system](https://github.com/facebookincubator/LogDevice)
  * [LogDevice: a distributed data store for logs](https://code.fb.com/core-data/logdevice-a-distributed-data-store-for-logs/)
  * [Open-sourcing LogDevice, a distributed data store for sequential data](https://logdevice.io/blog/2018/09/12/open-sourcing-announcement.html)
* [Logging](https://logging.apache.org) Apache logging services
* [loglab: Design & Apply Log Schema](https://github.com/haje01/loglab)
* [Logswan is a fast Web log analyzer using probabilistic data structures](https://github.com/fcambus/logswan)
* [loguru: A lightweight C++ logging library](https://github.com/emilk/loguru)
* [mulog: μ/log is a micro-logging library that logs events and data, not words!](https://github.com/BrunoBonacci/mulog) clojure, log 기록을 text가 아니라 clojure data로 기록
* [Palallax - Open Source Log Analyzer for Palo Alto Networks Next-Generation Firewall](http://www.ap-com.co.jp/ja/paloalto/palallax/index_en.html)
* [SenseLogs - Instant log data in seconds, not minutes](https://www.sensedeep.com/senselogs/)
* [YALV - Yet Another Log Viewer](http://marsinvasion.github.io/yalv/)
* [Zipkin - a distributed tracing system](https://github.com/openzipkin/zipkin)
  * Zipkin을 이용한 MSA 환경에서 분산 트렌젝션의 추적
    * [#1](http://bcho.tistory.com/1243)
    * [#2 - Spring과 Zipkin을 이용한 추적](http://bcho.tistory.com/1244)
    * [#3 -Stackdriver를 zipkin으로 사용하기](http://bcho.tistory.com/1245)
  * [Zipkin과 Scouter v2.5를 연동해보자](https://gunsdevlog.blogspot.com/2018/11/how-to-use-zipkin-scouter-storage.html)
  * [LINE 광고 플랫폼의 MSA 환경에서 Zipkin을 활용해 로그 트레이싱하기 - LINE ENGINEERING](https://engineering.linecorp.com/ko/blog/line-ads-msa-opentracing-zipkin/)
  * [Distributed tracing with Spring Cloud Sleuth and Zipkin | Spring Boot | Microservices | Example Code - YouTube](https://www.youtube.com/watch?v=hEgdIT7AEfc)
  * [How to Implement Distributed Logging & Tracing using Sleuth & Zipkin? - Making Java easy to learn](https://javatechonline.com/how-to-implement-distributed-logging-tracing-using-sleuth-zipkin/)

# Logrotate
* [logrotate 사용하기 (CentOS 기준)](http://jybaek.tistory.com/761)
* [logrotate를 이용하여 로그 파일을 자동으로 삭제하기](https://medium.com/encored-technologies-engineering-data-science/logrotate를-이용하여-로그-파일을-자동으로-삭제하기-dccf7b1b52b0)
* [(리눅스 업스킬 도전 #18) 로그 파일 회전시키기](https://jhrogue.blogspot.com/2020/10/18.html)
  * [linuxupskillchallenge/18.md at master · snori74/linuxupskillchallenge](https://github.com/snori74/linuxupskillchallenge/blob/master/18.md)
