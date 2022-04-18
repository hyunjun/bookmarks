Redis
=====

* [joinc.co.kr/REDIS](https://www.joinc.co.kr/w/man/12/REDIS)
* [practice - architecture, usage tip](https://gist.github.com/hyunjun/4ab30f4ebd401bcb0e60aabbab0b97bc)
* [practice - logging](https://gist.github.com/hyunjun/4ab30f4ebd401bcb0e60aabbab0b97bc#file-logging-md)
* [practice - coupang 오류 관련 내용](https://gist.github.com/hyunjun/4ab30f4ebd401bcb0e60aabbab0b97bc#file-coupang-md)
* [Redis 자료구조](http://daddycat.blogspot.com/2017/07/redis.html)
* [advanced-redis](https://github.com/iamtrk/advanced-redis)
* [How to take advantage of Redis just adding it to your stack](http://oldblog.antirez.com/post/take-advantage-of-redis-adding-it-to-your-stack.html)
* [Recovering Redis Data with GDB](http://bigeng.io/post/118963807718/recovering-redis-data-with-gdb)
* [Redis Hot Patch](http://benmmurphy.github.io/blog/2015/06/09/redis-hot-patch/)
* [How Twitter Uses Redis To Scale - 105TB RAM, 39MM QPS, 10,000+ Instances](http://highscalability.com/blog/2014/9/8/how-twitter-uses-redis-to-scale-105tb-ram-39mm-qps-10000-ins.html)
* [Keeping up with the cool databases we present: Redis](https://codepicnic.com/posts/keeping-up-with-the-cool-databases-we-present-redis-cedebb6e872f539bef8c3f919874e9d7)
* [Redis on AWS](http://www.slideshare.net/charsyam2/redis-on-aws)
* [FAILOVER WITH REDIS SENTINEL](http://engineering.vinted.com/2015/09/03/failover-with-redis-sentinel/)
* [Clarifications about Redis and Memcached](http://antirez.com/news/94)
* [Spring은 왜 memcached 대신 Redis를 선택했을까?](https://deveric.tistory.com/65)
* [Scaling Secure Applications with Spring Session and Redis - YouTube](https://www.youtube.com/watch?v=3kGrkVUZ_Fo)
* [Lazy Redis is better Redis](http://antirez.com/news/93)
* [A few things about Redis security](http://antirez.com/news/96)
* [Lock and cache using redis](https://github.com/seamusabshere/lock_and_cache)
* [Recent improvements to Redis Lua scripting](http://antirez.com/news/97)
* [Atomic 처리와 cache stampede 대책을 위해 Redis Lua script를 활용한 이야기](https://engineering.linecorp.com/ko/blog/atomic-cache-stampede-redis-lua-script/)
* [Redis의 SCAN은 어떻게 동작하는가?](http://tech.kakao.com/2016/03/11/redis-scan/)
* [DNS 기반의 Redis HA 구현](http://tech.kakao.com/2016/03/18/redis-ha-dns/)
* [Redis Labs](http://www.slideshare.net/RedisLabs)
* [Redis in a Multi Tenant Environment–High Availability, Monitoring & Much More!](http://www.slideshare.net/RedisLabs/redis-in-a-multi-tenant-environmenthigh-availability-monitoring-much-more)
* [High Availability with Redis Sentinel and Spring Lettuce Client | by Naciye Karademir | Trendyol Tech | Medium](https://medium.com/trendyol-tech/high-availability-with-redis-sentinel-and-spring-lettuce-client-9da40525fc82)
* [Redis 의 Sentinel](http://crystalcube.co.kr/m/post/177)
* [Redis Conf 2016: Redis in a Multi-Tenant Environmnet](https://www.youtube.com/watch?v=aZ64pM7OVaw)
* [RedisConf18: Building Light weight Microservices Using Redis - Redis Labs](https://www.youtube.com/watch?v=z25CPqJMFUk)
  * [Building Light-weight Microservices using Redis](https://medium.com/flywheel-tech/building-light-weight-microservices-using-redis-23f051624647)
* [Microservice Communication: A Spring Integration Tutorial with Redis](https://www.toptal.com/spring/spring-integration-tutorial-redis-microservices)
* [RedisConf18: Implementing a New Data Structure for Redis - Redis Labs](https://www.youtube.com/watch?v=pmxaztRsoF4)
* [RedisConf18 발표 후기](https://engineering.linecorp.com/ko/blog/detail/306)
* [Redis Networking Nerd Down: For Lovers of Packets and Jumbo Frames- John Bullard, Distil Networks](http://www.slideshare.net/RedisLabs)
* [Developing a Redis Module](https://www.youtube.com/watch?v=LPxx4QPyUPw)
* [**REDIS 데이터 모델들**](http://www.popit.kr/redis-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EB%AA%A8%EB%8D%B8%EB%93%A4/)
* [Intro To Redis Cluster Sharding – Advantages, Limitations, Deploying & Client Connections](http://highscalability.com/blog/2019/2/19/intro-to-redis-cluster-sharding-advantages-limitations-deplo.html)
* [Docker기반 Redis 구축하기 - (10) Redis Cluster Mode 설정하기 | Carreys 기술블로그](https://jaehun2841.github.io/2018/12/03/2018-12-03-docker-10/#%EB%93%A4%EC%96%B4%EA%B0%80%EB%A9%B0)
* [입 개발 Redis 에서 Redis Cluster 로 갈 때 주의해야할 부분들 | Charsyam's Blog](https://charsyam.wordpress.com/2021/10/03/%EC%9E%85-%EA%B0%9C%EB%B0%9C-redis-%EC%97%90%EC%84%9C-redis-cluster-%EB%A1%9C-%EA%B0%88-%EB%95%8C-%EC%A3%BC%EC%9D%98%ED%95%B4%EC%95%BC%ED%95%A0-%EB%B6%80%EB%B6%84%EB%93%A4/)
* [Radix? Redis!](https://tosslab.github.io/2017/05/09/radix_redis.html)
* [10. 데이터 폭풍이닷: 스크래핑으로 가져온 데이터 처리](https://highluck.github.io/#/project_k)
* 3개의 key column이 있으며, 하나의 key로 찾는 경우
  * scan or hash
  * C_B_A와 같이 key column을 조합해 문서 key로 쓰거나, C로 hash를 각각 만들어 사용
* 혀로그래머 charsyam은 구라쟁이
  * [입 개발 Redis 접속이 안되요!!! – Protected Mode](https://charsyam.wordpress.com/2016/07/11/%EC%9E%85-%EA%B0%9C%EB%B0%9C-redis-%EC%A0%91%EC%86%8D%EC%9D%B4-%EC%95%88%EB%90%98%EC%9A%94-protected-mode/)
  * [샤딩은 쉬워요 샤딩하세요](https://charsyam.wordpress.com/2017/05/24/%ED%98%80%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8-charsyam%EC%9D%80-%EA%B5%AC%EB%9D%BC%EC%9F%81%EC%9D%B4-1-%EC%83%A4%EB%94%A9%EC%9D%80-%EC%89%AC%EC%9B%8C%EC%9A%94-%EC%83%A4%EB%94%A9%ED%95%98%EC%84%B8/)
  * [캐시 멤캐시나 레디스 쓰세요. 쉬워요](https://charsyam.wordpress.com/2017/05/27/%ED%98%80%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8-charsyam%EC%9D%80-%EA%B5%AC%EB%9D%BC%EC%9F%81%EC%9D%B4-2-%EC%BA%90%EC%8B%9C-%EB%A9%A4%EC%BA%90%EC%8B%9C%EB%82%98-%EB%A0%88%EB%94%94%EC%8A%A4-%EC%93%B0/)
  * [레디스 관련 Q&A](https://charsyam.wordpress.com/2017/05/28/%ED%98%80%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8-charsyam%EC%9D%80-%EA%B5%AC%EB%9D%BC%EC%9F%81%EC%9D%B4-qa-%EB%A0%88%EB%94%94%EC%8A%A4-%EA%B4%80%EB%A0%A8-qa/)
  * [Redis에 심플한 key-value 로 수 억개의 데이터 저장하기](https://charsyam.wordpress.com/2011/11/06/redis%EC%97%90-%EC%8B%AC%ED%94%8C%ED%95%9C-key-value-%EB%A1%9C-%EC%88%98-%EC%96%B5%EA%B0%9C%EC%9D%98-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EC%A0%80%EC%9E%A5%ED%95%98%EA%B8%B0/)
  * [spring-security-oauth의 RedisTokenStore의 사용은 서비스에 적합하지 않습니다](https://charsyam.wordpress.com/2018/05/11/%EC%9E%85-%EA%B0%9C%EB%B0%9C-spring-security-oauth%EC%9D%98-redistokenstore%EC%9D%98-%EC%82%AC%EC%9A%A9%EC%9D%80-%EC%84%9C%EB%B9%84%EC%8A%A4%EC%97%90-%EC%A0%81%ED%95%A9%ED%95%98%EC%A7%80-%EC%95%8A/)
  * [Redis 버그 – Dataset 사이즈가 200GB가 넘어가면 죽는다구요?](https://charsyam.wordpress.com/2019/08/26/입-개발-redis-버그-dataset-사이즈가-200gb가-넘어가면-죽는다구요)
  * [왜 Redis 응답이 느린데, slowlog에는 안찍히나요?](https://charsyam.wordpress.com/2020/03/15/%ec%9e%85-%ea%b0%9c%eb%b0%9c-%ec%99%9c-redis-%ec%9d%91%eb%8b%b5%ec%9d%b4-%eb%8a%90%eb%a6%b0%eb%8d%b0-slowlog%ec%97%90%eb%8a%94-%ec%95%88%ec%b0%8d%ed%9e%88%eb%82%98%ec%9a%94/)
  * [입 개발 Redis 6.0 – ThreadedIO를 알아보자](https://charsyam.wordpress.com/2020/05/05/%ec%9e%85-%ea%b0%9c%eb%b0%9c-redis-6-0-threadedio%eb%a5%bc-%ec%95%8c%ec%95%84%eb%b3%b4%ec%9e%90/)
  * [입 개발 Redis 장애 종류 정리 | Charsyam's Blog](https://charsyam.wordpress.com/2020/11/20/%ec%9e%85-%ea%b0%9c%eb%b0%9c-redis-%ec%9e%a5%ec%95%a0-%ec%a2%85%eb%a5%98-%ec%a0%95%eb%a6%ac/)
  * [입 컨설팅 Self Managed Redis 가 좋을까? Managed Redis 가 좋을까? | Charsyam's Blog](https://charsyam.wordpress.com/2021/11/30/%ec%9e%85-%ec%bb%a8%ec%84%a4%ed%8c%85-self-managed-redis-%ea%b0%80-%ec%a2%8b%ec%9d%84%ea%b9%8c-managed-redis-%ea%b0%80-%ec%a2%8b%ec%9d%84%ea%b9%8c/)
  * [입 개발 Redis LRU(Least Recently Used Algorithm)에 대해서 | Charsyam's Blog](https://charsyam.wordpress.com/2022/01/28/%ec%9e%85-%ea%b0%9c%eb%b0%9c-redis-lruleast-recently-used-algorithm%ec%97%90-%eb%8c%80%ed%95%b4%ec%84%9c/)
* [Redis와 전자정부프레임워크 연동](http://daddycat.blogspot.com/2017/06/redis.html)
* [lua 사용 사례](http://knight76.tistory.com/entry/redis-lua-%EC%82%AC%EC%9A%A9-%EC%82%AC%EB%A1%80)
* lock
  * [Transactions and Locks](http://intro2libsys.info/introduction-to-redis/transactions-and-locks)
  * [6.2.3 Building a lock in Redis](https://redislabs.com/ebook/part-2-core-concepts/chapter-6-application-components-in-redis/6-2-distributed-locking/6-2-3-building-a-lock-in-redis/)
  * [SETNX key value](https://redis.io/commands/setnx)
* [분산 웹 캐시 (Wcache)의 개선과정 - Part 1](http://tech.kakao.com/2017/10/23/wcache-1/)
* [분산 웹 캐시 (Wcache)의 개선과정 - Part 2](http://tech.kakao.com/2017/10/23/wcache-2/)
* [Replication](https://redis.io/topics/replication)
  * [redis-replicator](https://github.com/leonchen83/redis-replicator)
* [Redis Node와 연동하기](https://www.zerocho.com/category/NodeJS/post/5a3238b714c5f9001b16c430)
* [운영에 필요한 최소한의 지식](http://jybaek.tistory.com/711) List, Hash
* [Why Redis?](https://www.youtube.com/watch?v=OG610oe_kxs)
* [**Dave Nielsen: Top 5 uses of Redis as a Database**](https://www.youtube.com/watch?v=jTTlBc2-T9Q) 내부 구조 기초
* [Redis as a Database. I’ve been using Redis a lot in the past… | by Tzafrir Ben Ami | Wix Engineering | Medium](https://medium.com/wix-engineering/redis-as-a-database-f9df579b09c0)
* [Redis Labs and SQL Server](https://www.youtube.com/watch?v=XQ9QEgLZAcQ)
* [Build A Node.js & Redis App From Scratch](https://www.youtube.com/watch?v=9S-mphgE5fA)
* [05 01 Implementing a Redis Cache](https://www.youtube.com/watch?v=ECz6Mv3T7Ec)
* [Why Your MySQL Needs Redis | Redis Labs](https://www.youtube.com/watch?v=_4HwUVNl9Nc)
* [Why and When You Should Use Redis](https://www.youtube.com/watch?v=CoQcNgfPYPc)
* [Scaling Redis at Twitter](https://www.youtube.com/watch?v=rP9EKvWt0zo)
* [Redis Use Patterns: An Introduction to the SQL Practitioner](https://www.youtube.com/watch?v=8Unaug_vmFI)
* [Amazon ElastiCache(Redis)를 이용한 채팅 애플리케이션 구성 방법](https://aws.amazon.com/ko/blogs/korea/how-to-build-a-chat-application-with-amazon-elasticache-for-redis)
* [**배민쇼핑라이브를 만드는 기술: 채팅 편 | 우아한형제들 기술블로그**](https://techblog.woowahan.com/5268/)
  * 배달의민족 쇼핑라이브에서 많을 때는 분당 2만 건이 넘는 메시지를 처리하기 위한 채팅을 직접 구현하기로 하면서 Redis의 Pub/Sub과 Webflux를 이용해서 채팅을 구현한 과정을 설명
  * 이전에 구현했던 경험을 통해 WebSocket의 사용 최소화, REST API를 사용할 수 있는 부분은 WebSocket의 커맨드를 이용하지 않도록 하여 WebSocket 처리에는 메시지를 보내고 받는 부분에 집중
  * WebFlux로 non-blocking의 이점을 얻기 위해 대부분의 데이터는 Redis를 이용하고 RDB에 보관해야 하는 API는 별도로 분리
  * WebSession을 사용했는데 어느 날 10,000개의 최대 세션 개수를 넘어서면서 오류가 발생하여 WebSession을 사용하지 않도록 개선
  * 관리자 사이트에서 너무 많은 메시지를 브라우저에서 렌더링하다가 멈추는 문제가 발생하여 리스트를 가상화하고 렌더링 횟수를 줄여서 성능 문제 해결
  * [배민쇼핑라이브를 만드는 기술: 채팅 편 | GeekNews](https://news.hada.io/topic?id=5219)
* [EC2에 Redis CLI 설치하기](https://jojoldu.tistory.com/348)
* [You should revise your Redis max connections setting](https://medium.com/appaloosa-store-engineering/you-should-revise-your-redis-max-connections-setting-8136f063c916)
  * heroku에서 사용할 때 이야기라 server에 설치해서 쓸 때와는 조금 거리가 있지만 참고
* [redis 만료키 삭제](https://www.kudryavka.me/?p=740)
* [우아한 Redis](https://www.slideshare.net/charsyam2/redis-196314086)
* [DevOps 엔지니어의 Redis Test 분투기 - Part 1 ](https://helloworld.kurly.com/blog/redis-fight-part-1/)
* [What I didn’t know I didn’t know about Redis](https://medium.com/swlh/what-i-didnt-know-i-didn-t-know-about-redis-6ad3729f29ed)
* [레디스 버전6 뉴피처와 주요 기능 테스트](https://medium.com/garimoo/%EB%A0%88%EB%94%94%EC%8A%A4-%EB%B2%84%EC%A0%846-%EB%89%B4%ED%94%BC%EC%B2%98%EC%99%80-%EC%A3%BC%EC%9A%94-%EA%B8%B0%EB%8A%A5-%ED%85%8C%EC%8A%A4%ED%8A%B8-45a7f53c4489)
* [레디스 ACL](https://medium.com/garimoo/%EB%A0%88%EB%94%94%EC%8A%A4-acl-7dc10b1b7acb)
* [add a subtitle Redis Strings Explained](https://medium.com/garimoo/add-a-subtitle-redis-strings-explained-90f30acc27fc)
* [클라이언트 사이드 캐싱](https://medium.com/garimoo/%ED%81%B4%EB%9D%BC%EC%9D%B4%EC%96%B8%ED%8A%B8-%EC%82%AC%EC%9D%B4%EB%93%9C-%EC%BA%90%EC%8B%B1-71a3ca7727ff)
* [AOF and RDB size comparison test](https://medium.com/garimoo/redis-aof-and-rdb-size-comparison-test-2dbb603af3f1)
* [Redis Documentation #3 데이터타입과 추상화](https://medium.com/garimoo/redis-documentation-3-%EB%8D%B0%EC%9D%B4%ED%84%B0%ED%83%80%EC%9E%85%EA%B3%BC-%EC%B6%94%EC%83%81%ED%99%94-e86bcd15c876)
* The Redis Series
  * [Install Redis inside Ubuntu VM. I will start a series about Redis, I am… | by Mohammed Hewedy | The Startup | Medium](https://medium.com/swlh/install-redis-inside-a-ubuntu-vm-d5022d42d8cc)
  * [Redis Persistence by Example. This is the Second Post in Redis… | by Mohammed Hewedy | Medium](https://medium.com/@mhewedy_46874/redis-persistence-by-example-167aacf3a028)
  * [Implement game leaderboard using Redis | by Mohammed Hewedy | Medium](https://medium.com/@mhewedy_46874/implement-game-scoring-using-redis-75660f739760)
  * [Implement Job Queue using Redis. This is the Forth Post in The Redis… | by Mohammed Hewedy | Medium](https://medium.com/@mhewedy_46874/implement-job-queue-in-redis-9f0f8d394561)
  * [Building REST API backed by Redis | by Mohammed Hewedy | The Startup | Medium](https://medium.com/swlh/building-rest-api-backed-by-redis-ae8ff4818460)
  * [Building Chat Service in Golang and Websockets Backed by Redis | by Mohammed Hewedy | Level Up Coding](https://levelup.gitconnected.com/building-chat-service-in-golang-and-websockets-backed-by-redis-b42a8784636c)
  * [Redis cluster configuration by example | Medium](https://medium.com/@mhewedy_46874/redis-cluster-configurations-by-example-5480a178e884)
  * [Redis Geospatial by example. This is the eighth post of The Redis… | by Mohammed Hewedy | Medium](https://medium.com/@mhewedy_46874/redis-geospatial-by-example-f5505a0962ef)
* [캐시 성능 향상기 (Improving Cache Speed at Scale) : TOAST Meetup](https://meetup.toast.com/posts/251)
* [if(kakao)2020 코멘터리 01 : 카카오톡 캐싱 시스템의 진화 — Kubernetes와 Redis를 이용한 캐시 팜 구성 – tech.kakao.com](https://tech.kakao.com/2020/11/10/if-kakao-2020-commentary-01-kakao/)
* [쿠버네티스 레디스 클러스터 구축기 - kakaoTV](https://tv.kakao.com/channel/3693125/cliplink/423589917)
* [쿠버네티스에 레디스 캐시 클러스터 구축기 – tech.kakao.com](https://tech.kakao.com/2022/02/09/k8s-redis/)
* [Redis Eviction 정책을 적용하여 효율적인 캐시 띄우기](https://chagokx2.tistory.com/102)
* [서버가 여러대면 로그인 정보는 어디에 저장할까? - Sticky Session, Session Clustering, Redis Session Storage](https://tjdrnr05571.tistory.com/3)
* [Redis 성능 향상을 위한 Redis 세션 저장소와 캐시 저장소의 분리](https://chagokx2.tistory.com/99)
* [**선물하기 시스템의 상품 재고는 어떻게 관리되어질까? - 우아한형제들 기술 블로그**](https://woowabros.github.io/experience/2021/01/19/product-stock.html) redis + RDB 배민 재고 관리
* [레디스(Redis)는 언제 어떻게 사용하는 게 좋을까](https://brunch.co.kr/@skykamja24/575)
* [입 개발 Redis가 maxmemory 보다 더 썼다가 OOM 에러를 던져요!!! | Charsyam's Blog](https://charsyam.wordpress.com/2021/04/14/%EC%9E%85-%EA%B0%9C%EB%B0%9C-redis%EA%B0%80-maxmemory-%EB%B3%B4%EB%8B%A4-%EB%8D%94-%EC%8D%BC%EB%8B%A4%EA%B0%80-oom-%EC%97%90%EB%9F%AC%EB%A5%BC-%EB%8D%98%EC%A0%B8%EC%9A%94/)
* [Improve Cache Speed at Scale - RedisConf 2020 - YouTube](https://www.youtube.com/watch?v=mPg20ykAFU4) Cache Stampede, TTL, PER, 디바운싱, Hot Keys, 읽기분산, 레플리카, 압축
* [How to Set up a Firewall for Redis using ufw | thisDaveJ](https://thisdavej.com/how-to-set-up-a-firewall-for-redis-using-ufw/)
* [Fun with Redis: Creating a Reactive Architecture Using Redis and Microservices - YouTube](https://www.youtube.com/watch?v=YEOoJZ13JtI)
* [(웹툰) Redis 캐시](https://iamsang.com/blog/2021/10/24/redis-cache/)
* [Redis Anti-Patterns Every Developer Should Avoid | Redis Developer Hub](https://developer.redis.com/howtos/antipatterns/)
* [우아한테크세미나 191121 우아한레디스 by 강대명님 - YouTube](https://www.youtube.com/watch?v=mPB2CZiAkKM)
* [Redis 야무지게 사용하기 | NHN FORWARD](https://forward.nhn.com/2021/sessions/16)
* [Render Redis | Render · Cloud Hosting for Developers](https://render.com/blog/redis)

# Book
* [Redis in Action](https://redislabs.com/community/ebook/)

# Clojure
* [redis-get-set](https://github.daumkakao.com/todd-ddd/redis-get-set)

# Command
* [Redis 에서 zadd 와 zincrby 의 차이](https://charsyam.wordpress.com/2018/09/06/%ec%9e%85-%ea%b0%9c%eb%b0%9c-redis-%ec%97%90%ec%84%9c-zadd-%ec%99%80-zincrby-%ec%9d%98-%ec%b0%a8%ec%9d%b4/)
* [Transactions in Redis](http://www.dr-josiah.com/2015/07/transactions-in-redis.html)
* [같은 주문에 2명의 라이더가 동시에 배달하는 문제 해결 - Redis Transaction을 이용하여 데이터 atomic 보장](https://tjdrnr05571.tistory.com/18)
* BGSAVE
  * [practice - backup & restore](https://gist.github.com/hyunjun/cfce6fc1ea6d0ca8995417ed64347538)
* CONFIG
  * `config get maxclients` or `echo "config get maxclients" | nc -v <redis server> <redis port>` 현재 설정된 최대 접속 허용 client 개수
  * [Redis RENAME-COMMAND Parameter](http://redisgate.kr/redis/configuration/param_rename-command.php)
    * 성능저하 혹은 운영상 위험이 발생할 수 있는 명령의 이름을 바꾸는 방법
    * redis.conf에서 해당 명령을 변경 e.g. flushall -> xflushall, flushdb -> xflushdb
* GEO
  * [입 컨설팅 오일나우에서의 Redis 사용 방법 개선하기 – PART #1 | Charsyam's Blog](https://charsyam.wordpress.com/2021/08/31/%ec%9e%85-%ec%bb%a8%ec%84%a4%ed%8c%85-%ec%98%a4%ec%9d%bc%eb%82%98%ec%9a%b0%ec%97%90%ec%84%9c%ec%9d%98-redis-%ec%82%ac%ec%9a%a9-%eb%b0%a9%eb%b2%95-%ea%b0%9c%ec%84%a0%ed%95%98%ea%b8%b0-part-1/)
* [INFO](https://redis.io/commands/INFO) disk usage 등 여러가지 정보
  * `info, info('cpu'), info('memory'), ...` in python
  * `info clients` or `echo "info clients" | nc -v <redis server> <redis port>` connected clients 개수
* [HSCAN](https://redis.io/commands/hscan) `hash name 0 \[match pattern>\]` patern = \*pattern or pattern\* or \*pattern\*
  * `hscan_iter` in python
  * [How to search a key pattern in redis hash?](https://stackoverflow.com/questions/35850608/how-to-search-a-key-pattern-in-redis-hash)
  * [Redis scan 이용하기 Spring에서 (hscan)](https://tjdrnr05571.tistory.com/11)
* redis-cli
  * [Writing a Redis client in pure Bash](http://digitalserb.me/writing-a-redis-client-in-pure-bash/)
  * `nc -v redis.mydomain.com 6379` [Linux - Install redis-cli only](https://stackoverflow.com/questions/21795340/linux-install-redis-cli-only)
  * [redis-cli 에서 –rdb는 주의해서 사용하셔야 합니다](https://charsyam.wordpress.com/2019/10/07/입-개발-redis-cli-에서-rdb는-주의해서-사용하셔야-합니다/)
* RENAME
  * [practice](https://gist.github.com/hyunjun/cfce6fc1ea6d0ca8995417ed64347538#file-rename-md) 앞의 hash를 뒤의 hash로 덮어씀. 앞의 hash는 삭제
* [SCAN](https://redis.io/commands/scan) `scan 0 \[match pattern\]` patern = \*pattern or pattern\* or \*pattern\* e.g. `scan 0 match *test*`
  * `scan_iter` in python
  * [Get all keys in Redis database with python](https://stackoverflow.com/questions/22255589/get-all-keys-in-redis-database-with-python)
  * [**패턴으로 TTL 적용하기**](https://jojoldu.tistory.com/349) scan으로 pattern match되는 key를 찾아 expire 적용하는 script
  * [Redis keys 대신 scan 이용하기](https://tjdrnr05571.tistory.com/11)

# Java
* [Redis Cache 기능을 활용한 성능 개선 이야기 part 1 | Recoding Life](https://jane096.github.io/project/redis-caching/)
* [Redis Cache 기능을 활용한 성능 개선 이야기 Part 2 | Recoding Life](https://jane096.github.io/project/redis-caching-part2/)

# Library
* [Gredis - Redis server built over grpc](https://github.com/voidabhi/gredis)
* [hiredis - Minimalistic C client for Redis >= 1.2](https://github.com/redis/hiredis)
* [ioredis: 🚀 A robust, performance-focused and full-featured Redis client for Node.js](https://github.com/luin/ioredis)
  * [ioredis에 로깅 끼워넣기 · /usr/lib/libsora.so](https://libsora.so/posts/ioredis-logging-with-monkey-patch/)
  * [ioredis-mock - Emulates ioredis by performing all operations in-memory](https://github.com/stipsan/ioredis-mock)
* [KeyDB - A Multithreaded Fork of Redis https://keydb.dev ](https://github.com/JohnSully/KeyDB)
  * [A Multithreaded Fork of Redis That’s 5X Faster Than Redis](https://docs.keydb.dev/blog/2019/10/07/blog-post/)
* [Lambda Store: Serverless Database for Redis®](https://lambda.store/)
  * [Serverless Redis Is Here!](https://medium.com/lambda-store/serverless-redis-is-here-34c2fa335f24)
  * [Swifter Than DynamoDB: Lambda Store — Serverless Redis | by Mattia Bianchi | Lambda Store | Medium](https://medium.com/lambda-store/swifter-than-dynamodb-lambda-store-serverless-redis-bfacfaf92c80)
* [Medis - a beautiful, easy-to-use Mac database management application for Redis. http://getmedis.com](https://github.com/luin/medis)
* [RedisAI | Real-Time ML Model Serving](https://redis.com/modules/redis-ai/)
* [Redis Geo](https://matt.sh/redis-geo)
* [redisgrip: Redis GUI Client](https://github.com/FiaDot/redisgrip)
* Redis Labs [Community Projects | Redis Labs](https://redislabs.com/community/oss-projects/)
  * [Redis In memory data processing](https://www.imcsummit.org/2019/eu/sites/2019.eu/files/slides/Redis%20In%20memory%20data%20processing.pdf)
  * [gesher: K8s Admission control proxy](https://github.com/RedisLabs/gesher)
  * [memtier_benchmark: NoSQL Redis and Memcache traffic generation and benchmarking tool](https://github.com/RedisLabs/memtier_benchmark)
  * [RedisAI - A Server for Machine and Deep Learning Models](https://oss.redislabs.com/redisai/)
  * [RedisBloom - Probabilistic Datatypes Module for Redis](https://oss.redislabs.com/redisbloom/)
  * [RedisGears - Programmable engine for data processing in Redis](https://oss.redislabs.com/redisgears/)
  * [RedisGraph - a graph database module for Redis](https://oss.redislabs.com/redisgraph/)
    * [RedisGraph](https://redislabs.com/redis-enterprise/technology/redisgraph/)
  * [RedisJSON - a JSON data type for Redis](https://oss.redislabs.com/redisjson/)
    * 새로운 도큐먼트 스토어. RediSearch 기반이며 실시간 도큐먼트 스토어로 JSON 타입을 사용해서 쿼리와 풀텍스트 서치 지원
    * Reids에서는 MongoDB와 ElasticSearch보다 더 빠르고 실시간 업데이트가 검색과 읽기에 영향을 주지 않는다고 주장
    * [RedisJSON: Public Preview & Performance Benchmarking | Redis](https://redis.com/blog/redisjson-public-preview-performance-benchmarking/)
  * [RediSearch - Redis Secondary Index & Query Engine](https://oss.redislabs.com/redisearch/)
  * [RedisTimeSeries - Time-Series data structure for Redis](https://oss.redislabs.com/redistimeseries/)
* RedisRaft [Jepsen report on RedisRaft – The Last Mind](http://blog.lastmind.io/archives/932)
* [redis-rdb-tools Parse Redis dump.rdb files, Analyze Memory, and Export Data to JSON https://rdbtools.com ](https://github.com/sripathikrishnan/redis-rdb-tools)
* [redis-traffic-stats - a query analyzer for Redis](https://github.com/hirose31/redis-traffic-stats)
* ~[SerenityDB - disk storage and real transactions under Redis compatible protocol](http://serenitydb.org/)~
* [Spark-Redis - A library for reading and writing data from and to Redis with Apache Spark](https://github.com/RedisLabs/spark-redis)
  * [Give Spark a 45x speed boost with Redis](https://www.infoworld.com/article/3045083/analytics/give-spark-a-45x-speed-boost-with-redis.html)
  * [Spark-Redis - A library for reading and writing data from and to Redis with Apache Spark](https://github.com/oeegee/spark-redis) 2.2.0
* [Treat Redis Lists like Unix Pipes](https://github.com/lukasmartinelli/redis-pipe)
* [twemproxy - A fast, light-weight proxy for memcached and redis](https://github.com/twitter/twemproxy)
  * [recommendation](https://github.com/twitter/twemproxy/blob/master/notes/recommendation.md#server_connections--1)
  * [nutcracker-web - Web interface plugin for nutcracker-ruby (Twemproxy)](https://github.com/kontera-technologies/nutcracker-web)

# Python
* [How to Use Redis with Python 3 and redis-py on Ubuntu 16.04](https://www.fullstackpython.com/blog/install-redis-use-python-3-ubuntu-1604.html)
* [Write Fast Apps Using Async Python 3.6 and Redis](https://eng.paxos.com/write-fast-apps-using-async-python-3.6-and-redis)
  * [subconscious - redis-backed (in memory) db for python3 that is asyncio compatible](https://github.com/paxos-bankchain/subconscious)
* [Dave Nielsen: Top 5 uses of Redis as a Database | PyData Seattle 2015](https://www.youtube.com/watch?v=jTTlBc2-T9Q)
* [redis-python-simple-tutorial](https://github.com/jsrimr/redis-python-simple-tutorial)

## Python Library
* [aioredis - asyncio (PEP 3156) Redis client library](http://aioredis.readthedocs.io/)
  * [github.com/aio-libs/aioredis](https://github.com/aio-libs/aioredis)
  * [Python aioredis.Redis() Examples](https://www.programcreek.com/python/example/98948/aioredis.Redis)
  * [Python aioredis.create_redis_pool() Examples](https://www.programcreek.com/python/example/98950/aioredis.create_redis_pool)
  * [How to use aioredis in tornado](https://groups.google.com/forum/#!msg/aio-libs/HHGm2-NC3UA/mxVinwHKAAAJ)
  * [hello_asyncio.py](https://github.com/rudyryk/python-samples/blob/master/hello_tornado/hello_asyncio.py#L85-L99)
  * [streamis.py](https://github.com/mivade/streamis/blob/master/streamis.py)
* [aioredlock - The asyncio implemetation of Redis distributed locks](https://github.com/joanvila/aioredlock)
  * [aioredlock을 이용한 분산 Lock 구현](https://blog.sinwoobang.me/post/188371203297/aioredlock을-이용한-분산-lock-구현)
* [asyncio-redis - Redis client for Python asyncio](https://github.com/jonathanslenders/asyncio-redis)
* [pydis: A redis clone in Python 3 to disprove some falsehoods about performance](https://github.com/boramalper/pydis)
* [rb: A Redis parallelization toolkit for Python](http://blog.getsentry.com/2015/08/20/rb-redis-parallelization-toolkit.html)
* [redis - Python client for Redis key-value store](https://pypi.python.org/pypi/redis)
  * [redis-py](http://redis-py.readthedocs.io/)
  * [practice - `hgetall` vs. `hscan_iter`, `hmset` vs. `hset` encoding 문제 발생](https://gist.github.com/hyunjun/1a607507f420efb5bcbc3dd3ef37b7ee)
  * [practice - `hset hget hmset hgetall` + json dumps/loads](https://github.com/hyunjun/practice/tree/master/python/test-redis)
  * [fakeredis: A fake version of a redis-py](https://pypi.org/project/fakeredis/)
    * [practice - patch redis.StrictRedis -> fakeRedis.StrictRedis](https://github.com/hyunjun/practice/blob/master/python/test-unittest/test/common/src/test_common.py#L75)
  * [mockredis](https://github.com/locationlabs/mockredis) 뭘 잘못 입력했는지 잘 안됨
  * troubleshooting [`hset`이 <json string value>에 대해 동작하지 않음](https://gist.github.com/hyunjun/4ab30f4ebd401bcb0e60aabbab0b97bc#file-troubleshooting-md)
* [redis-hashring - A Python library that implements a consistent hash ring for building distributed apps](https://github.com/closeio/redis-hashring)
* [Tornado-Redis - Asynchronous Redis client that works within Tornado IO loop](https://github.com/leporo/tornado-redis)

# PubSub
* [Redis Tutorial for Beginners 11 - Redis Publish Subscribe](https://www.youtube.com/watch?v=33N1mgiRYK0)
* [RedisConf17 - How Roblox Keeps Millions of Users up to Date with Redis Pub/Sub - Peter Philips](https://www.youtube.com/watch?v=nXTxXSWBayg)
  * [RedisConf17 - Roblox - How Roblox Keeps Millions of Users Up to Date with Redis Pub/Sub](https://www.slideshare.net/RedisLabs/redisconf17-roblox-how-roblox-keeps-millions-of-users-up-to-date-with-redis-pubsub)
* [입 개발 Redis 7.x 에서의 ShardedPubSub | Charsyam's Blog](https://charsyam.wordpress.com/2022/04/18/%EC%9E%85-%EA%B0%9C%EB%B0%9C-redis-7-x-%EC%97%90%EC%84%9C%EC%9D%98-shardedpubsub/)
* [Advanced Redis: Subscribe Script to Pub/Sub Channel](https://matt.sh/advanced-redis-pubsub-scripts)

## PubSub Python
* [**Redis Pubsub and Message Queueing**](https://stackoverflow.com/questions/27745842/redis-pubsub-and-message-queueing)
* [Is non-blocking Redis pubsub possible?](https://stackoverflow.com/questions/7871526/is-non-blocking-redis-pubsub-possible)
* [Non-Blocking PubSub in Python using Redis](https://ravi.pckl.me/short/non-blocking-pubsub-in-python-and-redis/)
* [CREATE A SIMPLE CHAT ROOM WITH REDIS PUBSUB](http://programeveryday.com/post/create-a-simple-chat-room-with-redis-pubsub/)
* [github.com/r4vi/redis-pubsub](https://github.com/r4vi/redis-pubsub)
  * [Non blocking Redis PubSub in Python](https://www.youtube.com/watch?v=CG4ieKmnyWY)
* [basic redis python pubsub](http://chasemp.github.io/2013/03/26/basic-redis-python-pubsub/)
* [Python & Redis PUB/SUB](https://medium.com/@johngrant/python-redis-pub-sub-6e26b483b3f7)
* [A short script exploring Redis pubsub functions in Python](https://gist.github.com/jobliz/2596594)
* [LINE LIVE 채팅 기능의 기반이 되는 아키텍처](https://engineering.linecorp.com/ko/blog/detail/85)

# Queue
* [Benchmarking Message Queue Latency](https://bravenewgeek.com/benchmarking-message-queue-latency/)
* [Building a Message Queue Using Redis in Go](http://big-elephants.com/2013-09/building-a-message-queue-using-redis-in-go/)
* [Asynchronous Queueing in Redis with Akka | by Orji samuel | The Startup | Medium](https://medium.com/swlh/asynchronous-queueing-in-redis-with-akka-8b707b784bca)
* jedis
  * [Queuing tasks with Redis](https://blog.rapid7.com/2016/05/04/queuing-tasks-with-redis/)
  * [Spring-data-redis 에서 Jedis로 TLS를 쓰면서 인증서 체크는 Disable 하는 방법](https://charsyam.wordpress.com/2019/09/06/입개발-sprint-data-redis-에서-jedis로-tls를-쓰면서-인증서-체크는-disable-하/)
* Lettuce [Jedis 보다 Lettuce 를 쓰자](https://jojoldu.tistory.com/418)

## Queue Library
* [EasyRedisMQ - A Simple .Net Message Queue that Uses Redis for the back end](https://github.com/jkruer01/EasyRedisMQ)
* [Resque (pronounced like "rescue") - a Redis-backed library for creating background jobs, placing those jobs on multiple queues, and processing them later](https://github.com/resque/resque)
* [RSMQ - REDIS SIMPLE MESSAGE QUEUE](http://smrchy.github.io/rsmq/)

## Queue Library Python
* [Flask asynchronous background tasks with Celery and Redis](http://allynh.com/blog/flask-asynchronous-background-tasks-with-celery-and-redis/)
* [Simple Python Queue with Redis](http://peter-hoffmann.com/2012/python-simple-queue-redis-queue.html)
* [Basic Message Queue with Redis](http://flask.pocoo.org/snippets/73/)
* [Asynchronous Tasks in Python with Redis Queue - Twilio](https://www.twilio.com/blog/asynchronous-tasks-in-python-with-redis-queue)
* [Background Tasks in Python using Redis Queues](https://timber.io/blog/background-tasks-in-python-using-task-queues/)
* [kubernetes.io/docs/tasks/job/fine-parallel-processing-work-queue/rediswq.py](https://kubernetes.io/docs/tasks/job/fine-parallel-processing-work-queue/rediswq.py)
* [Task queues](https://www.fullstackpython.com/task-queues.html)
* [HotQueue - a Python library that allows you to use Redis as a message queue within your Python programs](https://github.com/richardhenry/hotqueue)
* [Pyres - a Resque clone](https://github.com/binarydud/pyres)
* [RESTMQ - Redis based message queue](https://github.com/gleicon/restmq)
* [RQ (Redis Queue) - a simple Python library for queueing jobs and processing them in the background with workers](http://python-rq.org/)
  * [github.com/rq](https://github.com/rq)
  * [Redis rq를 이용한 간단한 비동기 작업 큐](http://mcchae.egloos.com/11261352)
  * [Flask by Example – Implementing a Redis Task Queue](https://realpython.com/flask-by-example-implementing-a-redis-task-queue/)
  * [Walkthrough: Deploying a Flask app with Redis Queue (RQ) Workers and Dashboard using Kubernetes](http://tiao.io/posts/walkthrough-deploying-a-flask-app-with-redis-queue-rq-workers-and-dashboard-using-kubernetes/)
  * [Simple Job Queues with django_rq](https://www.imagescape.com/blog/2013/06/13/simple-job-queues-django_rq/)

# Streams
* [Introduction to Redis Streams](https://redis.io/topics/streams-intro)
* [Kafka & Redis Streams](https://hackernoon.com/introduction-to-redis-streams-133f1c375cd3)
* [Streams: a new general purpose data structure in Redis](http://antirez.com/news/114)
* [Redis Streams and the Unified Log](https://brandur.org/redis-streams)
* [Milano Scala Group - Redis Streams with ZIO - YouTube](https://www.youtube.com/watch?v=jJnco6sMZQY)
* [The Design of Redis StreamsSalvatore Sanfilippo, Creator of Redis](https://www.youtube.com/watch?v=Ty1rQuRJijk)
* [Stream 사용 방법](https://jybaek.tistory.com/935)

# Tutorial
* [Redis cluster tutorial](https://redis.io/topics/cluster-tutorial)
* [개발자를 위한 레디스 튜토리얼 01](https://medium.com/garimoo/%EA%B0%9C%EB%B0%9C%EC%9E%90%EB%A5%BC-%EC%9C%84%ED%95%9C-%EB%A0%88%EB%94%94%EC%8A%A4-%ED%8A%9C%ED%86%A0%EB%A6%AC%EC%96%BC-01-92aaa24ca8cc)
* [개발자를 위한 레디스 튜토리얼 02](https://medium.com/garimoo/%EA%B0%9C%EB%B0%9C%EC%9E%90%EB%A5%BC-%EC%9C%84%ED%95%9C-%EB%A0%88%EB%94%94%EC%8A%A4-%ED%8A%9C%ED%86%A0%EB%A6%AC%EC%96%BC-02-f1029893e263)
* [개발자를 위한 레디스 튜토리얼 03](https://medium.com/garimoo/%EA%B0%9C%EB%B0%9C%EC%9E%90%EB%A5%BC-%EC%9C%84%ED%95%9C-%EB%A0%88%EB%94%94%EC%8A%A4-%ED%8A%9C%ED%86%A0%EB%A6%AC%EC%96%BC-03-1d5fa7ca9682)
* [개발자를 위한 레디스 튜토리얼 04](https://medium.com/garimoo/%EA%B0%9C%EB%B0%9C%EC%9E%90%EB%A5%BC-%EC%9C%84%ED%95%9C-%EB%A0%88%EB%94%94%EC%8A%A4-%ED%8A%9C%ED%86%A0%EB%A6%AC%EC%96%BC-04-17256c55493d)
* [Redis tutorial for beginners](https://www.youtube.com/watch?v=z9OPBVe6tgc)
* [Redis Tutorial - A Brief Introduction to Redis](https://www.youtube.com/watch?v=qr4FVhBTq0I)
* [Redis Tutorial - Intro to Redis w/ Node.js Demo](https://www.youtube.com/watch?v=uJb4HjtvcIE)
* [Redis Crash Course Tutorial](https://www.youtube.com/watch?v=Hbt56gFj998)
* [개발자를 위한 레디스 튜토리얼 01](https://meetup.toast.com/posts/224)
* [개발자를 위한 레디스 튜토리얼 02](https://meetup.toast.com/posts/225)
* [개발자를 위한 레디스 튜토리얼 03](https://meetup.toast.com/posts/226)
* [개발자를 위한 레디스 튜토리얼 04](https://meetup.toast.com/posts/227)
* [Redis Crash Course - the What, Why and How to use Redis as your primary database - YouTube](https://www.youtube.com/watch?v=OqCK95AS-YE)
* [Is Redis the ONLY database you need? // Fullstack app from scratch with Next.js & Redis - YouTube](https://www.youtube.com/watch?v=DOIWQddRD5M)
