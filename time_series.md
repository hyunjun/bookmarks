Time Series
===========

* [Neural networks for algorithmic trading. Part One — Simple time series forecasting](https://medium.com/@alexrachnog/neural-networks-for-algorithmic-trading-part-one-simple-time-series-forecasting-f992daa1045a)
* [Elasticsearch as a Time Series Data Store](https://www.elastic.co/blog/elasticsearch-as-a-time-series-data-store)
* [Time series classification](http://www.slideshare.net/hunkim/time-series-classification)
* [BEGINNER'S GUIDE TO TIME SERIES ANALYSIS](https://www.quantstart.com/articles/Beginners-Guide-to-Time-Series-Analysis)
* [Time series data: the worst and best use case in distributed databases](http://www.thedotpost.com/2015/06/paul-dix-time-series-data-the-worst-and-best-use-case-in-distributed-databases)
* [Displaying Time Series, Spatial, and Space-Time Data with R](http://zenk.chapelin.fr/book.pdf)
* [SERIAL CORRELATION IN TIME SERIES ANALYSIS](https://www.quantstart.com/articles/Serial-Correlation-in-Time-Series-Analysis)
* [TF-KR 첫모임: CNN과 Data Mutation을 이용한 Time Series Classification](https://www.youtube.com/watch?v=IiB6oElqCxA)
* [Time Series Prediction with LSTM Recurrent Neural Networks in Python with Keras](http://machinelearningmastery.com/time-series-prediction-lstm-recurrent-neural-networks-python-keras/)
* [ETS 모델 기반 시계열 예측](http://ko.logpresso.com/documents/time-series/ets) 지수평활법

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
  * [Quick Start](https://facebookincubator.github.io/prophet/docs/quick_start.html)
* [spark-ts - Time Series for Spark (The spark-ts Package)](https://github.com/sryza/spark-timeseries)
* [Timelion: The time series composer for Kibana](https://www.elastic.co/kr/blog/timelion-timeline)
* [TimesacleDB](http://www.timescaledb.com)
  * Postgres 엔진으로 구축된 새로운 오픈 소스 시계열 데이터베이스
  * 현재는 단일 노드 버전만 제공하고 있어 가용성에 문제
