Docker
======
* [도커 무작정 따라하기](http://www.slideshare.net/pyrasis/docker-fordummies-44424016)
* [도커(Docker) 튜토리얼 : 깐 김에 배포까지](http://blog.nacyot.com/articles/2014-01-27-easy-deploy-with-docker/)
* [가장 빨리 만나는 도커](http://www.pyrasis.com/private/2014/11/30/publish-docker-for-the-really-impatient-book)
* [Docker란 무엇인가? : Docker 기본 사용법](http://www.slideshare.net/pyrasis/docker-docker-38286477)
* [Docker, 그것은 무엇이고, 설치는 어떻게 할까?](http://blog.neonkid.xyz/85)
* [hello](https://www.youtube.com/watch?v=ExJXmMO5uvg)
* [생활코딩 docker](https://www.youtube.com/watch?v=Bhzz9E3xuXY)
* **초보를 위한 도커 안내서**
  * [도커란 무엇인가?](https://subicura.com/2017/01/19/docker-guide-for-beginners-1.html)
  * [설치하고 컨테이너 실행하기](https://subicura.com/2017/01/19/docker-guide-for-beginners-2.html)
  * [이미지 만들고 배포하기](https://subicura.com/2017/02/10/docker-guide-for-beginners-create-image-and-deploy.html)
* [시작하는 이들을 위한 컨테이너, VM, 그리고 도커에 대한 이야기](https://medium.com/@jwyeom63/%EC%8B%9C%EC%9E%91%ED%95%98%EB%8A%94-%EC%9D%B4%EB%93%A4%EC%9D%84-%EC%9C%84%ED%95%9C-%EC%BB%A8%ED%85%8C%EC%9D%B4%EB%84%88-vm-%EA%B7%B8%EB%A6%AC%EA%B3%A0-%EB%8F%84%EC%BB%A4%EC%97%90-%EB%8C%80%ED%95%9C-%EC%9D%B4%EC%95%BC%EA%B8%B0-3a04c000cb5c)
* [Docker: Getting Started with Docker Docker 시작하기](http://www.sauru.so/blog/getting-started-with-docker/)
* [Docker: Installation and Test Drive Utuntu 위에 Docker 설치하고 맛보기](http://www.sauru.so/blog/docker-installation-and-test-drive/)
* [Docker: 나의 첫 Docker Image Build and Push my own Docker Image](http://www.sauru.so/blog/build-my-first-docker-image/)
* ['쓸만한' Docker Image 만들기 - Part 1 Build an Usable Docker Image with Alpine Linux](http://www.sauru.so/blog/build-usable-docker-image-part1/)
* ['쓸만한' Docker Image 만들기 - Part 2 Build and Push a Docker Image For Go Development](http://www.sauru.so/blog/build-usable-docker-image-part2/)
* [Docker Cloud에서 자동빌드하기 Setting Automated Build on Docker Cloud](http://www.sauru.so/blog/automated-build-with-docker-cloud/)
* [내가 필요한 Docker Image 만들기](http://www.nurinamu.com/dev/2016/07/04/create-a-docker-image/)
* [leafcats.com/tag/docker](http://www.leafcats.com/tag/docker)
  * [가상머신과 도커(Docker)](http://www.leafcats.com/152)
* 케빈 TV
  * [시즌2 - 2회 Docker 1회 맛보기](https://www.youtube.com/watch?v=T-qkeSf2uzw)
  * [시즌2 - 3회 Docker 2회](https://www.youtube.com/watch?v=mjRtbb-hobk)
  * [시즌2 - 4회 Docker 3회](https://www.youtube.com/watch?v=Kf7a04de15s)
  * [S02E05 - Docker 4회 (2016-09-11)](https://www.youtube.com/watch?v=2wC9A52_eA0)
  * [S02E06 - Docker 5회 (2016-09-18)](https://www.youtube.com/watch?v=w6HuosHRCKA)
  * [S02E07 - Docker 6회 + Zeppelin 설치 (반만 성공) + FP 얘기 조금 (2016-09-25)](https://www.youtube.com/watch?v=wjEYAlVj3Vc)
* [docs.docker.com](https://docs.docker.com/)
* [github.com/docker-library/docs](https://github.com/docker-library/docs)
* [hub.docker.com/](https://hub.docker.com/)
  * [bi_deeplearning](https://hub.docker.com/r/imcomking/bi_deeplearning/) TensorFlow + Theano + Torch + Scikit-learn + Keras + Caffe + ...
  * [centos](https://hub.docker.com/_/centos/)
  * [elasticsearch](https://hub.docker.com/_/elasticsearch/)
  * [httpd](https://hub.docker.com/_/httpd/)
  * jenkins
    * [Combining Jenkins and Docker for Continuously Running Instances](http://www.focusedsupport.com/blog/beyond-builds-combining-jenkins-and-docker-for-continuously-running-instances/)
  * [mysql-server](https://hub.docker.com/r/mysql/mysql-server/)
    * [A tutorial on how to use MySQL with Docker](http://www.luiselizondo.net/a-tutorial-on-how-to-use-mysql-with-docker/)
    * [MySQL Docker Containers: Understanding the basics](http://severalnines.com/blog/mysql-docker-containers-understanding-basics)
    * [Setting up a MySQL Docker container](https://tectonic.com/quay-enterprise/docs/latest/mysql-container.html)
    * [Docker로 MySQL 사용하기](http://gyuha.tistory.com/490)

      ```
      sudo docker pull mysql:5.7.17
      sudo docker run -d --env MYSQL_ROOT_PASSWORD=test_root --env MYSQL_USER=test_user --env MYSQL_PASSWORD=testpwd --env MYSQL_DATABASE=test_db --name test_image_name -p 53306:3306 mysql:5.7.17
      mysql -h 127.0.0.1 -P 53306 -u test_user -ptestpwd test_db < table_schema.sql
      mysql -h 127.0.0.1 -P 53306 -u test_user -ptestpwd test_db
      ```
  * R
    * [hub.docker.com/r/mrchypark/tfr-rstudio/tags](https://hub.docker.com/r/mrchypark/tfr-rstudio/tags/)
  * redis

    ```
    $ sudo docker pull redis:3.0.7
    $ sudo docker run -p 56379:6379 redis:3.0.7
    $ nc -v 127.0.0.1 56379
    info
    ```
  * [sonarqube](https://hub.docker.com/_/sonarqube/)
    * [docker-sonarqube](https://github.com/SonarSource/docker-sonarqube/)
    * [Super quick Sonar/Postgres setup with docker](http://blog.anorakgirl.co.uk/2015/11/super-quick-sonarpostgres-setup-with-docker/)
    * [downloads.sonarsource.com/sonarqube](http://downloads.sonarsource.com/sonarqube/)
    * [github.com/SonarSource/sonar-examples](https://github.com/SonarSource/sonar-examples)
    * [Python Plugin](http://docs.sonarqube.org/display/PLUG/Python+Plugin)
    * [JavaScript Static Analysis Report System with SonarQube](http://readme.skplanet.com/?p=13679)
  * [Dockerfile for Pydata Eco Systems with Tensorflow](https://hub.docker.com/r/teamlab/pydata-tensorflow/)
  * [ubuntu](https://hub.docker.com/_/ubuntu/)
    * [Encoding Problems when running an app in docker (Python, Java, Ruby, …) with Ubuntu Containers (ascii, utf-8)](https://stackoverflow.com/questions/27931668/encoding-problems-when-running-an-app-in-docker-python-java-ruby-with-u/27931669)

      ```
      FROM ubuntu:latest

      RUN apt-get update -y && apt-get install -y ... locales
      ...
      ENV PYTHONIOENCODING="utf-8"
      RUN locale-gen ko_KR.UTF-8
      ENV LANG=ko_KR.UTF-8
      ENV LANGUAGE=ko_KR.UTF-8
      ENV LC_ALL=ko_KR.UTF-8
      ```
  * [ubuntu + python3.6](https://gist.github.com/monkut/c4c07059444fd06f3f8661e13ccac619)
    * ENTRYPOINT로 python3.6 사용
  * [DIT4C image for Apache Zeppelin](https://hub.docker.com/r/dit4c/dit4c-container-zeppelin/)
* [Docker로 파이썬 배포 운영하기](http://greatkim91.tistory.com/194)
* [파이썬 Docker 이미지 관리하기](http://greatkim91.tistory.com/195)
* [도커를 이용한 파이썬 모듈 배포하기 - 서준석](https://www.youtube.com/watch?v=RRT58hbDXNs)
* [docker로 만들어보는 가상 원격 데스크탑 - 이형규](https://www.youtube.com/watch?v=wReN7LG2zJg)
* [CoreOS : 설치부터 컨테이너 배포까지 - 김충섭](https://www.youtube.com/watch?v=pR5MoWHPtQs)
* [초보의 도커 간증 - 박성재님](https://www.youtube.com/watch?v=j3M8-R8GzXQ)
* [도커로 고스트 블로그 플랫폼 5분만에 설치하기 - 김한기](https://www.youtube.com/watch?v=MGXMRJP4LhQ)
* [도커 학습과 Boot2Docker - 이재홍(@pyrasis)](https://www.youtube.com/watch?v=MqL5exxZDg4)
* [Docker Histroy & Ecosystem - 김대권(@nacyot)](https://www.youtube.com/watch?v=K3ilFtXODZQ)
* [Docker로 레일스 배포하기 - 정창훈(@seapy)](https://www.youtube.com/watch?v=pcQtXnHXbLQ)
* [도커(Docker)로 루비 온 레일스(Ruby on Rails) 어플리케이션 배포하기 1/2](https://www.youtube.com/watch?v=LEeQvLx70MA)
* [도커(Docker)로 루비 온 레일스(Ruby on Rails) 어플리케이션 배포하기 2/2 이미지 배포 / 공유하기](https://www.youtube.com/watch?v=t_YzzLoyVn8)
* [Docker Korea 두번째 모임 : Docker와 로그 & 메트릭스 수집](https://www.youtube.com/watch?v=eFPsz0oCLSs)
* [Docker Tutorial for Beginners](https://examples.javacodegeeks.com/devops/docker/docker-tutorial-beginners/)
* [Docker Tutorial — Getting Started with Python, Redis, and Nginx](https://hackernoon.com/docker-tutorial-getting-started-with-python-redis-and-nginx-81a9d740d091)
* [Docker Machine Guide (VirtualBox on Mac OS X)](http://waterlink.github.io/blog/2015/08/31/docker-machine-guide-virtualbox-mac-os-x/)
* [docker the cloud](https://spoqa.github.io/2013/11/22/docker-the-cloud.html)
* [A quick introduction to Docker http://odewahn.github.io/docker-jumpstart](https://github.com/odewahn/docker-jumpstart/)
* [What is Docker?](https://www.conetix.com.au/blog/what-is-docker)
* [dockercon cfp summary](https://blog.docker.com/2015/04/dockercon-cfp-summary/)
* [Show HN: CLI for executing code in many different languages with Docker](https://docker-exec.github.io/)
* [Comparing Five Monitoring Options for Docker](http://rancher.com/comparing-monitoring-options-for-docker-deployments/)
* [Docker building dockers - keeping them small](https://github.com/jamiemccrindle/dockerception)
* [Docker Without Docker](https://chimeracoder.github.io/docker-without-docker/)
* [7 Things You Must Be Doing With Docker](http://blog.getcrane.com/7-things-must-docker)
* [Privilege Escalation via Docker](https://fosterelli.co/privilege-escalation-via-docker.html)
* [Creating honeypots using Docker](http://itinsight.hu/blog/posts/2015-05-04-creating-honeypots-using-docker.html)
* [ImageLayers.io - Docker Image Visualization and Badges](https://imagelayers.io)
* [Container Factory - Turn your Github repo into a published container image](http://www.containerfactory.io/)
* [A Quick Introduction to LXD](http://blog.scottlowe.org/2015/05/06/quick-intro-lxd/)
* [The case against Docker](https://www.andreas-jung.com/contents/the-case-against-docker)
* [Convert Any Server to a Docker Container](https://zwischenzugs.wordpress.com/2015/05/24/convert-any-server-to-a-docker-container/)
* [Tales of a Part-time Sysadmin: Dogfooding Docker to test Docker](https://blog.jessfraz.com/post/dogfooding-docker-to-test-docker/)
* [Serverspec(서버스펙)을 통한 도커 이미지 테스트 자동화](http://blog.nacyot.com/articles/2015-06-30-serverspec-with-docker/)
  * [Serverspec(서버스펙)을 통한 도커 이미지 테스트 자동화 코드](https://github.com/nacyot/serverspec_tutorial)
* [Building Better Docker Images](http://jonathan.bergknoff.com/journal/building-better-docker-images)
* [Docker, Mesos, Marathon, and the End of Pets](http://blog.factual.com/docker-mesos-marathon-and-the-end-of-pets)
* [Docker , the future of Virtualization for your Django web development](https://impythonist.wordpress.com/2015/06/21/docker-the-future-of-virtualization-for-your-django-web-development/)
* [Docker, CoreOS, Google, Microsoft, Amazon And Others Come Together To Develop Common Container Standard](http://techcrunch.com/2015/06/22/docker-coreos-google-microsoft-amazon-and-others-agree-to-develop-common-container-standard)
* [OPEN CONTAINER PROJECT](http://www.opencontainers.org/)
* [docker con](http://www.dockercon.com)
  * [DOCKERCON 2015 KEYNOTE VIDEOS](https://blog.docker.com/2015/06/dockercon-2015-keynote-videos/)
    * [DockerCon 2015 키노트 요약](http://pragmaticstory.com/2015/06/24/dockercon-2015-키노트-요약/)
  * [A Summary about Hykes' Keynote on Dockercon 2015](http://www.slideshare.net/hshenry/hykes-keynote-summary-on-dockercon-2015)
  * [Enabling Microservices @Orbitz - DockerCon 2015](http://www.slideshare.net/bacoboy/enabling-microservices-orbitz-dockercon-2015)
  * [Dockercon 2015 - Faster Cheaper Safer](http://www.slideshare.net/adriancockcroft/faster-cheaper-safer)
  * [Interconnecting containers at scale #Dockercon](http://www.slideshare.net/sarahnovotny/interconnecting-containers-at-scale-dockercon)
  * [DOCKERCON GENERAL SESSION DAY 1 AND DAY 2 VIDEOS](https://blog.docker.com/2016/06/dockercon-general-session-day-1-and-day-2-videos/)
* [10 Open Source Docker Tools You Should Be Using](http://blog.getcrane.com/10-open-source-docker-tools-you-should-be-using)
* [Docker and Microsoft announce more innovation to cross platforms and win hearts](http://azure.microsoft.com/blog/2015/06/23/docker-and-microsoft-announce-more-innovation-to-cross-platforms-and-win-hearts)
* [Container OS comparison](http://blog.codeship.com/container-os-comparison/)
* [A Go, Docker workflow](http://blog.crowdpatent.com/a-go-docker-workflow/)
* [Why Docker is Not Yet Succeeding Widely in Production](http://sirupsen.com/production-docker/)
* [Docker Misconceptions](https://valdhaus.co/writings/docker-misconceptions/)
* [My Slow Internet vs Docker](https://medium.com/google-cloud-platform-developer-advocates/my-slow-internet-vs-docker-7678ae1cae72)
* [Spin up a Docker dev/test Environment in 60 Minutes or Less](https://www.joyent.com/blog/spin-up-a-docker-dev-test-environment-in-60-minutes-or-less)
* [Running containers from Mac OS X](https://hyper.sh/blog/post/2015/07/30/running-containers-from-mac-os-x.html)
* [ANNOUNCING DOCKER 1.8: CONTENT TRUST, TOOLBOX, AND UPDATES TO REGISTRY AND ORCHESTRATION](http://blog.docker.com/2015/08/docker-1-8-content-trust-toolbox-registry-orchestration/)
  * [ANNOUNCING DOCKER TOOLBOX](https://blog.docker.com/2015/08/docker-toolbox/)
* [Migrating stateful containers using native Docker 1.8 Flocker plugin and Compose](https://clusterhq.com/2015/08/04/docker-volume-plugins/)
* [Full-stack Docker performance monitoring: From containers to applications](https://blog.ruxit.com/full-stack-docker-performance-monitoring-containers-and-applications/)
* [END-TO-END AUTOMATION FOR DOCKER-BASED APPLICATIONS ON DIGITALOCEAN](http://dchq.co/2/post/2015/09/end-to-end-automation-for-docker-based-applications-on-digitalocean.html)
* [How We Deploy Containers at Grammarly](http://tech.grammarly.com/blog/posts/How-We-Deploy-Containers-at-Grammarly.html)
* [EXTENDING DOCKER WITH PLUGINS](https://blog.docker.com/2015/06/extending-docker-with-plugins/)
* [large scale backend service develpment](http://www.slideshare.net/deview/212-large-scale-backend-service-develpment)
* [Docker CRIU Demo](https://zwischenzugs.wordpress.com/2015/10/11/docker-migration-in-flight-criu/)
* [AWS Korea container day](http://www.slideshare.net/awskorea/tag/container-day?adbsc=social_20151227_56754856&adbid=1657767227813305&adbpl=fb&adbpr=1563378127252216)
* [Docker Sotrage 의 거의 모든 것](http://play.joinc.co.kr/w/man/12/docker/storage)
* [10 Tips & Tricks with Docker](https://mercurenews.com/en/10-tips-tricks-with-docker)
* [10 Docker Tips and Tricks That Will Make You Sing A Whale Song of Joy](https://nathanleclaire.com/blog/2014/07/12/10-docker-tips-and-tricks-that-will-make-you-sing-a-whale-song-of-joy/)
* [Using Docker to Run Python](https://civisanalytics.com/blog/engineering/2014/08/14/Using-Docker-to-Run-Python/)
* [도커를 이용한 웹서비스 무중단 배포하기](http://subicura.com/2016/06/07/zero-downtime-docker-deployment.html)
* [Docker, AWS-ECR, Jenkins를 이용해서 웹서비스 무중단 배포하기](https://redice-inc.github.io/deploy-web-service-with-docker/)
* [Docker and Btrfs in practice](https://docs.docker.com/engine/userguide/storagedriver/btrfs-driver/)
* [Jérôme Petazzoni - Introduction to Docker and containers - PyCon 2016](https://www.youtube.com/watch?v=ZVaRK10HBjo)
* [Docker 로 Node.js 배포하기](http://seokjun.kr/docker-nginx-node/)
* [도커(Docker)로 루비 온 레일스 어플리케이션 배포하기 (1) 어플리케이션 이미지 만들기](http://blog.nacyot.com/articles/2014-08-08-rails-on-docker/)
* [웹호스팅계의 혁신, Docker](http://etinow.me/73)
* [2014 Red Hat Forum - Docker, 그 기발한 활용법 (부제 : dumpdocker – 자동덤프분석툴)](https://www.youtube.com/watch?v=Wk9LvdvI75A)
* [Discovering Docker Datacenter](https://medium.com/lucjuggery/discovering-docker-datacenter-cf0daccddc41)
* [개발자 장난감 시리즈, 시놀로지 NAS로 EC2 만들기](http://www.popit.kr/%EA%B0%9C%EB%B0%9C%EC%9E%90-%EC%9E%A5%EB%82%9C%EA%B0%90-%EC%8B%9C%EB%A6%AC%EC%A6%88-%EC%8B%9C%EB%86%80%EB%A1%9C%EC%A7%80-nas%EB%A1%9C-ec2-%EB%A7%8C%EB%93%A4%EA%B8%B0/)
* **[Docker를 기반으로 다양한 데이터베이스 환경 통합하기](http://blog.chequer.io/archives/860)**
* [Introducing Docker 1.13](https://blog.docker.com/2017/01/whats-new-in-docker-1-13/)
* [DevOps with Docker](https://readme.skplanet.com/?p=11449)
* [도커 컨테이너 활용 사례 Codigm - 남 유석 개발팀장 :: AWS Container Day](http://www.slideshare.net/awskorea/codigm-aws-container-day)
* [Docker and OOM(Out Of Memory) Killer](https://blog.2dal.com/2017/03/27/docker-and-oom-killer/)
* [codeschool.com/courses/try-docker](https://www.codeschool.com/courses/try-docker)
* [PART 5 OF DATA LAKE 3.0: YARN AND CONTAINERIZATION: SUPPORTING DOCKER AND BEYOND](https://hortonworks.com/blog/part-5-of-data-lake-3-0-yarn-and-containerization-supporting-docker-and-beyond/)
  * LinuxContainerExecutor를 통해 Docker 컨테이터를 실행하는 YARN에 대한 이야기
* [Docker](https://www.fullstackpython.com/docker.html)
* [Build and Deploy a Python Web App on Docker](https://www.distelli.com/docs/tutorials/build-and-deploy-python-with-docker/)
* bash/shell script
  * [bash](https://docs.docker.com/samples/library/bash/)
  * [Docker with shell script or Makefile](https://ypereirareis.github.io/blog/2015/05/04/docker-with-shell-script-or-makefile/)
  * [docker run a shell script in the background without exiting the container](http://stackoverflow.com/questions/31570208/docker-run-a-shell-script-in-the-background-without-exiting-the-container#answer-31570980)
* troubleshooting
  * `kernel:unregister_netdevice: waiting for lo to become free. Usage count = 1`
    * kernel bug, not yet resolved
    * [github.com/moby/moby/issues/5618](https://github.com/moby/moby/issues/5618)
  * `Target WSGI script ... cannot be loaded as Python module` [practice; -v로 연결한 directory의 permission 문제](https://gist.github.com/hyunjun/ed1cdebcf982e30b2cc1b6c039f2d7b7)
    * [Docker & File Permissions](https://serversforhackers.com/c/dckr-file-permissions)
  * [Docker for Mac에서 No space left on device 오류](https://blog.outsider.ne.kr/1295)
  * [Docker cache and apt-get update](http://lenguyenthedat.com/docker-cache/)
    * `docker build ...`가 `returned a non-zero code: 100`로 끝날 때의 해결책
    * Redhat 7.2, docker 1.10.3에서는 해결되지 않음
  * [Troubleshooting Container Networking](https://success.docker.com/article/Troubleshooting_Container_Networking)
* [내가 Docker를 시작했던 방법](http://realignist.me/code/2017/06/14/docker-my-usecase.html)
* [특정 포트의 실행 대기하기](http://ohgyun.com/749)
* [컨테이너에 HTTP 프록시 적용하기](http://ohgyun.com/747)
* [Docker를 기반으로 다양한 데이터베이스 환경 통합하기](https://medium.com/chequer/docker%EB%A5%BC-%EA%B8%B0%EB%B0%98%EC%9C%BC%EB%A1%9C-%EB%8B%A4%EC%96%91%ED%95%9C-%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%B2%A0%EC%9D%B4%EC%8A%A4-%ED%99%98%EA%B2%BD-%ED%86%B5%ED%95%A9%ED%95%98%EA%B8%B0-96aa68363775)
* install
  * [practice - installation script](https://gist.github.com/hyunjun/c316ab211c71ffb4cf90582e8a2c17b0)
  * uninstall

    ```
    $ cat /etc/redhat-release
    CentOS Linux release 7.3.1611 (Core)
    $ sudo service docker stop
    $ sudo yum remove docker-io
    $ sudo yum remove docker docker-common docker-selinux docker-engine
    ```
  * [How To Install Docker on CentOS 6](https://www.liquidweb.com/kb/how-to-install-docker-on-centos-6/)
  * [도커(Docker) 튜토리얼 : 0.8 맥에서 설치하기](http://blog.nacyot.com/articles/2014-02-11-dokcer-08-on-macosx/)
  * [우분투(Ubuntu) 14.04에서 도커(Docker) 설치 및 사용하기](http://blog.nacyot.com/articles/2014-04-18-docker-on-ubuntu-14-04/)
* [Docker를 이용한 크로스 컴파일 툴체인 이용하기](http://mcchae.egloos.com/11274635)
* [CircleCI: 커스텀 도커 이미지로 어플리케이션 빌드 시간 단축하기](https://engineering.huiseoul.com/circleci-%EC%BB%A4%EC%8A%A4%ED%85%80-%EB%8F%84%EC%BB%A4-%EC%9D%B4%EB%AF%B8%EC%A7%80%EB%A1%9C-%EB%B9%8C%EB%93%9C-%EC%8B%9C%EA%B0%84-%EB%8B%A8%EC%B6%95%ED%95%98%EA%B8%B0-5c3a889bd2f7)
* [Docker for Data Science](https://towardsdatascience.com/docker-for-data-science-4901f35d7cf9)
* [시스템 부팅시 도커 컨테이너 자동 실행](http://daddycat.blogspot.kr/2017/12/blog-post_21.html)
* [Docker Korea 스터디 그룹 모임](http://blog.nacyot.com/articles/2014-07-26-docker-korea/)
* [Docker Korea 스터디 그룹 두번째 모임](http://blog.nacyot.com/articles/2014-08-04-docker-korea-secord/)
* [이미지 기반 어플리케이션 배포 패러다임 Immutable Infrastructure](http://blog.nacyot.com/articles/2014-04-06-immutable-infrastructure/)
* [Running GUI apps with Docker](http://fabiorehm.com/blog/2014/09/11/running-gui-apps-with-docker/)
* [Docker(container)의 작동 원리: namespaces and cgroups](https://tech.ssut.me/2017/08/15/what-even-is-a-container/)
* [<컨테이너 가상화의 이해> chroot를 사용해 프로세스의 루트 바꾸기](https://steemit.com/kr/@mishana/1-chroot)
* [Why Docker makes sense for startups](https://medium.freecodecamp.org/why-docker-makes-sense-for-startups-e9be14a1f662)
* [A quick introduction to Docker tags](https://medium.freecodecamp.org/an-introduction-to-docker-tags-9b5395636c2a)

# BoxFuse
* [Why Immutable Infrastructure?](https://boxfuse.com/learn/why.html)
* [Immutable Infrastructure: No SSH](https://boxfuse.com/blog/no-ssh.html)
* [Petabyte-Scale Data Pipelines with Docker, Luigi and Elastic Spot Instances](http://tech.adroll.com/blog/data/2015/09/22/data-pipelines-docker.html)
* [Checkpoint and restore Docker container with CRIU](http://blog.circleci.com/checkpoint-and-restore-docker-container-with-criu/)
* [Don't expose the Docker socket (not even to a container)](https://www.lvh.io/posts/dont-expose-the-docker-socket-not-even-to-a-container.html)
* [WRITING AND RUNNING GO API'S IN DOCKER](http://ewanvalentine.io/writing-and-running-go-apis-in-docker/)
* [END-TO-END AUTOMATION FOR DOCKER-BASED PYTHON WITH REDIS ON AWS](http://dchq.co/2/post/2015/09/end-to-end-automation-for-docker-based-python-with-redis-on-aws.html)
* [Docker image with Tor, Privoxy and a process manager under 15 MB](https://medium.com/@rdsubhas/docker-image-with-tor-privoxy-and-a-process-manager-under-15-mb-c9e344111b61)
* [Developing with Docker at IFTTT](https://medium.com/engineering-at-ifttt/developing-with-docker-at-ifttt-5bd03b4e597c)

# Commands
* **[개발 환경에서 유용한 Docker 명령어 소개](https://spoqa.github.io/2017/06/22/docker-tip.html)**
* build
  * `docker build -t [name]:[tag] .`
  * `--build-arg` e.g. `sudo docker build --build-arg http_proxy=http://x.y.z.w:port --build-arg https_proxy=http://x.y.z.w:port -t [name]:[tag] .`
  * `--no-cache` clean build
  * [Docker v17.06.0-ce에 도입된 multi-stage 빌드 사용하기](https://blog.outsider.ne.kr/1300)
  * [.dockerignore](https://docs.docker.com/engine/reference/builder/)
    * 무조건 설정하자. 그렇지 않으면 해당 directory의 모든 파일을 일단 다 검색하고, 추가하려고 시도한 다음 필요없으면 버리기 때문에
    * 시간/공간 절약을 위해서는 무조건 사용하는 게 이득
    * 해당 directory에 큰 용량의 log나 data file이 있는 경우 build도 실패할 뿐더러, disk usage가 100%를 찍을 수도 있음
* cp `sudo docker cp [host path] [container id]:[container path]` [Copying files from host to docker container](http://stackoverflow.com/questions/22907231/copying-files-from-host-to-docker-container)
* exec

  ```
  sudo docker exec -it [container id] /bin/bash # to get bash into a running container
  sudo docker exec [container id] ls /some/path/
  ```
* images `sudo docker images`
* inspect `sudo docker inspect [container id] | grep IPAddress...`
* kill `sudo docker kill [container id]`
* logs `docker logs -f [container id]`
* ps `sudo docker ps [-a]`
* registry

  ```
  $ sudo docker logout [url]

  $ sudo vi /etc/systemd/system/docker.service.d/http-proxy.conf
  [Service]
  Environment="HTTP_PROXY=http://some.proxy.url:port" "HTTPS_PROXY=http://some.proxy.url:port" "NO_PROXY=localhost,127.0.0.1,.some.exclusion,..."

  $ sudo service docker restart
  $ sudo systemctl daemon-reload
  $ systemctl show --property=Environment docker
  $ sudo docker info | grep -i proxy

  $ sudo docker login [url]
  ```

  * [docker 로그인/로그아웃할 때의 사설 저장소 연동하기](http://knight76.tistory.com/entry/docker-login-%EC%82%AC%EC%84%A4-%EB%A0%88%EC%A7%80%EC%8A%A4%ED%8A%B8%EB%A6%AC)
  * **[Running Docker behind a proxy](https://crondev.com/running-docker-behind-proxy/)**
  * [도커 레지스트리(Docker Registry) 설치하기 + S3 연동](http://blog.nacyot.com/articles/2014-05-08-docker-registry-introduction/)
* rm `sudo docker rm [container id]`
  * `sudo docker ps -a | grep Exit | awk '{print $1}' | sudo xargs docker rm` [docker rmi cannot remove images, with: no such id](http://stackoverflow.com/questions/24733160/docker-rmi-cannot-remove-images-with-no-such-id)
  * [`docker rm $(docker ps -q -f 'status=exited')`](https://github.com/docker/docker/issues/18869)
  * [`docker volume rm $(docker volume ls -qf dangling=true)`](https://github.com/docker/docker/issues/18869)
* rmi `sudo docker rmi [-f] [image id]`
  * [`docker rmi $(docker images -q -f "dangling=true")`](https://github.com/docker/docker/issues/18869)
* run `sudo docker run [--rm|-d] -p hostPort:containerPort [name]`
  * `-m 32m` [Limit a container’s access to memory](https://docs.docker.com/engine/admin/resource_constraints/#limit-a-containers-access-to-memory)
  * `--net=host` to run as host mode for network(default bridge)
    * Use the same port for host & container
      * ... -p 12345:80 ...(X)    (e.g. On Dockerfile `EXPOST 80` for apache server)
      * ... -p 12345:12345 ...(O) (e.g. On Dockerfile `EXPOST 12345` even for apache server)
  * `-v /etc/localtime:/etc/localtime:ro` [How to make sure docker's time syncs with that of the host?](http://stackoverflow.com/questions/24551592/how-to-make-sure-dockers-time-syncs-with-that-of-the-host)
  * [practice](https://gist.github.com/hyunjun/c4ce053c28bd5df8b890aeae19af4270#file-run-md)
  * [practice of `--env-file=... --rm -v <local dir>:<container dir> -p <host port>:<container port>`](https://github.com/hyunjun/practice/commit/44863bda89d8e306e0b60974d089a8da26000c41)
  * [A Brief Primer on Docker Networking Rules: EXPOSE, -p, -P, --link](https://www.ctl.io/developers/blog/post/docker-networking-rules/)
  * [Start containers automatically](https://docs.docker.com/engine/admin/start-containers-automatically/)
  * pipe-like, stdin, stdout; 몇 가지 테스트해봤으나 잘 안됨
    * [Attach stdout of one container to stdin of another (pipe-like)](https://github.com/moby/moby/issues/14221)
  * [docker run 과 docker 네트워크 설정, 컨테이너 라이프사이클](http://www.leafcats.com/191)
* stop `sudo docker stop [container id]`

# CI Continuous Integration
* [Continuous Integration with Docker - 송주영 선임 :: AWS Container Day](http://www.slideshare.net/awskorea/continuous-integration-with-docker-aws-container-day)
* [I have a confession to make… I commit to master](https://hackernoon.com/i-have-a-confession-to-make-i-commit-to-master-6a804f334beb)

# Convox
* [Launch a Private Cloud in Minutes The simplicity of Heroku. The power of AWS](https://convox.com/)

# Dockerfile
* [Gotchas in Writing Dockerfile](http://kimh.github.io/blog/en/docker/gotchas-in-writing-dockerfile-en/)
* [How to Optimize Your Dockerfile](https://blog.tutum.co/2014/10/22/how-to-optimize-your-dockerfile/)
* practice
  * [some project with apache](https://gist.github.com/hyunjun/93f3cd9d76d3de50aa22c9477a700492#file-some_project_and_apache-md)
  * [ubuntu + python3, 한글](https://gist.github.com/hyunjun/93f3cd9d76d3de50aa22c9477a700492#file-ubuntu_python3_korean-md)
    * [docker - ko_KR.UTF-8 지원 우분투 14.04 이미지 만들기](http://forum.falinux.com/zbxe/?mid=lecture_tip&l=ru&page=4&m=1&document_srl=808302)
    * [Werkzeug raises BrokenFilesystemWarning](https://stackoverflow.com/questions/34515331/werkzeug-raises-brokenfilesystemwarning)
      * 언제 발생하는지 아직 정확히는 모르겠는데, 한글 설정이 안 되면 이런 오류가 발생할 때가 있음
  * [Oracle Java 8. Scala 2.11.8 and scala-sbt 0.13.16](https://gist.github.com/hyunjun/93f3cd9d76d3de50aa22c9477a700492#file-dockerfile_java_scala_sbt)
* crontab
  * 여러가지 방법을 시도해봤으나 모두 실패해 현재는 host에서 `sudo docker exec -it [container id] /path/to/script_name.sh`로 실행 중
  * [practice](https://gist.github.com/hyunjun/56159df74cbf3aafc936c3b199e99891)
    * cron만 돌리는 test였던 [ubuntu_cron_only](https://gist.github.com/hyunjun/56159df74cbf3aafc936c3b199e99891#file-ubuntu_cron_only-md), [centos68_cron_only](https://gist.github.com/hyunjun/56159df74cbf3aafc936c3b199e99891#file-centos68_cron_only-md) 이외에는 전부 실패
    * 이외에도 내부에서 일단 crontab을 등록해 돌아가는 지 확인해보려고 했지만, crontab -l로 등록 되는 거 까지만 확인하고 실행은 모두 실패

# [Kubernetes](http://kubernetes.io)
* [Kubernetes in 5 mins](https://www.youtube.com/watch?v=PH-2FfFD2PU)
* [Container Cluster Manager from Google](https://github.com/googlecloudplatform/kubernetes)
* [Large-scale cluster management at Google with Borg](http://blog.acolyer.org/2015/05/07/large-scale-cluster-management-at-google-with-borg/)
* [Google systems guru explains why containers are the future of computing](https://medium.com/s-c-a-l-e/google-systems-guru-explains-why-containers-are-the-future-of-computing-87922af2cf95)
* [KUBERNETES - THE FUTURE OF DEPLOYMENT](http://www.bashton.com/blog/2015/kubernetes-future-of-deployment/)
* [Omega, and what it means for Kubernetes: a Q&A about cluster scheduling](http://blog.kismatic.com/qa-with-malte-schwarzkopf-on-distributed-systems-orchestration-in-the-modern-data-center/)
* [Kubernetes: Open Source Container Cluster Orchestration](http://blog.kubernetes.io/2015/07/how-did-quake-demo-from-dockercon-work.html)
* [Omega, and what it means for Kubernetes: a Q&A about cluster scheduling](https://blog.kismatic.com/qa-with-malte-schwarzkopf-on-distributed-systems-orchestration-in-the-modern-data-center/?)
* [Try Kubernetes with Vagrant](http://lollyrock.com/articles/kubernetes-vagrant/)
* [CoreOS and Kubernetes 1.0](https://coreos.com/blog/kubernetes-1.0-and-cloud-native-computing-foundation/)
* [Kubernetes from the ground up: the API server](http://kamalmarhubi.com/blog/2015/09/06/kubernetes-from-the-ground-up-the-api-server/)
* [Official Kubernetes on CoreOS Guides and Tools](https://coreos.com/blog/official-kubernetes-on-coreos/)
* [Helm - The package manager for Kubernetes](https://helm.sh/)
* [Kubernetes from the ground up: the scheduler](http://kamalmarhubi.com/blog/2015/11/17/kubernetes-from-the-ground-up-the-scheduler/)
* [Scalable Microservices with Kubernetes](https://www.udacity.com/course/scalable-microservices-with-kubernetes--ud615)
* [Getting Started with Kubernetes](https://dzone.com/refcardz/kubernetes-essentials)
* [kakao의 오픈소스 Ep6 - Cite - cite , kubernetes , github , docker , container , microservice](http://tech.kakao.com/2016/12/26/opensource-6-cite/)
* Scalable Spark Deployment using Kubernetes
  * [Docker Image and Kubernetes Configurations for Spark 2.x](https://github.com/phatak-dev/kubernetes-spark)
  * [Part 1 : Introduction to Kubernetes](http://blog.madhukaraphatak.com/scaling-spark-with-kubernetes-part-1/)
  * [Part 2 : Installing Kubernetes Locally using Minikube](http://blog.madhukaraphatak.com/scaling-spark-with-kubernetes-part-2/)
  * [Part 3 : Kubernetes Abstractions](http://blog.madhukaraphatak.com/scaling-spark-with-kubernetes-part-3/)
  * [Part 4 : Service Abstractions](http://blog.madhukaraphatak.com/scaling-spark-with-kubernetes-part-4/)
  * [Part 5 : Building Spark 2.0 Docker Image](http://blog.madhukaraphatak.com/scaling-spark-with-kubernetes-part-5/)
  * [Part 6 : Building Spark 2.0 Two Node Cluster](http://blog.madhukaraphatak.com/scaling-spark-with-kubernetes-part-6/)
  * [Part 7 : Dynamic Scaling and Namespaces](http://blog.madhukaraphatak.com/scaling-spark-with-kubernetes-part-7/)
* **[Scaling Python Microservices with Kubernetes](http://blog.apcelent.com/scaling-python-microservices-kubernetes.html)**
* [NDC17 Kubernetes로 개발서버 간단히 찍어내기](https://www.slideshare.net/seungyongoh3/ndc17-kubernetes)
  * [terraform-aws-coreos-kubernetes](https://github.com/kz8s/tack)
* [GitHub 계정으로 Kubernetes 인증하기](https://dailyhotel.io/kubernetes-with-dex-integration-f456e22dd8e4)
* [Kubernetes on bare-metal in 10 minutes](https://blog.alexellis.io/kubernetes-in-10-minutes/)
* [처음 만난 Kubespray](http://knight76.tistory.com/entry/kubespary-%EC%B2%98%EC%9D%8C-%EB%A7%8C%EB%82%9C-Kubespray)
* [Kubernetes RBAC 위에서 DataDog agent 돌리기](https://andromedarabbit.net/kubernetes-rbac-%EC%9C%84%EC%97%90%EC%84%9C-datadog-agent-%EB%8F%8C%EB%A6%AC%EA%B8%B0/)
* [Kubernetes 운영 17개월의 성과와 교훈](https://dailyhotel.io/kubernetes-%EC%9A%B4%EC%98%81-17%EA%B0%9C%EC%9B%94%EC%9D%98-%EC%84%B1%EA%B3%BC%EC%99%80-%EA%B5%90%ED%9B%88-adf716bd72b1)
* [Introducing Kubeflow - A Composable, Portable, Scalable ML Stack Built for Kubernetes](http://blog.kubernetes.io/2017/12/introducing-kubeflow-composable.html?m=1)
* [The anatomy of Spark applications on Kubernetes](https://banzaicloud.com/blog/spark-k8s-internals/)
  * Kubernetes에 대한 Spark의 실험적 지원과 인-클러스터 클라이언트 모드에 대한 향후 지원에 대해 설명
  * Spark driver, Executor, Executor Shuffle Service, Resource Staging Server
* **[An Introduction to Kubernetes 쿠버네티스 살펴보기](https://subicura.com/remark/kubernetes-intro.html)**
* [Docker for Mac으로 Kubernetes 로컬에서 사용하기](https://blog.outsider.ne.kr/1346)
* [Rancher - Complete container management platform Deploy and manage Kubernetes with ease](https://rancher.com/)

# Library
* [Bocker - Docker implemented in 100 lines of bash https://www.p8952.info/projects.html](https://github.com/p8952/bocker)
* [Boot2Docker](https://github.com/boot2docker)
* [Capsule Shield: A Docker Alternative Tailor-Made for the JVM](http://blog.paralleluniverse.co/2015/10/08/container-capsules/)
* [codetainer allows you to create code 'sandboxes' you can embed in your web applications](https://github.com/codetainerapp/codetainer)
* [dcw is Docker Compose Wrapper to simplify everyday dev work with containers](https://github.com/rezzza/dcw)
* [DevLab is a utility that allows you to easily containerize your development workflow using Docker](https://github.com/TechnologyAdvice/DevLab)
* [Dinghy - Using Docker Machine on OS X with Dinghy](http://mageinferno.com/blog/using-docker-machine-os-x-dinghy)
* [Docker Bench - The Docker Bench for Security is a script that checks for all the automatable tests included in the CIS Docker 1.6 Benchmark. https://dockerbench.com](https://github.com/diogomonica/docker-bench-security)
* [Docker monitoring](https://ruxit.com/docker-monitoring/)
* [dokku - A docker-powered PaaS that helps you build and manage the lifecycle of applications http://dokku.viewdocs.io/dokku/](https://github.com/dokku/dokku)
  * [도쿠(Dokku)로 만드는 미니 히로쿠(Heroku)](http://blog.nacyot.com/articles/2014-01-30-deploying-application-with-dokku/)
* [domeide - Docker meets the IDE!](http://domeide.github.io/)
* [Droot - a super-easy application container engine with chroot without docker](https://github.com/yuuki1/droot)
* [Empire - Introducing Empire: A self-hosted PaaS built on Docker & Amazon ECS](http://engineering.remind.com/introducing-empire/)
* [Flocker 1.0: Container Data Management for Docker](https://clusterhq.com/2015/06/17/flocker-1-0/)
* [Galley is a command-line tool for orchestrating Docker containers in development and test environments](https://github.com/twitter-fabric/galley)
* [gockerize - Package golang service into minimal docker containers](https://github.com/aerofs/gockerize)
  * [Introducing gockerize](https://www.aerofs.com/blog/introducing-gockerize/)
* [hyper_ - Hypervisor-agnostic Docker Engine_](https://hyper.sh/)
  * [CLI and Daemon for Hyper](https://github.com/hyperhq/hyper)
* [instadocker - Run any Docker container on the cloudin just 3 seconds](http://instadocker.com/)
* [kompose - a tool to help users familiar with docker-compose move to Kubernete](http://kompose.io/)
* [Kontena - a docker platform in Ruby](Application Containers for Masses)
* [lorispack - Network Microsegmentation for Docker container deployments](https://github.com/sdnhub/lorispack)
* [Lorry - a docker-compose.yml validator and composer](https://lorry.io/)
* [netmanager 1.0 - Network management for docker containers](https://github.com/vmulas/docker-netmanager)
* [Network Containers](https://www.zerotier.com/blog/?p=490)
* [nginx-proxy](https://github.com/jwilder/nginx-proxy)
  * tcp request를 domain name base로 구분하여 각각의 docker container로 연결해주는 nginx 기반의 proxy
  * nginx-proxy container가 docker.sock를 연결하여 구동
    * `docker run -d -p 80:80 -v /var/run/docker.sock:/tmp/docker.sock:ro jwilder/nginx-proxy`
  * 다른 docker container 구동시 VIRTUAL_HOST env로 정의하면, docker-gen에 의해 nginx-proxy의 config가 변경되어 재구동
    * `docker run -e VIRTUAL_HOST=foo.bar.com ...`
* [Notary project comprises a server and a client for running and interacting with trusted collections](https://github.com/docker/notary)
* [Omnibus – Dependency Isolation Without Docker](https://blog.barricade.io/omnibus-dependency-isolation-without-docker/)
* [Packer](https://www.packer.io/)
  * [패커(Packer)로 도커(Docker) 이미지 빌드 및 AMI 자동 빌드 시스템 구축](http://blog.remotty.com/blog/2015/09/30/paekeopackerro-dokeodocker-imiji-bildeu-mic-ami-jadong-bildeu-siseutem-gucug/)
* [registry.hub.docker.com](https://registry.hub.docker.com)
* [rocker-compose - Docker composition tool with idempotency features for deploying apps composed of multiple containers](https://github.com/grammarly/rocker-compose)
* [seagull - Friendly Web UI to manage and monitor docker](https://github.com/tobegit3hub/seagull)

# Network [Networking](https://docs.docker.com/engine/userguide/networking/)
* [Docker Networking: Reborn](http://www.container42.com/2015/10/30/docker-networking-reborn/)
* [Docker network performance](https://jtway.co/docker-network-performance-b95bce32b4b9)
* [사용하기 어려운 도커, 네트워크 종류부터 알아두자](http://www.boannews.com/media/view.asp?idx=55957)
* Docker Network 구조
  * [(1) - docker0와 container network 구조](http://bluese05.tistory.com/15)
  * [(2) - container network 방식 4가지](http://bluese05.tistory.com/38)
  * [(3) - container 외부 통신 구조](http://bluese05.tistory.com/53)
  * [(4) - container link 구조](http://bluese05.tistory.com/54)
    * `--link` 이야기인데, 이건 [공식 가이드](https://docs.docker.com/engine/userguide/networking/)에서 더 이상 대부분의 경우 추천하지 않는다고 나옴
* [Docker 네트워크 구성과 설정](http://blog.neonkid.xyz/87)
* [Docker 사용자 정의 네트워크 구성](http://blog.neonkid.xyz/88)
* [NETWORK](https://www.joinc.co.kr/w/man/12/docker/InfrastructureForDocker/network)
* [PERFORMANCE](https://www.joinc.co.kr/w/man/12/docker/Performance)
* [Docker 네트워크에 관하여](https://kycfeel.github.io/2017/03/16/Docker-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC%EC%97%90-%EA%B4%80%ED%95%98%EC%97%AC/)
* [Docker 컨테이너 네트워크](https://sangwook.github.io/2015/01/16/docker-container-network.html)
* [Docker 네트워크](https://blog.naver.com/forioso/220718873417)
* [Docker 컨테이너 네트워크 설정시 ifconfig로 docker0를 찾을 수 없는 문제에 대해](http://crowjdh.blogspot.com/2016/03/docker-ifconfig-docker0.html)
* [도커 & 쿠버네티스의 네트워크 모델](http://ingeec.tistory.com/76)
* [native vs docker vs KVM network performance 비교](https://github.com/leeplay/study/blob/master/docker/native%20vs%20docker%20vs%20KVM%20network%20performance%20%EB%B9%84%EA%B5%90.md)
* [Testing Docker multi-host network performance](https://www.percona.com/blog/2016/08/03/testing-docker-multi-host-network-performance/)
* Networking for Docker Containers
  * [(a Primer) Part I](https://mesosphere.com/blog/networking-docker-containers/)
  * [Part II: Service Discovery for Traditional Apps and Microservices](https://mesosphere.com/blog/networking-docker-containers-part-ii-service-discovery-traditional-apps-microservices)
  * [Part III: Architectural Patterns for Service Registration, Service Discovery, and Load Balancing](https://mesosphere.com/blog/networking-docker-containers-part-iii-architectural-patterns-service-registration-service-discovery-load-balancing)

# Nomad
* [Nomad, a cluster manager and scheduler designed for microservices and batch workloads](https://www.hashicorp.com/blog/nomad.html)
* [오픈소스 간단 리뷰 - nomad : 가벼운 스케쥴러, 강력한 성능](http://tech.kakao.com/2017/01/25/nomad/)

# OpenStack
* [공개된 카카오 오픈 스택 관련 공개 및 강의 자료](http://knight76.tistory.com/entry/%ED%8E%8C-%EA%B3%B5%EA%B0%9C%EB%90%9C-%EC%B9%B4%EC%B9%B4%EC%98%A4-%EC%98%A4%ED%94%88-%EC%8A%A4%ED%83%9D-%EA%B4%80%EB%A0%A8-%EA%B3%B5%EA%B0%9C-%EB%B0%8F-%EA%B0%95%EC%9D%98-%EC%9E%90%EB%A3%8C)
* [처음 본 Kolla](http://knight76.tistory.com/entry/%EC%B2%98%EC%9D%8C-%EB%B3%B8-Kolla)
* [처음 본 오픈 스택의 Cinder](http://knight76.tistory.com/entry/%EC%B2%98%EC%9D%8C-%EB%B3%B8-%EC%98%A4%ED%94%88-%EC%8A%A4%ED%83%9D%EC%9D%98-Cinder)
* [처음 본 오픈스택 Swift](http://knight76.tistory.com/entry/%EC%B2%98%EC%9D%8C-%EB%B3%B8-%EC%98%A4%ED%94%88%EC%8A%A4%ED%83%9D-Swift)
* [처음 본 오픈 스택의 Nova](http://knight76.tistory.com/entry/%EC%B2%98%EC%9D%8C-%EB%B3%B8-Nova-Open-Stack)
* [처음 본 오픈 스택 Glance](http://knight76.tistory.com/entry/%EC%B2%98%EC%9D%8C-%EB%B3%B8-%EC%98%A4%ED%94%88-%EC%8A%A4%ED%83%9D-Glance)
* [openstack rpc worker는 thread임…](http://blog.woosum.net/archives/1589)

# RunC
* [Announcing a lightweight universal runtime container, by the OPEN CONTAINER PROJECT](http://runc.io/

# Swarm
* [docker swarm - 신명수](https://www.youtube.com/watch?v=DZOu7GkXULI)
* **[Docker Swarm을 이용한 쉽고 빠른 분산 서버 관리](https://subicura.com/2017/02/25/container-orchestration-with-docker-swarm.html)**
* [Adding Compose to the Swarm + Powerstrip + Flocker + Weave demo](https://clusterhq.com/blog/adding-compose-to-the-swarm-demo/)
* [Tutorial: Deploying Apache Storm on Docker Swarm](http://blog.baqend.com/post/142795871760/tutorial-deploying-apache-storm-on-docker-swarm?hash=3c62bfcf-d5c3-45cc-9490-f22597dc8260)
* [Swarm v. Fleet v. Kubernetes v. Mesos](http://radar.oreilly.com/2015/10/swarm-v-fleet-v-kubernetes-v-mesos.html)
* [Docker Clustering Tools Compared: Kubernetes vs Docker Swarm](http://technologyconversations.com/2015/11/04/docker-clustering-tools-compared-kubernetes-vs-docker-swarm/)
* [Scale Testing Docker Swarm to 30,000 Containers](http://blog.docker.com/2015/11/scale-testing-docker-swarm-30000-containers/)
* **[Docker 공식문서 에서 제시하는 개발-배포 Flow 따라가기 (Docker Swarm 사용하기)](http://jaynewho.com/post/21)**

# Triton
* [Triton Elastic Container Service](https://docs.joyent.com/public-cloud)
* [Comparing Triton containers to VMs and bare metal servers](https://www.joyent.com/blog/understanding-triton-containers)

# Troubleshooting
* `Bind address already in use`
  * container를 stop 했는데도, 해당 container가 사용하던 port를 반환받지 못함.  어느 정도 시간이 지난 후 다시 run 하면 되긴 하는데, 그 시간이 일정하지 않음.  짧은 경우도 있고 제법 긴 경우(몇 분?)도 있음
  * [github.com/moby/moby/issues/8714](https://github.com/moby/moby/issues/8714)
* [`docker: Error response from daemon: Container command '...' could not be invoked`](https://github.com/docker/docker/issues/20789)
  * Does the entrypoint exist?
  * Is it executable?
* `kernel:unregister_netdevice: waiting for lo to become free. Usage count = 1`
  * kernel bug로 cent os 7.x에서 docker를 사용하는 경우 계속 발생(ubuntu 쓰면 안 나타난다고 함)
  * service 영향은 상황마다 달라서 일률적으로 알 수 없다고 함
  * [www.reddit.com/r/docker/comments/6j2s2s/kernelunregister_netdevice_waiting_for_lo_to/](https://www.reddit.com/r/docker/comments/6j2s2s/kernelunregister_netdevice_waiting_for_lo_to/)
  * [Docker on CentOS 7.2: kernel:unregister_netdevice: waiting for lo to become free. Usage count = 1](https://stackoverflow.com/questions/43153503/docker-on-centos-7-2-kernelunregister-netdevice-waiting-for-lo-to-become-free)
* [Docker for mac eating disk space](https://www.chrissearle.org/2016/09/11/docker-for-mac-eating-disk-space/) 그냥 해당 directory 삭제 후 재시작
  * [Docker.qcow2 never shrinks - disk space usage leak in docker for mac](https://github.com/docker/for-mac/issues/371) 2017.03.17 현재, 곧 1년이 되며 여전히 해결 못함
* iTerm3.0 설치 후 docker quickstart terminal이 정상 동작하지 않을 때; [Replace /Applications/Docker/Docker Quickstart Terminal.app/Contents/Resources/Scripts/iterm.scpt with this](https://gist.github.com/gnachman/49cd5f8bcadc874ea8fc)
* [Docker daemon memory leak due to logs from long running process](https://stackoverflow.com/questions/27628276/docker-daemon-memory-leak-due-to-logs-from-long-running-process)
* [practice - docker memory full with python logging](https://github.com/hyunjun/practice/tree/master/docker/python_memory_overflow)

# Vagrant
* [Docker vs. Vagrant](https://www.upguard.com/articles/docker-vs-vagrant)
* [Speed up your Vagrant NFS shares with cachefilesd](http://chase-seibert.github.io/blog/2014/03/09/vagrant-cachefilesd.html)
* [Otto — the successor to Vagrant. Otto is the single solution to develop and deploy any application](https://www.hashicorp.com/blog/otto.html)
* [15분만에 윈도우에서 Ansible 테스트 환경 구축하기 (서버 1대 + 노드 5대)](https://sysnet4admin.blogspot.com/2017/06/vagrant-15-ansible-1-5.html)
* [HashiConf 17 참석기 : Day 1](https://blog.outsider.ne.kr/1320)
* [HashiConf 17 참석기 : Day 2](https://blog.outsider.ne.kr/1321)

# Windows
* [Windows Docker Toolbox에서 Host PC와 폴더 공유하기](http://bryan7.tistory.com/797)
* [Using Docker Tools on Windows 10 with Hyper-V](http://daddycat.blogspot.com/2017/07/using-docker-tools-on-windows-10-with.html)
