Time Series
===========

* [Neural networks for algorithmic trading. Part One — Simple time series forecasting](https://medium.com/@alexrachnog/neural-networks-for-algorithmic-trading-part-one-simple-time-series-forecasting-f992daa1045a)
* [Elasticsearch as a Time Series Data Store](https://www.elastic.co/blog/elasticsearch-as-a-time-series-data-store)
  * [시계열 데이터 스토어로서의 Elasticsearch](https://www.elastic.co/kr/blog/elasticsearch-as-a-time-series-data-store)
* [Time series classification](http://www.slideshare.net/hunkim/time-series-classification)
* [BEGINNER'S GUIDE TO TIME SERIES ANALYSIS](https://www.quantstart.com/articles/Beginners-Guide-to-Time-Series-Analysis)
* [Time series data: the worst and best use case in distributed databases](http://www.thedotpost.com/2015/06/paul-dix-time-series-data-the-worst-and-best-use-case-in-distributed-databases)
* [Displaying Time Series, Spatial, and Space-Time Data with R](http://zenk.chapelin.fr/book.pdf)
* [SERIAL CORRELATION IN TIME SERIES ANALYSIS](https://www.quantstart.com/articles/Serial-Correlation-in-Time-Series-Analysis)
* [TF-KR 첫모임: CNN과 Data Mutation을 이용한 Time Series Classification](https://www.youtube.com/watch?v=IiB6oElqCxA)
* [ETS 모델 기반 시계열 예측](http://ko.logpresso.com/documents/time-series/ets) 지수평활법
* **[머신러닝을 통한 타임시리즈 예측](http://hamait.tistory.com/837)**
* **[Time-series data: Why (and how) to use a relational database instead of NoSQL](https://blog.timescale.com/time-series-data-why-and-how-to-use-a-relational-database-instead-of-nosql-d0cd6975e87c)**
* [타임시리즈 데이터의 feature extraction 에 관한 논문&오픈소스 링크](http://hamait.tistory.com/860)
* [파이썬 코딩으로 말하는 데이터 분석 - 10. DTW (Data time wrapping)](http://hamait.tistory.com/862)
* [Time Series Analysis with Generalized Additive Models](https://opendatascience.com/blog/time-series-analysis-with-generalized-additive-models/)
* [Time Series Analysis With Generalized Additive Models](https://www.datasciencecentral.com/profiles/blogs/time-series-analysis-with-generalized-additive-models)
* [Scaling Time Series Data Storage — Part I](https://medium.com/netflix-techblog/scaling-time-series-data-storage-part-i-ec2b6d44ba39)
* [Challenge of the week: identifying patterns in complex time series](https://www.datasciencecentral.com/forum/topics/challenge-of-the-week-identifying-patterns-in-complex-time-series)

# Library
* [Curator: Tending your time-series indices](https://www.elastic.co/kr/blog/curator-tending-your-time-series-indices)
* [Gorilla: A Fast, Scalable, In-Memory Time Series Database](http://www.vldb.org/pvldb/vol8/p1816-teller.pdf)
* [hunting_criminals_demo](https://github.com/Atigeo/hunting_criminals_demo)
* [influxdata platform - THE PLATFORM FOR TIME-SERIES DATA](https://influxdata.com/time-series-platform/)
* [iSAX](http://www.cs.ucr.edu/~eamonn/iSAX/iSAX.html)
  * [iSAX 2.0: Indexing and Mining One Billion Time Series](http://www.cs.ucr.edu/~eamonn/iSAX_2.0.pdf)
  * [iSAX: Indexing and Mining Terabyte Sized Time Series](http://www.cs.ucr.edu/~eamonn/iSAX.pdf)
* [Kapacitor - Open source framework for processing, monitoring, and alerting on time series data](https://github.com/influxdb/kapacitor)
* [Khronus - A reactive time series database](https://github.com/Searchlight/khronus)
* [MetricsGraphics.js](http://metricsgraphicsjs.org/)
  * [metrics-graphics - A library optimized for concise, principled data graphics and layouts. http://metricsgraphicsjs.org](https://github.com/mozilla/metrics-graphics)
* [Prophet: forecasting at scale](https://research.fb.com/prophet-forecasting-at-scale/)
  * “일반인”들도 시계열 예측을 쉽게 할 수 있는 패키지를 오픈소스로 릴리즈(Python, R 지원)
  * 내부적인 동작은 대표적인 시계열 예측 방식인 ARIMA 계열이 아니라 Bayesian 방식의 Generalized Additive Model로 동작
  * 구간별로 나눠서 트렌드를 보기 때문에 추세의 변화를 자동으로 감지
  * 연단위 변화 요인은 푸리에 시리즈로 모델링함
  * 주단위 변화 요인은 더미 변수로 모델링함
  * 추석, 설날, 상품 출시, 광고 실시 등의 요인은 사용자 정의 리스트로 반영
  * dataframe 형식으로 (DateTime, Value)의 두 컬럼만 입력으로 넣으면 그 다음은 알아서 동작
  * [facebookincubator.github.io/prophet](https://facebookincubator.github.io/prophet)
  * [Quick Start](https://facebookincubator.github.io/prophet/docs/quick_start.html)
  * [github.com/facebookincubator/prophet](https://github.com/facebookincubator/prophet)
  * [Prophet R 패키지](https://cran.r-project.org/package=prophet)
  * [Prophet Python 패키지](https://pypi.python.org/pypi/fbprophet)
  * gas & electricity
    * [part 1](https://github.com/Avkash/mldl/blob/master/opower-prophet/Predicting%2Bgas%2Band%2Belectric%2Busage%2Busing%2BFacebook%2BProphet%2B-%2BPart1.ipynb)
    * [part 2](https://github.com/Avkash/mldl/blob/master/opower-prophet/Predicting%2Bgas%2Band%2Belectric%2Busage%2Busing%2BFacebook%2BProphet%2B-%2BPart2.ipynb)
    * [data](https://raw.githubusercontent.com/Avkash/mldl/master/opower-prophet/RefBldgHospitalNew2004_7.1_5.0_3C_USA_CA_SAN_FRANCISCO.csv)
* [spark-ts - Time Series for Spark (The spark-ts Package)](https://github.com/sryza/spark-timeseries)
* [Timelion: The time series composer for Kibana](https://www.elastic.co/kr/blog/timelion-timeline)
* [TimescaleDB](http://www.timescale.com)
  * Postgres 엔진으로 구축된 새로운 오픈 소스 시계열 데이터베이스
  * 현재는 단일 노드 버전만 제공하고 있어 가용성에 문제
  * [github.com/timescale/timescaledb](https://github.com/timescale/timescaledb)
  * [TimescaleDB](https://www.facebook.com/nextobe1/photos/a.313464989089503.1073741829.303538826748786/334135553689113/?type=3&theater)
    * TimescaleDB는 시계열 데이터에 대해 SQL을 확장할 수 있도록 설계된 오픈소스 데이터베이스
    * PostgreSQL에서 엔지니어링되어 시간과 공간을 가로 지르는 자동 파티셔닝 (파티셔닝 키)과 완벽한 SQL 지원 제공
    * PostgreSQL 확장 기능으로 패키지되어 Apache 2 오픈 소스 라이센스로 배포
    * TimescaleDB는 빠른 소스 및 복잡한 쿼리를 위해 최적화된 오픈 소스 시계열 데이터베이스
    * "완전한 SQL"을 말하며 전통적인 관계형 데이터베이스처럼 사용하기 쉽고 이전에는 NoSQL 데이터베이스용으로 예약된 방식으로 확장
    * TimescaleDB는 이 두가지 대안(관계형과 NoSQL)에서 요구하는 절충점과 비교하여 시계열 데이터에 대해 두가지 장점을 모두 제공
      * PostgreSQL이 기본적으로 지원하는 모든 SQL에 대한 완벽한 SQL 인터페이스(보조 인덱스, 비시간 기반 집계, 하위 쿼리, JOIN, 윈도우 함수 포함)
      * PostgreSQL을 사용하는 클라이언트 또는 툴에 연결. 변경은 필요 없음
      * 시간 중심 기능, API 기능 및 최적화
      * 데이터 보존 정책에 대한 강력한 지원
    * 시계열 데이터의 특성
      * 시간 중심 : 데이터 레코드에는 항상 타임 스탬프 존재
      * 인서트 전용 : 데이터는 거의 단독으로 Insert 전용
      * 최신 : 새 데이터는 일반적으로 최근 시간 간격에 관한 것이므로 이전 간격에 대한 데이터를 업데이트하거나 누락된 데이터를 거의 다시 채우지 않음
  * [It’s About Time For Time Series Databases](https://www.nextplatform.com/2018/01/25/time-time-series-databases/)

# Python
* [Time Series Prediction with LSTM Recurrent Neural Networks in Python with Keras](http://machinelearningmastery.com/time-series-prediction-lstm-recurrent-neural-networks-python-keras/)
* [How to Create an ARIMA Model for Time Series Forecasting with Python](https://machinelearningmastery.com/arima-for-time-series-forecasting-with-python/)
* [Aileen Nielsen - Time Series Analysis - PyCon 2017](https://www.youtube.com/watch?v=zmfe2RaX-14)
* [Time Series Analysis in Python: An Introduction Additive models for time series modeling](https://towardsdatascience.com/time-series-analysis-in-python-an-introduction-70d5a5b1d52a)
* [Using LSTMs to forecast time-series](https://towardsdatascience.com/using-lstms-to-forecast-time-series-4ab688386b1f)
