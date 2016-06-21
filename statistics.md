Statistics
==========
* **[21세기 통계학을 배우는 방법](http://statkclee.github.io/window-of-statistics/)**
* [통계는 숫자가 아니라 경험이 살린다](http://ppss.kr/archives/37791)
* [learnandrun.co.kr/category/learn-run/mathematics](http://learnandrun.co.kr/category/learn-run/mathematics)
* [Sample your data!](http://www.chrisgoldammer.com/posts/sampling.html)
* [Understanding Variance, Co-Variance, and Correlation](http://www.countbayesie.com/blog/2015/2/21/variance-co-variance-and-correlation)
* [uniform random float](http://mumble.net/~campbell/2014/04/28/uniform-random-float)
* [A Decentralized Lie Detector](http://www.augur.net/blog/a-decentralized-lie-detector)
* [이정희 그리고 생일 역설](http://ppss.kr/archives/37856)
* [Expectation and Variance from High School to Grad School](http://www.countbayesie.com/blog/2015/3/19/expectation-and-variance-from-high-school-to-grad-school)
* [Kernel Density Estimation(커널밀도추정)에 대한 이해](http://darkpgmr.tistory.com/147)
* [The Price is Right Again](http://www.amstat.org/publications/jse/v20n2/burks.pdf)
* [[statistics] Naive Bayesian, HMM, Maximum Entropy Model, CRF](https://github.com/dsindex/blog/wiki/%5Bstatistics%5D-Naive-Bayesian,-HMM,-Maximum-Entropy-Model,-CRF)
* [Engineering Statistics](http://www.itl.nist.gov/div898/handbook/index.htm)
* [http://bcho.tistory.com/category/빅데이타/통계학이론](http://bcho.tistory.com/category/%EB%B9%85%EB%8D%B0%EC%9D%B4%ED%83%80/%ED%86%B5%EA%B3%84%ED%95%99%20%EC%9D%B4%EB%A1%A0)
* [Statistics: P values are just the tip of the iceberg](http://www.nature.com/news/statistics-p-values-are-just-the-tip-of-the-iceberg-1.17412?WT.ec_id=NATURE-20150430)
* [Why We Need a Statistical Revolution](http://www.stats.org/super-learning-and-the-revolution-in-knowledge/)
* [Mean Shift Clustering](http://spin.atomicobject.com/2015/05/26/mean-shift-clustering/)
* [Pattern Recognition](http://iskim3068.tistory.com/m/post?categoryId=473315)
* [The Extent and Consequences of P-Hacking in Science](http://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1002106)
* [Exact computation of sums and means](https://radfordneal.wordpress.com/2015/05/21/exact-computation-of-sums-and-means/)
* [Why squared error?](http://www.benkuhn.net/squared)
* [How to lie with statistics](https://janav.wordpress.com/2014/01/03/how-to-lie-with-statistics/)
  * [통계로 거짓말 하는 방법](http://ppss.kr/archives/47334)
* [SERIAL CORRELATION IN TIME SERIES ANALYSIS](https://www.quantstart.com/articles/Serial-Correlation-in-Time-Series-Analysis)
* [정규분포](http://navercast.naver.com/contents.nhn?rid=22&contents_id=2490)
* [Evaluating Splatoon's Ranking System](http://www.evanmiller.org/evaluating-splatoons-ranking-system.html)
* [Understanding the t-distribution and its normal approximation](http://rpsychologist.com/d3/tdist/)
* [Statistics for Hackers by Jake VanderPlas](https://speakerdeck.com/jakevdp/statistics-for-hackers)
* [Frequentism and Bayesianism: A Python-driven Primer](http://arxiv.org/abs/1411.5018)
* [Probability, Mathematical Statistics, Stochastic Processes](http://www.math.uah.edu/stat/)
* [Probabilistic algorithms for fun and pseudorandom profit](http://www.slideshare.net/TylerTreat/probabilistic-algorithms-for-fun-and-pseudorandom-profit)
* [인지모델링 - 수리심리학 + 베이지안 인지모델링 + IT 모델링](http://psygrammer.github.io/coco/)
* [자유도의 의미](http://blog.naver.com/hancury/220625928193)
* [The Automatic Statistician - An artificial intelligence for data science](http://www.automaticstatistician.com/examples/)
* [Common Probability Distributions: The Data Scientist’s Crib Sheet](https://blog.cloudera.com/blog/2015/12/common-probability-distributions-the-data-scientists-crib-sheet/)
  * 데이터 사이언스에 많이 사용되는 확률밀도함수들
    * Bernoulli
      * 동전의 앞/뒤처럼 이벤트가 0 또는 1밖에 일어나지 않는 분포
      * 동전은 확률이 0.5/0.5 겠지만 다른 경우도 있을 수 있음
    * Uniform
      * 주사위처럼 모든 결과에 대한 확률이 동일한 확률분포
    * Binomial
      * 동전을 n번 던졌을 때 p번만큼 앞면이 나올 확률은?
      * Binomial은 이렇게 0 또는 1이 나오는 이벤트(각각이 Bernoulli확률을 갖는 이벤트)에 대해 1이 발생활 횟수에 대한 확률
    * Poisson
      * 1시간에 평균 10번의 전화통화가 온다고 가정. 그렇다면 한시간에 12번 전화통화가 올 확률은? 이것이 바로 poisson(포아송) 확률
      * 이것은, 예를 들어, 60분 중 48번의 실패(0)와 12번의 성공(1)을 하면 ok. 또는, 60분이 아니라 더 잘게 쪼개서 988번의 실패와 12번의 성공을 하면 ok
      * 이처럼 시행횟수가 크고 이벤트가 일어날 확률이 작은 bionomial 분포가 바로 poisson 분포에 수렴(이 때문에 binomial의 근사로도 사용)
    * Hypergeometric
      * 까만공과 하얀공이 절반씩 있는데 그것을 여러번 뽑는다고 가정. 그럼 이것은 Binomial과 동일한가?
      * 아님. 왜냐면 공을 뽑을 때 만약 그 공을 다시 채워넣지 않는다면 남아있는 공의 확률은 바뀌기 때문
      * Binomial의 경우와 달리 replacement(다시 보충)를 허용하지 않는 것이 바로 hypergeometric 확률입니다.
    * Geometric
      * 주사위를 굴렸을 때 한번에 6이 나올 확률은? 두번만에 6이 나올 확률은? 세번만에, 네번만에...
      * 이처럼 geometric 분포는 어떤 이벤트가 일어날 때까지의 횟수에 대한 확률
      * 이벤트의 확률이 어떠하든 늘 "가장 첫번째"에 이벤트가 발생할 확률이 가장 크다
    * Negative Binomial
      * Geometric이 한번 성공할 때까지 걸리는 횟수에 대한 분포라면 negative binominal은 n번 성공할 때까지 걸리는 횟수에 대한 분포
비슷하게 안지은거야?;;)
    * Exponential
      * bionomial의 연속버전이 poisson이었다면, geometric의 연속버전이 exponential분포
      * 다시말해 "평균 5분만에 전화가 걸려온다고 할 때 다음 전화가 7분 후에 걸려올 확률은?"
    * Weibull
      * exponential이 "다음 이벤트가 성공할 때 까지의 실패구간은"에 대한 함수였다면 반대로 Weibull은 "첫 실패가 발생할 때까지 이번 이벤트가 성공할 구간"에 대한 확률
    * Gaussian (Normal)
      * 너무 유명한 확률분포
      * 특히 매우 많은 수의 동일 확률분포를 가진 샘플들의 산술평균은 그 샘플들이 어떤 분포를 따르든(binomial이든 exponential이든 아님 다른거든) 결국 Gaussian 분포로 수렴한다는 "중심극한정리"가 매우 유용하기에 매우 많은 곳에 적용 가능
    * Log-normal
      * 변수의 log 값이 Gaussian을 나타내는 분포
      * 다시말해 Gaussian을 exponential 한 함수
    * Student’s t-distribution
      * 정규분포의 mean 값에 대한 판단을 내릴 떄 사용하는 확률분포
    * Chi-squared distribution
      * Gaussian 분포를 가진 확률변수의 제곱들의 합에 대한 분포
      * 예를 들어 k자유도의 chi-squared는 k개의 독립적인 Gaussian들에 대한 합의 확률분포
* [Statistical Methods for HCI Research](http://yatani.jp/teaching/doku.php?id=hcistats:start)
* [Statistics for everyone](http://statistics4everyone.blogspot.com/2016/05/p-story-i.html)
* [변동계수](https://ko.m.wikipedia.org/wiki/%EB%B3%80%EB%8F%99%EA%B3%84%EC%88%98) 평균 + 분산값 통합 평가

# Bayes
* [베이지언 확률](http://darkpgmr.tistory.com/119)
* [http://www.countbayesie.com](http://www.countbayesie.com)
  * [Bayes' Theorem with Lego](http://www.countbayesie.com/blog/2015/2/18/bayes-theorem-with-lego)
  * [Building a Voight-Kampff Test with Bayes Factor](http://www.countbayesie.com/blog/2015/2/27/building-a-bayesian-voight-kampff-test)
  * [A Guide to Bayesian Statistics](https://www.countbayesie.com/blog/2016/5/1/a-guide-to-bayesian-statistics)
* [The Bayesian Case Model: A Generative Approach for Case-Based Reasoning and Prototype Classification](http://papers.nips.cc/paper/5313-the-bayesian-case-model-a-generative-approach-for-case-based-reasoning-and-prototype-classification)
* [Bayes’ Theorem, Predictions and Confidence Intervals](http://kukuruku.co/hub/algorithms/bayes-theorem-predictions-and-confidence-intervals)
* [Bayesian truth serum](http://nel.mit.edu/bayesian-truth-serum)
* [Kalman and Bayesian Filters in Python](http://nbviewer.ipython.org/github/rlabbe/Kalman-and-Bayesian-Filters-in-Python/blob/master/table_of_contents.ipynb)
  * [Kalman Filter textbook using Ipython Notebook. Focuses on building intuition and experience, not formal proofs. Includes Kalman filters,extended Kalman filters, unscented Kalman filters, particle filters, and more. All exercises include solutions](https://github.com/rlabbe/Kalman-and-Bayesian-Filters-in-Python)
  * [Kalman and Bayesian Filters in Python](https://drive.google.com/file/d/0By_SW19c1BfhSVFzNHc0SjduNzg/view)
  * [How a Kalman filter works, in pictures](http://www.bzarg.com/p/how-a-kalman-filter-works-in-pictures/)
  * [칼만 필터를 이용하여 위치에서 속도를 구하는 예제](http://pinkwink.kr/781)
* [공학자를 위한 Python 사용법 25 - Quaternion을 이용한 자세 추정 칼만 필터](http://myjr52.tumblr.com/post/128707132156/%EA%B3%B5%ED%95%99%EC%9E%90%EB%A5%BC-%EC%9C%84%ED%95%9C-python-%EC%82%AC%EC%9A%A9%EB%B2%95-25)
* [Using naive bayes to predict movie review sentiment](http://blog.dataquest.io/blog/naive-bayes-movies/)
* [Continuous Bayes](http://www.sidhantgodiwala.com/blog/2015/03/14/continuous-bayes/)
* [A Case Study in Empirical Bayes](http://www.ebaytechblog.com/2015/02/06/a-case-study-in-empirical-bayes/)
* [BAYESIAN STATISTICS AS A WAY TO INTEGRATE INTUITION AND DATA](https://keen.io/blog/98491909836/bayesian-statistics-as-a-way-to-integrate-intuition-and)
* [나이브 베이즈 분류 (Naive Bayesian classification) #1 - 소개](http://bcho.tistory.com/tag/%EB%82%98%EC%9D%B4%EB%B8%8C%20%EB%B2%A0%EC%9D%B4%EC%A6%88)
* [베이지안 네트워크](http://newsight.tistory.com/158)
* [Think Bayes](http://allendowney.blogspot.kr/)
  * [Chapter 02. Introduction : Credibility, Models, and Parameters](https://github.com/psygrammer/bayesianR/blob/master/part1/ch01_02/ch01_02_intro.md)
* [Proper postulates](http://posterior.egloos.com/category/Intro%20to%20Bayes%20stat/page/2)
  * [베이즈 정리](http://posterior.egloos.com/9604153)
  * [주관적 확률의 사용과 그 경험과학적 의미](http://posterior.egloos.com/9603023)
* [Probabilistic Programming and Bayesian Methods for Hackers](https://github.com/CamDavidsonPilon/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers/blob/master/Chapter1_Introduction/Chapter1.ipynb)
* [An intro to Bayesian methods and probabilistic programming from a computation/understanding-first, mathematics-second point of view](http://camdavidsonpilon.github.io/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers/#contents)
* [BAYESIAN INFERENCE OF A BINOMIAL PROPORTION - THE ANALYTICAL APPROACH](http://www.quantstart.com/articles/Bayesian-Inference-of-a-Binomial-Proportion-The-Analytical-Approach)
* [집단지성프로그래밍 ch6. 문서 필터링](http://www.slideshare.net/icristi/ch6-48743141)
* [An Intuitive Explanation of Bayes' Theorem](http://www.yudkowsky.net/rational/bayes)
* [Probabilistic Programming & Bayesian Methods for Hackers](http://camdavidsonpilon.github.io/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers/)
* [메르스 바로 알기: 양성일 때 메르스 환자일 확률은 얼마나 될까?](http://ppss.kr/archives/49107)
* [베이지언이 되자~!](http://pgr21.com/?b=8&n=59237)
* [Bayes’ Theorem](http://crucialconsiderations.org/rationality/bayes-theorem/)
* [A Tutorial on Learning With Bayesian Networks](http://research.microsoft.com/pubs/69588/tr-95-06.pdf)
* [Basic MCMC and Bayesian statistics in... BASIC!](http://sumsar.net/blog/2015/08/basic-mcmc-and-bayesian-statistics-in-basic/)
* [Bayesian Financial Models](http://toddmoses.com/articles/read/bayesian_financial_models)
* [Bayesian Cookies](http://www.sidhantgodiwala.com/blog/2015/07/12/bayesian-cookies/)
* [In praise of Bayes](http://www.cs.ubc.ca/~murphyk/Bayes/economist.html)
* [A Brief Introduction to Graphical Models and Bayesian Networks](http://www.cs.ubc.ca/~murphyk/Bayes/bnintro.html)
* [Bayesian democracy](https://samgentle.com/posts/2015-08-28-bayesian-democracy)
* [The Bayesian Reproducibility Project](http://alexanderetz.com/2015/08/30/the-bayesian-reproducibility-project/)
* [Using Bayes Factors to Get the Most out of Linear Regression: A Practical Guide Using R](https://thewinnower.com/papers/278-using-bayes-factors-to-get-the-most-out-of-linear-regression-a-practical-guide-using-r)
* [베이즈 이론이 푸리에 정리를 만났을 때](https://brunch.co.kr/@cojette/1)
* [Naive Bayesian Classification(나이브 베이즈 분류)](http://unlimitedpower.tistory.com/entry/NLP-Naive-Bayesian-Classification%EB%82%98%EC%9D%B4%EB%B8%8C-%EB%B2%A0%EC%9D%B4%EC%A6%88-%EB%B6%84%EB%A5%98)
* [Bayes Theorem and Naive Bayes](http://alexhwoods.com/2015/11/08/bayes-theorem-and-naive-bayes/)
* [SigOpt for ML: Unsupervised Learning with Even Less Supervision Using Bayesian Optimization](http://blog.sigopt.com/post/140871698423/sigopt-for-ml-unsupervised-learning-with-even)
* [bayes.js - MCMC and Bayes in the browser](https://github.com/rasmusab/bayes.js)
* [Human-level concept learning through probabilistic program induction Bayesian Program Learning (BPL) model for one-shot learning](http://gitxiv.com/posts/jS9LJ5kh9ny6iqD7Z/human-level-concept-learning-through-probabilistic-program)
* [Bayesian reasoning implicated in some mental disorders](https://www.sciencenews.org/article/bayesian-reasoning-implicated-some-mental-disorders)
* [Bayesian Deep Learning](http://twiecki.github.io/blog/2016/06/01/bayesian-deep-learning/)

# Haskell
* [A gentle introduction to statistical relational learning: maths, code, and examples](http://phdp.github.io/posts/2015-07-13-srl-code.html)

# Library
* [Javascript library for the visualization of statistical distributions](https://github.com/richarddmorey/stat-distributions-js)
* [Stan is a probabilistic programming language implementing full Bayesian statistical inference](http://mc-stan.org/)

# Poisson Distribution
* [Understanding Waiting Times Between Events with the Poisson and Exponential Distributions](http://nbviewer.ipython.org/github/nicolewhite/notebooks/blob/master/Poisson.ipynb)

# Probability
* [Probability Cheatsheet](http://www.wzchen.com/probability-cheatsheet)
* [Foundations of probability theory](https://terrytao.wordpress.com/2015/09/29/275a-notes-0-foundations-of-probability-theory/)
* [Heuristic models for marginal probability assessment updates](http://xheimlichkeit.com/methods/2015/10/12/how-to-update-probabilities.html)

# Python
* [How To Implement These 5 Powerful Probability Distributions In Python](http://hpc-asia.com/how-to-implement-these-5-powerful-probability-distributions-in-python/)
* [An Introduction to Statistics with Python](http://work.thaslwanter.at/Stats/html/)
* [PyMC: Bayesian Stochastic Modelling in Python http://pymc-devs.github.com/pymc/](https://github.com/pymc-devs/pymc)
  * [Probabilistic Programming & Bayesian Methods for Hackers](http://camdavidsonpilon.github.io/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers/)
  * [A/B Testing with Hierarchical Models in Python](http://blog.dominodatalab.com/ab-testing-with-hierarchical-models-in-python/)
* [Computational Statistics in Python](http://people.duke.edu/~ccc14/sta-663/index.html)
* [bayesianPy](http://psygrammer.github.io/bayesianPy/)
* [pomegranate is a package for graphical models and Bayesian statistics for Python, implemented in cython](https://github.com/jmschrei/pomegranate)
* [통계적 사고: 파이썬을 이용한 탐색적 자료 분석](http://think-stat.xwmooc.org/)
* [ThinkBayes (IPython notebook included)](https://github.com/rlabbe/ThinkBayes)

# R
* [bayesianR](http://psygrammer.github.io/bayesianR/)
