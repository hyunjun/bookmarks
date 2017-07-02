Redis
=====
* [Writing a Redis client in pure Bash](http://digitalserb.me/writing-a-redis-client-in-pure-bash/)
* [advanced-redis](https://github.com/iamtrk/advanced-redis)
* [How to take advantage of Redis just adding it to your stack](http://oldblog.antirez.com/post/take-advantage-of-redis-adding-it-to-your-stack.html)
* [Recovering Redis Data with GDB](http://bigeng.io/post/118963807718/recovering-redis-data-with-gdb)
* [Redis Hot Patch](http://benmmurphy.github.io/blog/2015/06/09/redis-hot-patch/)
* [How Twitter Uses Redis To Scale - 105TB RAM, 39MM QPS, 10,000+ Instances](http://highscalability.com/blog/2014/9/8/how-twitter-uses-redis-to-scale-105tb-ram-39mm-qps-10000-ins.html)
* [Keeping up with the cool databases we present: Redis](https://codepicnic.com/posts/keeping-up-with-the-cool-databases-we-present-redis-cedebb6e872f539bef8c3f919874e9d7)
* [Transactions in Redis](http://www.dr-josiah.com/2015/07/transactions-in-redis.html)
* [Redis on AWS](http://www.slideshare.net/charsyam2/redis-on-aws)
* [FAILOVER WITH REDIS SENTINEL](http://engineering.vinted.com/2015/09/03/failover-with-redis-sentinel/)
* [Clarifications about Redis and Memcached](http://antirez.com/news/94)
* [Lazy Redis is better Redis](http://antirez.com/news/93)
* [A few things about Redis security](http://antirez.com/news/96)
* [Lock and cache using redis](https://github.com/seamusabshere/lock_and_cache)
* [Recent improvements to Redis Lua scripting](http://antirez.com/news/97)
* [Redis의 SCAN은 어떻게 동작하는가?](http://tech.kakao.com/2016/03/11/redis-scan/)
* [DNS 기반의 Redis HA 구현](http://tech.kakao.com/2016/03/18/redis-ha-dns/)
* [Redis Labs](http://www.slideshare.net/RedisLabs)
* [Redis in a Multi Tenant Environment–High Availability, Monitoring & Much More!](http://www.slideshare.net/RedisLabs/redis-in-a-multi-tenant-environmenthigh-availability-monitoring-much-more)
* [Redis 의 Sentinel](http://crystalcube.co.kr/m/post/177)
* [Redis Conf 2016: Redis in a Multi-Tenant Environmnet](https://www.youtube.com/watch?v=aZ64pM7OVaw&feature=youtu.be)
* [Redis Networking Nerd Down: For Lovers of Packets and Jumbo Frames- John Bullard, Distil Networks](http://www.slideshare.net/RedisLabs)
* [[입 개발] Redis 접속이 안되요!!! – Protected Mode](https://charsyam.wordpress.com/2016/07/11/%EC%9E%85-%EA%B0%9C%EB%B0%9C-redis-%EC%A0%91%EC%86%8D%EC%9D%B4-%EC%95%88%EB%90%98%EC%9A%94-protected-mode/)
* [Developing a Redis Module](https://www.youtube.com/watch?v=LPxx4QPyUPw)
* **[REDIS 데이터 모델들](http://www.popit.kr/redis-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EB%AA%A8%EB%8D%B8%EB%93%A4/)**
* [Redis cluster tutorial](https://redis.io/topics/cluster-tutorial)
* [Radix? Redis!](https://tosslab.github.io/2017/05/09/radix_redis.html)
* [10. 데이터 폭풍이닷: 스크래핑으로 가져온 데이터 처리](https://highluck.github.io/#/project_k)
* 3개의 key column이 있으며, 하나의 key로 찾는 경우
  * scan or hash
  * C_B_A와 같이 key column을 조합해 문서 key로 쓰거나, C로 hash를 각각 만들어 사용
* 혀로그래머 charsyam은 구라쟁이
  * [샤딩은 쉬워요 샤딩하세요](https://charsyam.wordpress.com/2017/05/24/%ED%98%80%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8-charsyam%EC%9D%80-%EA%B5%AC%EB%9D%BC%EC%9F%81%EC%9D%B4-1-%EC%83%A4%EB%94%A9%EC%9D%80-%EC%89%AC%EC%9B%8C%EC%9A%94-%EC%83%A4%EB%94%A9%ED%95%98%EC%84%B8/)
  * [캐시 멤캐시나 레디스 쓰세요.  쉬워요](https://charsyam.wordpress.com/2017/05/27/%ED%98%80%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8-charsyam%EC%9D%80-%EA%B5%AC%EB%9D%BC%EC%9F%81%EC%9D%B4-2-%EC%BA%90%EC%8B%9C-%EB%A9%A4%EC%BA%90%EC%8B%9C%EB%82%98-%EB%A0%88%EB%94%94%EC%8A%A4-%EC%93%B0/)
  * [레디스 관련 Q&A](https://charsyam.wordpress.com/2017/05/28/%ED%98%80%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8-charsyam%EC%9D%80-%EA%B5%AC%EB%9D%BC%EC%9F%81%EC%9D%B4-qa-%EB%A0%88%EB%94%94%EC%8A%A4-%EA%B4%80%EB%A0%A8-qa/)
* [Redis와 전자정부프레임워크 연동](http://daddycat.blogspot.com/2017/06/redis.html)

# Command
* [INFO](https://redis.io/commands/INFO) disk usage 등 여러가지 정보

# Library
* [Gredis - Redis server built over grpc](https://github.com/voidabhi/gredis)
* [rb: A Redis parallelization toolkit for Python](http://blog.getsentry.com/2015/08/20/rb-redis-parallelization-toolkit.html)
* [REDIS SIMPLE MESSAGE QUEUE](http://smrchy.github.io/rsmq/)
* [Redis Geo](https://matt.sh/redis-geo)
* [redis-hashring - A Python library that implements a consistent hash ring for building distributed apps](https://github.com/closeio/redis-hashring)
* [SerenityDB - disk storage and real transactions under Redis compatible protocol](http://serenitydb.org/)
* [Treat Redis Lists like Unix Pipes](https://github.com/lukasmartinelli/redis-pipe)

# Python
* [How to Use Redis with Python 3 and redis-py on Ubuntu 16.04](https://www.fullstackpython.com/blog/install-redis-use-python-3-ubuntu-1604.html)
