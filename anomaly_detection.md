Anomaly Detection
=================

* [awesome-anomaly-detection](https://github.com/hoya012/awesome-anomaly-detection)
* [Introduction to Anomaly Detection: Concepts and Techniques](https://iwringer.wordpress.com/2015/11/17/anomaly-detection-concepts-and-techniques/)
* [NOT Yet Another Anomaly Detection Package](https://www.getlytics.com/blog/post/check_out_anomalyzer)
* [Probabilistic Programming for Anomaly Detection](http://blog.fastforwardlabs.com/post/143792498983/probabilistic-programming-for-anomaly-detection)
* [Statistical Process Control (SPC)](https://www.moresteam.com/toolbox/statistical-process-control-spc.cfm)
  * [Histogram](https://www.moresteam.com/toolbox/histogram.cfm)
* [Comparing two histograms](http://stackoverflow.com/questions/6499491/comparing-two-histograms)
* ARIMA
* DBScan
* [What is a simple algorithm to detect anomalies in time-series data?](https://www.quora.com/What-is-a-simple-algorithm-to-detect-anomalies-in-time-series-data)
* [Anomaly Detection of Time Series Data Using Machine Learning & Deep Learning](https://www.xenonstack.com/blog/data-science/anomaly-detection-of-time-series-data-using-machine-learning-deep-learning)
* [Time Series Anomaly Detection. Models and System Architectures: ARMA… | by Vadim Smolyakov | Towards Data Science](https://towardsdatascience.com/time-series-anomaly-detection-b10fdb542974)
* [Anomaly detection](http://www.slideshare.net/ChulKim12/anomaly-detection-63382182)
* [데이터 입수 이상징후 탐지](http://readme.skplanet.com/?p=13557)
* [A note about finding anomalies](https://towardsdatascience.com/a-note-about-finding-anomalies-f9cedee38f0b)
* [시계열 데이터를 분석하여 미래 예측(Anomaly Detection)](https://www.popit.kr/%EC%8B%9C%EA%B3%84%EC%97%B4-%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%A5%BC-%EB%B6%84%EC%84%9D%ED%95%98%EC%97%AC-%EB%AF%B8%EB%9E%98-%EC%98%88%EC%B8%A1-%ED%95%98%EA%B8%B0anomaly-detection/)
* [Anomaly Detection with GANs](https://www.slideshare.net/ssuser06e0c5/anomaly-detection-with-gans)
* [Detecting Performance Anomalies in External Firmware Deployments](https://medium.com/netflix-techblog/detecting-performance-anomalies-in-external-firmware-deployments-ed41b1bfcf46)
  * 소프트웨어 업데이트 패치 개발 시 아무리 테스트를 많이 해도 실제 사용자들에게 배포된 이후에 중요한 문제가 나오는 경우가 다수
  * Netflix에서 이상치 탐지 알고리즘을 적용하여 가급적 초기에 이상 상황을(이전 버전에 비해 반응 속도가 현저히 느려짐 등) 자동으로 탐지하는 방법을 공개
* [Anomaly detection using deep one class classifier](https://www.slideshare.net/ssuser06e0c5/anomaly-detection-using-deep-one-class-classifier)
* [**이상 감지 - ANOMALY DETECTION**](http://intothedata.com/02.scholar_category/anomaly_detection)
* [기계 진동(소음)에 나타나는 이상 패턴을 자동으로 탐지할 수 있을까?](https://inforience.net/2019/05/07/machine_vibration/)
* [기계 진동(소음)에 나타나는 이상 패턴을 자동으로 탐지할 수 있을까? (2)](https://inforience.net/2019/06/08/machine-vibration2)
* [How to detect anomalies in Audio Signal Processing of the heart with sound coming from mobile phone](https://medium.com/@luigi.bungaro/how-to-detect-anomalies-in-audio-signal-processing-of-the-heart-with-sound-coming-from-mobile-e034e8fd709b)
* [Fast Adaptive RNN Encoder-Decoder for Anomaly Detection in SMD Assembly Machine](https://github.com/YeongHyeon/FARED_for_Anomaly_Detection)
* [자신의 실수를 개선하면서 조금씩 똑똑해지는 anomaly detection 모델을 만들 수 있을까?](https://inforience.net/2019/06/22/interactive-anomaly-detection/)
* ARIMA 대 LSTM-주간 호텔 취소 예측
  * 과거; 매주 호텔 취소를 예측하기 위해 프로젝트를 진행
  * 이 연구의 원래 의도는 그러한 취소의 동인을 식별하고 분류를 사용하여 고객이 취소할지 (예 : 고객 취소 = 1, 취소하지 않는 고객 = 0) 예측
  * 첫번째 단계는 데이터 조작에 pandad 사용. 즉, 주별로 취소를 정렬한 다음 매주 총 취소수를 얻기 위해 합산
  * 그런 다음 ARIMA와 LSTM을 사용하여 테스트세트에서 향후 취소를 예측하기로 결정. 이는 두개의 개별 호텔 데이터세트 (H1와 H2)에 대해 수행
  * LSTM은 보다 변동성이 높은 데이터세트 (H2)에서 더 나은 성능, ARIMA는 부드러운 트렌드(H1) 데이터세트에서 더 높은 예측 정확도
  * 결론; LSTM과 같은 머신러닝 모델은 다른 모델과 마찬가지로 상황에 적합한 것은 아니며 모델을 선택하기 전에 작업중인 데이터를 이해해야 한다
  * [Part 1: Predicting Hotel Cancellations with Support Vector Machines and ARIMA](https://www.michael-grogan.com/hotel-cancellations/)
  * [Part 2: Predicting Hotel Cancellations with a Keras Neural Network](https://www.michael-grogan.com/hotel-cancellations-neuralnetwork/)
  * [Part 3: Predicting Weekly Hotel Cancellations with an LSTM Network](https://www.michael-grogan.com/hotel-cancellations-lstm/)
* [Operational AI: 지속적으로 학습하는 Anomaly Detection 시스템 만들기](https://deview.kr/2019/schedule/286)
* [보안 모니터링을 위한 머신러닝 알고리즘 적용기](https://engineering.linecorp.com/ko/blog/machine-learning-for-security-monitoring/)
* [Introduction to Deep Anomaly Detection](https://kh-kim.github.io/blog/2019/12/12/Deep-Anomaly-Detection.html)
* [“Anomaly Detection 개요： (1) 이상치 탐지 분야에 대한 소개 및 주요 문제와 핵심 용어, 산업 현장 적용 사례 정리”](http://research.sualab.com/introduction/review/2020/01/30/anomaly-detection-overview-1.html)
* [Anomaly Detection 개요： (2) Out-of-distribution(OOD) Detection 문제 소개 및 핵심 논문 리뷰](http://research.sualab.com/introduction/review/2020/02/20/anomaly-detection-overview-2.html)
* [엘라스틱 지도학습으로 IDS 정오탐 구분해보기](https://www.popit.kr/%EC%97%98%EB%9D%BC%EC%8A%A4%ED%8B%B1-%EC%A7%80%EB%8F%84%ED%95%99%EC%8A%B5%EC%9C%BC%EB%A1%9C-ids-%EC%A0%95%EC%98%A4%ED%83%90-%EA%B5%AC%EB%B6%84%ED%95%B4%EB%B3%B4%EA%B8%B0/)
* [Simple Anomaly Detection Using Plain SQL | Haki Benita](https://hakibenita.com/sql-anomaly-detection)
* [Anomaly Detection on AWS (Korean) | AWS 교육 및 자격증](https://www.aws.training/Details/Video?id=61180)
* [실시간 데이터 검증하기 | MakinaRocks Tech Blog](https://makinarocks.github.io/testing-data-in-online-env/)

# Book
* [엘라스틱서치로 알아보는 이상징후 분석: Data Anomaly Detection](https://play.google.com/store/books/details/강명훈_엘라스틱서치로_알아보는_이상징후_분석?id=eqjDDwAAQBAJ)

# Library
* [CFA_for_anomaly_localization](https://github.com/sungwool/cfa_for_anomaly_localization)
* [rule_engine: Anomaly classification with rules](https://github.com/jjthomas/rule_engine)
  * [A Fast Decision Rule Engine for Anomaly Detection - YouTube](https://www.youtube.com/watch?v=KSf3NoXONqI)

# Python
* [anomaly detection with python](https://speakerdeck.com/rosiebloxsom/anomaly-detection-with-python)
* [5 Ways to Detect Outliers That Every Data Scientist Should Know (Python Code)](https://towardsdatascience.com/5-ways-to-detect-outliers-that-every-data-scientist-should-know-python-code-70a54335a623)
* [Anomaly Detection with PyOD!. Have you used this wonderful Python… | by Dr. Dataman | Towards Data Science](https://towardsdatascience.com/anomaly-detection-with-pyod-b523fc47db9)
* [Anomaly Detection in Time Series Data using Keras](https://morioh.com/p/41c762032173)
* [Baypiggies January 2022: Time Series Anomaly Detection - YouTube](https://www.youtube.com/watch?v=I58aW_w1dwk)
* [A Complete Anomaly Detection Algorithm From Scratch in Python: Step by Step Guide | by Rashida Nasrin Sucky | Oct, 2020 | Towards Data Science](https://towardsdatascience.com/a-complete-anomaly-detection-algorithm-from-scratch-in-python-step-by-step-guide-e1daf870336e)
* [Unsupervised Anomaly Detection with Isolation Forest - Elena Sharova - YouTube](https://www.youtube.com/watch?v=5p8B2Ikcw-k)
* [pyculiarity](https://pypi.python.org/pypi/pyculiarity/0.0.2)
