SQL
===
* [Intro to Database Systems : Schema Refinement - Functional Dependencies](http://blog.dancrisan.com/intro-to-database-systems-schema-refinement-functional-dependencies)
* [Common DB schema change mistakes | Database Lab · Instant clones of PostgreSQL databases · Postgres.ai](https://postgres.ai/blog/20220525-common-db-schema-change-mistakes)
* [Keeping track of database schema changes - DEV Community](https://dev.to/hernanreyes/keeping-track-of-database-schema-changes-2g62)
* [A Tiny Intro to Database Systems](http://blog.dancrisan.com/a-tiny-intro-to-database-systems)
* [누구나 바로 이해할 수 있는 데이터베이스 기초지식](https://brunch.co.kr/@04925bf0d77f43e/8)
* [How to work optimally with relational databases](https://medium.freecodecamp.org/how-to-work-optimally-with-relational-databases-627073f82d56)
* [The Wide World of Databases](https://blog.usejournal.com/a-light-introduction-to-databases-1154183ab852)
* [In memory database plus traditional database combination back end architecture pattern](https://www.linkedin.com/grp/post/746917-5990940001540542468)
* [DISTRIBUTED SQL DATABASE FOR THE AGE OF DOCKER](https://crate.io/)
* [Aven is a code generator, create an .aven scheme file and the generator will iterate over your Database, tables and columns](https://github.com/joelbugarini/aven-generator)
* [An Improved Private Mechanism for Small Databases](http://arxiv.org/abs/1505.00244)
* [Simplify: move code into database functions](https://sivers.org/pg)
* [PROBABILISTIC M2M RELATIONSHIPS USING BLOOM FILTERS](http://zacharyvoase.com/2012/08/31/m2mbloom/)
* [New course: Learn SQL interactively on Khan Academy](http://cs-blog.khanacademy.org/2015/05/just-released-full-introductory-sql.html)
* [Top 5 SQL and Database Courses to Learn Online](https://medium.com/hackernoon/top-5-sql-and-database-courses-to-learn-online-48424533ac61)
* [SQLBolt, a series of interactive lessons and exercises](http://sqlbolt.com/)
  * [SQLBolt - 인터랙티브 예제로 SQL 배우기 | GeekNews](https://news.hada.io/topic?id=4619)
* [Effective Micro-caching in Relational Database](http://www.briskat.com/blog/Effective-Caching/)
* [Graphs in the database: SQL meets social networks](http://techportal.inviqa.com/2009/09/07/graphs-in-the-database-sql-meets-social-networks/)
* [**sqlfiddle.com**](http://sqlfiddle.com/)
* [Solving Sudoku with SQL](http://www.developerfusion.com/article/84374/solving-sudoku-with-sql)
* [Practical Persistence in Go: SQL Databases](http://www.alexedwards.net/blog/practical-persistence-sql)
* [Why your query language should be explicit](http://blog.hiphipjorge.com/why-your-database-should-be-explicit/)
* [Advanced Queries With SQL That Will Save Your Time](https://towardsdatascience.com/advanced-queries-with-sql-that-will-save-your-time-48a45b7ca2e3)
* [How to Build Advanced SQL. Building more maintainable, readable… | by SeattleDataGuy | Better Programming | Jul, 2020 | Medium](https://medium.com/better-programming/how-to-build-advanced-sql-798d615ba323)
* [The Sequel to SQL](https://www.codeschool.com/courses/the-sequel-to-sql)
* [Thoughts on Time-series Databases](http://jmoiron.net/blog/thoughts-on-timeseries-databases/)
* [DB 102: Database Orientation - Row vs. Column](http://www.ibmsystemsmag.com/Blogs/You-and-i/Archive/db-102-database-orientation-row-vs-column/)
* [NewSQL vs. NoSQL for New OLTP](https://www.youtube.com/watch?v=uhDM4fcI2aI)
* Tiger Beetle [Redesigning OLTP for a New Order of Magnitude - YouTube](https://www.youtube.com/watch?v=32LMicc0gRA)
  * [VidiGo | 비디고 - Analyze Video AI](https://vidigo.ai/h/result/summary/22564)
    * 세계는 더욱 거래적으로 변화하고 있다
      * 세계는 서버에서 서버리스, 초당 청구로 변화, 에너지 소스도 석탄에서 클린 에너지로 전환되어 더 거래적으로 변화
      * 인도의 upi가 2019년에 100억 건의 실시간 거래 처리, 이는 다른 국가들도 뒤따르고 있음을 시사
      * 온라인 거래 처리량이 여러 분야에서 크게 증가했으나, 가장 인기 있는 oltp 데이터베이스는 20~30년 전 설계
    * OLTP 데이터베이스의 재설계 필요성
      * 현재 oltp 데이터베이스는 캐싱 의존성 증가와 대규모 배포 문제 경험, 일부 시스템은 완전히 다른 기술로 전환 선택
      * 오픈소스 oltp 데이터베이스는 미션 크리티컬한 의미에서 온라인 아님, 일부 시스템은 프로프라이어터리 클라우드 데이터베이스로 이동
      * Oltp를 수백만 단위의 트랜잭션으로 확장할 수 있는 방법 모색 필요, 이를 위해서는 스케일 방식 변경이 중요
    * Tiger Beetle의 탄생과 목적
      * Tiger beetle은 분산 금융 트랜잭션 데이터베이스를 최적화하여 oltp 성능을 향상시키기 위해 개발
      * Tiger beetle은 apache 2 라이센스 하에 공개되며 모든 환경에서 어떤 규모의 oltp도 실행할 수 있는 목표
      * Oltp와 관련된 모든 메타데이터를 제어 평면으로 이동시켜 일반 목적 처리와 oltp 사이의 구분 가능
    * 더블 엔트리 회계와 OLTP의 결합
      * 비즈니스 트랜잭션을 추적하기 위한 완벽한 스키마로서 더블 엔트리 회계 방식을 사용하여 oltp 워크로드 최적화
      * 단일 네트워크 요청으로 수천 개의 비즈니스 트랜잭션을 처리할 수 있는 방식으로 쿼리 증폭을 우리의 이점으로 전환
      * 고정 크기 구조체에 비즈니스 트랜잭션을 패킹하여 네트워크 요청당 최대 1만 개까지 처리 가능
    * 분산 시스템의 효율적인 트랜잭션 처리
      * 복제된 상태 머신 아키텍처를 사용하여 클러스터 전체에서 동일한 상태를 유지
      * Tiger beetle은 성공을 가정하고 오류 코드만 반환하여 네트워크 트래픽 절약
      * 최소한의 시스템 호출과 메모리 복사로 높은 트랜잭션 처리량 달성
    * 데이터베이스 성능 최적화 전략
      * Oltp 작업 부하에서 발생하는 경합을 줄이기 위해 tiger beetle은 고유한 네트워크 프로토콜 사용
      * 컴퓨팅 파워의 발전과 네트워크 지연 시간의 차이를 고려하여 수직 및 수평 확장 방식 혼합
      * Lsm 트리와 같은 최신 데이터 저장 기술을 적용하여 쓰기 지연 문제를 해결하고 성능 개선
    * Tiger Beetle 스토리지 엔진의 혁신
      * Tiger beetle은 모든 데이터 의존성을 메모리에 사전 캐싱하여 디스크 i/o 없이 트랜잭션 실행
      * 다양한 lsm 트리 기법 개발로 예측 가능한 성능과 쓰기 지연 없는 환경 제공
      * 데이터 파일의 결정론적 생성으로 빠른 복구와 더 나은 내구성 달성
    * 합의 프로토콜과 스토리지 엔진의 결합
      * Tiger beetle은 합의 로그 하나로 8,000개의 트랜잭션을 복제하여 합의 비용 최소화
      * View stamp replication 프로토콜 사용으로 고효율 동기화 복제 및 자동 장애 조치 구현
      * 글로벌 중복성 활용과 스토리지 엔진과 합의 프로토콜 간 긴밀한 통합으로 내구성 및 회복력 강화
    * 합의 프로토콜 비교 Raft와 VSR
      * 가장 직관적이고 최적화된 합의 논문 중 하나로 소개
      * Raft와 vsr은 리더 선출 방식에서 차이; vsr은 다음 리더가 누구인지 예측 가능
      * Vsr은 메모리 상에서 실행될 수 있어 디스크 작업에 대한 부담 감소
    * Raft의 한계와 Tiger Beetle의 혁신
      * Raft는 저장 장치 결함을 처리하지 못해 클러스터 중지 가능
      * Tiger beetle은 암호화 해시 체인을 사용하여 로그 복구 최적화
      * Tiger beetle은 결정론적 데이터베이스 설계를 통해 고성능과 안정성 제공
    * Tiger Beetle 시뮬레이션과 실제 적용 사례
      * Tiger beetle 시뮬레이터는 다양한 네트워크 및 저장 장치 결함 테스트
      * Golden gate bridge에서 실행되는 tiger beetle 클러스터 시뮬레이션 소개
      * 시뮬레이션을 통해 tiger beetle의 내구성과 성능을 검증 가능
  * [새로운 규모를 위한 OLTP 재설계 | 완벽한 영상요약, 릴리스에이아이 | Lilys AI](https://lilys.ai/digest/484968?sId=32LMicc0gRA)
    * 1. 서버리스 컴퓨팅과 에너지 거래의 변화.
      * 세계가 점차 *트랜잭션 중심*으로 변화. 서버를 서버리스로, 청구를 초당청구로 전환
      * 과거 3년마다 서버를 구매하거나 월단위 임대를 했다면, 지금은 매 초마다 중요한 거래
      * 또한 석탄에서 깨끗한 에너지로의 변화도 진행 중, 세계 곳곳의 스마트 미터가 이제 한 달에 한 번이 아닌 30분마다 에너지 거래
      * 서버구동 데이터베이스는 아직 올 인 메모리 방식 유지, 캐싱 의존도 증가, 뉴올더 매그니투드에 대한 재설계 필요성
    * 2. 인도와 브라질은 결제 트랜잭션 상승 예상
      * 인도 UPI는 2019년에 100억건의 실시간 거래 처리, 올해 8월만 100억건 처리
      * 브라질은 월 30억 건으로, 매년 200% 성장하고 있어, 인도 선도하며 다른 나라들도 뒤쳐지지 않음
      * 세계는 점차 더 많은 거래로 변화하고 있으며 온라인 거래량은 세 가지 섹터에서 세 배 증가
      * 오늘날 가장 인기 있는 OLTP 데이터베이스인 PostgreSQL, MySQL 및 SQLite은 20~30년 전 설계, 새로운 세계와 규모에 부적합
    * 3.️ 작은 폭 DB인 TigerBeetle로 OLTP의 스케일링과 안전성에 도전
      * 운영 경비: 추가 장치에 대한 비용 지불과, 운영 경험의 변화 중요
      * 산업공학의 '더 적은 리소스로 더 많은 것을 한다'의 관점, 단일 머신에서 수백만 트랜잭션으로 확장하는 것이 목표
      * 서로 다른 색으로 보통 이해되는 컴퓨터과학 원리들을 하나로 조화롭게 결합하는 최상의 디자인 고민, 이로써 TigerBeetle 창조
      * OLAP과의 연관성, 데이터 일관성 등을 고려한 TigerBeetle은 안전하고 효율적인 OLTP 처리를 위한 분산 금융 거래 데이터베이스
    * 4.OLTP 벤치마크, Debit Credit과 ACID
      * Debit Credit은 첫 OLTP 벤치마크였고, Jim Gray와 24명의 공동 저자들이 참여
      * Jim Gray는 Tandem에서 Transactions Processing 전문가로 활동하며 ACID 용어와 다섯 분 규칙을 제안
      * 이로 인해 다양한 벤치마크 전쟁이 일어나게 되고 Transaction Processing Performance Council이 형성
      * 데이터베이스 트랜잭션 언어가 SQL인 반면 실제 비즈니스 트랜잭션 언어는 이중 분개 회계이며, 이것이 쿼리 증폭의 긴장 야기
    * 5. Double Entry의 장점 및 데이터베이스 디자인의 역사적 변화
      * Double Entry의 장점은 OLTP 비즈니스 거래를 처리할 수 있고 표준화되어
        * 서로 다른 128바이트 거래/두 개의 CPU 캐시 라인에서 동일한 작업을 처리할 수 있는 단일 네트워크 요청에서 최대 8,000개 거래 처리
      * 거래는 UUID, 디스트리뷰티드, 증감전용 계정 ID, 거래 시간/메타데이터 등 필요, 메모리 밴드너디로 인한 DB 디자인 역사적인 변화 설명
      * 늘어나는 부하에 따라 요청이 충원되고 수많은 거래가 발생하면 최고의 처리량과 로우 레이턴시를 제공
    * 6.️ 메모리 효율성을 위한 Zig프로그래밍
      * 메모리 대역폭을 효율적으로 사용하기 위해 '프린시플 오브 제로 메모리 알로케이션'에 투자
      * 스타트업 시 모든 필요한 것을 할당하며 런타임에는 'malloc' 또는 'free' 사용하지 않음. Zig에 투자한 이유는 *메모리 효율성*과 일치
      * 분산 로그와 *상태 머신* 아키텍처를 활용하여 효율적인 *트랜잭션 처리* 및 *데이터 일관성* 유지
      * 네트워크 프로토콜을 최적화하여 *계정 업데이트 락을 제거*하고 *트랜잭션 처리량*을 극대화
      * 수평 샤디의 *계좌 별로 16,000개의 락을 필요로 하는* OLTP 워크로드의 병목 현상을 극복하기 위한 효율적인 방법론 구현
    * 7. 네트워크 덜 기다리고 성능 향상방법 트라이거 비틀
      * 트랜잭션 완료를 기다리는 CPU를 네트워크 요청으로 느려지지 않게 해야함
      * 트래젝션 데이터를 모든 CPU 코어에 복제하여 성능적 분리로 스케일링을 가능하게 함
      * *트랜잭션 실행 과정*에서 IO가 없게 하여 성능을 최적화하고 디스크와 네트워크를 건드리지 않음
      * B-트리와 LSM 트리로 저작 비용을 고려하여 트랜잭션을 메모리로 빠르게 이동시키고 *캐싱 기술*을 활용
      * 라이트 스톨 문제, 컴팩션 작업을 예측하고 제한하여 비동기적 차단현상을 최소화
    * 8. LSM 트리에서 LSM 포레스트로 발전
      * 시간을 바(bar)로, 박(bar)을 비트(beats)로 나누고, 각 요청과 관련된 CPU, 디스크, 메모리 압축은 이 비트들을 획일적으로 퍼트림
      * 개선되고자 하는 기술을 가바지 콜렉션처럼 생각, 'stop-the-world'에서 'pause, jitter-free compaction' 전환 방법 설명
      * 모든 데이터에 대해 하나의 트리를 사용하는 문제를 다루는 기술 소개, 이로 인해 어느 시점에서는 RUM 추측을 넘어서야 할 것이라 제안
      * 다양한 사이즈/유형 데이터를 하나의 트리에 저장하는 문제는 다른 작업 최적화에 영향, 이를 해결위해 'RUMBER'로 발전시키는 방법 소개
      * 비슷한 작업 유형에 따라 여러 개 트리를 사용하여 쓰기, 읽기 및 메모리 최적화를 가능하게 하는 'LSM 포레스트'로 전환하는 예시 제시
    * 9. 저장 방법과 데이터 손실에 대한 고찰
      * NetApp과의 연구에서 보니 규모가 커질수록 저장 매체의 내구성이 중요
      * Scale 환경에서는 작은 확률이 커진다. *BSE 의약품* 연구에서 2년 동안 *커뮤니티 디스크*는 0.5% 데이터 손상 가능성
      * SQLite는 데이터의 도난을 방지하기 위해 데이터베이스 파일에 *데이터 중복*을 추가하지 않았다. 그로 인해 데이터 손실 가능성 높음
      * PostgreSQL과 MySQL은 *비정상 종료 일관성* 모델을 갖췄지만, 저장 고장 감지나 복구에는 취약
      * Tigerle은 *명시적* 저장 고장 모델로 설계, *저장 고장이 발생한다*를 전제로 하여 데이터 손실을 줄이기 위한 수 많은 기술 사용
    * 10. Tiger Beetle의 스토리지 엔진 기술
      * Tiger Beetle은 *부모 자식 간의 체크섬*을 활용하여 데이터 무결성을 유지
      * 메타데이터를 위한 *두 번째 작은 Write-Ahead Log*를 활용하여 데이터 손상 식별하고 복구
      * Just-In-Time compaction 기술 통해 저장 엔진이 deterministic하게 파일 생성, RAID같은 방법보다 더 효율적인 global redundancy 제공
      * 스토리지 엔진과 합의 프로토콜을 통합하여 *로컬 장애에서 글로벌 재생산성을 보장*, *데이터 무결성/성능 향상 기술*을 통합
    * 11. 복제와 합의 기술의 차이점 및 동작 방식 비교
      * 복제와 합의에는 8,000개의 트랜잭션을 복제하는 테크닉이 사용
      * 합의 로그의 단일 항목은 8,000개의 트랜잭션을 복제, 시스템 내에 중복 데이터 전송 감소
      * VSR 프로토콜은 Raft에 비해 리더 선출 및 데이터 보관 측면에서 더 적합한 기술로 인식
      * Raft는 레플리카 간 데이터 무결성 관리 시 문제가 발생할 수 있지만 VSR은 이를 손쉽게 처리 가능
      * 리더와 백업 레플리카 간 전송 데이터 무결성과 가용성을 아우르는 합의 프로토콜의 중요성을 강조
    * 12. 저장 장애 대비로 VSSR과 Raft를 혼용하는 Tiger Beetle의 독특한 기술
      * VSR은 메모리에서만 실행되는 프로토콜로 Raft와 같이 안정된 저장장치에서도 작동 가능
      * Tiger Beetle은 VSR과 협력하여 디스크 문제를 감지하고 복구 가능한 저장 엔진을 가지고 있음
      * 암호화 해시 체인을 통해 Raft 이상의 상황 처리 가능, 모든 기계에 손상된 로그가 있는 경우에도 처리 가능
      * Tiger Beetle은 로그를 결합하고 진행함으로써 백업 작업을 최적화하며, 빠르게 작동하고 오류의 회복을 백그라운드에서 진행
    * 13.️ Tiger Beetle의 성능과 안정성
      * Tarle에서는 '복구 방법'으로 '구성원'에게 수행할 올바른 조치가 무엇인지 알아보라고 요청하며 여러 기능들에 대한 많은 작업을 수행
      * Consensus를 통한 속도 향상의 효과가 크며, 사전 복제 및 동시에 상태 머신에서의 실행이 주요 요소 중 하나
      * Tiger Beetle은 초당 988,000개의 트랜잭션 처리 가능
        * 추가 인덱스를 구현하면 여러 속성 쿼리와 'zigzag merge join'을 통해 트랜잭션을 빠르고 안정적으로 수행 가능
      * 안전성이 성능보다 중요하며, 새로운 기술을 도입하여 안정성과 성능을 상호 보완
      * 30년 동안 검증된 기술을 수용하되 혁신을 통해 조합하며 우수한 결과 창출
    * 14.️ NASA의 10가지 안전 규칙을 따른 TigerDB 설계
      * NASA의 안전규칙 10가지를 따라 'TigerDB'에서 4,000개의 검증이 진행
      * 자원 *메모리와 동시성* 등에도 한계를 두며, 코드의 안정성을 높임
      * 분산 데이터베이스로서의 'Tiger'뿐만 아니라 결정적 분산 데이터베이스로도 설계됨
      * 테스트에는 완전히 *결정적*이며, 시뮬레이션된 환경에서 다양한 실험을 함으로써 코드의 올바름 및 활동성을 확인
      * 또한 시간을 가속시키는 시뮬레이션 테스트로 버그를 재현하고 빠르게 수정함을 강조
    * 15.️ 네트워크 문제 시뮬레이션 및 데이터베이스 오류 발견
      * 앤디 팽로가 유명한 방울목욕을 하면서 멤버들에게 할던 강의를 드리는 레드 데저트 환경
      * 네트워크 문제를 시뮬레이션하며 네트워크 패킷을 제외하여 네트워크를 깨뜨리고 비틀스 그룹을 분할
      * 다양한 도구를 사용하여 기본이 되는 사이트를 찾거나 디스크 데이터를 *파괴하는 실험* 등을 통해 코드의 다양한 버그를 발견중
* [Database expert on why NoSQL mattered — and SQL still matters](https://medium.com/s-c-a-l-e/database-guru-on-why-nosql-matters-and-sql-still-matters-c64239fe84fd)
* [DBMS는 RDB와 NoSQL만 있나요? | 요즘IT](https://yozm.wishket.com/magazine/detail/2806/)
* [SQL Style Guide](http://www.sqlstyle.guide/)
* [SQL Commands Cheat Sheet - Download in PDF & JPG Format - Intellipaat](https://intellipaat.com/blog/tutorial/sql-tutorial/sql-commands-cheat-sheet/)
* [How does a relational database work](http://coding-geek.com/how-databases-work/)
* [Generating MoM, YoY and CMGR from SQL](http://tech.yunojuno.com/sql-window-functions)
* [Crab adds SQL to your command lin](http://etia.co.uk/)
* [PizzaHack - Project from Maghimim 2015 camp for teaching about the SQL Injection vulnerability, and about SQL](https://github.com/benjamingr/pizzahack)
* [free.codebashing.com/courses/python/lessons/sql_injection](https://free.codebashing.com/courses/python/lessons/sql_injection) 파이썬으로 대화형 sql injection test
* [How I bypassed Cloudflare's SQL Injection filter](https://www.astrocamel.com/web/2020/09/04/how-i-bypassed-cloudflares-sql-injection-filter.html)
* [Error-Based SQL Injection.. : 네이버블로그](https://blog.naver.com/crehacktive3/222187681939)
* [웹 개발자를 위한 SQL injection 웹 해킹 보안 가이드](https://blog.naver.com/nanotoly/222214308327)
* [A Scientific Notation Bug in MySQL left AWS WAF Clients Vulnerable to SQL Injection - GoSecure](https://www.gosecure.net/blog/2021/10/19/a-scientific-notation-bug-in-mysql-left-aws-waf-clients-vulnerable-to-sql-injection/)
* [데이터베이스 보안을 향상시키는 11가지 기술 - ITWorld Korea](https://www.itworld.co.kr/news/201094)
* [Welcome to the π-Base - A community database of topological examples with automated deduction and powerful search](http://topology.jdabbs.com/)
* [Yesquel: scalable SQL storage for Web applications](http://sigops.org/sosp/sosp15/current/2015-Monterey/printable/106-aguilera.pdf)
* [FreeGeoDB - Free database of geographic place names and corresponding geospatial data](https://github.com/delight-im/FreeGeoDB)
* [RDBMS Genealogy](https://hpi.de/naumann/projects/rdbms_genealogy.html)
* ["Transactions: myths, surprises and opportunities" by Martin Kleppmann](https://www.youtube.com/watch?v=5ZjhNTM8XU8)
* [#WDILTW – To use a RDBMS is to use a transaction](http://ronaldbradford.com/blog/wdiltw-to-use-a-rdbms-is-to-use-a-transaction-2021-02-19/)
* [DBMS는 어떻게 트랜잭션을 관리할까?](https://d2.naver.com/helloworld/407507)
* [Enterprise Architecting Series: Transaction Service · Present](https://present.do/presentations/61346fa75b179c0da7466a9a?page=0)
* [DB 트랜잭션 격리 수준 그림과 예시로 쉽게 이해하기 - 1편 | by 10x 개발자 | Aug, 2022 | Medium](https://medium.com/@10x.developer.kr/db-%ED%8A%B8%EB%9E%9C%EC%9E%AD%EC%85%98-%EA%B2%A9%EB%A6%AC-%EC%88%98%EC%A4%80-%EA%B7%B8%EB%A6%BC%EA%B3%BC-%EC%98%88%EC%8B%9C%EB%A1%9C-%EC%89%BD%EA%B2%8C-%EC%9D%B4%ED%95%B4%ED%95%98%EA%B8%B0-1%ED%8E%B8-5bef68de8b7b)
* [GalaXQL - Interactive SQL tutorial](http://sol.gfxile.net/galaxql.html)
* [Learn SQL - Free Interactive SQL Tutorial](https://www.learnsqlonline.org/)
* [SQL Tutorial for Beginners – Learn SQL Programming Online -Intellipaat](https://intellipaat.com/blog/tutorial/sql-tutorial/)
* [(즐겁게 배우는 SQL) 기획 소개](https://jhrogue.blogspot.com/2020/11/sql.html)
* [즐겁게 배우는 SQL - YouTube](https://www.youtube.com/playlist?list=PLdntWJk2tJPLinuRXcokohNLgc83ejwUt)
  * [(즐겁게 배우는 SQL #1) 정말 간단한 질의부터 시작하자](https://jhrogue.blogspot.com/2020/11/sql-1.html)
  * [(즐겁게 배우는 SQL #2) 행을 정렬하자](https://jhrogue.blogspot.com/2020/11/sql-2.html)
  * [(즐겁게 배우는 SQL #3) 데이터를 필터링하자 - Select Distinct](https://jhrogue.blogspot.com/2020/11/sql-3-select-distinct.html)
  * [(즐겁게 배우는 SQL #4) 데이터를 필터링하자 - where](https://jhrogue.blogspot.com/2020/11/sql-4-where.html)
  * [(즐겁게 배우는 SQL #5) 데이터를 필터링하자 - limit](https://jhrogue.blogspot.com/2020/11/sql-5-limit.html)
  * [(즐겁게 배우는 SQL #6) 데이터를 필터링하자 - between](https://jhrogue.blogspot.com/2020/12/sql-6-between.html)
  * [(즐겁게 배우는 SQL #7) 데이터를 필터링하자 - in](https://jhrogue.blogspot.com/2020/12/sql-7-in.html)
  * [(즐겁게 배우는 SQL #8) 데이터를 필터링하자 - like](https://jhrogue.blogspot.com/2020/12/sql-8-like.html)
  * [(즐겁게 배우는 SQL #9) 데이터를 필터링하자 - GLOB](https://jhrogue.blogspot.com/2020/12/sql-9-glob.html)
  * [(즐겁게 배우는 SQL #10) 데이터를 필터링하자 - IS NULL](https://jhrogue.blogspot.com/2020/12/sql-10-is-null.html)
  * [(즐겁게 배우는 SQL #11) 테이블을 조인하자 - JOIN 설명](https://jhrogue.blogspot.com/2020/12/sql-11-join.html)
  * [(즐겁게 배우는 SQL #12) 테이블을 조인하자 - INNER JOIN](https://jhrogue.blogspot.com/2020/12/sql-12-inner-join.html)
  * [(즐겁게 배우는 SQL #13) 테이블을 조인하자 - LEFT JOIN](https://jhrogue.blogspot.com/2020/12/sql-13-left-join.html)
  * [(즐겁게 배우는 SQL #14) 테이블을 조인하자 - CROSS JOIN](https://jhrogue.blogspot.com/2020/12/sql-14-cross-join.html)
  * [(즐겁게 배우는 SQL #15) 테이블을 조인하자 - SELF JOIN](https://jhrogue.blogspot.com/2020/12/sql-15-self-join.html)
  * [(즐겁게 배우는 SQL #16) 테이블을 조인하자 - FULL OUTER JOIN](https://jhrogue.blogspot.com/2020/12/sql-16-full-outer-join.html)
  * [(즐겁게 배우는 SQL #17) 데이터를 그룹으로 묶어보자 - Group By](https://jhrogue.blogspot.com/2020/12/sql-17-group-by.html)
  * [(즐겁게 배우는 SQL #18) 데이터를 그룹으로 묶어보자 - HAVING](https://jhrogue.blogspot.com/2020/12/sql-18-having.html)
  * [(즐겁게 배우는 SQL #19) 집합 연산자를 배우자 - Union](https://jhrogue.blogspot.com/2020/12/sql-19-union.html)
  * [(즐겁게 배우는 SQL #20) 집합 연산자를 배우자 - Except와 Intersect](https://jhrogue.blogspot.com/2020/12/sql-20-except-intersect.html)
  * [(즐겁게 배우는 SQL #21) 집합 연산자를 배우자 - MySQL에서 Intersect와 Except 흉내내기](https://jhrogue.blogspot.com/2020/12/sql-21-mysql-intersect-except.html)
  * [(즐겁게 배우는 SQL #22) 서브 질의를 배우자 - 서브 질의](https://jhrogue.blogspot.com/2020/12/sql-22.html)
  * [(즐겁게 배우는 SQL #23) 서브 질의를 배우자 - Exists](https://jhrogue.blogspot.com/2020/12/sql-23-exists.html)
  * [(즐겁게 배우는 SQL #24) 서브 질의를 배우자 - Case](https://jhrogue.blogspot.com/2020/12/sql-24-case.html)
  * [(즐겁게 배우는 SQL #25) 보너스 - 지금까지 배운 내용 응용하기](https://jhrogue.blogspot.com/2021/01/sql-25.html)
  * [(즐겁게 배우는 SQL #26) CRUD 연산의 기본기를 배우자 - C(Create)를 위한 INSERT](https://jhrogue.blogspot.com/2021/01/sql-26-crud-ccreate-insert.html)
  * [(즐겁게 배우는 SQL #27) CRUD 연산의 기본기를 배우자 - U(Update)를 위한 UPDATE](https://jhrogue.blogspot.com/2021/01/sql-27-crud-uupdate-update.html)
  * [(즐겁게 배우는 SQL #28) CRUD 연산의 기본기를 배우자 - D(Delete)를 위한 DELETE](https://jhrogue.blogspot.com/2021/01/sql-28-crud-ddelete-delete.html)
  * [(즐겁게 배우는 SQL #29) CRUD 연산의 기본기를 배우자 - 삽입하거나 기존 행을 대체하는 REPLACE](https://jhrogue.blogspot.com/2021/01/sql-29-crud-replace.html)
  * [(즐겁게 배우는 SQL #30) 트랜잭션이 뭐지?](https://jhrogue.blogspot.com/2021/01/sql-30.html)
  * [(즐겁게 배우는 SQL #31) 데이터를 정의하자 - SQL 데이터 타입](https://jhrogue.blogspot.com/2021/01/sql-31-sql.html)
  * [(즐겁게 배우는 SQL #32) 데이터를 정의하자 - 테이블 생성](https://jhrogue.blogspot.com/2021/01/sql-32.html)
  * [(즐겁게 배우는 SQL #33) 데이터를 정의하자 - 테이블 변경](https://jhrogue.blogspot.com/2021/01/sql-33.html)
  * [(즐겁게 배우는 SQL #34) 데이터를 정의하자 - 테이블 열 이름 변경](https://jhrogue.blogspot.com/2021/01/sql-34.html)
  * [(즐겁게 배우는 SQL #35) 데이터를 정의하자 - 테이블 제거](https://jhrogue.blogspot.com/2021/01/sql-35.html)
  * [(즐겁게 배우는 SQL #36) 데이터를 정의하자 - 청소(Vacuum)](https://jhrogue.blogspot.com/2021/01/sql-36-vacuum.html)
  * [(즐겁게 배우는 SQL #37) 제약 조건 - 기본 키](https://jhrogue.blogspot.com/2021/01/sql-37.html)
  * [(즐겁게 배우는 SQL #38) 제약 조건 - 외래 키](https://jhrogue.blogspot.com/2021/01/sql-38.html)
  * [(즐겁게 배우는 SQL #39) 제약 조건 - NOT NULL 제약](https://jhrogue.blogspot.com/2021/01/sql-39-not-null.html)
  * [(즐겁게 배우는 SQL #40) 제약 조건 - UNIQUE 제약](https://jhrogue.blogspot.com/2021/01/sql-40-unique.html)
  * [(즐겁게 배우는 SQL #41) 제약 조건 - CHECK 제약](https://jhrogue.blogspot.com/2021/01/sql-41-check.html)
  * [(즐겁게 배우는 SQL #42) 제약 조건 - AUTOINCREMENT 제약](https://jhrogue.blogspot.com/2021/01/sql-42-autoincrement.html)
  * [(즐겁게 배우는 SQL #43) 뷰 - 뷰 생성](https://jhrogue.blogspot.com/2021/02/sql-43.html)
  * [(즐겁게 배우는 SQL #44) 뷰 - 뷰 제거](https://jhrogue.blogspot.com/2021/02/sql-44.html)
  * [(즐겁게 배우는 SQL #45) 색인 - 색인](https://jhrogue.blogspot.com/2021/02/sql-45.html)
  * [(즐겁게 배우는 SQL #46) 색인 - 표현식 기반의 색인](https://jhrogue.blogspot.com/2021/02/sql-46.html)
  * [(즐겁게 배우는 SQL #47) 트리거 - 트리거](https://jhrogue.blogspot.com/2021/02/sql-47.html)
  * [(즐겁게 배우는 SQL #48) 트리거 - INSTEAD OF 트리거](https://jhrogue.blogspot.com/2021/02/sql-48-instead-of.html)
  * [(즐겁게 배우는 SQL #49) 윈도우 함수 - 윈도우 함수(1)](https://jhrogue.blogspot.com/2021/02/sql-49-1.html)
  * [(즐겁게 배우는 SQL #50) 윈도우 함수 - 윈도우 함수(2)](https://jhrogue.blogspot.com/2021/02/sql-50-2.html)
  * [(즐겁게 배우는 SQL #51) (보충) where와 having 차이점 설명](https://jhrogue.blogspot.com/2021/12/sql-51-where-having.html)
* [DB update set에서 주의할 점](https://yeonyeon.tistory.com/319)
* [JOIN 조인 + 예시](https://velog.io/@hyun5no/JOIN-%EC%A1%B0%EC%9D%B8-%EC%98%88%EC%8B%9C)
* [The difference between WHERE and HAVING – SQL Bits](https://sql-bits.com/the-difference-between-where-and-having/)
* [SQLrevisited: Difference between DELETE vs DROP vs TRUNCATE in SQL](https://www.sqlrevisited.com/2022/08/delete-vs-drop-vs-truncate-in-sql.html)
* [WHERE vs HAVING and GROUP BY vs PARTITION BY Clause in SQL - Tech Point Fundamentals](https://www.techpointfunda.com/2021/12/where-vs-having-clause-in-sql.html)
* [DB에 하지 말아야 할 겪은 일들](https://velog.io/@juunini/DB%EC%97%90-%ED%95%98%EC%A7%80-%EB%A7%90%EC%95%84%EC%95%BC-%ED%95%A0-%EA%B2%AA%EC%9D%80-%EC%9D%BC%EB%93%A4)
* [고독쓰나미 - YouTube](https://www.youtube.com/channel/UClUrjhtzmAJL-sgXe6sNUkw)
* [Torturing Databases for Fun and Profit](https://www.usenix.org/conference/osdi14/technical-sessions/presentation/zheng_mai)
* [EDB is a framework to make and manage backups of your database](https://github.com/RoxasShadow/EDB)
* [클라우드 기반의 데이터베이스 백업 및 복구 플랫폼 | 쿠팡 엔지니어링 | Coupang Engineering Blog](https://medium.com/coupang-engineering/towards-a-robust-cloud-based-database-backup-and-recovery-platform-6732f476e3a3)
  * [쿠팡이 클라우드 기반 ‘데이터베이스 백업 플랫폼’을 만든 이유 | 요즘IT](https://yozm.wishket.com/magazine/detail/2146/)
* [IntelliJ 0xDBE](http://tiveloper.tistory.com/category/IDE%20%26%20Apps/IntelliJ%200xDBE)
* [Chaos Tomb: Visualizing Gameplay with D3 and SQL](http://www.moria.us/ludumdare/ld32/analytics/)
* [Exploring the Wall Street Journal's Pulitzer-Winning Medicare Investigation with SQL](http://2015.padjo.org/tutorials/sql-walks/exploring-wsj-medicare-investigation-with-sql/)
* [Readings in Database Systems, 5th Edition](http://www.redbook.io/)
* [aquerytool.com](http://aquerytool.com/)
* [dbguide.net](http://www.dbguide.net/index.db)
* [코드카데미, SQL 중급 강의 무료 공개](http://www.bloter.net/archives/254362)
* [SQL,SELECT문처리순서/과정 parsing,optimization,execution,fetch,옵티마이저,파싱,실행,패치](http://ojc.asia/bbs/board.php?bo_table=LecOrccleTun&wr_id=113)
* [How to Optimize SQL Queries. This article sorts out some special… | by Pawan Jain | Jun, 2020 | Towards Data Science](https://towardsdatascience.com/how-to-optimize-sql-queries-742177cd5cc6)
* [How to Optimize SQL Queries Part II | by Pawan Jain | Jul, 2020 | Towards Data Science](https://towardsdatascience.com/how-to-optimize-sql-queries-part-ii-407311784112)
* [SQL Query Optimization: Level Up Your SQL Performance Tuning | by Garvit Arya | Feb, 2022 | Better Programming](https://betterprogramming.pub/sql-query-optimization-level-up-your-sql-performance-tuning-d93af175b24b)
* [Top 10 Tips to Improve SQL Query Performance | by Bigscal Technologies | Medium](https://medium.com/@Bigscal-Technologies/top-10-tips-to-improve-sql-query-performance-f40f25047661)
* [Valentina Cupać on Twitter: "What's the logical order of SQL query operations? SQL Query Execution Order (Visualized). #SQL #Databases https://t.co/PWgGe0SNbU" / Twitter](https://twitter.com/ValentinaCupac/status/1556906177686036480)
* [SQL Query Order of Execution | Sisense](https://www.sisense.com/blog/sql-query-order-of-operations/)
* [SQL queries run in this order](https://www.linkedin.com/feed/update/urn:li:activity:7001435210026225664/)
* [Parsing SQL - Federico Tomassetti - Software Architect](https://tomassetti.me/parsing-sql/)
* [(SQL초보자를 위한, 쿼리최적화 for SQL튜닝)SQL쿼리작성Tip,최적화팁,최적화된SQL작성방법교육](http://www.slideshare.net/topcredu/sql-for-sqlsqltipsql)
* [초보자 확실히 기억해야 하는 SQL 가이드](https://brunch.co.kr/@04925bf0d77f43e/7)
* [제3회 스포카콘 SQL 쿼리 최적화 맛보기](https://www.slideshare.net/ssuser7f6de5/3-sql-243154656)
* [비전공자를 위한 SQL](https://brunch.co.kr/magazine/sql-beginner)
* [나만 모르고 있던 – Flyway (DB 마이그레이션 Tool)](http://www.popit.kr/%EB%82%98%EB%A7%8C-%EB%AA%A8%EB%A5%B4%EA%B3%A0-%EC%9E%88%EB%8D%98-flyway-db-%EB%A7%88%EC%9D%B4%EA%B7%B8%EB%A0%88%EC%9D%B4%EC%85%98-tool/)
* [예제로 배우는 SQL 프로그래밍](http://www.sqlprogram.com/)
* [DB-Engines Ranking - Trend Popularity](http://db-engines.com/en/ranking_trend)
* [Comparison of different SQL implementations](http://troels.arvin.dk/db/rdbms/)
* [DB 데이터를 Hadoop에 저장 시 삽질 두가지](http://www.popit.kr/db-%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%A5%BC-hadoop%EC%97%90-%EC%A0%80%EC%9E%A5-%EC%8B%9C-%EC%82%BD%EC%A7%88-%EB%91%90%EA%B0%80%EC%A7%80/)
* 혀로그래머 charsyam은 구라쟁이
  * [샤딩은 쉬워요 샤딩하세요](https://charsyam.wordpress.com/2017/05/24/%ED%98%80%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8-charsyam%EC%9D%80-%EA%B5%AC%EB%9D%BC%EC%9F%81%EC%9D%B4-1-%EC%83%A4%EB%94%A9%EC%9D%80-%EC%89%AC%EC%9B%8C%EC%9A%94-%EC%83%A4%EB%94%A9%ED%95%98%EC%84%B8/)
  * [캐시 멤캐시나 레디스 쓰세요.  쉬워요](https://charsyam.wordpress.com/2017/05/27/%ED%98%80%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8-charsyam%EC%9D%80-%EA%B5%AC%EB%9D%BC%EC%9F%81%EC%9D%B4-2-%EC%BA%90%EC%8B%9C-%EB%A9%A4%EC%BA%90%EC%8B%9C%EB%82%98-%EB%A0%88%EB%94%94%EC%8A%A4-%EC%93%B0/)
  * [레디스 관련 Q&A](https://charsyam.wordpress.com/2017/05/28/%ED%98%80%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8-charsyam%EC%9D%80-%EA%B5%AC%EB%9D%BC%EC%9F%81%EC%9D%B4-qa-%EB%A0%88%EB%94%94%EC%8A%A4-%EA%B4%80%EB%A0%A8-qa/)
* [WebSanitizer ScanningVideotest acunetix com](https://www.youtube.com/watch?v=M0FZgeM2rgo)
* [패스트캠퍼스 SQL튜닝캠프 1일차 - 인덱스 구조와 스캔 방식](http://jojoldu.tistory.com/162)
* [고치면서 배우는 즐거운 SQL](https://brunch.co.kr/@linterpreteur/26)
* [SQL이란: 데이터 쿼리와 관리](https://ko.khanacademy.org/computing/computer-programming/sql)
* [데이터베이스 관리 도구: SQLGate 키보드 단축키](http://blog.gaerae.com/2017/11/sqlgate-keyboard-shortcuts.html)
* [Software engineer — from monolith to cloud: Auto Increment to UUID](https://coder.today/software-engineer-from-monolith-to-cloud-auto-increment-to-uuid-a62f92f387c4)
* [Reasons why SELECT * is bad for SQL performance | Tanel Poder Consulting](https://tanelpoder.com/posts/reasons-why-select-star-is-bad-for-sql-performance/)
* [UUIDs are Popular, but Bad for Performance — Let’s Discuss](https://www.percona.com/blog/2019/11/22/uuids-are-popular-but-bad-for-performance-lets-discuss/)
* [Generating UUIDs at scale on the Web | by Matthieu Wipliez | Teads Engineering | Jul, 2020 | Medium](https://medium.com/teads-engineering/generating-uuids-at-scale-on-the-web-2877f529d2a2)
* [uuid-readable: Generate Easy to Remember, Readable UUIDs, that are Shakespearean and Grammatically Correct Sentences 🥳](https://github.com/Debdut/uuid-readable)
* [Understanding How UUIDs Are Generated - Digital Bunker](https://digitalbunker.dev/2020/09/30/understanding-how-uuids-are-generated/)
* [Why Did We Shift Away From Database-Generated Ids?](https://medium.com/ingeniouslysimple/why-did-we-shift-away-from-database-generated-ids-7e0e54a49bb3)
* [Don't Use Database Generated IDs | The Startup](https://medium.com/swlh/dont-use-database-generated-ids-d703d35e9cc4)
* [Instagram 에서 ID 샤딩하기](https://charsyam.wordpress.com/2011/12/04/instagram-%EC%97%90%EC%84%9C-id-%EC%83%A4%EB%94%A9%ED%95%98%EA%B8%B0)
* [Code Quality Comparison of Firebird, MySQL, and PostgreSQL](https://medium.com/@CPP_Coder/code-quality-comparison-of-firebird-mysql-and-postgresql-53e39fc3298d)
* [SQL Best Practices — Designing An ETL Video](https://hackernoon.com/sql-best-practices-designing-an-etl-video-1933665f9861)
* [RDB에서 데이터 ETL을 위한 최소한의 테이블 설계](https://burning-dba.tistory.com/157)
* [**DBMS 버퍼 관리의 두 가지 흐름 가상 메모리 페이지 교체 알고리즘 활용…페이지 부재 발생 빈도 줄여 성능 향상**](http://www.datanet.co.kr/news/articleView.html?idxno=115592)
* [DBMS의 탄생과 발전, 그리고 역사](http://www.datanet.co.kr/news/articleView.html?idxno=114558)
* [01 - History of Databases (CMU Databases / Spring 2020)](https://www.youtube.com/watch?v=SdW5RKUboKc&list=PLSE8ODhjZXjasmrEd2_Yi1deeE360zv5O)
* [중국의 어떤 서버 개발자의 디비 설계](https://blog.naver.com/imays/221461537682)
  * [practice - 중국의 어떤 서버 개발자의 디비 설계](https://gist.github.com/hyunjun/0f83fd13165444e38645a74bc4e1c1f1#file-db_design-md)
* [An explanation of the difference between Isolation levels vs. Consistency levels](https://dbmsmusings.blogspot.com/2019/08/an-explanation-of-difference-between.html)
* [What every developer should know about database consistency | Roberto Vitillo's Blog](https://robertovitillo.com/what-every-developer-should-know-about-database-consistency/)
* [A Better Way to Write SQL queries for Developers](https://hackernoon.com/a-better-way-to-write-sql-queries-for-developers-b645f4fdcff0)
* [관계형 데이터 모델링](https://opentutorials.org/module/4134)
  * [관계형 데이터 모델링](https://www.youtube.com/playlist?list=PLuHgQVnccGMDF6rHsY9qMuJMd295Yk4sa)
* [Database 모델링에 대해서 정리해 봅니다](https://developer88.tistory.com/327)
* [데이터 모델링이란? (관계형 DB 편)](https://bitnine.tistory.com/446)
* [검색엔진과 DB Like 검색의 결과가 다른 이유](https://www.slideshare.net/heungrae_kim/db-like)
* [코호트 분석(Cohort Analysis)을 SQL로 구현하는 테스트 코드](https://www.sangkon.com/using_sql_for_cohort/)
* [Write-Ahead Log for Dummies](https://work.tinou.com/2012/09/write-ahead-log.html)
* [번역 데이터 구조와 설계 — 튜토리얼](https://medium.com/@khwsc1/%EB%B2%88%EC%97%AD-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EA%B5%AC%EC%A1%B0%EC%99%80-%EC%84%A4%EA%B3%84-%ED%8A%9C%ED%86%A0%EB%A6%AC%EC%96%BC-b25792a0aa86)
* [**Database basics: writing a SQL database from scratch in Go**](https://notes.eatonphil.com/database-basics.html)
* [Choosing a Database Technology](https://towardsdatascience.com/choosing-a-database-technology-d7f5a61d1e98)
* [The Best Medium-Hard Data Analyst SQL Interview Questions](https://quip.com/2gwZArKuWk7W)
* [Things I Wished More Developers Knew About Databases](https://medium.com/@rakyll/things-i-wished-more-developers-knew-about-databases-2d0178464f78)
* [Understanding Database IOPS - Part 1 | Kloud DB](http://www.klouddb.io/understanding-database-iops-part-1/)
* [오라클12c 행제한구문 실습, MySQL의 top-N 쿼리, 페이징 쿼리 (Pagination Query) - YouTube](https://www.youtube.com/watch?v=HT3EltCwgmw)
* [How to Implement Cursor Pagination Like a Pro | by Megan Chang | The Startup | Medium](https://medium.com/swlh/how-to-implement-cursor-pagination-like-a-pro-513140b65f32)
* [A Snowflake deep dive](https://hhhypergrowth.com/a-snowflake-deep-dive/) 기술이야기는 아니고 snowflake 소개
* [Database of Databases - Home](https://dbdb.io/)
* [How to use Indexing for SQL Query Optimization | Towards Data Science](https://towardsdatascience.com/indexing-for-sql-query-optimization-139b57db9fc6)
* [SERIES: 데이터베이스 인덱스 공부](https://hudi.blog/series/%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%B2%A0%EC%9D%B4%EC%8A%A4-%EC%9D%B8%EB%8D%B1%EC%8A%A4-%EA%B3%B5%EB%B6%80)
* [Speed Up DB Queries Like a Pro - DEV Community](https://dev.to/lovestaco/speed-up-db-queries-like-a-pro-2d95)
  * [데이터베이스 쿼리 속도를 높이는 인덱스 활용법 | 요즘IT](https://yozm.wishket.com/magazine/detail/3045/)
* [Using SQL to Estimate Customer Lifetime Value (LTV) without Machine Learning - Data Science Central](https://www.datasciencecentral.com/profiles/blogs/using-sql-to-estimate-customer-lifetime-value-ltv-without-machine)
* [Understanding Connections & Pools](https://sudhir.io/understanding-connections-pools/)
* [내가 만든 서비스는 얼마나 많은 사용자가 이용할 수 있을까? - 3편(DB Connection Pool)](https://hyuntaeknote.tistory.com/12)
* [**ConnectionStrings.com - Forgot that connection string? Get it here!**](https://www.connectionstrings.com/) 각 DB별 connection string 모음
* [Maximum number of database connections - Vlad Mihalcea](https://vladmihalcea.com/maximum-database-connections/)
* [What can we learn from SQL's 50 year reign? A story of 2 Turing Awards](https://blog.arctype.com/sql-50-years/)
* [Running a bakery on Emacs and PostgreSQL // Just a Summary](https://bofh.org.uk/2019/02/25/baking-with-emacs/)
* [You might as well timestamp it |> Changelog](https://changelog.com/posts/you-might-as-well-timestamp-it) flag보다 timestamp를 써야 한다는 주장
  * [is_leave vs leaved_at vs leave_status](https://jojoldu.tistory.com/577)
* [DB 시간 값을 DEFAULT로 넣지 마세요](https://sturdy-mink-c2f.notion.site/DB-DEFAULT-17f020f4210280a9a574e9ea99680ee2)
* [The State of the Open Source Database Industry in 2020: Part Three - Percona Database Performance Blog](https://www.percona.com/blog/2020/04/22/the-state-of-the-open-source-database-industry-in-2020-part-three/)
* [Database Performance Secrets of the Stars! - YouTube](https://www.youtube.com/watch?v=J9Z30ie5J6Q)
* [Demystifying Database Performance for Developers](https://www.crunchydata.com/blog/demystifying-database-performance-for-developers)
* [Against SQL](https://scattered-thoughts.net/writing/against-sql/)
* [A beginner's guide to database multitenancy - Vlad Mihalcea](https://vladmihalcea.com/database-multitenancy/)
* [칼럼｜데이터베이스의 '주류 교체', 숨막히게 더딜지라도... - CIO Korea](https://www.ciokorea.com/news/204299)
* [칼럼 | 개발자가 ‘데이터베이스’를 먼저 감안해야 할 이유 - CIO Korea](https://www.ciokorea.com/news/324526)
* [영상 : 초보자가 저지르기 쉬운 DB 코딩 실수 3가지 :: 자바캔(Java Can Do IT)](https://javacan.tistory.com/entry/%EC%98%81%EC%83%81-%EC%B4%88%EB%B3%B4%EC%9E%90%EA%B0%80-%EC%A0%80%EC%A7%80%EB%A5%B4%EA%B8%B0-%EC%89%AC%EC%9A%B4-DB-%EC%BD%94%EB%94%A9-%EC%8B%A4%EC%88%98-3%EA%B0%80%EC%A7%80)
* [A future for SQL on the web](https://jlongster.com/future-sql-web)
  * [웹용 SQL의 미래 | GeekNews](https://news.hada.io/topic?id=4808)
* [Stephen Colebourne's blog: Big problems at the timezone database](https://blog.joda.org/2021/09/big-problems-at-timezone-database.html)
* [통계 서버를 구축하며!. 소개 | by Jason Kang | Uniquegood | Oct, 2021 | Medium](https://medium.com/uniquegood/%ED%86%B5%EA%B3%84-%EC%84%9C%EB%B2%84%EB%A5%BC-%EA%B5%AC%EC%B6%95%ED%95%98%EB%A9%B0-c071c6d4f945) 주제 분류가 좀 애매하지만 동시성 문제를 이야기하니 우선 여기에
* [pubkey/client-side-databases: An implementation of the exact same app in Firestore, AWS Datastore, PouchDB, RxDB and WatermelonDB](https://github.com/pubkey/client-side-databases)
* [Database Replication Explained. Part 1 — Single Leader Replication | by Zixuan Zhang | Nov, 2021 | Towards Data Science](https://towardsdatascience.com/database-replication-explained-5c76a200d8f3)
* [Database Replication Explained 2. Part 2— Multi Leader Replication | by Zixuan Zhang | Nov, 2021 | Towards Data Science](https://towardsdatascience.com/database-replication-explained-10ff929bdf8a)
* [Database Replication Explained 3. Part 3 -Leaderless Replication | by Zixuan Zhang | Nov, 2021 | Towards Data Science](https://towardsdatascience.com/database-replication-explained-3-32d6deceeca7)
* [How to optimize your SQL Database to handle millions of records — part 1 | by SianLoong | Medium](https://sianloong90.medium.com/how-to-optimise-your-sql-database-to-handle-million-records-part-1-748d68f2dee1)
* [Is Kubernetes slowing down my database? | DB Exam Study](https://dbexamstudy.blogspot.com/2021/11/is-kubernetes-slowing-down-my-database.html)
* [Goodbye etcd, Hello PostgreSQL: Running Kubernetes with an SQL Database | by Martin Heinz | Jul, 2023 | Better Programming](https://betterprogramming.pub/goodbye-etcd-hello-postgresql-running-kubernetes-with-an-sql-database-7e1b2e9b5f8f)
* [Databases in 2021: A Year in Review - OtterTune](https://ottertune.com/blog/2021-databases-retrospective/)
  * [2021년 데이터베이스들 리뷰 | GeekNews](https://news.hada.io/topic?id=5652)
* [글로벌 칼럼 | ‘진화 혹은 변혁’ 클라우드 데이터 웨어하우스의 미래 - ITWorld Korea](https://www.itworld.co.kr/news/218994)
* [Thread by @ergestx on Thread Reader App – Thread Reader App](https://threadreaderapp.com/thread/1479811885377765383.html)
  * [SQL 팁 : 나의 SQL 작성 패턴 | GeekNews](https://news.hada.io/topic?id=5896)
* [Different Ways to Check and Delete Duplicate Records in SQL - Tech Point Fundamentals](https://www.techpointfunda.com/2021/11/deleting-duplicate-records-in-sql.html)
* [How to choose the right database for your project | by Anthony Papoutsis | Mar, 2022 | Medium](https://apapoutsis.medium.com/how-to-choose-the-right-database-for-your-project-ffd4bf054833)
* [How to choose the right database for your service | by Natan Silnitsky | Wix Engineering | Medium](https://medium.com/wix-engineering/how-to-choose-the-right-database-for-your-service-97b1670c5632)
* [“데이터 계층을 위한 탄력적 컴퓨팅” 서버리스 데이터베이스의 이해 - ITWorld Korea](https://www.itworld.co.kr/news/228914)
* [A database for 2022 · Tailscale](https://tailscale.com/blog/database-for-2022/)
* [SQL 가독성을 높이는 다섯 가지 사소한 습관](https://velog.io/@datarian/good-sql-code)
* [SQL 가독성을 높이는 다섯 가지 사소한 습관 | 요즘IT](https://yozm.wishket.com/magazine/detail/1519/)
* [MySQL에서 SQL 문장 가독성 향상시키는 법 | 요즘IT](https://yozm.wishket.com/magazine/detail/2758/)
* [Alternative to MapReduce for search in distributed databases - DEV Community](https://dev.to/tarantool/alternative-to-mapreduce-for-search-in-distributed-databases-890)
* [Building data-centric apps with a reactive relational database](https://riffle.systems/essays/prelude/)
* [아직도 DBA는 좋은 직업인가요? | GeekNews](https://news.hada.io/topic?id=6530)
* [Why SQL Needs Software Libraries | Future](https://future.com/sql-needs-software-libraries/)
* [Everything Is a Funnel, But SQL Doesn’t Get It | by Motif Analytics | Jun, 2022 | Medium](https://motifanalytics.medium.com/everything-is-a-funnel-but-sql-doesnt-get-it-c35356424044)
* [DataBase](https://velog.io/@oceanwater1234/DB-SQL)
* [Scan sharing - IBM Documentation](https://www.ibm.com/docs/en/db2/11.1?topic=methods-scan-sharing)
* [05 - Buffer Pools (CMU Intro to Database Systems / Fall 2021) - YouTube](https://www.youtube.com/watch?v=Moz2AgC9hG4)
* [MVCC 구조와 이해](https://mozi.tistory.com/561)
* [고가용성의 웹 서비스를 위한 데이터베이스 클러스터링](https://hudi.blog/database-clustering/) clustering
* [오래된 DB와 이별하는 방법 :: GS Retail Engineering](https://gsretail.tistory.com/25)
* [DB migration 방법론 :: GS Retail Engineering](https://gsretail.tistory.com/29)
* [DB 마이그레이션 시 순번 전략 체크하자! - YouTube](https://www.youtube.com/watch?v=rCmNGDc2e5Q)
* [Number와 boolean 은 최대한 Not Null로 선언하기](https://jojoldu.tistory.com/718)
* ['is not NULL'과 '!= NULL'은 다르다?](https://yeonyeon.tistory.com/307)
* [SQL NULLs are Weird!](https://jirevwe.github.io/sql-nulls-are-weird.html)
  * [SQL의 NULL은 이상함 | GeekNews](https://news.hada.io/topic?id=18679)
* [디비 주문구조 설계 - 동시성 고려를 위한.. : 네이버블로그](https://blog.naver.com/pjt3591oo/223187705803)
* [디비 추적 가능한 테이블 설계 : 네이버 블로그](https://blog.naver.com/pjt3591oo/223188329119)
* [디비 게시판 구조 설계 - 게시글 관리 그.. : 네이버블로그](https://blog.naver.com/pjt3591oo/223193892552)
* [BULK 처리 Write에 집중해서 개선해보기 - 컬리 기술 블로그](https://helloworld.kurly.com/blog/bulk-performance-tuning/)
* [Database Fundamentals](https://tontinton.com/posts/database-fundementals/)
* [You'll regret using natural keys](https://blog.ploeh.dk/2024/06/03/youll-regret-using-natural-keys/)
  * [자연 키를 사용하는 것을 후회하게 될 꺼에요 | GeekNews](https://news.hada.io/topic?id=15198)
* [SQL Has Problems. We Can Fix Them: Pipe Syntax In SQL](https://research.google/pubs/sql-has-problems-we-can-fix-them-pipe-syntax-in-sql/)
  * [SQL의 문제점과 해결 방안: SQL의 파이프 문법 | GeekNews](https://news.hada.io/topic?id=16466)
* [Base Entity 활용하기](https://sturdy-mink-c2f.notion.site/Base-Entity-18a020f4210280478408cf40759bc576)
* [가독성 좋은 GUID, 왜 RDBMS에서 이렇게 유용해졌을까? - YouTube](https://www.youtube.com/watch?v=ekwNi5_u72I)
* [DB PK로 사용해도 되는 GUID, UUID7은 축복인가 vs 폭탄인가? - YouTube](https://www.youtube.com/watch?v=PQOcbo2NqMw)
* [스냅샷 구조 이해하기](https://sturdy-mink-c2f.notion.site/1ad901fdcb0549978173459ed5a50e77)
  * [스냅샷 구조 이해하기 | Notion | 강경수 | 댓글 18](https://www.linkedin.com/posts/kakasoo_%EC%8A%A4%EB%83%85%EC%83%B7-%EA%B5%AC%EC%A1%B0-%EC%9D%B4%ED%95%B4%ED%95%98%EA%B8%B0-notion-activity-7378990939673063424-4RtU)
* [the-5-types-of-database: Slides and notes for the talk "Explaining the 5 types of database and how to choose between them"](https://github.com/Aiven-Labs/the-5-types-of-database)
  * [Explaining the 5 types of database and how to choose between them — Tibs - YouTube](https://www.youtube.com/watch?v=YZmyumwFWOg)
  * [데이터베이스 5가지 유형과 선택 가이드: 관계형, 컬럼, 문서, 키-값, 그래프](https://livewiki.com/ko/content/database-types-choose-tibs)
* [밑바닥 부터 구현하는 데이터베이스 1 - 운영체제에 파일을 어떻게 읽고 쓸까? - Roach Wiki](https://roach-wiki.com/wiki/doc-1762867059)
* [SQ라이트의 대안, 설치 없이 바로 쓰는 데이터베이스 4종 | ITWorld](https://www.itworld.co.kr/article/4127743/sq%EB%9D%BC%EC%9D%B4%ED%8A%B8%EC%9D%98-%EB%8C%80%EC%95%88-%EC%84%A4%EC%B9%98-%EC%97%86%EC%9D%B4-%EB%B0%94%EB%A1%9C-%EC%93%B0%EB%8A%94-%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%B2%A0%EC%9D%B4%EC%8A%A4-4%EC%A2%85.html)

# Altibase
* [Altibase](https://github.com/ALTIBASE/altibase)

# Amazon Aurora Database
* [Redesigning MySQL - AWS Tech Talk on the Aurora Database](https://engineering.opendns.com/2015/04/07/redesigning-mysql-aws-tech-talk-on-the-aurora-database/)
* [Now Available – Amazon Aurora](https://aws.amazon.com/ko/blogs/aws/now-available-amazon-aurora/)
* [최소한의 다운타임으로 아마존 RDS Aurora DB로 이전하기](http://blog.sendbird.com/ko/%EC%B5%9C%EC%86%8C%ED%95%9C%EC%9D%98-%EB%8B%A4%EC%9A%B4%ED%83%80%EC%9E%84%EC%9C%BC%EB%A1%9C-%EC%95%84%EB%A7%88%EC%A1%B4-rds-aurora-db%EB%A1%9C-%EC%9D%B4%EC%A0%84%ED%95%98%EA%B8%B0/)
* [MySQL에서 RDS(Aurora) 로 이관하기](https://blog.stibee.com/mysql%EC%97%90%EC%84%9C-rds-aurora-%EB%A1%9C-%EC%9D%B4%EA%B4%80%ED%95%98%EA%B8%B0-227db1da8fd8)
* [Amazon Aurora 내부 들여다보기 (1) – 쿼럼 및 상관 오류 해결 방법](https://aws.amazon.com/ko/blogs/korea/amazon-aurora-under-the-hood-quorum-and-correlated-failure)
* [20180726 AWS KRUG - RDS Aurora에 40억건 데이터 입력하기](https://www.slideshare.net/addnull/20180726-aws-krug-rds-aurora-40-107532095)
* [Amazon Aurora – MySQL에서 DB 부하에 대한 최적화 방법](https://aws.amazon.com/ko/blogs/korea/planning-and-optimizing-amazon-aurora-with-mysql-compatibility-for-consolidated-workloads)
* [재해복구(DR)를 위한 오로라 데이터베이스 구성 | 우아한형제들 기술블로그](https://techblog.woowahan.com/2604/)
* [AWS Aurora DB Cluster & Instance Parameter 튜닝](https://pkgonan.github.io/2019/01/aws-aurora-db-parameter-tuning)
* [Aurora 로컬 스토리지 성능 테스트 | 우아한형제들 기술블로그](https://techblog.woowahan.com/2621/)
* [Amazon Aurora MySQL Database Administrator’s Handbook (요약 및 의역)](http://blog.hwang.gg/20190702/)
* [Amazon Aurora Multi-Master를 통한 고가용성 MySQL 애플리케이션 만들기](https://aws.amazon.com/ko/blogs/korea/building-highly-available-mysql-applications-using-amazon-aurora-mmsr)
* [Aurora MySQL를 운영하면서 알면 좋을 것 같은 미세한 팁 | 우아한형제들 기술블로그](https://techblog.woowahan.com/2653/)
* [Aurora MySQL 스냅샷을 Parquet 로 S3 에 Export](https://chang12.github.io/rds-snapshot-export-to-s3/)
* [When Should I Use Amazon Aurora and When Should I use RDS MySQL? - Percona Database Performance Blog](https://www.percona.com/blog/2018/07/17/when-should-i-use-amazon-aurora-and-when-should-i-use-rds-mysql/)
* [A First Glance at Amazon Aurora Serverless RDS - Percona Database Performance Blog](https://www.percona.com/blog/2020/10/27/a-first-glance-at-amazon-aurora-serverless-rds/)
* [AWS Announces New Database Service Babelfish for Aurora PostgreSQL in Preview](https://www.infoq.com/news/2020/12/aws-postgresql-aurora-babelfish/)
* [Amazon Aurora PostgreSQL 에서 pg_bigm 모듈사용하기](https://jojoldu.tistory.com/590)
* [(AWS Aurora) PostgreSQL에서 Lock 쿼리 확인하고 원인 종료하기](https://jojoldu.tistory.com/591)
* [입 개발 MariaDB Connector 와 AWS Aurora | Charsyam's Blog](https://charsyam.wordpress.com/2021/12/11/%ec%9e%85-%ea%b0%9c%eb%b0%9c-mariadb-connector-%ec%99%80-aws-aurora/)
* [Planning I/O in Amazon Aurora | AWS Database Blog](https://aws.amazon.com/de/blogs/database/planning-i-o-in-amazon-aurora/)
* [Leveraging AWS Aurora for Event Sourcing | by Lomig Mégard | SwissBorg Engineering | Feb, 2022 | Medium](https://medium.com/swissborg-engineering/leveraging-aws-aurora-for-event-sourcing-e8323dce58b6)
* [**Aurora MySQL vs Aurora PostgreSQL | 우아한형제들 기술블로그**](https://techblog.woowahan.com/6550/)
* [Amazon Aurora Serverless v2 정식 출시 – 워크로드 요구 사항에 따른 즉각적인 DB 크기 조정 | Amazon Web Services 한국 블로그](https://aws.amazon.com/ko/blogs/korea/amazon-aurora-serverless-v2-is-generally-available-instant-scaling-for-demanding-workloads/)
* [No, AWS, Aurora Serverless v2 Is Not Serverless - Last Week in AWS Blog](https://www.lastweekinaws.com/blog/no-aws-aurora-serverless-v2-is-not-serverless/)
  * [AWS Aurora Serverless v2 는 Serverless가 아니다 | GeekNews](https://news.hada.io/topic?id=6796)
* [Amazon RDS Custom에서 Oracle Database 재생성 하기 | AWS 기술 블로그](https://aws.amazon.com/ko/blogs/tech/recreate-amazon-rds-custom-oracle-instance/)
* [Common pitfalls when migrating MySQL to Aurora using AWS DMS | EverSQL](https://www.eversql.com/common-pitfalls-when-migrating-mysql-to-aurora-using-aws-dms/)
* [AWS Data Migration Service(DMS)를 활용하여 Amazon Aurora PostgreSQL 블루/그린 배포 환경 생성하기 | AWS 기술 블로그](https://aws.amazon.com/ko/blogs/tech/amazon-aurora-postgres-blue-green-with-dms/)
* [블루/그린 배포를 이용한 Aurora MySQL 버전 무중단 업그레이드 경험 공유 | by Siheon Kim | Feb, 2023 | HBsmith](https://blog.hbsmith.io/%EB%B8%94%EB%A3%A8-%EA%B7%B8%EB%A6%B0-%EB%B0%B0%ED%8F%AC%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%9C-aurora-mysql-%EB%B2%84%EC%A0%84-%EB%AC%B4%EC%A4%91%EB%8B%A8-%EC%97%85%EA%B7%B8%EB%A0%88%EC%9D%B4%EB%93%9C-%EA%B2%BD%ED%97%98-%EA%B3%B5%EC%9C%A0-23c52b988abe)
* [Amazon RDS MySQL 블루/그린 배포환경에서 전환 작업 이후 복구 환경 구성을 위한 동기화 기법 | AWS 기술 블로그](https://aws.amazon.com/ko/blogs/tech/amazon-rds-mysql-blue-green-after-restoring/)
* [우아한형제들에서 RDS를 모니터링 하는 방법 | AWS 기술 블로그](https://aws.amazon.com/ko/blogs/tech/how-to-monitor-rds-in-woowabrothers/)
* [AWS RDS Storage 성능 비교. AWS 서비스에 사용할 Storage에 대한 자료를 찾아보다가  AWS… | by Kimmatt | 직방 기술 블로그 | Apr, 2023 | Medium](https://medium.com/zigbang/aws-rds-storage-%EC%84%B1%EB%8A%A5-%EB%B9%84%EA%B5%90-3d1150b97b2e)
* [Amazon Aurora I/O-Optimized 클러스터 구성- I/O 집약적 애플리케이션을 위한 최대 40% 비용 절감할 수 있는 스토리지 옵션 | Amazon Web Services 한국 블로그](https://aws.amazon.com/ko/blogs/korea/new-amazon-aurora-i-o-optimized-cluster-configuration-with-up-to-40-cost-savings-for-i-o-intensive-applications/)
* [실시간 복제 데이터를 이관시키는 방법. 안녕하세요. 스테이지랩스(STAYGE Labs) Back-End 팀… | by Victor Kang | staygelabs | May, 2023 | Medium](https://medium.com/stayge-labs/%EC%8B%A4%EC%8B%9C%EA%B0%84-%EB%B3%B5%EC%A0%9C-%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%A5%BC-%EC%9D%B4%EA%B4%80%EC%8B%9C%ED%82%A4%EB%8A%94-%EB%B0%A9%EB%B2%95-498d3d52c8b4) migration DynamoDB to Aurora PostgreSQL
* [The growing pains of database architecture](https://www.figma.com/blog/how-figma-scaled-to-multiple-databases/)
  * Amazon RDS에서 단일 Postgres 데이터베이스를 사용하고 있던 Figma가 더는 하나의 데이터베이스로 서비스하기 어려워서 점진적으로 개선해 나간 과정을 정리한 글
  * Figma는 2022년까지 Amazon RDS Postgres 데이터베이스 사용, CPU 사용률 65%
    * 이 문제를 완화하기 위해 일단 데이터베이스의 사용을 올리고 읽기 리플리카를 만든 뒤 PgBouncer를 추가해서 연결 수 제어
    * 하지만 부하의 상당 부분이 쓰기와 관련되어 있었고 복제 지연시간 때문에 모든 읽기를 리플리카로 옮길 수 있는 상황도 아님
  * 수평 확장이 되는 NoSQL이나 Vitess 등을 고려했지만
    * 애플리케이션 수정도 많이 필요
    * 직접 운영에 필요한 관련 경험이 없었기 때문에
    * 매니지드 솔루션을 그대로 이용하고자 함
  * 데이터베이스를 테이블별로 수직 분할하기로 결정
    * 테이블 그룹을 자체 데이터베이스 베이스로 옮기기로 하고
    * 이 수직 파티셔닝은 원본 데이터베이스에 부담을 줄이면서 향후 테이블의 하위 집합을 수평으로 샤딩할 수 있는 장점
  * 문제는 파티셔닝이 쉬운지 여부
    * 테이블을 이동하면 트랜잭션이나 조인 등의 기능을 잃게 되므로
    * 애플리케이션 재작성하는 비용이 클 수 있음
  * Ruby에서 ActiveRecord를 사용하고 있었으므로
    * 런타임 유효성 검사기를 만들어서 같은 테이블 그룹을 참조하는 쿼리와 트랜잭션을 기록해서 파티셔닝의 후보로 만듦
  * 마이그레이션 중 가용성 영향을 1분 미만이면서 반복할 수 있고 파티션을 취소할 수 있는 요구사항을 맞추려면 직접 만드는 수밖에 없었음
  * 애플리케이션이 파티셔닝과 호환되도록 한 뒤 PgBouncer를 하나 더 추가해서 트래픽을 분할하여 호환성 검사를 하면서 서비스에 영향이 가게 하고 문제가 없으면 분리된 데이터베이스를 보게 함
  * 첫 작업에서 2개의 테이블을 옮기고 2022년 10월에는 50개의 테이블을 옮기면서 CPU 사용률은 10%까지 감소
* [PostgreSQL의 Fillfactor와 영향도 | AWS 기술 블로그](https://aws.amazon.com/ko/blogs/tech/postgresql_fillfactor/)
* [케이타운포유의 순간적인 스파이크 트래픽 대응을 위한 Amazon Aurora 오토스케일링 전략 | AWS 기술 블로그](https://aws.amazon.com/ko/blogs/tech/amazon-aurora-auto-scaling-strategy-for-ktown4u-global-spike-traffic-response/)
* [AWS RDS Aurora I/O-Optimized 적용 후기 – Lamanus' Archive](https://lamanus.kr/113)
* [Aurora DB 클러스터 역추적 - Amazon Aurora](https://docs.aws.amazon.com/ko_kr/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Managing.Backtrack.html)
  * [Aurora MySQL Immersion Day](https://catalog.workshops.aws/awsauroramysql/en-US/provisioned/backtrack/)
  * [Aurora MySQL Backtrack을 이용한 빠른 복구 방법 - 진교선 :: AWS Database Modernization Day 온라인](https://www.slideshare.net/awskorea/aurora-mysql-backtrack-aws-database-modernization-day)
  * [Amazon Aurora MySQL Backtrack을 이용한 빠른 복구 방법 - 진교선 :: AWS Database Modernization Day 온라인 - YouTube](https://www.youtube.com/watch?v=zSZVCdC3PFo)
* [Amazon Aurora를 애플리케이션 개발자가 사용하기 위한 10가지 팁 – 1부 | AWS 기술 블로그](https://aws.amazon.com/ko/blogs/tech/part-1-10-amazon-aurora-tips-for-application-developers/)
* [Amazon Aurora를 어플리케이션 개발자가 사용하기 위한 10가지 팁 – 2부 | AWS 기술 블로그](https://aws.amazon.com/ko/blogs/tech/part-2-10-amazon-aurora-tips-for-application-developers/)
* [Amazon CloudWatch를 이용한 Amazon Aurora I/O Optimized 기능에 대한 비용 절감 예상하기 | AWS 기술 블로그](https://aws.amazon.com/ko/blogs/tech/estimate-cost-savings-for-the-amazon-aurora-i-o-optimized-feature-using-amazon-cloudwatch/)
* [Amazon RDS for MySQL의 Active/Active 복제를 위한 Group Replication 플러그인 소개 | AWS 기술 블로그](https://aws.amazon.com/ko/blogs/tech/amazon-rds-for-mysql-active-active-group-replication-plugin/)
* [Aurora MySQL 업그레이드엔 블루/그린 배포 어때? | by Rocket | Jan, 2024 | 여기어때 기술블로그](https://techblog.gccompany.co.kr/aurora-mysql-%EC%97%85%EA%B7%B8%EB%A0%88%EC%9D%B4%EB%93%9C%EC%97%94-%EB%B8%94%EB%A3%A8%EA%B7%B8%EB%A6%B0-%EB%B0%B0%ED%8F%AC-%EC%96%B4%EB%95%8C-f13787974c95)
* [Oracle to AWS Aurora PG 1탄 (Shareplex AWS 전환 여정)](https://gsretail.tistory.com/53)
* [Oracle to AWS Aurora PG 2탄 !! (DB 이사가요~)](https://gsretail.tistory.com/54)
* [Oracle to AWS Aurora PG 3탄 개발자의 청천벽력 이야기](https://gsretail.tistory.com/52)
* [Amazon Aurora MySQL 버전 3으로 업그레이드 (MySQL 8.0 호환) | AWS 기술 블로그](https://aws.amazon.com/ko/blogs/tech/amazon-aurora-mysql-version-3-upgrade-mysql-8-0-compatability/)
* [로컬 인스턴스 스토리지를 사용하여 SQL Server용 Amazon RDS Custom에서 TempDB 성능 최적화 | AWS 기술 블로그](https://aws.amazon.com/ko/blogs/tech/optimize-tempdb-performance-in-amazon-rds-custom-for-sql-server-using-local-instance-storage/)
* [Amazon RDS: A Comprehensive Tutorial on AWS RDS with Hands-On Practice by Fanaticus - YouTube](https://www.youtube.com/watch?v=WMFc3D96tSE)
* [Amazon Aurora MySQL 버전 2(MySQL 5.7 호환)에서 버전 3(MySQL 8.0 호환)으로 업그레이드 체크리스트, 1부 | AWS 기술 블로그](https://aws.amazon.com/ko/blogs/tech/database-amazon-aurora-mysql-version-2-with-mysql-5-7-compatibility-to-version-3-with-mysql-8-0-compatibility-upgrade-checklist-part-1/)
* [Amazon Aurora MySQL 버전 2(MySQL 5.7 호환)에서 버전 3(MySQL 8.0 호환)으로 업그레이드 체크리스트, 2부 | AWS 기술 블로그](https://aws.amazon.com/ko/blogs/tech/database-amazon-aurora-mysql-version-2-with-mysql-5-7-compatibility-to-version-3-with-mysql-8-0-compatibility-upgrade-checklist-part-2/)
* [Amazon Aurora MySQL 3버전(MySQL 8.0 호환)의 블루/그린 배포를 통한 업그레이드 시 권장 확인 사항 | AWS 기술 블로그](https://aws.amazon.com/ko/blogs/tech/amazon-aurora-mysql3-mysql-8-0-blue-green-deployment-upgrade/)
* [Sendbird의 Amazon Aurora MySQL 에서의 대용량 테이블 스키마 변경을 위한 SB-OSC 개발 및 적용 사례 | AWS 기술 블로그](https://aws.amazon.com/ko/blogs/tech/how-sendbird-developed-and-applied-sb-osc-for-very-large-amazon-aurora-mysql-operations/)
* [Amazon Aurora MySQL 버전 3의 바이너리 로깅을 이용한 최적화 | AWS 기술 블로그](https://aws.amazon.com/ko/blogs/tech/binary-logging-optimizations-in-amazon-aurora-mysql-version-3/)
* [Amazon Aurora MySQL 스토리지 공간 활용도 이해하기 | AWS 기술 블로그](https://aws.amazon.com/ko/blogs/tech/understanding-amazon-aurora-mysql-storage-space-utilization/)
* [Amazon Aurora MySQL 블루/그린 배포 전환 후 롤백 전략 구현 | AWS 기술 블로그](https://aws.amazon.com/ko/blogs/tech/implement-a-rollback-strategy-after-an-amazon-aurora-mysql-blue-green-deployment-switchover/)
* [Amazon Aurora Blue/Green Deployment를 활용하여 애플리케이션 계층을 포함한 데이터베이스 변경 사전 테스트하기 | AWS 기술 블로그](https://aws.amazon.com/ko/blogs/tech/pretesting-database-changes-including-application-with-amazon-aurora-blue-green-deployments/)
  * Amazon Aurora Blue/Green Deployment는 애플리케이션 계층을 포함한 데이터베이스 변경의 사전 테스트를 가능하게 하는 효과적인 방법
  * 이 플랫폼은 CQRS 패턴, Amazon Route53의 트래픽 흐름 및 트래픽 정책, 그리고 블루/그린 배포를 활용하여 프로덕션 환경에서 현실적인 테스트 수행
  * 사전 테스트는 변경으로 인한 문제를 사전에 파악하고, 운영 전환의 안정성을 높이는 데 도움
  * 이 플랫폼은 애플리케이션 계층과의 긴밀한 연결을 인식하여 데이터베이스 관리자와 개발자가 함께 테스트를 수행하도록 지원
* [Load vector embeddings up to 67x faster with pgvector and Amazon Aurora | AWS Database Blog](https://aws.amazon.com/blogs/database/load-vector-embeddings-up-to-67x-faster-with-pgvector-and-amazon-aurora/)
* [Amazon Bedrock과 프롬프트 엔지니어링을 활용한 보안성 높은 RAG 애플리케이션 구축하기 | AWS 기술 블로그](https://aws.amazon.com/ko/blogs/tech/secure-rag-applications-using-prompt-engineering-on-amazon-bedrock/)
* [Distributed SQL Databases - Amazon Aurora DSQL - AWS](https://aws.amazon.com/ko/rds/aurora/dsql/)
  * [Introducing Amazon Aurora DSQL | AWS Database Blog](https://aws.amazon.com/ko/blogs/database/introducing-amazon-aurora-dsql/)
  * [Concurrency control in Amazon Aurora DSQL | AWS Database Blog](https://aws.amazon.com/ko/blogs/database/concurrency-control-in-amazon-aurora-dsql/)
  * [AWS가 SQL DB의 한계를 부셔버렸네요. Serverless SQL DB 서비스 : Aurora DSQL을 소개합니다. - YouTube](https://www.youtube.com/watch?v=TGQuSrePOPU)

# Book
* [SQL 전문가 되어보기](https://wikidocs.net/book/159)
* [SQLite로 가볍게 배우는 데이터베이스](https://wikidocs.net/book/1530)
* [더북(TheBook): 오라클 SQL과 PL/SQL을 다루는 기술](https://thebook.io/006696/)
* [더북(TheBook): SQL 코딩의 기술](https://thebook.io/006882/) 1~3장만
* [더북(TheBook): 모두의 SQL](https://thebook.io/006977/)
* [더북(TheBook): 누구나 쉽게 SQL](https://thebook.io/080202/)
* [Readings in Database Systems, 5th Edition](http://www.redbook.io/)
* [SQL Indexing and Tuning e-Book for developers: Use The Index, Luke covers Oracle, MySQL, PostgreSQL, SQL Server, ...](https://use-the-index-luke.com/)
* [PostgreSQL 14 Internals : Postgres Professional](https://postgrespro.com/community/books/internals)
* [PostgreSQL 14 Internals, Part II : Postgres Professional](https://postgrespro.com/blog/pgsql/5969682)

# Conference
* [VDTRIESTE24 Going beyond ORMs - Conference by Andres Almiray - YouTube](https://www.youtube.com/watch?v=dRU_5SNy-FY)
  * [VidiGo VDTRIESTE24 Going beyond ORMs - Conference by An](https://vidigo.ai/share/summary/03fbe79e9151)
  * [VDTRIESTE24 ORM을 넘어서 - 안드레스 알미레이의 컨퍼런스 | 완벽한 영상요약, 릴리스에이아이 | Lilys AI](https://lilys.ai/digest/740557)

# Database
* [joinc](http://www.joinc.co.kr/modules/moniwiki/wiki.php/Site/Database)
* [A Database Model for Simple Board Games](http://www.vertabelo.com/blog/technical-articles/a-database-model-for-simple-board-games)
* [DB/분산 초보자를 위한 CAP 이론](http://hamait.tistory.com/197)
* [Paper: OLTP Through the Looking Glass, and What We Found There](http://blog.lastmind.io/archives/896)
* [Paper: Main Memory Database Systems: An Overview](http://blog.lastmind.io/archives/899)
* [Paper: Staring into the Abyss: An Evaluation of Concurrency Control with One Thousand Cores](http://blog.lastmind.io/archives/903)
* [Paper: Fast Serializable Multi-Version Concurrency Control for Main-Memory Database Systems – The Last Mind](http://blog.lastmind.io/archives/941)
* [Foundations of Databases](http://webdam.inria.fr/Alice/)
* [1 ~ 4세대 DBMS로 보는 데이터베이스 발전 과정과 양상에 대해 정리하기 | by Ryan Kim | Jul, 2021 | Medium](https://equus3144.medium.com/1-4%EC%84%B8%EB%8C%80-dbms%EB%A1%9C-%EB%B3%B4%EB%8A%94-%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%B2%A0%EC%9D%B4%EC%8A%A4-%EB%B0%9C%EC%A0%84-%EA%B3%BC%EC%A0%95%EA%B3%BC-%EC%96%91%EC%83%81%EC%97%90-%EB%8C%80%ED%95%B4-%EC%A0%95%EB%A6%AC%ED%95%98%EA%B8%B0-b94c1d93914d)
* [15 futuristic databases you’ve never heard of - YouTube](https://www.youtube.com/watch?v=jb2AvF8XzII)
* [Do You Even Need a Database?](https://www.dbpro.app/blog/do-you-even-need-a-database)
  * [Do You Even Need a Database? | GeekNews](https://news.hada.io/topic?id=28587)
  * 대부분의 초기 제품에는 DB가 불필요하며, 플랫 파일·인메모리 해시맵·바이너리 서치만으로도 수억 DAU까지 커버 가능. DB는 조인·다중 조건 검색·동시 쓰기·트랜잭션이 필요할 때 도입

# DuckDB
* [Announcing DuckDB 1.0.0 – DuckDB](https://duckdb.org/2024/06/03/announcing-duckdb-100.html)
  * [DuckDB 1.0.0 릴리즈 | GeekNews](https://news.hada.io/topic?id=15160)
* [DuckDB is an in-process SQL OLAP Database Management System](https://github.com/duckdb/duckdb)
* [Eduardo Blancas - Using embedded SQL engines for plotting massive datasets on a laptop - YouTube](https://www.youtube.com/watch?v=M2hoEYXkBa8) sqlite
* [FOSDEM 2023 - DuckDB In The Python Land - Pedro Holanda - YouTube](https://www.youtube.com/watch?v=-rCZQHXSunc)
* [DuckDB: Bringing analytical SQL directly to your Python shell — Pedro Holanda - YouTube](https://www.youtube.com/watch?v=dVzfNZN9NKI)
* [Comparing SQLite, DuckDB and Arrow with UN Trade Data · Pachá](https://pacha.dev/blog/2021/08/27/comparing-sqlite-duckdb-and-arrow-with-un-trade-data/)
* [DuckDBT: Not a database or a dbt adapter but a secret third thing – DuckCon #3 (San Francisco) - YouTube](https://www.youtube.com/watch?v=NQmOiEJ8fEs)
* [Gábor Szárnyas - DuckDB: The Power of a Data Warehouse in your Python Process - YouTube](https://www.youtube.com/watch?v=q_SKaOeRiOI)
* [DuckDB Doesn’t Need Data To Be a Database](https://www.nikolasgoebel.com/2024/05/28/duckdb-doesnt-need-data.html)
  * [데이터 없이도 데이터베이스가 되는 DuckDB | GeekNews](https://news.hada.io/topic?id=15093)
* [DuckDB as the New jq - Paul Gross’s Blog](https://www.pgrs.net/2024/03/21/duckdb-as-the-new-jq/)
  * [새로운 jq로서의 DuckDB | GeekNews](https://news.hada.io/topic?id=13948)
* [DuckDB 사용법(DuckDB Python + Jupyter Lab) · 어쩐지 오늘은](https://zzsza.github.io/data-engineering/2024/10/25/duckdb/)
  * [DuckDB 사용법(DuckDB Python + Jupyter Lab) | GeekNews](https://news.hada.io/topic?id=17450)
* [pandas vs Polars vs DuckDB: A Data Scientist's Guide to Choosing the Right Tool | CodeCut](https://codecut.ai/pandas-vs-polars-vs-duckdb-comparison/)
* [DuckLake: SQL as a Lakehouse Format – DuckDB](https://duckdb.org/2025/05/27/ducklake.html)
* [Unleashing the Power of DuckDB: A Modern Analytical Database Engine | Barani Dakshinamoorthy](https://kr.linkedin.com/pulse/unleashing-power-duckdb-modern-analytical-database-dakshinamoorthy-j6hie)
  * DuckDB의 주요 활용법 종합 가이드. 로컬 인메모리 분석, MotherDuck 클라우드 배포, Streamlit·Apache Superset 연동, ML 데이터 전처리까지. 라이선스 비용 없이 ad-hoc 분석부터 프로덕션 파이프라인까지 커버

# Library
* [alasql.org](http://alasql.org/)
* [Arctype | The fast and easy-to-use SQL client](https://arctype.com/)
* [awesome-db-tools: Everything that makes working with databases easier](https://github.com/mgramin/awesome-db-tools)
* [bytebase: Web-based, zero-config, dependency-free database schema change and version control tool for teams. Public demo: https://demo.bytebase.com ](https://github.com/bytebase/bytebase)
  * [Bytebase - 웹 기반 DB스키마 변경 및 버전 관리도구 오픈소스 | GeekNews](https://news.hada.io/topic?id=4793)
* [ChartDB - Database schema diagrams visualizer](https://chartdb.io/)
  * [ChartDB - 무료/오픈소스 DB 디자인 편집기 | GeekNews](https://news.hada.io/topic?id=16518)
* [cozo: A general-purpose, transactional, relational database that uses Datalog and focuses on graph data and algorithms](https://github.com/cozodb/cozo)
* [dataherald: Interact with your SQL database, Natural Language to SQL using LLMs](https://github.com/Dataherald/dataherald)
  * [Dataherald - 자연어-to-SQL 엔진, 전체 오픈소스로 전환 | GeekNews](https://news.hada.io/topic?id=15008)
* [DBCore - Rapidly prototype applications powered by your database](https://www.dbcore.org/)
  * [DBCore - DB기반으로 빠르게 프로토타입 앱 생성하는 오픈소스 | GeekNews](https://news.hada.io/topic?id=5366)
* [**dbcrossbar** - an open source tool that copies large, tabular datasets between many different databases and storage formats. Data can be copied from any source to any destination](https://www.dbcrossbar.org/)
* dbdb.io [**Home - Database of Databases**](https://dbdb.io/)
* [DBeaver](https://dbeaver.io/)
  * [Mac, Linux 에서 쓸만한 DB Tool - DBeaver](http://lifeones.tistory.com/129)
  * [데이터베이스 연결 도구 - DBeaver 설치](https://jybaek.tistory.com/858)
  * [`Failed to create the Java Virtual Machine`](https://gist.github.com/hyunjun/7de243f9871514fa4aa7e8c3b0d00f97)
  * [.ini 파일 설정](https://baekjungho.github.io/database-dbeaverini/)
  * [#Docker | DBeaver for Data Import | #PostgreSQL #DBeaver #Database #디비버 - YouTube](https://www.youtube.com/watch?v=pflNgrCiBE8)
* [dblab: The database client every command line junkie deserves](https://github.com/danvergara/dblab)
  * [Dblab - 인터랙티브한 터미널용 DB 클라이언트 | GeekNews](https://news.hada.io/topic?id=15284)
* [DBLog: A Generic Change-Data-Capture Framework | by Netflix Technology Blog | Netflix TechBlog](https://netflixtechblog.com/dblog-a-generic-change-data-capture-framework-69351fb9099b)
* [db_seeder: Relational database data generator..](https://github.com/KonnexionsGmbH/db_seeder)
* [DbSchema – Database Design & Management Tool for Teams](https://dbschema.com/)
  * [Visual Database Design and Management Tool - DbSchema - YouTube](https://www.youtube.com/watch?v=IjWRQ7qfLhg)
* [Dolt – It's Git for Data](https://github.com/dolthub/dolt)
* [dqlite: Embeddable, replicated and fault tolerant SQL engine](https://github.com/canonical/dqlite)
* [dsq: Commandline tool for running SQL queries against JSON, CSV, Excel, Parquet, and more](https://datastation.multiprocess.io/blog/2022-01-11-dsq.html)
* [dungbeetle: A distributed job server built specifically for queuing and executing heavy SQL read jobs asynchronously. Separate out reporting layer from apps. MySQL, Postgres, ClickHouse](https://github.com/zerodha/dungbeetle)
* ERD
  * [ERD 다이어그램 툴 종류와 설치 경로 정리](http://gomcine.tistory.com/entry/ERD-%EB%8B%A4%EC%9D%B4%EC%96%B4%EA%B7%B8%EB%9E%A8-%ED%88%B4-%EC%A2%85%EB%A5%98%EC%99%80-%EC%84%A4%EC%B9%98-%EA%B2%BD%EB%A1%9C-%EC%A0%95%EB%A6%AC)
  * [ERD (Entity-Relation Diagram) 표기법](https://hudi.blog/entity-relation-diagram/)
  * [AQueryTool은 웹 기반 ERD 툴 + SQL 자동 생성 프로그램](http://aquerytool.com/)
  * [dbdiagram - Draw Entity-Relationship Diagrams, Painlessly](https://dbdiagram.io/)
  * [DBML: Database Markup Language · /usr/lib/libsora.so](https://libsora.so/posts/dbml-entity-relation-diagram-as-code/)
  * [erdplus.com](https://erdplus.com)
  * [SequenceDiagram.org - UML Sequence Diagram Online Tool](https://sequencediagram.org/)
* [falcon - Free, open-source SQL client for Windows and Mac](https://github.com/plotly/falcon)
* [fdap: This a repository on the Apache Flight, Datafusion, Arrow and Parquet ecosystem](https://github.com/bgachara/fdap)
  * [Building Modern Databases with the FDAP Stack • Andrew Lamb & Olimpiu Pop • GOTO 2025 - YouTube](https://www.youtube.com/watch?v=Gd-mhbiy8Vo)
    * [현대 데이터베이스 구축: FDAP 스택 • GOTO 2025](https://livewiki.com/ko/content/fdap-stack-modern-databases)
* [Flyway - Version control for your database. Robust schema evolution across all your environments. With ease, pleasure and plain SQL](https://flywaydb.org/)
* [ggsql: A grammar of graphics for SQL](https://ggsql.org/)
  * [ggsql: A grammar of graphics for SQL | Posit](https://opensource.posit.co/blog/2026-04-20_ggsql_alpha_release/)
  * [ggsql - SQL을 위한 그래픽 문법 | GeekNews](https://news.hada.io/topic?id=28742)
  * SQL 쿼리에 VISUALIZE·DRAW·PLACE 등 시각화 절을 추가해 Grammar of Graphics 기반 차트 생성. ggplot2 18년 경험을 살린 선언적 DSL, 런타임 의존성 없는 경량 바이너리
* goose [Overview - pressly/goose](https://pressly.github.io/goose/)
* [Harlequin: The SQL IDE for Your Terminal](https://harlequin.sh/)
* [ingestr: ingestr is a CLI tool to copy data between any databases with a single command seamlessly](https://github.com/bruin-data/ingestr)
  * [ingestr - 명령 하나로 DB간 데이터를 복사해주는 CLI 도구 | GeekNews](https://news.hada.io/topic?id=13578)
* [Instant SQL Formatter](http://www.dpriver.com/pp/sqlformat.htm)
  * [SQL문의 가독성을 높여주는 웹사이트 소개 feat.instant SQL formatter](https://stricky.tistory.com/154)
* Jailer [Open Jail - The Jailer Project Web Site](https://wisser.github.io/Jailer/)
* Jetbrains
  * [DataGrip 팁 모음](http://ohgyun.com/770)
  * [코딩 효율 개선에 도움이 되는 DataGrip 단축키 10가지 | The DataGrip Blog](https://blog.jetbrains.com/ko/datagrip/2022/06/13/top-10-datagrip-shortcuts-to-empower-your-coding/)
  * [JetBrains Rider에서의 데이터베이스 작업 수행](https://blog.jetbrains.com/kr/2020/03/working-with-databases-in-jetbrains-rider/)
  * [DataGrip 살펴 보기 - Yun Blog | 기술 블로그](https://cheese10yun.github.io/data-grip/)
  * [DataGrip 에서 안전하게 Command 수행하기](https://jojoldu.tistory.com/707)
* [malloy: Malloy is an experimental language for describing data relationships and transformations](https://github.com/looker-open-source/malloy)
  * [Malloy - 더 나은 SQL by Looker | GeekNews](https://news.hada.io/topic?id=5840)
* migration
  * [flyway - Evolve your Database Schema easily and reliably across all your instances](https://flywaydb.org/) plain SQL 사용
  * [liquibase.org - source control for your database](http://www.liquibase.org/)  xml 작성, rollback 지원
* [orbit-db - Peer-to-Peer Databases for the Decentralized Web](https://github.com/orbitdb/orbit-db)
* [prql: PRQL is a modern language for transforming data — a simple, powerful, pipelined SQL replacement](https://github.com/prql/prql)
  * [PRQL - 데이터 변환을 위한 더 간단하고 강력한 SQL 제안 | GeekNews](https://news.hada.io/topic?id=5853)
* [qStudio Release Version 3.0 » qStudio](https://www.timestored.com/qstudio/release-version-3)
  * [Show HN: qStudio - 10년간 개발한 무료 SQL Editor | GeekNews](https://news.hada.io/topic?id=15162)
* [**RadonDB: 대륙의 뉴타입 슈주쿠(Shùjùkù, 数据库, database) !?**](https://www.popit.kr/%EB%8C%80%EB%A5%99%EC%9D%98-%EB%89%B4%ED%83%80%EC%9E%85-%EC%8A%88%EC%A3%BC%EC%BF%A0shujuku-%E6%95%B0%E6%8D%AE%E5%BA%93-database/) MySQL or PostgreSQL 기반의 분산 데이터베이스 이야기
* [Readyset is a MySQL and Postgres wire-compatible caching layer that sits in front of existing databases to speed up queries and horizontally scale read throughput. Under the hood, ReadySet caches the results of cached select statements and incrementally updates these results over time as the underlying data changes](https://github.com/readysettech/readyset)
  * [ReadySet - MySQL/Postgres를 위한 투명한 데이터베이스 캐시 레이어 | GeekNews](https://news.hada.io/topic?id=13468)
* [Rel – The desktop relational database management system](https://reldb.org/c/)
* [Replibyte - 개발DB를 실제 데이터로 채우는 도구 | GeekNews](https://news.hada.io/topic?id=6488)
* [Rockset - a scalable, reliable search and analytics service in the cloud that makes it easy to build fast operational applications on TBs of data simply using SQL](https://rockset.com)
  * [Complex SQL on Excel Spreadsheets - Studying Trends in Federal Pell Grant Data](https://towardsdatascience.com/complex-sql-on-excel-spreadsheets-274bc93ade89)
* [sequel fumpt - Type some SQL. Move the slider to set output width](https://sqlfum.pt/)
  * [sqlfmt: an opinionated online SQL formatter](https://www.cockroachlabs.com/blog/sql-fmt-online-sql-formatter/)
* [SpacetimeDB](https://spacetimedb.com/)
  * [1000X Faster Than PostgreSQL?! - YouTube](https://www.youtube.com/watch?v=k7ZemI82Qxs)
* [**sq: swiss-army knife for data**](https://sq.io/) jq for relational data
  * [SQ - swiss-army knife for data | GeekNews](https://news.hada.io/topic?id=3841)
* [sqitch: Sensible database change management](https://github.com/sqitchers/sqitch)
* [sqldef.github.io](https://sqldef.github.io/)
  * [sqldef: Idempotent schema management for MySQL, PostgreSQL, SQLite, and SQL Server](https://github.com/sqldef/sqldef)
  * [Sqldef: MySQL, PostgreSQL, SQLite용 멱등적 스키마 관리 도구 | GeekNews](https://news.hada.io/topic?id=26557)
* [sqlglot: Python SQL Parser and Transpiler](https://github.com/tobymao/sqlglot)
* [sqlfluff](https://www.sqlfluff.com/) The SQL Linter for humans
* [SQLPad - A web app for writing and running SQL queries and visualizing the results. Supports Postgres, MySQL, SQL Server, ClickHouse, Crate, Vertica, Presto, SAP HANA, Snowflake, BigQuery, SQLite, and many others via ODBC](https://rickbergfalk.github.io/sqlpad/#/)
* [SQL Translation - Translate your SQL from one dialect to another](https://www.jooq.org/translate/)
* Teleport [Introducing Database Access | Teleport](https://goteleport.com/blog/introducing-database-access/) NAT
* table_ddl [mariadb mysql 특정 스키마 테이블 ddl 추출 프로그램 배포](https://stricky.tistory.com/468)
* [TigerBeetle - 1000x Faster Financial Transactions (OLTP) Database](https://tigerbeetle.com/)
  * [The FASTEST and SAFEST Database - YouTube](https://www.youtube.com/watch?v=sC1B3d9C_sI)
* [Trino | Distributed SQL query engine for big data](https://trino.io/)
  * [Trino | Why leaving Facebook/Meta was the best thing we could do for the Trino Community](https://trino.io/blog/2022/08/02/leaving-facebook-meta-best-for-trino.html)
    * 페이스북에서 만든 Presto의 초기 멤버들이 페이스북을 나와서 Trino로 리브랜딩하고 Trino 재단을 만들었는데 그게 왜 좋은 결정이었는지를 설명한 글
    * Presto를 처음 오픈소스로 릴리스한 2012년은 Facebook이 IPO 하기 전, 오픈소스로 프로젝트를 오픈하는 데 문제가 없었음
    * 사람들은 커뮤니티를 만들지 회사를 만드는 게 아니고 회사는 목표 자체가 커뮤니티와는 다름
    * 오픈소스는 "누구도 특별하지 않다"는 엄격한 정책이 있지만
    * Facebook 내에서 Prestor가 중요한 프로젝트가 되면서 승인/성과를 위해서 프로젝트의 커밋 권한을 받으려고 함
    * 처음에 한 실수는 Presto라는 이름의 애정이 있어서 이름을 바꾸지 않으려고 했고
    * 페이스북도 Presto가 커뮤니티 소속이라는 합의가 있다고 믿었지만 실제로는 커뮤니티가 나가자 페이스북의 소유가 됨
    * 그래서 페이스북을 나와야 했고 Trino로 리브랜딩해서 홍보도 새로 해야 했지만 그래도 커뮤니티의 힘을 믿었고 빠르게 스타도 증가
* [usql - Universal command-line interface for SQL databases](https://github.com/xo/usql)
* [UXSql Application Builder](https://www.notion.so/UXSql-Application-Builder-18857e102ca54c37b4e5f887f68f3a55) MSSQL, MySQL 가능
* VisualSQL [We Made SQL Visual - Why and How](https://chartio.com/blog/why-we-made-sql-visual-and-how-we-finally-did-it/)
* [**Waltz: A Distributed Write-Ahead Log**](https://wecode.wepay.com/posts/waltz-a-distributed-write-ahead-log)
* [whodb: A lightweight next-gen data explorer - Postgres, MySQL, SQLite, MongoDB, Redis, MariaDB, Elastic Search, and Clickhouse with Chat interface](https://github.com/clidey/whodb)
  * [Clidey WhoDB](https://whodb.clidey.com/)
  * [WhoDB - 가볍고 강력한 데이터베이스 관리 도구 | GeekNews](https://news.hada.io/topic?id=18872)
* [YDB — an open-source Distributed SQL Database](https://ydb.tech/)
* [Yugabyte Cloud - Yugabyte](http://www.yugabyte.com/cloud/)
  * [Yugabyte Cloud: a Managed Distributed SQL Database](https://www.infoq.com/news/2021/10/yugabyte-cloud/)

# MariaDB
* [HowTo: Install ClusterControl to Provision, Monitor and Manage MariaDB/Percona MariaDB MySQL Cluster](http://cloudstats.me/2015/08/13/howto-install-clustercontrol-from-severalnines-for-easy-mysql-galera-cluster-management/)
* [How to Install MariaDB on Ubuntu 18.04](https://linuxize.com/post/how-to-install-mariadb-on-ubuntu-18-04/)
* [Call me Maybe: MariaDB Galera Cluster](https://aphyr.com/posts/327-call-me-maybe-mariadb-galera-cluster)
  * [Clarification on “Call me Maybe: MariaDB Galera Cluster”](https://www.percona.com/blog/2015/09/17/clarification-call-maybe-mariadb-galera-cluster/)
* [Spring 4 + MyBatis 3 + MariaDB (Maven) 기반 게시판 예제](http://forest71.tistory.com/2)
  * [Project9 - Spring 4 + MyBatis 3 + MariaDB (Maven) 기반으로 제작한 웹 프로젝트 템플릿](http://forest71.tistory.com/78)
* [빌링 시스템 장애, 이러지 말란 Maria~ | 우아한형제들 기술블로그](https://techblog.woowahan.com/2517/)
* [MariaDB에서 서브쿼리 인덱스 걸기](http://bomdol.tistory.com/347)
* [Spider Storage Engine Overview](https://mariadb.com/kb/en/library/spider-storage-engine-overview/) with built-in sharding features
* [How to migrate from Oracle Database with ease](https://www.slideshare.net/MariaDB/how-to-migrate-from-oracle-database-with-ease)
* ["SELECT COUNT(\*)" 수행 속도 문제](https://blog.naver.com/birdparang/221574304831)
* [MariaDB 설치 및 설정](https://jojoldu.tistory.com/461)
* [MariaDB에서 root 암호 인증 방식이 먹히지 않는 이유(feat. unix_socket)](http://jhrogue.blogspot.com/2020/02/b-mariadb-root-feat-unixsocket.html)
* [Authentication from MariaDB 10.4](https://mariadb.com/kb/en/authentication-from-mariadb-104/)
* [Less passwords, more security: unix socket authentication and other MariaDB hardening tips](https://www.slideshare.net/ottokekalainen/less-passwords-more-security-unix-socket-authentication-and-other-mariadb-hardening-tips)
* [Observability Differences Between MySQL 8 and MariaDB 10.4](https://www.percona.com/blog/2020/02/05/observability-differences-between-mysql-8-and-mariadb-10-4/)
* [Streaming backups in parallel using tee | DBA Dojo](https://dbadojo.com/2020/09/02/streaming-backups-in-parallel-using-tee/)
* [팁 MariaDB 사용자별 최대 쿼리 실행 시간 다르게 주기 :: 자바캔(Java Can Do IT)](https://javacan.tistory.com/entry/tip-mariadb-max-statement-time-per-user)
* [Logging all MariaDB and MySQL queries into the Slow Log - Vettabase](https://vettabase.com/blog/logging-all-mariadb-and-mysql-queries-into-the-slow-log/)
* [마리아DB 파티션 테이블+자동 증가 칼럼 대박 버그 :: 자바캔(Java Can Do IT)](https://javacan.tistory.com/entry/%EB%A7%88%EB%A6%AC%EC%95%84DB-%ED%8C%8C%ED%8B%B0%EC%85%98-%ED%85%8C%EC%9D%B4%EB%B8%94%EC%9E%90%EB%8F%99-%EC%A6%9D%EA%B0%80-%EC%B9%BC%EB%9F%BC-%EB%8C%80%EB%B0%95-%EB%B2%84%EA%B7%B8)
* [미친 라이브 데모를 통해 보는Write-Scale Out MariaDB Xpand (10 node cluster)](https://www.allshowtv.com/detail.html?idx=749)
* [mariadb procedure exception 처리 예제](https://stricky.tistory.com/522)
* [MariaDB vs MySQL - 호환성/포크된 이유/주요 차이점 비교 | GeekNews](https://news.hada.io/topic?id=232)
* [mariadb instr 함수 커스트마이징 하기 (오라클 버전 파라미터 적용)](https://stricky.tistory.com/523)
* [#MariaDB - 데이터베이스(DB) 초기화](https://velog.io/@discphy/MariaDB-%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%B2%A0%EC%9D%B4%EC%8A%A4DB-%EC%B4%88%EA%B8%B0%ED%99%94)
* [가난한 자의 MariaDB 프로시저 로깅 · 감자도스](https://blog.potados.com/dev/poor-mans-procedure-logging-in-mariadb/)
* [Authentication Plugin - Unix Socket](https://mariadb.com/kb/en/authentication-plugin-unix-socket/)
* CDC
  * [mariadb-cdc로 MariaDB CDC 사용하기 :: 자바캔(Java Can Do IT)](https://javacan.tistory.com/entry/mariadb-cdc-intro)
  * [개밥 먹기 : MariaDB(MySQL) CDC 모듈 직접 개발하고 사용하기 1년 :: 자바캔(Java Can Do IT)](https://javacan.tistory.com/entry/dogfooding-dev-and-use-mariadb-mysql-CDC-module)
* [ClustrixDB](https://mariadb.com/products/clustrixdb/) distributed RDB
* Galera [DIAMANTI Use Case : MariaDB with Galera Cluster | by Simon.kim | Mar, 2021 | Medium](https://knk1034.medium.com/diamanti-use-case-mariadb-with-galera-cluster-f921402ff282)
* SkySQL [Jacob's Cafe :: 수십억건 데이터 처리를 위한 MariaDB Analytics (SkySQL)](https://calebpro.tistory.com/628)
* [Testcontainers로 Mariadb 연동 통합 테스트하기 :: 자바캔(Java Can Do IT)](https://javacan.tistory.com/entry/mariadb-integration-test-using-testcontainers)

# MSSQL MS SQL
* [practice - case when](https://gist.github.com/hyunjun/ac68186c394a0f4bb882b48fca9fd27a#file-case_when-md)
* [practice - top 1 to read the latest row](https://gist.github.com/hyunjun/ac68186c394a0f4bb882b48fca9fd27a#file-top_1-md)
* [practice - troubleshooting](https://gist.github.com/hyunjun/ac68186c394a0f4bb882b48fca9fd27a)
* [User Defined Stored Procedures in SQL](https://www.datacamp.com/community/tutorials/user-defined-stored-procedure)
* [저장 프로시저 (Stored Procedure) 란?](https://devkingdom.tistory.com/323)
* [Install SQL Server on Ubuntu](https://docs.microsoft.com/en-us/sql/linux/sql-server-linux-setup-ubuntu)
* [SQL Server 에게 String 이란? (NVARCHAR 인가 VARCHAR 인가) | 우아한형제들 기술블로그](https://techblog.woowahan.com/2605/)
* [SQL Server Tutorial](https://www.techonthenet.com/sql_server/index.php)
* [Some Aspects of MS SQL Server Monitoring. Part 1](https://hackernoon.com/some-aspects-of-ms-sql-server-monitoring-part-1-b6e67b313f6f)
* [임시테이블, 테이블변수 간 성능이슈](https://hackhyun.tistory.com/276)
* [토크ON세미나 47차. SQL 데이터분석 입문 | T아카데미](https://www.youtube.com/playlist?list=PL9mhQYIlKEheDlm4xo7xHbOLodw1VwLcL)
* [쿼리 수행시간 확인방법](https://blog.naver.com/smonone/221508523991)
* [Docker + MSSQL 개발하기](https://hyesunzzang.tistory.com/91)
* [SQL서버 커밋할 수 없는 트랜잭션](https://hackhyun.tistory.com/288)
* [MSSQL Server Tutorial For beginners - Techringe](https://www.techringe.com/mssql-server-tutorial-for-beginners/)
* [SQL서버 VALUES의 다양한 용법(테이블 값 생성자) :: 전산이야기](https://hackhyun.tistory.com/295)
* [맥북 docker 에 mssql 설치 하기](https://stricky.tistory.com/500)
* [신입 개발자, DB를 최적화 하다! 1편. 소개 | by Jason Kang | Uniquegood | Sep, 2021 | Medium](https://medium.com/uniquegood/%EC%BD%94%EC%96%B4-%EC%84%9C%EB%B2%84%EC%97%90-%EC%83%9D%EA%B8%B0%EB%8A%94-%EB%AC%B8%EC%A0%9C%EC%A0%90%EC%9D%84-%ED%95%B4%EA%B2%B0%ED%95%98%EC%9E%90-1%ED%8E%B8-55b899e0fbdd)
* [신입 개발자, DB를 최적화 하다! 2편. 소개 | by Jason Kang | Uniquegood | Sep, 2021 | Medium](https://medium.com/uniquegood/%EC%8B%A0%EC%9E%85-%EA%B0%9C%EB%B0%9C%EC%9E%90-db%EB%A5%BC-%EC%B5%9C%EC%A0%81%ED%99%94-%ED%95%98%EB%8B%A4-2%ED%8E%B8-c9f71951c90)
* [Intro to SQL - YouTube](https://www.youtube.com/watch?v=vbPw0tmQmws)
* [Improving Database Development, CI/CD with Storage Snapshot | by Kittikun Chartmala | Agoda Engineering & Design | Feb, 2022 | Medium](https://medium.com/agoda-engineering/improving-database-development-ci-cd-with-storage-snapshot-799765fd3fa9)
* [SQLServer JDBC의 이상한 동작](http://www.popit.kr/sqlserver-jdbc%EC%9D%98-%EC%9D%B4%EC%83%81%ED%95%9C-%EB%8F%99%EC%9E%91/)
* [날짜 참조 테이블 만들기 (매월 월요일 구하기.. : 네이버블로그](https://blog.naver.com/sqlmvp/220274628593)
* [Architect a disaster recovery for SQL Server on AWS: Part 1 | AWS Database Blog](https://aws.amazon.com/blogs/database/part-1-architect-a-disaster-recovery-for-sql-server-on-aws/)
  * [AWS에서 SQL Server를 위한 재해 복구 설계: 1부 | AWS 기술 블로그](https://aws.amazon.com/ko/blogs/tech/aws-based-sql-server-disaster-recovery-architecture-design-part1/)
* [Architect a disaster recovery for SQL Server on AWS: Part 2 | AWS Database Blog](https://aws.amazon.com/ko/blogs/database/part-2-architect-a-disaster-recovery-for-sql-server-on-aws/)
  * [AWS에서 SQL Server를 위한 재해 복구 설계: 2부 | AWS 기술 블로그](https://aws.amazon.com/ko/blogs/tech/aws-based-sql-server-disaster-recovery-architecture-design-part2/)
* [Architect a disaster recovery for SQL Server on AWS: Part 3 | AWS Database Blog](https://aws.amazon.com/blogs/database/part-3-architect-a-disaster-recovery-for-sql-server-on-aws/)
  * [AWS에서 SQL Server의 재해 복구 아키텍처 설계: Part3 | AWS 기술 블로그](https://aws.amazon.com/ko/blogs/tech/aws-based-sql-server-disaster-recovery-architecture-design-part3/)
* [Architect a disaster recovery for SQL Server on AWS: Part 4 | AWS Database Blog](https://aws.amazon.com/blogs/database/part-4-architect-a-disaster-recovery-for-sql-server-on-aws/)
  * [AWS에서 SQL Server를 위한 재해 복구 아키텍처 설계: 4부 | AWS 기술 블로그](https://aws.amazon.com/ko/blogs/tech/aws-based-sql-server-disaster-recovery-architecture-design-part4/)
* [database MSSQL 데이터베이스, EC2 우분투에 설치하고 SSMS로 접속하기 - 마도학자 로스카츠의 AI 머신러닝](https://losskatsu.github.io/database/mssql-ec2-ubuntu/)

# MySQL
* practice
  * [비개발자를 위한 MySQL](https://github.com/kciter/MySQLForNonDeveloper/blob/master/README.md)
  * [개발했더니 내 서재였던 건에 대하여 - 리디주식회사 RIDI Corporation](https://www.ridicorp.com/blog/2020/05/12/got-developed-as-a-my-library/)
  * [queries](https://gist.github.com/hyunjun/17e9b03a1b0faa38c662) 비밀번호 변경 등 기타 명령도 포함
    * [MySQL 비밀번호 분실, 초기화 방법 (DB관리자 필수로 알아둘 내용) - YouTube](https://www.youtube.com/watch?v=50dECqfg0xU)
  * [use case](https://gist.github.com/hyunjun/0d56ce004f1db78d4eff4d2842575581)
    * 분리된 table을 통합하는 과정에서의 경험
    * unique constraint에서 null을 사용하는 경우의 핵심
    * table에 존재하지 않는지 검사하고 입력하는 INSERT 구문
    * 다른 table에 존재하는 record 삭제하는 DELETE 구문
    * ON DUPLICATE KEY UPDATE와 IF를 사용한 입력
  * [MySQL: 테이블 이름 변경에 view 활용하기](https://ohgyun.com/789)
  * [MySQL 중복 데이터 제거 트러블 슈팅 - 현구막 기술 블로그](https://hyeon9mak.github.io/mysql-delete-duplicate-data-troubleshooting/)
  * [`date_trunc` 함수를 구현하자](https://walkingfox.tistory.com/175)
  * ALTER
    * [MySQL 테이블 수정](http://egloos.zum.com/kwon37xi/v/1635464)
    * [MySQL ALTER 명령을 이용한 테이블 변경](http://ra2kstar.tistory.com/3)
    * `ALTER TABLE [table name] RENAME [new table name]`
    * `ALTER TABLE [table name] ADD [column name] [type]`
    * [Unexpected slow ALTER TABLE in MySQL 5.7](https://www.percona.com/community-blog/2020/04/23/unexpected-slow-alter-table-mysql-5-7/)
    * [practice - create insert alter](https://gist.github.com/hyunjun/17e9b03a1b0faa38c662#file-create_insert_alter-md)
  * `COALESCE(<column name>, 0)` column 값이 NULL인 경우 0 출력
  * CREATE
    * `CREATE TABLE [table name] LIKE [org table name]; -- index까지 복사. 물론 데이터는 복사하지 않음`
    * `CREATE TABLE [table name] SELECT * FROM [org table name]; -- 데이터를 복사해서 만들지만 index를 복사하지는 않음`
  * INSERT
    * [13.2.5.2 INSERT ... ON DUPLICATE KEY UPDATE Syntax](https://dev.mysql.com/doc/refman/5.5/en/insert-on-duplicate.html)
    * [Mysql 의 Insert .. On Duplicate Key Update 유의사항](http://knight76.tistory.com/entry/Mysql-%EC%9D%98-Insert-On-Duplicate-Key-Update-%EC%9C%A0%EC%9D%98%EC%82%AC%ED%95%AD)
    * [Insert multiple records into MySQL with a single query](http://www.electrictoolbox.com/mysql-insert-multiple-records/)
    * [여러 행 SELECT해서 INSERT 하기 :: Outsider's Dev Story](https://blog.outsider.ne.kr/263)
    * [sql 독학 강의 # mysql insert 사용 방법 17편 -sTricky](https://stricky.tistory.com/268)
    * [MySQL 양방향 암호화 복호화 insert 및 select 예제](https://stricky.tistory.com/330)
    * [MySQL은 '따닥'을 어떻게 방어할까](https://velog.io/@wisepine/MySQL%EC%9D%80-%EB%94%B0%EB%8B%A5%EC%9D%84-%EC%96%B4%EB%96%BB%EA%B2%8C-%EB%B0%A9%EC%96%B4%ED%95%A0%EA%B9%8C)
  * [LOAD, mysqlimport](https://hyunjun.github.io/mysqlimport/)
    * [csv 파일을 직접 MySQL 테이블로 Import 하는 방법 (대용량 파일 import 팁)](http://moonlighting.tistory.com/140)
    * [MySql: LOAD DATA INFILE 로 대용량 데이터 인서트하기](http://ohgyun.com/777)
    * load data infile; 속도가 느림
      * `mysql -h xxx.yyy.zzz.www -u [user id] -p[password] [database] -N -e "LOAD DATA local infile \"./[data file]\" REPLACE INTO TABLE [table name] ([column1], [column2],...[columnN])"`
      * [13.2.7 LOAD DATA INFILE Syntax](http://dev.mysql.com/doc/refman/5.1/en/load-data.html)
      * [MySQL 파일을 이용하여 테이블에 값 삽입하기](http://ra2kstar.tistory.com/2)
    * [MySQL database 정보 import하기](http://tac.softonnet.com/troubleshoot/viewbody.php?code=troubleshoot&page=1&number=26&keyfield=category&key=db) mysqlimport
    * [MySQL: Import CSV, not using LOAD DATA | Die wunderbare Welt von Isotopp](https://blog.koehntopp.info/2020/09/28/mysql-import-csv-not-using-load-data.html)
    * [I loaded 100,000,000 rows into MySQL (fast) - YouTube](https://www.youtube.com/watch?v=rP0lZ_T5P28)
  * [LOAD_FILE() function](https://www.w3resource.com/mysql/string-functions/mysql-load_file-function.php)
  * RANK
    * [sql rank over 함수 알면 손쉽게 랭킹을 매길 수 있다](https://codingdog.tistory.com/entry/sql-rank-over-%ED%95%A8%EC%88%98-%EC%95%8C%EB%A9%B4-%EC%86%90%EC%89%BD%EA%B2%8C-%EB%9E%AD%ED%82%B9%EC%9D%84-%EB%A7%A4%EA%B8%B8-%EC%88%98-%EC%9E%88%EB%8B%A4)
  * [replace into & insert into 차이점, 주의할점이 무엇인지 쉽고 간단하게 확인하기](https://stricky.tistory.com/456)
  * SELECT
    * [`SELECT p.FirstName, p.LastName, a.City, a.State FROM Person p LEFT JOIN Address a ON p.PersonId = a.PersonId`](https://leetcode.com/problems/combine-two-tables/solution/)
    * [`SELECT a.Name AS Employee FROM Employee AS a JOIN Employee AS b ON a.ManagerId = b.Id AND a.Salary > b.Salary`](https://leetcode.com/problems/employees-earning-more-than-their-managers/solution/)
    * [`SELECT Email From Person GROUP BY Email HAVING COUNT(Id) > 1`](https://leetcode.com/problems/duplicate-emails/solution/)
    * [`SELECT Name AS 'Customers' FROM Customers WHERE Id NOT IN (SELECT CustomerId FROM Orders)`](https://leetcode.com/problems/customers-who-never-order/solution/)
    * [`SELECT IFNULL((SELECT DISTINCT Salary FROM Employee ORDER BY Salary DESC LIMIT 1 OFFSET 1), NULL) AS SecondHighestSalary`](https://leetcode.com/problems/second-highest-salary/solution/)
    * [`SELECT class FROM courses GROUP BY class HAVING COUNT(DISTINCT student) >= 5`](https://leetcode.com/problems/classes-more-than-5-students/solution/)
    * [`SELECT * FROM cinema WHERE id % 2 = 1 AND description != 'boring' ORDER BY rating DESC`](https://leetcode.com/problems/not-boring-movies/solution/)
    * [practice - create insert select](https://gist.github.com/hyunjun/17e9b03a1b0faa38c662#file-create_insert_select-md)
    * [GROUP_CONCAT](https://gist.github.com/hyunjun/17e9b03a1b0faa38c662#file-select_group_by-md)
      * [Can I concatenate multiple MySQL rows into one field?](https://stackoverflow.com/questions/276927/can-i-concatenate-multiple-mysql-rows-into-one-field)
    * age가 '만 xx세'로 되어 있을 때 숫자만 뽑아 그 차이를 구하는 경우

      ```
      $ mysql -h [x.y.z.w] -u [userid] -p[password] [database] -N -e "SELECT a.keyword, a.iage, b.keyword, b.iage, a.iage - b.iage FROM (SELECT \`key\`,keyword, age, CHAR_LENGTH(age), CONVERT(SUBSTRING(age, 2, CHAR_LENGTH(age)-2), UNSIGNED) iage, represent, family FROM [table] WHERE age IS NOT NULL) as a join (SELECT \`key\`,keyword, age, CHAR_LENGTH(age), CONVERT(SUBSTRING(age, 2, CHAR_LENGTH(age)-2), UNSIGNED) iage, represent, family FROM [table] WHERE age IS NOT NULL) as b on a.\`key\` != b.\`key\`"
      ```
    * [MySQL 기본 select SQL 예제](https://stricky.tistory.com/328)
    * [MySQL where in (서브쿼리) vs 조인 조회 성능 비교 (5.5 vs 5.6)](https://jojoldu.tistory.com/520)
    * [MySQL Update Subquery 성능 비교 (ver.5.6)](https://jojoldu.tistory.com/522)
    * [1. 페이징 성능 개선하기 - No Offset 사용하기](https://jojoldu.tistory.com/528)
    * [2. 페이징 성능 개선하기 - 커버링 인덱스 사용하기](https://jojoldu.tistory.com/529)
    * [3-1. 페이징 성능 개선하기 - 검색 버튼 사용시 페이지 건수 고정하기](https://jojoldu.tistory.com/530)
    * [3-2. 첫 페이지 조회 결과 cache 하기](https://jojoldu.tistory.com/531)
    * [MySQL IN절을 통한 성능 개선 방법](https://jojoldu.tistory.com/565) 범위 조건에서는 인덱스 효과를 제대로 보지 못함 -> IN은 기존의 MySQL 이 가지고 있던 범위 조건의 비효율 회피
  * [practice - create insert recursive union](https://gist.github.com/hyunjun/17e9b03a1b0faa38c662#file-create_insert_recursive_union-md)
  * SHOW
    * `show [full] processlist` [터미널에서 쿼리 전체 보기](https://jybaek.tistory.com/823)
    * [Show Comment of Fields FROM Mysql Table](https://stackoverflow.com/questions/5404051/show-comment-of-fields-from-mysql-table)
    * [mysql show 명령어 완벽 정리](https://stricky.tistory.com/251)
  * [`UPDATE salary SET sex = CASE sex WHEN 'm' THEN 'f' ELSE 'm' END;`](https://leetcode.com/problems/swap-salary/solution/)
  * [mysql 실무에 유용한 sql 로직 모음 #01](https://stricky.tistory.com/512)
  * [mysql 실무에 유용한 sql 로직 모음 #02](https://stricky.tistory.com/513)
  * [업그레이드 된 아이템 구하기](https://justinaofjune.tistory.com/49)
* troubleshooting
  * [MySQL 에서 한글이 께어질때 수정을 하는 방법 UTF-8사용](http://blog.daum.net/iamwhoi/5740153)
    * [11.1.6 Configuring the Character Set and Collation for Applications](https://dev.mysql.com/doc/refman/5.7/en/charset-applications.html)
  * [practice - Error: 1366](https://gist.github.com/hyunjun/0d56ce004f1db78d4eff4d2842575581#file-error_1366-md)
  * [practice - Error: 1467](https://gist.github.com/hyunjun/0d56ce004f1db78d4eff4d2842575581#file-error_1467-md)
  * [MySQL error 2006: mysql server has gone away](http://stackoverflow.com/questions/7942154/mysql-error-2006-mysql-server-has-gone-away) e.g. `--max_allowed_packet=268435456`
    * `SHOW VARIABLES LIKE 'max_allowed_packet';` or `SELECT @@max_allowed_packet;`
    * `set global max_allowed_packet=64*1024*1024;` to set (with privileged account such as root)
    * `~/.my.cnf`나 `/etc/my.cnf`등 여러 개의 cnf file이 있을 수 있으니 적절한 file에서 수정 후 mysql을 재시작(e.g. `service mysql restart`)하는 방식으로 해야 할 수도 있음
    * python code with MySQLdb or mysqlclient; `cursor.execute('SET GLOBAL max_allowed_packet=67108864', ())` root 권한이 필요해서 안될 듯
  * [FULLTEXT 인덱스와 일반 인덱스 성능 차이](http://ohgyun.com/766)
  * [max_execution_time 설정하기](http://ohgyun.com/767)
  * [Online Alter에도 헛점은 있더구나 – gdb, mysqld-debug 활용 사례](http://gywn.net/2018/10/online-alter-for-varchar/)
  * [MySQL online alter부터 CPU 100% 장애까지](https://tech.devsisters.com/posts/cro-mysql-online-alter/)
  * [MySQL Lock 상황 문제 해결](https://www.popit.kr/mysql-lock-상황-문제-해결)
  * [#1071 - Specified key was too long](http://stackoverflow.com/questions/1814532/1071-specified-key-was-too-long-max-key-length-is-767-bytes)
  * [Connect to MySQL after hitting ERROR 1040: Too many connections - Percona Database Performance Blog](https://www.percona.com/blog/2019/07/23/connect-to-mysql-after-hitting-error-1040-too-many-connections/)
  * [MySQL 8 root 비밀번호 분실, 초기화 방법 (DB관리자 필수로 알아둘 내용) How to reset MySQL root password - YouTube](https://www.youtube.com/watch?v=aUpsnwG7zOQ)
  * [Access denied for user 'root@'@'localhost' 해결방법 :: oziguyo](https://oziguyo.tistory.com/36)
  * [데이터가 있었는데요, 아니 없어요 - 컬리 기술 블로그](https://helloworld.kurly.com/blog/commit-mvcc-set-autocommit/)
* [MySQL root 계정에 대한 소켓 플러그인 제거하고 암호 설정하기 | 웹으로 말하기](https://mytory.net/archives/14460)
* [MySQL 로컬 개발시 아이디 비번을 파일에 적어두고 쓰는 방법 | 웹으로 말하기](https://mytory.net/archives/14458)
* [DATABASE2 - MySQL](https://opentutorials.org/course/3161)
* [Node.js - MySQL](https://opentutorials.org/course/3347)
* [mysql](https://hackmysql.com/tags/mysql/)
* [count 1편 - count에 대해 몰랐던 사실](http://blog.naver.com/pjt3591oo/221030483713)
* [count 2편 - benchmarking 해보기](http://blog.naver.com/pjt3591oo/221030656488)
* [MySQL NULL 처리 삽질](http://www.popit.kr/mysql-null-%EC%B2%98%EB%A6%AC-%EC%82%BD%EC%A7%88/)
* [리눅스 서버 구축하기 7. MySQL 설치](http://library.gabia.com/contents/infrahosting/3564)
* [**MySQL Tutorial**](http://www.mysqltutorial.org/)
* [왕초보용! 갖고 노는 MySQL 데이터베이스 강좌 - YouTube](https://www.youtube.com/watch?v=dgpBXNa9vJc)
* [how innodb lost its advantage](http://dom.as/2015/04/09/how-innodb-lost-its-advantage/)
* [How MySQL Is Able To Scale To 200 Million QPS - MySQL Cluster](http://highscalability.com/blog/2015/5/18/how-mysql-is-able-to-scale-to-200-million-qps-mysql-cluster.html)
* [Working with JSON in MySQL](https://scotch.io/tutorials/working-with-json-in-mysql)
* [JSON Labs Release: Native JSON Data Type and Binary Format](http://mysqlserverteam.com/json-labs-release-native-json-data-type-and-binary-format/)
* [30 mins with JSON in MySQL](http://dasini.net/blog/2015/11/17/30-mins-with-json-in-mysql/)
* [Max JSON column length in MySQL](https://stackoverflow.com/questions/40711101/max-json-column-length-in-mysql)
* [MySQL JSON vs. TEXT. JSON 타입 컬럼으로 저장하는 것이 좋을까요 ?  TEXT타입 컬럼이… | by Sunguck Lee | 당근마켓 팀블로그 | Aug, 2022 | Medium](https://medium.com/daangn/json-vs-text-c2c1448b8b1f)
  * MySQL에서 데이터타입인 JSON과 TEXT 성능 비교
    * 데이터베이스에서 JSON을 지원한 뒤로 유용한 기능이지만 언제 JSON을 쓰고 언제 TEXT를 써야 할 지 파악 가능
  * 큰 데이터를 기준으로 비교한 결과 COUNT 쿼리는 JSON을 파싱하지 않아서 거의 비슷한 성능
  * JSON 내부의 필드로 COUNT 쿼리를 하는 경우는 파싱하느라고 시간이 좀 더 소요
  * 대신 데이터를 조회하는 경우는 JSON 처리에 TEXT보다 오래 걸리기 때문에 JSON이 TEXT보다 훨씬 오래 소요
  * 대신 JSON은 내부의 특정 필드만 접근하거나 업데이트하는 경우나 특정 JSON 필드를 인덱스로 생성할 때는 그 효과를 볼 수 있음
* [MySQL performance optimization: 50% more work with 60% less latency variance](http://engineering.pinterest.com/post/122520169079/mysql-performance-optimization-50-more-work-with)
* [MySQL Optimizer Error. 옵티마이저 에러 & 힌트 | by Sunguck Lee | 당근마켓 테크 블로그 | May, 2023 | Medium](https://medium.com/daangn/mysql-optimizer-error-e438aa02e622)
* [on ORDER BY optimization](http://dom.as/2015/07/30/on-order-by-optimization/)
* [「개발 큐레이션」 MySQL과 쿼리 최적화](https://www.notion.so/MySQL-e8004e99b0f24a7cace27e7576b0c292)
* [MySQL의 ORDER BY로 지정한 순서대로 정렬하기](https://brunch.co.kr/@hopeless/4)
* [Learn to stop using shiny new things and love MySQL](https://engineering.pinterest.com/blog/learn-stop-using-shiny-new-things-and-love-mysql)
* [Open-sourcing Pinterest MySQL management tools](https://engineering.pinterest.com/blog/open-sourcing-pinterest-mysql-management-tools)
* [Full Outer Join in MySQL](http://stackoverflow.com/questions/4796872/full-outer-join-in-mysql)
* [인덱스 정리 및 팁](http://jojoldu.tistory.com/243)
* [MySQL InnoDB의 Adaptive Hash Index 활용](http://tech.kakao.com/2016/04/07/innodb-adaptive-hash-index/)
* [MySQL Ascending index vs Descending index](http://tech.kakao.com/2018/06/19/AscendingAndDescendingIndex/)
* [mysql 테이블과 인덱스 설계 시 주의사항 13가지](http://egloos.zum.com/tiger5net/v/5660848)
* [인덱스 생성, 조회](http://egloos.zum.com/hanaduri/v/19112)
* [패스트캠퍼스 SQL튜닝캠프 2일차 - 인덱스 향상](http://jojoldu.tistory.com/167)
* [Index에 대해서 정리해 봅니다. #MySQL](https://developer88.tistory.com/332)
* [**MySQL Workbench의 VISUAL EXPLAIN으로 인덱스 동작 확인하기**](https://engineering.linecorp.com/ko/blog/mysql-workbench-visual-explain-index/)
* [B-trees and database indexes](https://planetscale.com/blog/btrees-and-database-indexes)
  * [B-트리와 데이터베이스 인덱스 | GeekNews](https://news.hada.io/topic?id=16702)
* [B tree as Index](https://hugehoo-blog.vercel.app/blog/Database/B%20tree%20as%20Index)
* [인덱스 1편 - BTree 그리고 인덱스(INDEX)의 정체](https://blog.naver.com/pjt3591oo/222479946713)
* [인덱스 2편 - 여러분은 페이지네이션을 limit과 offset을 이용하여 구현하지 않나요?](https://blog.naver.com/pjt3591oo/222646508657)
* [인덱스 3편 - 다중 컬럼 인덱스와 사용되는 인덱스 만들기](https://blog.naver.com/pjt3591oo/222863820957)
* [DB Index 동작원리를 알아보자 | Eric's DevLog (데브로그)](https://www.kyungyeon.dev/posts/66)
* [mysql 커버링 인덱스란 무엇인가? | sTricky](https://stricky.tistory.com/441) cover index
* [Index Dive 비용 최적화. MySQL 서버의 실행계획 수립(Index Dive) 단계에서 많은… | by Sunguck Lee | 당근마켓 팀블로그 | Jun, 2022 | Medium](https://medium.com/daangn/index-dive-%EB%B9%84%EC%9A%A9-%EC%B5%9C%EC%A0%81%ED%99%94-1a50478f7df8)
* [인덱스 4편 - 스캔 종류 : 네이버 블로그](https://blog.naver.com/pjt3591oo/223089194436)
* [재입고 알림 신청 개발기 | by Jeenz | 29CM TEAM | Nov, 2022 | Medium](https://medium.com/29cm/%EC%9E%AC%EC%9E%85%EA%B3%A0-%EC%95%8C%EB%A6%BC-%EC%8B%A0%EC%B2%AD-%EA%B0%9C%EB%B0%9C%EA%B8%B0-6b6a08902d6f)
* [gildang MySQL tutorial](http://gildang.co.kr/?p=2383)
* [MySQL Slow Query log Monitoring using Beats & ELK](http://www.slideshare.net/YoungHeonKim1/mysql-slow-query-log-monitoring-using-beats-elk)
* [MySQL INSERT IF NOT EXISTS](https://number1.co.za/mysql-insert-if-not-exists/)

  ```
  INSERT INTO list (code, name, address,)
  SELECT 'ABC', 'ABC name', 'Johannesburg'
  FROM list
  WHERE NOT EXISTS(
      SELECT code, name, address
      FROM list
      WHERE code = 'ABC'
    AND name = 'ABC name'
    AND address = 'Johannesburg'
  )
  LIMIT 1
  ```

* [MySQL: PHP를 사용하지 않고 Query만으로 unserialize하는 방법](http://blog.gaerae.com/2016/07/how-to-unserialize-data-using-mysql-without-using-php.html)
* [MySQL: id BETWEEN start AND end Instead of LIMIT start, step For Better Database Performance](http://www.kavoir.com/2009/04/mysql-id-between-start-and-end-instead-of-limit-start-step-for-better-database-performance.html)
* [MySQL 바이너리 로그를 활용한 DB 복구 방법 in Windows](http://aljjabaegi.tistory.com/92)
* [vagrant로 설치하는 mysql / phpmyadmin](https://raspberrypikor.blogspot.com/2016/12/vagrant-mysql.html)
* [MySQL에서 파티션 일부를 다른 파티션 테이블로 옮겨보기](http://gywn.net/2017/01/how_to_move_partition_data_to_another/)
* [MySQL 파티셔닝 테이블 SELECT가 느려요](http://gywn.net/2019/08/mysql-poor-performance-with-super-many-partitions/)
* [**MySQL에서 Affected Rows를 병맛나게 활용해보자**](http://gywn.net/2018/03/mad-usage-with-mysql-affected-rows/)
* [Perfecting Lambda Architecture with Oracle Data Integrator (and Kafka / MapR Streams)](https://www.mapr.com/blog/perfecting-lambda-architecture-oracle-data-integrator-and-kafka-mapr-streams)
  * MySQL 데이터베이스의 변경 내용을 스트림으로 캡처하기 위해 Oracle Data Integrator, Apache Kafka / MapR Stream를 구성하는 과정
* [ORACLE to Mysql DBMS로의 전환 프로세스](https://stricky.tistory.com/319)
* [천방지축 RDBMS 때려잡기: Oracle to MySQL 변환기 | NHN FORWARD](https://forward.nhn.com/2021/sessions/15)
* [Change Data Captures CDC from MySQL Database to Kafka with Kafka Connect and Debezium - DZone Integration](https://dzone.com/articles/change-data-captures-cdc-from-mysql-database-to-ka)
* [Replicating Relational Databases with StreamSets Data Collector](https://streamsets.com/blog/blogreplicating-relational-databases-with-streamsets-data-collector/)
  * MySQL 데이터베이스의 변경 내용을 스트림으로 캡처하기 위해 StreamSets을 이용
  * StreamSets은 JDBC를 이용하여 폴링 기반의 스트림 데이터 캡처가 가능
  * 본문에서 MySQL 데이터베이스의 변경 사항을 캡처하고 HDFS/Hive/Impala로 streaming 하는 과정을 설명
* [Delayed Replication을 이용해 유실된 데이터 빠르게 복구하기](http://tmondev.blog.me/220970798327)
* [Group Replication in Percona Server for MySQL](https://www.percona.com/blog/2020/01/17/group-replication-in-percona-server-for-mysql/)
* [MySQL Group Replication 구축](https://saramin.github.io/2021-09-28-mysql-group-replication/)
* [데이터베이스의 확장성과 가용성을 위한 MySQL Replication](https://hudi.blog/mysql-replication/)
* [부하 분산을 위해 MySQL을 Master/Slave로 이중화를 구성해 본 이야기 | Recoding Life](https://jane096.github.io/project/mysql-master-slave-replication/)
* [**무뇽이와 알아보는 대규모 데이터 관리 - 데이터베이스 복제하기(리플리케이션)**](https://velog.io/@backfox/%EB%AC%B4%EB%87%BD%EC%9D%B4%EC%99%80-%EC%95%8C%EC%95%84%EB%B3%B4%EB%8A%94-%EB%8C%80%EA%B7%9C%EB%AA%A8-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EA%B4%80%EB%A6%AC-%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%B2%A0%EC%9D%B4%EC%8A%A4-%EB%B3%B5%EC%A0%9C%ED%95%98%EA%B8%B0%EB%A6%AC%ED%94%8C%EB%A6%AC%EC%BC%80%EC%9D%B4%EC%85%98-f4pota6h)
* [**MySQL을 NoSQL로 사용하기**](http://advent.perl.kr/2012/2012-12-12.html)
  * 2010년 글 memcached 400,000/sec get vs. 100,000/sec select MySQL/InnoDB
  * plugin을 통해 750,000/sec으로 성능 향상
* utf8mb4
  * [How to support full Unicode in MySQL databases](https://mathiasbynens.be/notes/mysql-utf8mb4)
  * [In MySQL, never use “utf8”. Use “utf8mb4”. | by Adam Hooper | Medium](https://adamhooper.medium.com/in-mysql-never-use-utf8-use-utf8mb4-11761243e434)
  * [Migrating to utf8mb4: Things to Consider - Percona Database Performance Blog](https://www.percona.com/blog/migrating-to-utf8mb4-things-to-consider/)
* [Calculating disk space usage per MySQL DB](https://dba.stackexchange.com/questions/14337/calculating-disk-space-usage-per-mysql-db)
* [How to Install Only MySQL Client on CentOS, Redhat, Fedora and Ubuntu](http://www.looklinux.com/install-mysql-client-on-centos-redhat-fedora-and-ubuntu/)
  * `yum install mysql` tried to install `mariadb` & `mariadb-libs` on Redhat 7.2(`CentOS Linux release 7.2.1511 (Core)`)
* [MySQL 8.0 맥에 설치하기 #DBeaver - YouTube](https://www.youtube.com/watch?v=gTYw8CZZujE)
* [MySQL 설치 (윈도우 환경)](https://www.popit.kr/mysql-%EC%84%A4%EC%B9%98-%EC%9C%88%EB%8F%84%EC%9A%B0-%ED%99%98%EA%B2%BD/)
* [윈도우10 MySQL Community 8.0 버전 다운로드 및 설치 방법 가이드](https://stricky.tistory.com/342)
* [MySQL 맥 OS에 설치하기 - 로스카츠의 AI 머신러닝](https://losskatsu.github.io/it-infra/mysql-install-mac/)
* [MySQL Performance - Number of Tables Vs. Number of Rows](https://stackoverflow.com/questions/9965203/mysql-performance-number-of-tables-vs-number-of-rows)
* [MySQL Server와 Workbench Windows에 설치하기](https://mixedcode.com/blog/detail?pid=52)
* [phpmyadmin의 궁극적인 대안: MySQL Workbench + 터널링](http://earlybird.kr/2027)
* [WorkBench 쿼리 타임아웃](http://jybaek.tistory.com/760)
* [Node.js와 MySQL 연동시키기](https://jungwoon.github.io/node.js/2017/07/17/Node_with_MySQL/)
* [MySQL: Fulltext search에서 하이픈 캐릭터 사용하기](http://ohgyun.com/757)
* [surrogate key 와 natural key](http://ohgyun.com/756)
* [primary key vs foreign key in mysql | Tutorial 8 in hindi - YouTube](https://www.youtube.com/watch?v=K5EbghMBow0)
* [Difference between Primary key and Unique key - GeeksforGeeks](https://www.geeksforgeeks.org/difference-between-primary-key-and-unique-key/)
* [Create foreign key in mysql | Create table with foreign key | Tutorial 9 in hindi - YouTube](https://www.youtube.com/watch?v=TLD0zkD9MtQ)
* [카카오뱅크 – Percona / MariaDB / MySQL](https://osskorea.wordpress.com/2017/08/02/%EC%B9%B4%EC%B9%B4%EC%98%A4%EB%B1%85%ED%81%AC-percona-mariadb-mysql/)
* [카카오뱅크, 마이SQL 잘 쓰는 비결](http://v.media.daum.net/v/20170917095558384)
* [오픈소스 데이터베이스, 은행 서비스에 첫발을 내밀다](https://www.slideshare.net/deview/135-80845610)
* [오픈소스 디비로 행원이 되어보다](https://brunch.co.kr/@chan/10)
  * [그날, 그리고 그날을 회고하며](https://brunch.co.kr/@chan/12)
  * [벌써 3월! 나는 누구인가?](https://brunch.co.kr/@chan/14)
* [국내 최초의 시도, 카카오뱅크의 오픈소스 데이터 베이스](http://yun4794.blog.me/221138075348)
* [오픈소스 데이터베이스, 흐르는 은행 데이터에 빨대를 꽂아보다](https://gywn.net/2019/09/ifkakao-kakaobank-uldraman/) CDC, Uldraman 울드라맨
* [데이터야 안전하게 놀아보자 v.1](https://www.slideshare.net/dongchansung/v1-83328271)
* [Different locations for MySQL databases?](https://askubuntu.com/questions/14418/different-locations-for-mysql-databases)
* [대용량 테이블 스키마 변경하기](http://jojoldu.tistory.com/244) alter table
* [MySQL Query 추적하기](http://blog.plura.io/?p=4493)
* [beaker_session MySQL server has gone away](https://ash84.net/2017/11/10/beaker_session-mysql-server-has-gone-away/)
* [MariaDB Binlog을 이용한 변경사항 추적](https://www.ridicorp.com/blog/2017/10/30/binlog-collector)
* [MySQL binlog파서와 memcached plugin의 콜라보레이션! | gywndi's database](https://gywn.net/2020/08/mysql-binlog-memcached-plugin-collaboration/)
* [Streaming MySQL Binlogs to S3 (or Any Object Storage) - Percona Database Performance Blog](https://www.percona.com/blog/streaming-mysql-binlogs-to-s3-or-any-object-storage/)
* [MySQL binlog 사이즈(기한) 제한 | 웹으로 말하기](https://mytory.net/archives/14570)
* [mysql binlog를 알아보자 : 네이버 블로그](https://blog.naver.com/pjt3591oo/223302518766)
* [pt-query-digest](https://www.percona.com/doc/percona-toolkit/LATEST/pt-query-digest.html)
* [Optimizing slow web pages with mk-query-digest](https://www.percona.com/blog/2011/04/07/optimizing-slow-web-pages-with-mk-query-digest/)
* [Poor man’s query logging](https://www.percona.com/blog/2008/11/07/poor-mans-query-logging/)
* tcpdump
  * [Troubleshooting MySQL Slow Queries with Tcpdumps](https://www.databasejournal.com/features/mysql/article.php/3916226/Troubleshooting-MySQL-Slow-Queries-with-Tcpdumps.htm)
  * [Analyze MySQL Queries Using tcpdump](https://www.badllama.com/content/analyze-mysql-queries-using-tcpdump)
  * [Use tcpdump to monitor mysql](https://gist.github.com/gstark/10268260)
  * [How to catch MySQL SQL with tcpdump in Linux](https://web.liferay.com/web/david.zhang/blog/-/blogs/how-to-catch-mysql-sql-with-tcpdump-in-linux)
* [Managing Hierarchical Data in MySQL](http://mikehillyer.com/articles/managing-hierarchical-data-in-mysql/) e.g. 게시판
* [MySQL 실행 계획](http://12bme.tistory.com/160)
* [MySQL High Availability at GitHub](https://githubengineering.com/mysql-high-availability-at-github/)
* [Speed Up Your Database 300 Times](https://speakerdeck.com/afilina/speed-up-your-database-300-times)
* [Why SQL is beating NoSQL, and what this means for the future of data](https://blog.timescale.com/why-sql-beating-nosql-what-this-means-for-future-of-data-time-series-database-348b777b847a)
* [MySQL for Excel](https://www.mysql.com/why-mysql/windows/excel)
* [MySQL 전방탐색 지원](https://www.popit.kr/경-mysql-전방탐색-지원-축)
* [MySQL performance-schema-instruments 사용에 따른 성능 영향 실험](https://engineering.linecorp.com/ko/blog/mysql-research-performance-schema-instruments/)
* [An in-depth look at Database Indexing](https://medium.freecodecamp.org/database-indexing-at-a-glance-bb50809d48bd)
* **MySQL High Availability Framework Explained** ScaleGrid라는 MySQL service 회사에서 자사의 기술을 이용해 설명했지만, 일반적인 High Availability를 이해하기 위한 기초로 굉장히 좋은 글
  * [Part I: Introduction](https://scalegrid.io/blog/mysql-high-availability-framework-explained-part-1/)
  * [Part II: Semisynchronous Replication](https://scalegrid.io/blog/mysql-high-availability-framework-explained-part-2/)
  * [Part III: Failure Scenarios](https://scalegrid.io/blog/mysql-high-availability-framework-explained-part-3/)
  * [Part III: Failure Scenarios](http://highscalability.com/blog/2019/4/16/mysql-high-availability-framework-explained-part-iii-failove.html)
* [Failed to read auto-increment value from storage engine 해결 방법](https://jojoldu.tistory.com/417)
* [MySQL – Keep an eye on your auto_increment values – lefred's blog: tribulations of a MySQL Evangelist](https://lefred.be/content/mysql-keep-an-eye-on-your-auto_increment-values/)
* [(MySQL) Auto Increment에서 TypeSafe Bulk Insert 진행하기 (feat.EntityQL, JPA)](https://jojoldu.tistory.com/558)
* [EntityQL로 OneToMany (1:N) Bulk Insert 구현하기](https://jojoldu.tistory.com/560)
* [MySQL 자동 증가 칼럼의 최신 데이터 조회시 주의 사항](https://javacan.tistory.com/entry/MySQL-auto-inc-col-gotcha)
* [**MySQL을 이용한 분산락으로 여러 서버에 걸친 동시성 관리 | 우아한형제들 기술블로그**](https://techblog.woowahan.com/2631/)
* [**Lock으로 이해하는 Transaction의 Isolation Level**](https://suhwan.dev/2019/06/09/transaction-isolation-level-and-lock)
* [Transaction의 Isolation Level - 트랜잭션 격리수준](https://blog.naver.com/pjt3591oo/221754164462)
* [MySQL 트랜잭션 Isolation Level로 인한 장애 사전 예방 법 – gywndi's database](https://gywn.net/2012/05/mysql-transaction-isolation-level/)
* [프로그래밍 초식 : DB 트랜잭션 조금 이해하기 1, 2 :: 자바캔(Java Can Do IT)](https://javacan.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D-%EC%B4%88%EC%8B%9D-DB-%ED%8A%B8%EB%9E%9C%EC%9E%AD%EC%85%98-%EC%A1%B0%EA%B8%88-%EC%9D%B4%ED%95%B4%ED%95%98%EA%B8%B0-1-2)
* [Distributed Transactions & Two-phase Commit | by Animesh Gaitonde | Geek Culture | Medium](https://medium.com/geekculture/distributed-transactions-two-phase-commit-c82752d69324)
* [DB를 이용한 분산 락 구현(MariaDB, MySQL)](https://javacan.tistory.com/entry/distributed-lock-using-db)
* [꿀벌개발일지 :: lock=none, algorithm=inplace 으로 테이블 변경하기](https://ohgyun.com/800)
* [락(Lock)너는 무엇을 잠그는 녀석이니?](https://blog.naver.com/pjt3591oo/222479605880)
* [MySQL Gap Lock 다시보기. 우리가 일반적으로 알고 있는 데이터베이스 서버의 잠금(Lock)은… | by 당근마켓 | 당근마켓 팀블로그 | Mar, 2022 | Medium](https://medium.com/daangn/mysql-gap-lock-%EB%8B%A4%EC%8B%9C%EB%B3%B4%EA%B8%B0-7f47ea3f68bc)
* [MySQL Gap Lock (두번째 이야기). Why ? | by Sunguck Lee | 당근 테크 블로그 | Oct, 2023 | Medium](https://medium.com/daangn/mysql-gap-lock-%EB%91%90%EB%B2%88%EC%A7%B8-%EC%9D%B4%EC%95%BC%EA%B8%B0-49727c005084)
* [MySQL 데이터베이스 한번에 끝내기 SQL Full Tutorial Course using MySQL Database](https://www.youtube.com/watch?v=vgIc4ctNFbc)
* [MySQL InnoDB의 메모리 캐시 서버로 변신! | STAR::DATABASE](https://stardba.net/chan/mysql-innodb-as-cache-server-monitoring/)
  * [**MySQL InnoDB의 메모리 캐시 서버로 변신! – 설정편 –**](https://gywn.net/2019/09/mysql-innodb-as-cache-server-config/)
  * [**MySQL InnoDB의 메모리 캐시 서버로 변신! – 모니터링편 –**](https://gywn.net/2019/09/mysql-innodb-as-cache-server-monitoring/)
  * [**MySQL InnoDB의 메모리 캐시 서버로 변신! – 활용편 –**](https://gywn.net/2020/01/mysql-innodb-as-cache-server-monitoring-advanced/)
* [Setting up an InnoDB Cluster With a Few Lines of Code - Percona Database Performance Blog](https://www.percona.com/blog/2020/05/05/setting-up-an-innodb-cluster-with-a-few-lines-of-code/)
* [Do Not Pass This Way Again](https://grimoire.ca/mysql/choose-something-else)
* [How to create a user in MySQL/MariaDB and grant permissions on a specific database](http://www.daniloaz.com/en/how-to-create-a-user-in-mysql-mariadb-and-grant-permissions-on-a-specific-database/)
* [Zero Downtime Schema Migrations](https://medium.com/invoca-engineering-blog/zero-downtime-schema-migrations-29f81f9ea6db)
* [Migrating Facebook to MySQL 8.0 - Facebook Engineering](https://engineering.fb.com/2021/07/22/data-infrastructure/mysql/)
* [Why Uber Engineering Switched from Postgres to MySQL | Uber Engineering Blog](https://eng.uber.com/postgres-to-mysql-migration/)
* [이커머스 플랫폼의 주문 DB 마이그레이션 경험기](https://techblog.lycorp.co.jp/ko/experience-in-migrating-order-db-on-ecommerce-platform) Oracle to MySQL
* [읽기 전용 설정으로 MySQL 이전하기](https://techblog.lycorp.co.jp/ko/migrate-mysql-with-read-only-mode)
* [Replica 에 Write 가 된다고? MySQL Writable Replica 로 데이터 분석용 DB 만들기](https://blog.gangnamunni.com/2020/02/05/mysql_writable_replica_on_aws.html)
* [MySQL (MariaDB) 인덱스 컨디션 푸시다운](https://jojoldu.tistory.com/474)
* [1. 커버링 인덱스 (기본 지식 / WHERE / GROUP BY)](https://jojoldu.tistory.com/476)
* [2. 커버링 인덱스 (WHERE + ORDER BY / GROUP BY + ORDER BY )](https://jojoldu.tistory.com/481)
* [MySQL의 다양한 실행 프로그램 mysqld_safe, mysql.server, mysqld_multi feat.mysqld](https://stricky.tistory.com/164)
* [MySQL 8.0 테이블스페이스 관리 방법 변경 내용 feat.테이블 스페이스 삭제한다면?!](https://stricky.tistory.com/166)
* [MySQL 8.0 – Who stopped mysqld and how long did it take ? – lefred's blog: tribulations of a MySQL Evangelist](https://lefred.be/content/mysql-8-0-who-stopped-mysqld-and-how-long-did-it-take/)
* [MySQL 5.6 EOL is February 2021 !! – lefred's blog: tribulations of a MySQL Evangelist](https://lefred.be/content/mysql-5-6-eol-is-february-2021/) 8.0
* [Upgrading MySQL (Percona Server) from 5.7 to 8.0 | by Flant staff | Flant | Medium](https://medium.com/flant-com/upgrading-mysql-percona-server-5-to-8-4bce53bdce5c)
* [MySQL 8.0 업그레이드 전 짚어봐야할 몇 가지! | STAR::DATABASE](https://stardba.net/sun/checkpoint-mysql80-upgrade/)
* [MySQL 8.0.22: Asynchronous Replication Automatic Connection (IO Thread) Failover - Percona Database Performance Blog](https://www.percona.com/blog/2020/10/26/mysql-8-0-22-asynchronous-replication-automatic-connection-io-thread-failover/)
* [커넥션(connection)은 어떻게 관리되나](https://blog.naver.com/pjt3591oo/222984240944)
* [MySql 8.0 on OEL 7.9](https://support.dbagenesis.com/post/mysql-8-installation-on-oel-7-9)
* [MySQL Server와 Workbench Windows에 설치하기](https://mixedcode.com/blog/52)
* [5 MySQL features you need to know](https://opensource.com/article/20/3/mysql-features)
* [18 Things You Can Do to Remove MySQL Bottlenecks Caused by High Traffic (Part One)](https://www.percona.com/blog/2020/04/03/18-things-you-can-do-to-remove-mysql-bottlenecks-caused-by-high-traffic-part-one/)
* [Need to Connect to a Local MySQL Server? Use Unix Domain Socket!](https://www.percona.com/blog/2020/04/13/need-to-connect-to-a-local-mysql-server-use-unix-domain-socket/)
* median 값 구하기 [SQL MySQL의와 계산의 중간에 간단한 방법](https://cnpnote.tistory.com/entry/SQL-MySQL%EC%9D%98%EC%99%80-%EA%B3%84%EC%82%B0%EC%9D%98-%EC%A4%91%EA%B0%84%EC%97%90-%EA%B0%84%EB%8B%A8%ED%95%9C-%EB%B0%A9%EB%B2%95)
* [MySql 의 기본 사용법과 주요 명령어들 총정리](https://developer88.tistory.com/20)
* [Explain의 도움을 받아 Full Scan을 방지하자 #풀스캔 방지](https://developer88.tistory.com/326)
* [MySQL EXPLAIN ANALYZE](https://hackmysql.com/post/book-2/)
* [MySQL :: 슬로우쿼리 잡는 명령어, ‘EXPLAIN ANALYZE’ 해석법](https://velog.io/@wisepine/MySQL-%EC%8A%AC%EB%A1%9C%EC%9A%B0%EC%BF%BC%EB%A6%AC-%EC%9E%A1%EB%8A%94-%EB%AA%85%EB%A0%B9%EC%96%B4-EXPLAIN-ANALIZE-%ED%95%B4%EC%84%9D%EB%B2%95)
* [MySQL (Percona XtraDB) slave replication crash resilience settings](https://dev.to/cosimo/mysql-percona-xtradb-slave-replication-crash-resilience-settings-3d8e)
* [mysql 복제(replication)서버 구성](https://blog.naver.com/pjt3591oo/223307257886)
* [Improving MySQL Password Security with Validation Plugin](https://www.percona.com/blog/2020/06/03/improving-mysql-password-security-with-validation-plugin/)
* [Best Practices for MySQL Backups - Percona Database Performance Blog](https://www.percona.com/blog/2020/05/27/best-practices-for-mysql-backups/)
* [Charset and Collation Settings Impact on MySQL Performance - Percona Database Performance Blog](https://www.percona.com/blog/2019/02/27/charset-and-collation-settings-impact-on-mysql-performance/)
* [sql에서 collation이 왜 중요할까요?](https://codingdog.tistory.com/entry/sql%EC%97%90%EC%84%9C-collation%EC%9D%B4-%EC%99%9C-%EC%A4%91%EC%9A%94%ED%95%A0%EA%B9%8C%EC%9A%94)
* [MySQL 콜레이션은 어떻게 동작할까? | 요즘IT](https://yozm.wishket.com/magazine/detail/2736/)
* [MySQL/MariaDB character sets and collations explained – why utf8 is not UTF-8 | Hello DevOps](https://www.hellodevops.blog/posts/database-character-sets-and-collations-explained/)
* [Mysql objects 개념 정리 for 개발자](https://stricky.tistory.com/315)
* [Mysql FEDERATED Engine 으로 dblink 구현하기](https://stricky.tistory.com/325)
* [MySQL SQL 독학 강의 전체 A to Z](https://stricky.tistory.com/333)
* [MySQL Deadlocks Are Our Friends - Percona Database Performance Blog](https://www.percona.com/blog/2020/07/07/mysql-deadlocks-are-our-friends/)
* [MySQL from a Developers Perspective | Die wunderbare Welt von Isotopp](https://blog.koehntopp.info/2020/08/04/mysql-from-a-developers-perspective.html)
* [MySQL Transactions - the physical side | Die wunderbare Welt von Isotopp](https://blog.koehntopp.info/2020/07/27/mysql-transactions.html)
* [MySQL Challenge: 100k Connections - Percona Database Performance Blog](https://www.percona.com/blog/2019/02/25/mysql-challenge-100k-connections/)
* [Sometimes they come back: exfiltration through MySQL and CVE-2020-11579 - Shielder](https://www.shielder.it/blog/mysql-and-cve-2020-11579-exploitation/)
* [MySQL Query Performance Troubleshooting: Resource-Based Approach - Percona Database Performance Blog](https://www.percona.com/blog/2020/07/15/mysql-query-performance-troubleshooting-resource-based-approach/)
* [Please stop using this UPSERT anti-pattern - SQLPerformance.com](https://sqlperformance.com/2020/09/locking/upsert-anti-pattern)
* [실행계획을 분석해서 SQL 성능튜닝을 해보자(feat.MySQL) | Recoding Life](https://jane096.github.io/project/refactoring-sql/)
* [MySQL 쿼리 튜닝의 첫걸음 | 요즘IT](https://yozm.wishket.com/magazine/detail/2260/)
* [The MySQL cheatsheet we all need | Better Programming](https://medium.com/better-programming/the-mysql-cheatsheet-we-all-need-d1af0377bdc6)
* [MySQL 쓰면서 하지 말아야 할 것 17가지 – Lael's World](https://blog.lael.be/post/370)
* [MySQL 내부 구조](https://brunch.co.kr/@jehovah/21)
* [**Building HashTag M : N Relation with Node.js, Sequelize(MySQL) | by Ryan Kim | Oct, 2020 | Medium**](https://equus3144.medium.com/building-hashtag-m-n-relation-with-node-js-sequelize-mysql-3dde6824d2a0)
* [Blog of (former?) MySQL Entomologist: Linux /proc Filesystem for MySQL DBAs - Part I, Basics](https://mysqlentomologist.blogspot.com/2021/01/linux-proc-filesystem-for-mysql-dbas.html)
* [How to delete lots of rows from a MySQL database without indefinite locking – Bram.us](https://www.bram.us/2021/01/14/how-to-delete-lots-of-rows-from-a-mysql-database-without-indefinite-locking/)
* [MySQL/MariaDB에서 유저에게 multiple host를 부여하는 방법 - Nephtyw’S Programming Stash](https://nephtyws.github.io/database/mariadb-mysql-subnet-host/)
* [🛢CSV 파일 MySQL DB에 추가하기 - YouTube](https://www.youtube.com/watch?v=XLoit2-DPaI)
* [MySQL and UUIDs | Die wunderbare Welt von Isotopp](https://blog.koehntopp.info/2021/04/06/mysql-and-uuids.html)
* [MySQL에서 리셋되는 시퀀스 만들어보기 | gywndi's database](https://gywn.net/2021/06/resetable-sequence-for-mysql/)
* [데이터베이스에서 위도경도 관리 - MySQL Spatial SQL](https://blog.naver.com/ndskr/222444680248)
* [MySQL document store 초간단 테스트 | gywndi's database](https://gywn.net/2021/07/mysql-document-store-test/)
* [Build a Python Web Scraper + Advanced MySQL Queries](https://arctype.com/blog/mysql-advanced-queries/)
* [How to Connect A GraphQL API and A MySQL Database in Your GraphQL Layer | StepZen blog](https://stepzen.com/blog/connect-a-mysql-db-and-graphql-api-in-a-gql-layer)
* [번역 MySQL의 ENUM 타입을 사용하지 말아야 할 8가지 이유](https://velog.io/@leejh3224/%EB%B2%88%EC%97%AD-MySQL%EC%9D%98-ENUM-%ED%83%80%EC%9E%85%EC%9D%84-%EC%82%AC%EC%9A%A9%ED%95%98%EC%A7%80-%EB%A7%90%EC%95%84%EC%95%BC-%ED%95%A0-8%EA%B0%80%EC%A7%80-%EC%9D%B4%EC%9C%A0)
* [Login y Logout con NodeJS y MySQL usando jsonwebtokens - YouTube](https://www.youtube.com/watch?v=PRoTFE2RSfQ)
* [Upgrading MySQL at Shopify — Infrastructure (2022)](https://shopify.engineering/upgrading-mysql-shopify)
* [brew로 MySQL 5.7을 MySQL 8로 업그레이드 하면서 겪은 에러 기록 | 웹으로 말하기](https://mytory.net/2022/02/14/brew-mysql-upgrade.html)
* [Upgrading GitHub.com to MySQL 8.0 - The GitHub Blog](https://github.blog/2023-12-07-upgrading-github-com-to-mysql-8-0/)
  * GitHub.com이 성장하면서 단일 MySQL에서 아키텍처를 발전해 오고 있었는데 1,200개 이상의 MySQL 호스트를 8.0으로 업그레이드한 과정
  * SLO에 영향을 주지 않으면서 업그레이드하기 위해 계획, 테스트, 업그레이드에 1년 넘게 소요
  * MySQL 5.7의 수명이 거의 종료됨에 따라 8.0 으로 업그레이드 해야 했다.
  * GitHub의 MySQL 인프라 구성
    * 1,200개 이상의 호스트로 구성되어 있고 Azure와 베어 메탈 호스트의 조합
    * 300TB 이상의 데이터를 저장하고 50개 이상의 데이터베이스 클러스터에서 초당 5,500만 건의 쿼리 처리
    * 각 클러스터는 primary와 replicas를 이용한 고가용성 구성
    * 수평/수직 샤딩을 모두 활용하여 데이터가 파티셔닝
    * 대규모 도메인 영역을 위해 수평 샤딩 된 Vitess 클러스터도 존재
  * SLO/SLA를 준수하면서 업그레이드해야 하지만 모든 장애를 미리 고려할 수는 없으므로 중단없이 MySQL 5.7로 롤백할 수 있어야 함. 다양한 워크로드가 있으므로 클러스터를 원자단위로 업그레이드 해야하고 혼합 버전을 오랫동안 운영해야 함
  * 2022년 7월부터 업그레이드 준비 시작
  * MySQL 8.0의 설정값을 결정하기 위해 벤치마크했고 두 버전을 운영해야 했기에 도구와 자동화가 두 버전 모두 처리 필요
  * 모든 애플리케이션의 CI에 MySQL 8.0을 추가해서 CI에서 5.7과 8.0을 같이 실행
  * 업그레이드 전략
    * replicas를 먼저 업그레이드하고 트래픽을 받도록 한 뒤 모니터링하면서 교체해 나가고 5.7은 롤백을 위해 띄워두었지만, 트래픽은 안 가게 함
    * Replica 토폴로지를 조정해서 8.0 primary가 5.7 primary를 복제하도록 구성, 8.0 replicas 아래에는 5.7 세트와 8.0 세트로 구성해서 8.0만 트래픽을 처리하도록 함
    * Primary를 직접 업그레이드하지 않고 페일오버를 통해 MySQL 8.0 Replica가 Primary로 승격되도록 함
    * 백업이나 비 프로덕션을 위한 MySQL도 모두 업그레이드
    * 롤백할 필요가 없다는 걸 확인 후 5.7 서버 모두 제거
  * [GitHub Upgrades its MySQL Infrastructure from v5.7 to 8.0 - InfoQ](https://www.infoq.com/news/2024/02/github-mysql-upgrade-v8/)
* [MySQL Best of 2021](https://blogs.oracle.com/mysql/post/mysql-best-of-2021)
* [MySQL의 변신…”이제는 분석용 클라우드 DB” - Byline Network](https://byline.network/2022/04/0406/)
* [MySQL Command Line Interface. 요즘은 세상의 모든 컴퓨터 화면이 그래픽 인터페이스로 바뀐 것 처럼 | by Sunguck Lee | 당근마켓 팀블로그 | May, 2022 | Medium](https://medium.com/daangn/mysql-command-line-interface-21de489e7db5)
  * MySQL client CLI가 다른 데이터베이스에 비해 기능이 부족해서 CLI를 직접 수정해서 편의 기능을 추가하는 방법 설명
  * 프롬프트에 서버 정보 등을 표시하거나 PostgreSQL처럼 자주 쓰는 명령어의 단축 명령어를 추가해서 `\\d`를 입력하면 `SHOW DATABSAES;` 실행 가능
  * 미리 파일에 저장해둔 SQL을 실행하거나 회사 정책에 따른 경고문을 표시할 수 있도록 수정한 client 코드 같이 제공
* [MySQL kill 명령어 (프로세스 kill하기)](https://blog.doosikbae.com/entry/MySQL-kill-%EB%AA%85%EB%A0%B9%EC%96%B4)
* [MySQL Heatwave를 살펴보았습니다 – gywndi's database](https://gywn.net/2022/05/mysql-heatwave/)
* [MySQL table lock / table mutex / 송장번호 가상계번호 발급 / 번호 중복 발급 방지 방법](https://blog.naver.com/oralol/222836743527)
* [How to Make a Simple CRUD Application using ReactJS, NodeJS and MySQL](https://morioh.com/p/0ecf22d4888d)
* [MySQL Infusion UDF | A MySQL functionality enhancement UDF](https://morioh.com/p/2232cef40044)
* [MySQL Batch Update 성능 측정 및 분석 - Yun Blog | 기술 블로그](https://cheese10yun.github.io/mysql-batch-update/)
* [MySQL CATS (Contention-Aware Transaction Scheduling) | by Sunguck Lee | 당근마켓 팀블로그 | Nov, 2022 | Medium](https://medium.com/daangn/mysql-cats-contention-aware-transaction-scheduling-71fe6956e87e)
* [최신 하드웨어를 활용하는 MySQL 스토리지 엔진 공동 연구 -한국어판- - YouTube](https://www.youtube.com/watch?v=UuYWwDlGvBE)
* [MySQL `sql_mode`로 알아보는 시스템 변수 permanent, runtime설정](https://blog.jiniworld.me/64)
* [MySQL BOOLEAN 컬럼. PostgreSQL 서버와 같은 RDBMS 서버는 네이티브하게… | by Sunguck Lee | 당근마켓 팀블로그 | Mar, 2023 | Medium](https://medium.com/daangn/mysql-boolean-%EC%BB%AC%EB%9F%BC-7abd9b35c664)
* [MySQL에 View를 만들 땐 파생 테이블을 주의하자](https://velog.io/@hyemin916/%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%B2%A0%EC%9D%B4%EC%8A%A4%EC%97%90-View%EB%A5%BC-%EB%A7%8C%EB%93%A4-%EB%95%90-%EC%9E%84%EC%8B%9C-%ED%85%8C%EC%9D%B4%EB%B8%94%EC%9D%84-%EC%A3%BC%EC%9D%98%ED%95%98%EC%9E%90)
* [입만 가지고 떠드는 개발자가 ChatGPT에게 외주줘서 만든 Mysql 복제지연 모니터링](https://d2.naver.com/helloworld/8532139)
* [MySQL 접속 장애 예방 및 해결 방법, How to prevent and solve MySQL connection failure - YouTube](https://www.youtube.com/watch?v=7uvtQwJP5zc)
* [PlanetScale is bringing vector search and storage to MySQL](https://planetscale.com/blog/planetscale-is-bringing-vector-search-and-storage-to-mysql)
* [MySQL DECIMAL vs DOUBLE(FLOAT): 뭘 선택해야 할까?(Feat. 고정 소수점 vs 부동 소수점)](https://woonys.tistory.com/entry/MySQLDECIMAL-vs-DOUBLEFLOAT-%EB%AD%98-%EC%84%A0%ED%83%9D%ED%95%B4%EC%95%BC-%ED%95%A0%EA%B9%8CFeat-%EA%B3%A0%EC%A0%95-%EC%86%8C%EC%88%98%EC%A0%90-vs-%EB%B6%80%EB%8F%99-%EC%86%8C%EC%88%98%EC%A0%90)
* [MAMP의 MySQL 포트가 3306이 아닌데도 localhost라고만 적었을 때 접속이 되는 이유 – 형우의 웹개발](https://mytory.net/archives/16179)
* [VARCHAR vs. TEXT, 뭐가 다를까? | 요즘IT](https://yozm.wishket.com/magazine/detail/2726/)
* [CHAR vs. VARCHAR, 언제 어떻게 써야 할까? | 요즘IT](https://yozm.wishket.com/magazine/detail/2717/)
* [MySQL 의 Geospatial Index (1) – Changhyun Lee – software engineer](https://chang12.github.io/mysql-geospatial-index-1/)
* [스마트스토어센터 Oracle에서 MySQL로의 무중단 전환기](https://d2.naver.com/helloworld/6512234)

## MySQL backup dump
* [MySQL 백업 mysqldump 사용법 정리](http://qnfmfmd.tistory.com/76)
* [**장애와 관련된 XtraBackup 적용기 | 우아한형제들 기술블로그**](https://techblog.woowahan.com/2576/) mysqldump, mysqlbinlog, XtraBackup
* [The MySQL Clone Wars: Plugin vs. Percona XtraBackup - Percona Database Performance Blog](https://www.percona.com/blog/2021/01/19/the-mysql-clone-wars-plugin-vs-percona-xtrabackup/)
* [How to Migrate MySQL to AWS RDS Using mysqldump and DMS | by Phoebe Baek | Cloud Villains | Sep, 2022 | Medium](https://medium.com/@phoebebaek/how-to-migrate-mysql-to-aws-rds-using-dump-and-dms-1db41eb248b7)
* [NodeJS로 mysqldump하고 진행 상황 확인하기 · 감자도스](https://blog.potados.com/dev/nodejs/show-mysqldump-progress-on-nodejs/)
* [mysqldump 표준 출력을 곧장 gpg 암호화해 파일로 저장하는 bash 명령 | 웹으로 말하기](https://mytory.net/archives/14523)
* [MySQL DB 백업 복원 mysqldump 명령어](https://ponyozzang.tistory.com/657)
* [Xtrabackup으로 DB 복구하기](https://jojoldu.tistory.com/469)

## MySQL Library
* [MySQL/MariaDB의 inet_aton/ntoa 함수를 대체할 JPA 컨버터](https://javacan.tistory.com/entry/inet-aton-ntoa-jpa-converter)
* [New Logical Backup and Restore Utilities in the MySQL Shell](https://elephantdolphin.blogspot.com/2020/07/new-logical-backup-and-restore.html)
* [ADT - Almighty Data Trasmitter](http://tech.kakao.com/2016/06/27/opensource-5-adt/)
  * [github.com/kakao/adt](https://github.com/kakao/adt)
* [awesome-mysql-performance: 🔥 A curated list of awesome links related to MySQL / MariaDB / Percona performance tuning](https://github.com/Releem/awesome-mysql-performance)
* [binlog2sql: Binlog to Raw SQL Conversion and Point In Time Recovery - Percona Database Performance Blog](https://www.percona.com/blog/2020/07/09/binlog2sql-binlog-to-raw-sql-conversion-and-point-in-time-recovery/)
* [canal: 阿里巴巴 MySQL binlog 增量订阅&消费组件](https://github.com/alibaba/canal)
  * [Introduction · alibaba/canal Wiki](https://github.com/alibaba/canal/wiki/Introduction)
* [Directus - Free and Open-Source MySQL Database GUI](http://getdirectus.com/)
  * [A Terminal Client for MySQL with AutoCompletion and Syntax Highlighting](https://github.com/dbcli/mycli)
* [DocStore: Document Database for MySQL at Facebook](https://www.percona.com/live/mysql-conference-2015/sites/default/files/slides/Facebook%20DocStore%20Percona%202015.pdf)
* [dolphie: An intuitive feature-rich top tool for monitoring MySQL in real time](https://github.com/charles-001/dolphie)
* [fluent-plugin-mysql-replicator](https://github.com/y-ken/fluent-plugin-mysql-replicator)
* [Galera Cluster](http://galeracluster.com/)
* [**Maxwell's daemon, an application that reads MySQL binlogs and writes row updates to Kafka, Kinesis, RabbitMQ, Google Cloud Pub/Sub, or Redis as JSON**](http://maxwells-daemon.io/)
  * 실시간에 가깝게 mysql 데이터를 가져옴. 텅스텐CDC에 비해 안정적이며, 필요한 테이블/컬럼 단위로 필터링 처리 가능
  * [MySQL CDC, Streaming Binary Logs and Asynchronous Triggers](https://www.percona.com/blog/2016/09/13/mysql-cdc-streaming-binary-logs-and-asynchronous-triggers/)
* [Herb: Multi-DC Replication Engine for Uber’s Schemaless Datastore](https://eng.uber.com/herb-datacenter-ggnggnggreplication/)
  * Uber가 2014년부터 진행했던 프로젝
  * MySQL로 Schemaless를 구현한 사례, Herb라는 센터간 복제 기술로 고도화 실현
  * [Designing Schemaless, Uber Engineering’s Scalable Datastore Using MySQL](https://eng.uber.com/schemaless-part-one/)
  * [The Architecture of Schemaless, Uber Engineering’s Trip Datastore Using MySQL](https://eng.uber.com/schemaless-part-two/)
  * [Using Triggers On Schemaless, Uber Engineering’s Datastore Using MySQL](https://eng.uber.com/schemaless-part-three/)
* [mycli - Mycli is a command line interface for MySQL, MariaDB, and Percona with auto-completion and syntax highlighting](http://mycli.net/)
* [mysos - MySQL on Mesos (moving to the Apache Incubator)](https://github.com/twitter/mysos)
* [mysql-5.6 - Facebook's branch of the Oracle MySQL v5.6 database. This includes MyRocks](https://github.com/facebook/mysql-5.6)
  * [MyRocks: A space- and write-optimized MySQL database](https://code.facebook.com/posts/190251048047090)
  * [How Facebook Migrated a Database From InnoDB to MyRocks](https://code.facebook.com/posts/1478526992216557/migrating-a-database-from-innodb-to-myrocks)
    * 페이스북은 InnoDB를 MyRocks로 스토리지 엔진을 전환하여 스토리지 사용량을 절반으로 감소
    * InnoDB를 MyRocks로 마이그레이션하는 방법을 간단히 설명
  * [Migrating Messenger storage to optimize performance](https://code.facebook.com/posts/201318390519340/migrating-messenger-storage-to-optimize-performance/) facebook messenger storage, migration from HBase to MyRocks
  * [How Facebook Accelerates SQL at Extreme Scale](https://www.datanami.com/2020/08/31/how-facebook-accelerates-sql-at-extreme-scale/)
* mysqlsh
  * [mysql shell(mysqlsh) 설치 및 사용방법](https://myinfrabox.tistory.com/213)
  * [JavaScript Mode and the MySQL Shell (aka Extending the MySQL Shell with JavaScript) - YouTube](https://www.youtube.com/watch?v=vf0UEZd3KII)
* [MySQLTuner-perl](https://github.com/major/MySQLTuner-perl)
* [OSC - Facebook releases a new OnlineSchemaChange tool written in Python](http://www.eversql.com/facebook-releases-a-new-onlineschemachange-tool-written-in-python/)
* [Planche - Javascript MySQL GUI Client Tool](https://github.com/plancheproject/planche)
* [PlanetScale: The world’s most advanced database platform](https://planetscale.com/)
  * [플래닛스케일 리뷰 | 수평 확장 가능한 마이SQL 호환 서버리스 DB 플랫폼 - ITWorld Korea](https://www.itworld.co.kr/news/207029)
  * [학습을 위한 온라인 무료 DB – PlanetScale](https://trycoding.notion.site/trycoding/DB-PlanetScale-0953d909bf814e85b84509b5a08df238)
* [python-mysql-replication](https://github.com/noplay/python-mysql-replication)
* Sysbench [How to Install and Use Sysbench - mortensi](https://www.mortensi.com/2021/06/how-to-install-and-use-sysbench/)
* [TiDB is a distributed SQL database compatible with MySQL protocol](https://github.com/pingcap/tidb#run-as-mysql-protocol-server)
* [Yahoo MySQL Performance Analyzer](https://github.com/yahoo/mysql_perf_analyzer)
* [vitess - A database clustering system for horizontal scaling of MySQL](https://vitess.io/)
  * [Vitess를 활용한 Slack의 데이터스토어 스케일링 | GeekNews](https://news.hada.io/topic?id=3392)
* [WeSQL is an innovative MySQL distribution that adopts a compute-storage separation architecture, with storage backed by S3 (and S3-compatible systems). It can run on any cloud, ensuring no vendor lock-in](https://github.com/wesql/wesql)
  * [WeSQL - S3를 저장소로 사용하는 혁신적인 MySQL 배포판 | GeekNews](https://news.hada.io/topic?id=18058)

## MySQL Sharding
* [Sharding Pinterest: How we scaled our MySQL fleet](https://medium.com/@Pinterest_Engineering/sharding-pinterest-how-we-scaled-our-mysql-fleet-3f341e96ca6f)
* [MySQL Sharding에 관한 자료들](http://jason-heo.github.io/mysql/2015/08/23/mysql-sharding.html)
* [Apache ShardingSphere를 이용한 DB Sharding](https://blog.naver.com/asei/221511101848)
* [LINE Manga 데이터베이스 샤딩 – 서버 엔지니어 편](https://engineering.linecorp.com/ko/blog/line-manga-server-side/)
* [LINE Manga 데이터베이스 샤딩 – 데이터베이스 엔지니어 편](https://engineering.linecorp.com/ko/blog/line-manga-database/)
* [ADT 활용 예제1: MySQL Shard 데이터 재분배](http://tech.kakao.com/2016/07/01/adt-mysql-shard-rebalancing/)
* [The Next Evolution of the Database Sharding Architecture](https://www.infoq.com/articles/next-evolution-of-database-sharding-architecture/)
* [kingshard - A high-performance MySQL proxy](https://github.com/flike/kingshard)
* [proxysql.com](https://proxysql.com/)
  * [IMDEV 2023 ProxySQL로 DB 문제 해결하기 - YouTube](https://www.youtube.com/watch?v=a4tUa5cs9kk)

# Oracle
* [오라클 중복레코드삭제 다양한 방법들 - YouTube](https://www.youtube.com/watch?v=3XZiBjFOSAs)
* [Oracle | 오라클 클라우드 ATP Database 생성과 DBeaver로 연결하기](https://yian.tistory.com/49)
* [10 Best Online Courses to Learn Oracle and PL/SQL for Beginners | HackerNoon](https://hackernoon.com/10-best-online-courses-to-learn-oracle-and-plsql-for-beginners)
* [Is Null, Not Null 왜 사용할까요? 당신의 조건문은 Null에 안전한가요?](https://devjong12.tistory.com/30)
* examples
  * [practice - oracle queries](https://gist.github.com/hyunjun/20ed3f7d381fadc17dbe)
* Pro\*C
  * [Pro\*C 목차 및 sample](http://downman.tistory.com/31)

# ORM Object Relational Mapping
* [ORM: DB에 오브젝트를 쓰자](https://www.youtube.com/watch?v=B6iOqljc7U8)
* [ORM: The Good, the Great, and the Ugly - YouTube](https://www.youtube.com/watch?v=3EvhK7-DlZA)

# Percona
* [SQL Query Formatting Tools Used At Percona](https://www.percona.com/blog/2020/06/03/sql-query-formatting-tools-used-at-percona/)
* [The Steps Involved in Creating a Percona Product Release - Percona Database Performance Blog](https://www.percona.com/blog/2021/03/25/the-steps-involved-in-creating-a-percona-product-release/)
* [An Overview of Sharding in PostgreSQL and How it Relates to MongoDB's - Percona Database Performance Blog](https://www.percona.com/blog/2019/05/24/an-overview-of-sharding-in-postgresql-and-how-it-relates-to-mongodbs/)
* PMM
  * [Percona Monitoring and Management Documentation](https://www.percona.com/doc/percona-monitoring-and-management/index.html)
  * [PMM 이야기 1편 – INTRO](http://gywn.net/2018/03/pmm-intro/)
  * [PMM팁1탄! MySQL을 READ-ONLY 기준으로 표기해보기](http://gywn.net/2019/01/pmm-tip1-classified-by-mysql-readonly/)
  * [Percona PMM - A beginner's guide - Vlad Mihalcea](https://vladmihalcea.com/percona-pmm-beginner-guide/)
* [pstress - Database concurrency and crash recovery testing tool](https://github.com/Percona-QA/pstress)
* pt-online-schema-change
  * [Percona pt-online-schema-change 설치 및 사용하기](https://jojoldu.tistory.com/358)
  * [소소한 데이터 이야기 – pt-online-schema-change 편 -](http://gywn.net/2017/08/small-talk-pt-osc/)
  * [MySQL Online-DDL. 당근 마켓의 서비스는 쉬지 않고 발전하고 있어요. 하지만 이런… | by Sunguck Lee | 당근마켓 팀블로그 | Apr, 2022 | Medium](https://medium.com/daangn/mysql-online-ddl-faf47439084c)

# PostgreSQL
* [한국 PostgreSQL](http://postgresql.kr)
* [Postgres Guide](http://www.postgresguide.com/)
* [PostgreSQL Tutorial](http://www.postgresqltutorial.com/)
* [practice - unique index and null](https://gist.github.com/hyunjun/0b0b90a536a623edc59da4605adbf519#file-unique_index_and_null-md)
* [Scaling out PostgreSQL for CloudFlare Analytics using CitusDB](https://blog.cloudflare.com/scaling-out-postgresql-for-cloudflare-analytics-using-citusdb/)
* [Postgres CLI with autocompletion and syntax highlighting](https://github.com/amjith/pgcli)
* [Managing big enough data in postgres](http://blog.tarkalabs.com/2015/04/16/managing-big-enough-data-in-postgres/)
* [Bottled Water: Real-time integration of PostgreSQL and Kafka](http://blog.confluent.io/2015/04/23/bottled-water-real-time-integration-of-postgresql-and-kafka/)
* [Compressing PostgreSQL JSONB data 12x using cstore_fdw](https://www.citusdata.com/blog/14-marco/156-compressing-jsonb-using-cstore-fdw)
* [How to update objects inside JSONB arrays with PostgreSQL](https://medium.freecodecamp.org/how-to-update-objects-inside-jsonb-arrays-with-postgresql-5c4e03be256a)
* [Using PostgreSQL JSONB with Go](https://morioh.com/p/c0009e8ffe11)
* [Migrating to JSON in PostgreSQL](https://developer.s24.com/blog/migrating-json-postgresql.html)
* [Unleash the Power of Storing JSON in Postgres](https://blog.codeship.com/unleash-the-power-of-storing-json-in-postgres/)
* [Cut Out the Middle Tier: Generating JSON Directly from Postgres](https://blog.crunchydata.com/blog/generating-json-directly-from-postgres)
* [PostgreSQL vs. MS SQL Server](http://www.pg-versus-ms.com/)
* [A simple relational data access tool for NodeJS](https://github.com/robconery/massive-js)
* [A proof of concept MongoDB clone built on Postgres](https://github.com/JerrySievert/mongolike)
* [Zero-downtime Postgres migrations - the hard parts](https://gocardless.com/blog/zero-downtime-postgres-migrations-the-hard-parts/)
* [Move fast and migrate things: how we automated migrations in Postgres | by Vineet Gopal | Benchling Engineering](https://benchling.engineering/move-fast-and-migrate-things-how-we-automated-migrations-in-postgres-d60aba0fc3d4)
* [Upsert Lands in PostgreSQL 9.5 – a First Look](http://www.craigkerstiens.com/2015/05/08/upsert-lands-in-postgres-9.5/)
* [Postgres UPSERT ON DUPLICATE and how other databases implement UPSERT](http://michaelroders.tumblr.com/post/119356965581/postgres-upsert-on-duplicate-and-how-other)
* [Postgres Job Queues & Failure By MVCC](https://brandur.org/postgres-queues)
* [PostgreSQL: the good, the bad, and the ugly](http://lwn.net/SubscriberLink/645020/e1ba36cff8248df0/)
* [Postgres pushes past MySQL in developer hearts](http://www.techrepublic.com/article/postgres-pushes-past-mysql-in-developer-hearts/)
* [Stopping Time In PostgreSQL](http://blog.thefourthparty.com/stopping-time-in-postgresql/)
* [POSTGIS 2.2 LEVERAGING POWER OF POSTGRESQL 9.5](http://www.postgresonline.com/journal/archives/350-PostGIS-2.2-leveraging-power-of-PostgreSQL-9.5.html)
* [SQL MERGE is quite distinct from UPSERT](http://www.postgresql.org/message-id/CAM3SWZRP0c3g6+aJ=YYDGYAcTZg0xA8-1_FCVo5Xm7hrEL34kw@mail.gmail.com)
* [Watch "Fashion Is Hard. PostgreSQL Is Easy"](https://tech.zalando.com/blog/watch-fashion-is-hard-postgresql-is-easy/)
* [Discovering the Computer Science Behind Postgres Indexes](http://blog.codeship.com/discovering-computer-science-behind-postgres-indexes/)
* [Introducing HypoPG, hypothetical indexes for PostgreSQL](http://www.postgresql.org/about/news/1593/)
* [How to scale PostgreSQL on Amazon RDS using pg_shard](https://www.citusdata.com/blog/14-marco/178-scaling-out-postgresql-on-amazon-rds-using-masterless-pg-shard)
* [High Availability for PostgreSQL, Batteries Not Included](https://www.compose.io/articles/high-availability-for-postgresql-batteries-not-included/)
* [High availability and scalable reads in PostgreSQL](https://blog.timescale.com/scalable-postgresql-high-availability-read-scalability-streaming-replication-fb95023e2af)
* [Making Postgres and Elasticsearch work together like it's 2015](https://github.com/zombodb/zombodb)
* [Documenting Your PostgreSQL Database](http://www.craigkerstiens.com/2013/07/29/documenting-your-postgres-database/)
* [Harnessing Postgres race conditions](https://www.lirbank.com/harnessing-postgres-race-conditions)
  * [Harnessing Postgres race conditions | 박상길](https://www.linkedin.com/posts/%EC%83%81%EA%B8%B8-%EB%B0%95-b6ab145a_harnessing-postgres-race-conditions-activity-7432913371550789632-jrhc)
* [Transaction ID Wraparound in Postgres](http://blog.getsentry.com/2015/07/23/transaction-id-wraparound-in-postgres.html)
* [Making Postgres Bloom](http://www.pipelinedb.com/blog/making-postgres-bloom)
* [POSTGRESQL: A FULL TEXT SEARCH ENGINE - PART 1](http://shisaa.jp/postset/postgresql-full-text-search-part-1.html)
* [Full-Text Search Battle: PostgreSQL vs Elasticsearch | sudo README](https://rocky.dev/full-text-search)
* [Postgres Full-Text Search: A Search Engine in a Database](https://www.crunchydata.com/blog/postgres-full-text-search-a-search-engine-in-a-database)
* [PostgreSQL 9.5 New Features With Examples](http://h30507.www3.hp.com/hpblogs/attachments/hpblogs/Japan-Enterprise-Topics/124/1/PostgreSQL%209.5%20New%20Features%20English%2020150807-1.pdf)
* ["Big data" features coming in PostgreSQL 9.5](http://lwn.net/Articles/653411/)
* [Scaling out PostgreSQL at CloudFlare with CitusDB](https://www.citusdata.com/blog/19-ozgun/148-scaling-out-postgresql-at-cloudflare-with-citusdb)
* [Aquameta Layer 0: meta - Writable System Catalog for PostgreSQL](http://blog.aquameta.com/2015/08/29/intro-meta/)
* [PostgreSQL Magic](http://goto.project-a.com/postgresql-magic/)
* [PostgreSQL, pg_shard, and what we learned from our failures](https://www.citusdata.com/blog/19-ozgun/265-postgresql-pgshard-and-what-we-learned-our-failures)
* [A few PostgreSQL tricks](http://blog.endpoint.com/2015/01/a-few-postgresql-tricks.html)
* [PostgreSQL replication with Londiste from Skytools 3](https://blog.lateral.io/2015/09/postgresql-replication-with-londiste-from-skytools-3/)
* [Multi-Master Replication Solutions for PostgreSQL](https://www.percona.com/blog/2020/06/09/multi-master-replication-solutions-for-postgresql/)
* [EXPLAIN - explained](http://jberkus.github.io/explain_explained/index.html)
* [PostgreSQL EXPLAIN — pgMustard](https://www.pgmustard.com/docs/explain)
* [EXPLAIN ANALYZE in PostgreSQL and how to interpret it - Cybertec](https://www.cybertec-postgresql.com/en/how-to-interpret-postgresql-explain-analyze-output/)
* [PostgreSQL Foreign Data Wrappers](https://www.kentik.com/postgresql-foreign-data-wrappers/)
* [PostgreSQL Monitoring Cheatsheet](http://russ.garrett.co.uk/2015/10/02/postgres-monitoring-cheatsheet/)
* [PostgreSQL - A Platform for Multiple Sources Data Retrieval](https://abdulyadi.files.wordpress.com/2015/10/presentation.pdf)
* [다우기술, 포스트그레스 한국어 메뉴얼 공식 오픈](http://www.venturesquare.net/715186)
* [PostgreSQL 업그레이드 이야기](http://nrise.github.io/2016/08/19/upgradedatabase/)
* [Getting PostgreSQL transactions under control with SQLAlchemy](http://layer0.authentise.com/getting-postgresql-transactions-under-control-with-sqlalchemy.html)
* [MySQL vs PostgreSQL - Why you shouldn't use MySQL](https://www.youtube.com/watch?v=emgJtr9tIME)
* [PostgreSQL Schema를 MySQL로 마이그레이션 시켜보자](https://donghun.dev/PostgreSQL-To-MySQL)
* [PostgreSQL 9.6 Parallel Query & FDW](http://www.popit.kr/postgresql-9-6-parallel-query-fdw/)
* [Parallel queries in PostgreSQL - Percona Database Performance Blog](https://www.percona.com/blog/2019/02/21/parallel-queries-in-postgresql/)
* [PostgreSQL Exercises](https://pgexercises.com/)
* [PostgreSQL에 실시간 기능 도입하기](https://realm.io/kr/news/making-postgresql-realtime/)
* [The Night the PostgreSQL IDs Ran Out](https://hackernoon.com/the-night-the-postgresql-ids-ran-out-9430a2dbb895)
* [구식 포스트그레SQL이 다시 유행하는 이유](http://www.itworld.co.kr/news/107495)
* [Modern, native tool for relational database](https://medium.com/tableplus/modern-native-tool-for-relational-database-79efc35b647d)
* PostgreSQL 11 – Server-side Procedures
  * [Part 1](https://blog.2ndquadrant.com/postgresql-11-server-side-procedures-part-1/)
  * [Part 2](https://blog.2ndquadrant.com/postgresql-11-server-side-procedures-part-2/)
* [PostgreSQL 파티션 테이블](http://postgresql.kr/blog/postgresql_partition_table.html)
* [Five Things You Didn’t Know About PostgreSQL](https://vimeo.com/43536445)
* [How to scale PostgreSQL 10 using table inheritance and declarative partitioning](https://blog.timescale.com/scaling-partitioning-data-postgresql-10-explained-cd48a712a9a1)
* [Postgres as the Substructure for IoT and the Next Wave of Computing](https://blog.timescale.com/postgres-accidental-iot-platform-timescaledb-postgresql-time-series-data-7983d28da5af)
* [PostgreSQL 11 Partitioning Improvements](https://pgdash.io/blog/partition-postgres-11.html) PostgreSQL 11에서 파티셔닝에 관련하여 향상된 기능 소개
* [**How to build a PostgreSQL database to store tweets - Learning how to stream from Twitter API**](https://towardsdatascience.com/how-to-build-a-postgresql-database-to-store-tweets-1be9c1d48c7)
* [Bye bye Mongo, Hello Postgres](https://www.theguardian.com/info/2018/nov/30/bye-bye-mongo-hello-postgres)
  * Guardian에서 MongoDB에서 Postgres로 마이그레이션한 스토리
  * 데이터베이스 API Call을 복제하여 구 개의 데이터베이스서 실행하고 로깅을 하는 방법을 포함하여 데이터베이스 롤아웃 및 마이그레이션 작업 과정
* [The Internals of PostgreSQL for database administrators and system developers](http://www.interdb.jp/pg/index.html)
* [Lessons learned scaling PostgreSQL database to 1.2bn records/month](https://medium.com/@gajus/lessons-learned-scaling-postgresql-database-to-1-2bn-records-month-edc5449b3067)
* [Parallelism in PostgreSQL](https://www.percona.com/blog/2019/07/30/parallelism-in-postgresql/)
* [Postgres Handles More Than You Think](https://www.infoq.com/articles/postgres-handles-more-than-you-think/)
* [NoSQL과RDBMS 중 적합한 데이터베이스 선택하기(feat.인스타그램DB)](https://mustread.tistory.com/5)
* [Comparison of JOINS: MongoDB vs. PostgreSQL](https://www.enterprisedb.com/blog/comparison-joins-mongodb-vs-postgresql)
* [Oracle vs PostgreSQL: First Glance](https://rolkotech.blogspot.com/2020/05/oracle-vs-postgresql.html)
* [PostgreSQL vs. Oracle: Difference in Costs, Ease of Use & Functionality | by Kristi Anderson | Jul, 2020 | Medium](https://medium.com/@kristi.anderson/postgresql-vs-oracle-difference-in-costs-ease-of-use-functionality-642638152509)
* [How to Install Postgres 12](https://www.youtube.com/watch?v=tXFnplU0ous)
* [윈도우에 PostgreSQL 설치하기 - 로스카츠의 AI 머신러닝](https://losskatsu.github.io/it-infra/postgresql-win/)
* [A multi-node, elastic, petabyte scale, time-series database on Postgres for free (and more ways we are investing in our community)](https://blog.timescale.com/blog/multi-node-petabyte-scale-time-series-database-postgresql-free-tsdb/)
* [How one word in PostgreSQL unlocked a 9x performance improvement](https://jlongster.com/how-one-word-postgresql-performance)
* [How to Scale Postgres - Automation, Tuning & Sharding - Speaker Deck](https://speakerdeck.com/lfittl/how-to-scale-postgres-automation-tuning-and-sharding)
* [Herding elephants: Lessons learned from sharding Postgres at Notion](https://www.notion.so/blog/sharding-postgres-at-notion)
* [Types of Indexes in PostgreSQL - Highgo Software Inc](https://www.highgo.ca/2020/06/22/types-of-indexes-in-postgresql/)
* [B-tree indexes - learn more about the heart of PostgreSQL - YouTube](https://www.youtube.com/watch?v=n5-xEEQFqPY)
* [Why We Switched From MongoDB to PostgresSQL](https://amasad.me/gpt_post)
* [PSQL TIMESTAMP/AT TIME ZONE 바로 알기 · Billo Park](https://blog.billo.io/devposts/psql_at_time_zone/)
* [psql command line tutorial and cheat sheet | postgres](https://tomcam.github.io/postgres/)
* [Handling NULL Values in PostgreSQL - Percona Database Performance Blog](https://www.percona.com/blog/2020/03/05/handling-null-values-in-postgresql/)
* [PostgreSQL의 슬로우 쿼리에 대처하기 | Hyperconnect Tech Blog](https://hyperconnect.github.io/2020/08/31/improve-slow-query.html)
* [Why PostgreSQL WAL Archival is Slow - Percona Database Performance Blog](https://www.percona.com/blog/2020/09/09/why-postgresql-wal-archival-is-slow/)
* [Lessons Learned from Running Postgres 13: Better Performance, Monitoring & More](https://pganalyze.com/blog/postgres13-better-performance-monitoring-usability)
* [Mastering PostgreSQL Administration](https://momjian.us/main/writings/pgsql/administration.pdf)
* [PostgreSQL 13 Features Distilled. Index optimization, incremental… | by Kovid Rathee | Sep, 2020 | Towards Data Science](https://towardsdatascience.com/postgresql-13-features-distilled-c0c0adcfa020)
* [Improving Postgres Connection Scalability: Snapshots - Microsoft Tech Community](https://techcommunity.microsoft.com/t5/azure-database-for-postgresql/improving-postgres-connection-scalability-snapshots/ba-p/1806462)
* [Postgres Observability](https://pgstats.dev/)
* [Stored Procedures as a backend. or “How we got rid of Django and whole… | by Oleg Zech | Oct, 2020 | Medium](https://gnuhost.medium.com/stored-procedures-as-a-backend-c5d2db452fc2)
* [BLOB cleanup in PostgreSQL - CYBERTEC | Data Science & PostgreSQL](https://www.cybertec-postgresql.com/en/blob-cleanup-in-postgresql/)
* [PostgreSQL Database Security: What You Need To Know - Percona Database Performance Blog](https://www.percona.com/blog/2021/01/04/postgresql-database-security-what-you-need-to-know/)
* [Removing PostgreSQL Bottlenecks Caused by High Traffic - Percona Database Performance Blog](https://www.percona.com/blog/2020/05/29/removing-postgresql-bottlenecks-caused-by-high-traffic/)
* [Five Easy to Miss PostgreSQL Query Performance Bottlenecks](https://pawelurbanek.com/postgresql-query-bottleneck)
* [Migrating From Oracle to PostgreSQL - What You Should Know | Severalnines](https://severalnines.com/database-blog/migrating-oracle-postgresql-what-you-should-know)
* [A Complete Guide to SQL Triggers in PostgreSQL - DB Tracking Example](https://blog.arctype.com/learn-sql-triggers/)
* [Talking to Postgres Through Java 16 Unix-Domain Socket Channels - Gunnar Morling](https://www.morling.dev/blog/talking-to-postgres-through-java-16-unix-domain-socket-channels/)
* [Role of Foreign Data Wrappers in Migrations to PostgreSQL](https://www.migops.com/blog/2021/02/15/role-of-foreign-data-wrappers-in-migrations-to-postgresql/)
* [Change Data Capture in Postgres With Debezium](https://info.crunchydata.com/blog/postgres-change-data-capture-with-debezium)
* [Postgres regex search over 10,000 GitHub repositories (using only a Macbook)](https://devlog.hexops.com/2021/postgres-regex-search-over-10000-github-repositories)
* [Faster data migrations in Postgres](https://www.citusdata.com/blog/2021/02/20/faster-data-migrations-in-postgres/)
* [PostgreSQL on ARM-based AWS EC2 Instances: Is It Any Good? - Percona Database Performance Blog](https://www.percona.com/blog/2021/01/22/postgresql-on-arm-based-aws-ec2-instances-is-it-any-good/)
* [PostgreSQL: Asynchronous and "direct" IO support for PostgreSQL](https://www.postgresql.org/message-id/20210223100344.llw5an2aklengrmn@alap3.anarazel.de)
* [PostgreSQL 데이터 Client에서 KST로 확인하기 (feat. DataGrip)](https://jojoldu.tistory.com/567)
* [Setting up Streaming Replication in PostgreSQL 13 and Streaming Replication Internals - MigOps](https://www.migops.com/blog/2021/03/31/setting-up-streaming-replication-in-postgresql-13-and-streaming-replication-internals/)
* [BRIN Index for PostgreSQL: Don't Forget the Benefits - Percona Database Performance Blog](https://www.percona.com/blog/2019/07/16/brin-index-for-postgresql-dont-forget-the-benefits/)
* [10 Things I Hate About PostgreSQL | by Rick Branson | Medium](https://rbranson.medium.com/10-things-i-hate-about-postgresql-20dbab8c2791)
* [PostgreSQL Security Hardening | Teleport](https://goteleport.com/blog/securing-postgres-postgresql/)
* [PostgreSQL RDS Slow 쿼리 Slack으로 알람 보내기](https://jojoldu.tistory.com/570)
* [Using PostgreSQL as a Data Warehouse](https://www.narrator.ai/blog/using-postgresql-as-a-data-warehouse/)
  * [PostgreSQL을 데이터 웨어하우스로 사용하기 | GeekNews](https://news.hada.io/topic?id=4239)
* [Mac에 PostgreSQL없이 PSQL만 설치하기](https://jojoldu.tistory.com/574)
* [large csv to postgresql](https://gist.github.com/TimDSChoi/ca30197f502e3ff5c0743c8d46a48449) 대용량 csv를 입력하는 예(문제가 있음)
* [An early look at Postgres 14: Performance and Monitoring Improvements](https://pganalyze.com/blog/postgres-14-performance-monitoring)
* [Hierarchical Structures in PostgreSQL](https://hoverbear.org/blog/postgresql-hierarchical-structures/)
* [Globally Distributed Postgres · Fly](https://fly.io/blog/globally-distributed-postgres/)
* [Let's build a distributed Postgres proof of concept | notes.eatonphil.com](https://notes.eatonphil.com/distributed-postgres.html)
* [PostgreSQL, Memory and the Cloud™ · Alexander Sosna](https://sosna.de/posts/pgaas-memory-overcommit/)
* [PostgreSQL에서 Order By가 선적용되는 슬로우 쿼리 해결책](https://jojoldu.tistory.com/596)
* [Five Things You Didn't Know About PostgreSQL | Kevin's Blog](https://blog.kevinlee.io/blog/2012/08/25/five-things-you-didnt-know-about-postgresql/)
* [PostgreSQL 서버 관리자 지침서](https://docs.google.com/document/u/2/d/e/2PACX-1vTDZ9xHfw301ADVShOtjrcVHyqwS6HMfrNfRA_qRT5NTik25yyc9x1DJPyb6t5eTNAiCiQbNULS4tId/pub)
* [PostgreSQL 14 on Kubernetes (with examples!)](https://blog.crunchydata.com/blog/postgresql-14-on-kubernetes)
* [Announcing Open Source Babelfish for PostgreSQL: An Accelerator for SQL Server Migration · Babelfish](https://babelfishpg.org/blog/releases/2021/10/babelfish-launch/)
* [AWS Announces the General Availability and Open Sourcing of Babelfish for PostgreSQL](https://www.infoq.com/news/2021/11/babelfish-postgresql-oss-ga/)
* [Bringing Kafka based architecture to the next level using simple PostgreSQL tables | by Sixfold Tech Blog | Oct, 2021 | Medium](https://sixfold.medium.com/bringing-kafka-based-architecture-to-the-next-level-using-simple-postgresql-tables-415f1ff6076d)
* [엔터프라이즈DB, ‘포스트그레SQL 14’ 발표··· "하이엔드 워크로드 지원" - CIO Korea](https://www.ciokorea.com/news/210274)
* [Lesser Known PostgreSQL Features | Haki Benita](https://hakibenita.com/postgresql-unknown-features)
* [Postgres HA: roles are dynamic](https://tapoueh.org/blog/2021/12/postgres-ha-roles-are-dynamic/)
* [Postgres is a great pub/sub & job server](https://webapp.io/blog/postgres-is-the-answer/)
* [여러컬럼으로 Join 맺어야할 경우의 인덱스](https://jojoldu.tistory.com/628)
* [PostgreSQL Nested Loop Join을 HashJoin으로 개선하기](https://jojoldu.tistory.com/784)
* [신입 개발자의 인덱스 장애 회고담 | Onepredict Engineering](https://onepredict.github.io/failure-retrospective/)
* [PostgreSQL (Aurora) 10 vs 11 버전 성능 비교](https://jojoldu.tistory.com/630)
* [PostgreSQL 11 에서의 add column not null & default 성능 개선](https://jojoldu.tistory.com/731)
* [NodeJS 와 PostgreSQL Query Timeout](https://jojoldu.tistory.com/631)
* [NOT IN 쿼리 성능 개선하기 (PostgreSQL)](https://jojoldu.tistory.com/632)
* [NodeJS 와 PostgreSQL Connection Pool](https://jojoldu.tistory.com/634)
* [Free Postgres Databases · Fly](https://fly.io/blog/free-postgres/)
* [Five Tips For a Healthier Postgres Database in the New Year](https://blog.crunchydata.com/blog/five-tips-for-a-healthier-postgres-database-in-the-new-year)
* [Slow Query 문제](https://bumbum.oopy.io/c459acf8-6ed8-43d0-9c14-655d3988b437)
* [The Internals of PostgreSQL : Introduction](https://www.interdb.jp/pg/)
* [How Postgres Stores Rows - Ketan Singh](https://ketansingh.me/posts/how-postgres-stores-rows/)
* [How we optimized PostgreSQL queries 100x | by Vadim Markovtsev | Mar, 2022 | Towards Data Science](https://towardsdatascience.com/how-we-optimized-postgresql-queries-100x-ff52555eabe)
* [blog.md](https://gist.github.com/jcoleman/1e6ad1bf8de454c166da94b67537758b)
  * Transactional DDL, Locking, Table Operations, Column Operations, Index Operations, Constraints, Enum Types, Bonus: Library for Ruby on Rails
* [Postgres everywhere | InfoWorld](https://www.infoworld.com/article/3655953/postgres-everywhere.html)
* [Faster Geospatial Enrichment](https://tech.marksblogg.com/faster-geospatial-enrichment.html)
* [How To Benchmark PostgreSQL Queries Well](https://www.tangramvision.com/blog/how-to-benchmark-postgresql-queries-well)
* [Speeding up sort performance in Postgres 15](https://www.citusdata.com/blog/2022/05/19/speeding-up-sort-performance-in-postgres-15/)
* [Postgres Handles More Than You Think](https://www.infoq.com/articles/postgres-handles-more-than-you-think/)
* [PostgreSQL 14 Internals : Postgres Professional](https://postgrespro.com/community/books/internals)
* [Postgres 15 improves UNIQUE and NULL - Blog @ RustProof Labs](https://blog.rustprooflabs.com/2022/07/postgres-15-unique-improvement-with-null)
* [Money operations with Node.js and PostgreSQL | by Alex Vasilyev | Jul, 2022 | Medium](https://luckylibora.medium.com/money-operations-with-node-js-and-postgresql-91d1f06ff263)
* [Postgres Tutorials | Crunchy Data](https://www.crunchydata.com/developers/tutorials)
* [Multi-tenant application architecture with Node.js — Express, and PostgreSQL | by Larbi Sahli | Jul, 2022 | Medium](https://medium.com/@larbisahli/multi-tenant-application-architecture-with-node-js-express-and-postgresql-3b94ea270a72)
* [Postgres System Columns Explained (ctid, xmin,xmax) - YouTube](https://www.youtube.com/watch?v=AveRgUrC7FM)
* [Postgres Architecture Explained - YouTube](https://www.youtube.com/watch?v=Q56kljmIN14)
* [Open sourcing our fork of PgBouncer](https://blog.cloudflare.com/open-sourcing-our-fork-of-pgbouncer/)
* [Just Use Postgres for Everything | Amazing CTO](https://www.amazingcto.com/postgres-for-everything/)
  * [그냥 Postgres를 모든 곳에 사용하세요 | GeekNews](https://news.hada.io/topic?id=8018)
* [PostgreSQL14 Memoize 성능 비교 (feat. 13 vs 14 Nested Loop)](https://jojoldu.tistory.com/700)
* [PostgreSQL 소개 및 설정 방법 (Nest.js 기준) : 네이버 블로그](https://m.blog.naver.com/gi_balja/223033188093)
* [20x faster than pgvector: introducing pg_embedding extension for vector search in Postgres and LangChain - Neon](https://neon.tech/blog/pg-embedding-extension-for-vector-search)
* [Why we replaced Pinecone with PGVector | by Jeffrey Ip | Nov, 2023 | Medium](https://medium.com/@jeffreyip54/why-we-replaced-pinecone-with-pgvector-2f679d253eba)
  * LLM 평가 인프라를 만드는 ConfidentAI에서 벡터 데이터베이스인 Pinecone을 쓰다가 PostgreSQL에서 벡터 검색을 지원하는 PGVector로 갈아탄 이유 설명
  * Pinecon은 PoC할 때는 편하지만 데이터 동기화 문제와 벡터랑 용량 제한으로 결국 확장성에 문제 발생
  * PGVector의 경우 HNWS 도입으로 성능이 좋아져서 Pinecone 대체 가능
* [Postgres as a search engine](https://anyblockers.com/posts/postgres-as-a-search-engine)
  * Postgres is a versatile tool that can be used to build a retrieval system with semantic, full-text, and fuzzy search capabilities
  * The author demonstrates how to combine these techniques: full-text search with tsvector, semantic search with pgvector, and fuzzy matching with pg_trgm, to create a robust search engine within Postgres
  * The author also discusses the use of Reciprocal Ranked Fusion (RRF) for merging results and the importance of understanding why something matched or not
  * The author also provides tips on tuning full text search, such as weighing tsvectors and adjusting for length. Additionally, the author suggests reranking with a cross-encoder model and boosting results to improve user experience
  * The author concludes by mentioning the limitations of Postgres and suggests alternative solutions
  * [Postgres를 검색엔진으로 활용하기 | GeekNews](https://news.hada.io/topic?id=16468)
* [벡터 데이터베이스는 잘못된 추상화임 | GeekNews](https://news.hada.io/topic?id=17501) pgai Vectorizer
* [PostgreSQL 11 에서의 add column not null & default 성능 개선](https://jojoldu.tistory.com/731)
* [postgres json 값 가져오기 방법으로 case 절을 리팩토링 해 봅시다. - Codingdog Blog](https://codingdog.pe.kr/2023/09/02/postgres-json-%EA%B0%92-%EA%B0%80%EC%A0%B8%EC%98%A4%EA%B8%B0-%EB%B0%A9%EB%B2%95%EC%9C%BC%EB%A1%9C-case-%EC%A0%88%EC%9D%84-%EB%A6%AC%ED%8C%A9%ED%86%A0%EB%A7%81-%ED%95%B4-%EB%B4%85%EC%8B%9C%EB%8B%A4/)
* [PostgreSQL 모든 View 의 접근 기록 테이블에 적재하기 (애플리케이션 변경 없이)](https://jojoldu.tistory.com/742)
* [How Cloudflare Was Able to Support 55 Million Requests per Second With Only 15 Postgres Clusters](https://newsletter.systemdesign.one/p/postgresql-scalability)
* [Postgres is Enough](https://gist.github.com/cpursley/c8fb81fe8a7e5df038158bdfe0f06dbb)
  * [PostgreSQL로 충분하다 | GeekNews](https://news.hada.io/topic?id=13231)
* [Wait... PostgreSQL can do WHAT? - YouTube](https://www.youtube.com/watch?v=VEWXmdjzIpQ)
  * [VidiGo Wait... PostgreSQL can do WHAT?](https://vidigo.ai//chatbot/summary/XwDdGOF3tinyXOD)
    * 2. PostgreSQL의 객체 관계형 데이터베이스로서의 특징
      * Postgresql은 객체 지향 개념과 복잡한 데이터 구조를 관계형 데이터베이스 디자인과 결합하여 다양한 네이티브 데이터 타입과 사용자 정의 타입을 지원
      * 게임 캐릭터와 같은 복잡한 데이터 구조를 저장하고 쿼리하는 데 필요한 기능 제공
      * 테이블 상속과 저장 프로시저를 포함한 객체 지향 프로그래밍의 핵심 개념을 구현하여 백엔드 애플리케이션으로부터 데이터 로직을 분리 가능
    * 3. PostgreSQL 확장성과 백엔드 스택 대체 가능성
      * Postgresql의 확장성 덕분에 캐싱, 메시지 큐, nosql 데이터베이스 등 백엔드 스택의 다양한 기술 대체 가능
      * Json 웹 토큰 생성, html 랜더링 등 다양한 작업을 위한 postgresql 확장 기능을 사용하여 인프라를 단순화, 유지 보수 용이
      * Rest api와 graphql 쿼리를 포함하여 거의 모든 백엔드 요구 사항을 충족시킬 수 있는 강력하고 신뢰할 수 있는 플랫폼으로서의 역할
  * [잠깐만요... PostgreSQL은 무엇을 할 수 있나요? | 완벽한 영상요약, 릴리스에이아이 | Lilys AI](https://lilys.ai/digest/391690?sId=VEWXmdjzIpQ)
    * 3.💻포스트그레SQL: 객체-관계형 데이터베이스 기능
      * 포스트그레SQL은 객체-관계형 데이터베이스로, 객체지향 개념과 관계형 데이터베이스 디자인 융합
      * 포스트그레SQL은 다양한 데이터 유형을 지원, 특히 날짜/시간, 네트워크 주소, 지오메트리 유형을 기본 제공
      * 또한 사용자 정의 유형을 정의하고 시스템에 내장된 것처럼 사용할 수 있어 효율적이며 유연한 데이터 관리가 가능
      * 예를 들어, 롤플레잉 게임의 캐릭터 데이터를 저장하기 위해 사용자 정의 유형을 만들어 테이블에 활용 가능
    * 5.💻PostgreSQL의 프로시저와 패키지로 *코드 실행*이 가능함.
      * 객체지향 프로그래밍은 코드와 데이터를 함께 묶는 것이라는 점을 간과해서는 안 됨
      * PostgreSQL은 코드를 데이터베이스에서 실행할 때 경쟁 상대보다 더 많은 기능 제공
      * 저장 프로시저에서 지원되는 프로그래밍 언어 목록을 확인하고 코드를 직접 실행하기 위해 언어 핸들러 활성화 필요
      * 또한 이를 위해 패키지 매니저가 필요한데, PostgreSQL 확장을 위한 패키지 매니저 존재. 시작 프로시저의 코드는 이미 테스트 데이터를 삽입
    * 6.💻PostgreSQL 기능과 저장 프로시저, 데이터베이스를 백엔드 응용프로그램에서 자유롭게 활용
      * PostgreSQL의 객체지향 기능과 저장 프로시저 덕분에 데이터베이스는 단순한 저장소가 아니라 백엔드 응용프로그램을 데이터 로직으로부터 해방 가능
      * 유저 관리와 같은 데이터 로직이 Posix 확장성의 도움으로 완전히 데이터베이스 내에서 자체 포함 가능
        * 해시 비밀번호 생성, JSON 웹 토큰, QR 코드 생성, 개인 데이터 익명화, 템플릿에서 HTML 렌더링 등 가능
      * PostgreSQL에 대해 배울수록 확장점이 어디에서나 있어 실제로 전체 백엔드로 대체할 수 있는 특징
      * PostgreSQL로 키-값 저장소를 쉽게 구축할 수 있으며, Redis와 같이 만료되는 값들을 가질 수 있도록 PG 크롬 익스텐션 설치
        * 포스티크, 데이터베이스에서 브로커 소프트웨어인 RabbitMQ를 단순하게 대체함으로써 사내 백엔드 작업 큐를 향상
    * 7.💻 MongoDB와 NoSQL 데이터베이스의 장점 및 PostgreSQL의 활용
      * PostgreSQL은 JSON 데이터 유형을 네이티브로 지원하며 SQL과 유사한 쿼리 언어 지원
      * NoSQL 데이터베이스는 SQL과 유사한 언어로 적응, Guardian과 같은 기업이 JSON 문서를 PostgreSQL로 옮길 경우
        * 디스크 공간이 더 많이 필요, 다른 기능들과의 통합 및 인프라 유지보수가 감소
      * PostgreSQL은 Apache AG 프로젝트를 이용해 그래프 데이터베이스로 변환 가능
      * 시계열 데이터에는 TimescaleDB를 활용하여 IoT 기기 메트릭을 모니터링하거나 사용자 활동 로그를 분석 가능
        * 또한 TimescaleDB는 Grafana와 원활하게 작동한다.
    * 8.💻텍스트 데이터 처리: Elasticsearch vs PostgreSQL Full-Text Search
      * 텍스트 데이터 검색 시 'like' 문이 아닌 검색 엔진 사용 필요
        * Elasticsearch는 불용어, 어간 추출 및 검색 결과 순위 매기기를 통해 유사 단어의 결과를 찾아 정렬
      * 일반적 백엔드 설정에서는 Elasticsearch가 이 기능을 담당
        * Elasticsearch는 다른 곳에서 데이터를 지속적으로 색인하고, PostgreSQL 데이터베이스와 통합하여 동일한 기능 제공 가능
      * PostgreSQL의 전체 텍스트 검색 기능을 통합하면 데이터 동기화가 필요 없음. 항상 최신 색인을 제공, 인프라가 단순화, 유지보수가 더 용이
      * 대부분의 프로젝트에서 Elasticsearch 클러스터를 실행하는 것은 과다하다고 생각하는 경우가 많음
    * 9.💻PostgreSQL로 데이터 검색 및 머신러닝 모델 실행, 백엔드 단순화
      * 텍스트 관련한 LLMs(대형 언어 모델)을 이용하여 open source LLM 모델을 쿼리하고, 데이터베이스 쪽에서 실행되는 챗봇을 상상
      * PostgreSQL을 사용하면 데이터베이스 테이블 생성, PostgreSQL이 역할 기반의 액세스 제어 처리, 저장 프로시저를 사용하여 단순 CRUD 이상 제공
      * PostgreSQL은 메시징, 메시지 대기열, 키-값 저장소, 객체 그래프 및 시계열 데이터 저장소, 전체 텍스트 검색 및 머신러닝 기능을 제공
      * 또한, PostgreSQL에서는 저장 프로시저를 단위 테스트 가능, 이를 통해 웹 프레임워크와 같은 방식으로 코드를 테스트 가능
    * 10.💻PostgreSQL과 GraphQL이 함께 동작하여 백엔드 인프라를 간소화
      * PostgreSQL에서는 PG GraphQL 확장 기능으로 데이터와 GraphQL 엔티티 간 투명한 매핑을 제공하여 단일 함수 호출로 GraphQL 쿼리를 실행 가능
      * PG GraphQL을 PostgREST와 결합하면 HTTP를 통해 GraphQL 쿼리를 실행 가능
      * Omni 프로젝트는 컨테이너 관리, S3 파일 저장 및 결제 지원까지 모두 PostgreSQL 내에서 관리하는 아이디어 추구
      * PostgreSQL은 ORM을 사용하여 백엔드 인프라를 더 간단하게 유지하고 이해하기 쉽게 만들거나 기업급 신뢰성 보장
      * 다른 데이터베이스나 검색 클러스터 대신 PostgreSQL로 긴 여정을 함께하며 프로젝트에 장기적인 혜택을 창출 가능
* [EC2에 PostgreSQL 설치 🐘 - YouTube](https://www.youtube.com/watch?v=0wfZJyCcljk)
* [Making a Postgres query 1,000 times faster - Mattermost](https://mattermost.com/blog/making-a-postgres-query-1000-times-faster/)
  * [Postgres 쿼리 1,000배 더 빠르게 만들기 | GeekNews](https://news.hada.io/topic?id=14930)
* [PostgreSQL 단일 테이블 컬럼을 최대한 활용하기](https://jojoldu.tistory.com/788)
* [How to Get the Most out of Postgres Memory Settings | Tembo](https://tembo.io/blog/optimizing-memory-usage)
  * [Postgres 메모리 설정을 최대한 활용하는 방법 | GeekNews](https://news.hada.io/topic?id=15540)
* [Maciej Walkowiak | PostgreSQL and UUID as primary key](https://maciejwalkowiak.com/blog/postgres-uuid-primary-key/)
  * [PostgreSQL와 UUID를 기본 키로 사용하는 것에 대해 | GeekNews](https://news.hada.io/topic?id=15713)
* [Full Text Search over Postgres: Elasticsearch vs. Alternatives - ParadeDB](https://blog.paradedb.com/pages/elasticsearch_vs_postgres) FTS
  * [Postgres에서의 전문 검색: Elasticsearch vs. 대체제들 | GeekNews](https://news.hada.io/topic?id=16311)
* [Just use Postgres](https://mccue.dev/pages/8-16-24-just-use-postgres)
  * [그냥 Postgres 쓰세요 | GeekNews](https://news.hada.io/topic?id=16365)
* [PostgreSQL: PostgreSQL 17 Released!](https://www.postgresql.org/about/news/postgresql-17-released-2936/)
  * [PostgreSQL 17 출시 | GeekNews](https://news.hada.io/topic?id=16950)
* [Postgres에서 PDF 전문 검색하기 | GeekNews](https://news.hada.io/topic?id=17535)
* [트랜잭셔널 메시징에도, 그냥 PostgreSQL 쓰세요 | 요즘IT](https://yozm.wishket.com/magazine/detail/2833/) PGMQ
* [PostgreSQL, 2024년 올해의 DBMS로 선정 | GeekNews](https://news.hada.io/topic?id=18751)
* [7+ million Postgres tables | Kailash Nadh | IndiaFOSS 2024 | FOSS United - YouTube](https://www.youtube.com/watch?v=xhi5Q_wL9i0)
* [I replaced my entire tech stack with Postgres... - YouTube](https://www.youtube.com/watch?v=3JW732GrMdg)
* [Kubernetes 환경에서 PostgreSQL 백업과 복구하기 – 매주 한 page, 기술 한 spoon](https://showinfo8.com/2025/07/19/kubernetes-%ed%99%98%ea%b2%bd%ec%97%90%ec%84%9c-postgresql-%eb%b0%b1%ec%97%85%ea%b3%bc-%eb%b3%b5%ea%b5%ac%ed%95%98%ea%b8%b0/)
* [TeslaMate (테슬라메이트) 자동백업 스크립트](https://seonggi.kr/291)
  * [TeslaMate (테슬라메이트) 자동백업 스크립트 | Choi Seong Gi (최성기)](https://www.linkedin.com/posts/seonggi_teslamate-%ED%85%8C%EC%8A%AC%EB%9D%BC%EB%A9%94%EC%9D%B4%ED%8A%B8-%EC%9E%90%EB%8F%99%EB%B0%B1%EC%97%85-%EC%8A%A4%ED%81%AC%EB%A6%BD%ED%8A%B8-activity-7391660851105099777-mko4)
* [백엔드는 PostgreSQL 하나로 끝 (DB 비용 반으로 줄이는 방법) - YouTube](https://www.youtube.com/watch?v=OZrmFD2ajlQ)
* [Slotted Page - Roach Wiki](https://roach-wiki.com/slotted-page)
  * 가변 크기 레코드를 고정 크기 페이지에 저장할 때 내부 단편화 해결을 위한 Slotted Page 자료구조. Pointer Array와 Cell 영역 분리로 간접 참조 및 빈 공간 회수
* [RDB에서 큰 컬럼을 인덱스로 잡으면 안되는 이유 - Roach Wiki](https://roach-wiki.com/rdb)
  * B-Tree 인덱스에서 큰 데이터의 Page Split과 Overflow Page 격리. Primary Page를 가볍게 유지해 Fanout 최대화 및 디스크 I/O 최소화
  * [요즘 근황 - github issue 자동 처리 cron job | 승현 정](https://www.linkedin.com/posts/%EC%8A%B9%ED%98%84-%EC%A0%95-376842221_%EC%9A%94%EC%A6%98-%EA%B7%BC%ED%99%A9-%ED%9A%8C%EC%82%AC%EC%97%90%EC%84%9C%EB%8A%94-github-issue-%EB%A5%BC-%ED%85%9C%ED%94%8C%EB%A6%BF%EC%97%90-%EB%A7%9E%EA%B2%8C-%EC%98%AC%EB%A6%AC%EB%A9%B4-activity-7432756344430030848-89i2)
* [PostgreSQL SharedBuffer 깊이 파헤치기 - Roach Wiki](https://roach-wiki.com/wiki/doc-1760077774)
* [Postgres Sandbox](https://database.build/)
* [Postgres Scan Types in EXPLAIN Plans | Crunchy Data Blog](https://www.crunchydata.com/blog/postgres-scan-types-in-explain-plans)
  * PostgreSQL에서 쿼리 성능을 최적화하는 데 필수적인 EXPLAIN 시스템 스캔 유형
    * 쿼리가 데이터를 검색하는 다양한 방식 설명
    * 단순히 쿼리의 내용뿐 아니라 Postgres가 답을 찾는 방식이 성능에 결정적인 영향
* [Postgres is NOT A DATABASE. - YouTube](https://www.youtube.com/watch?v=b7eXdUOzUTM)
  * [Postgres: 단순한 데이터베이스를 넘어선 올인원 백엔드 솔루션](https://livewiki.com/ko/content/postgres-not-database)
* [Scaling PostgreSQL to power 800 million ChatGPT users | OpenAI](https://openai.com/index/scaling-postgresql/)
  * [OpenAI: 8억 명의 사용자를 지탱하는 PostgreSQL 대규모 확장 전략 | GeekNews](https://news.hada.io/topic?id=26069)
  * [오픈AI가 8억 사용자를 PostgreSQL로 처리하는 비결 - YouTube](https://www.youtube.com/watch?v=RKl6NZ2msTg)
    * [OpenAI는 왜 8억 사용자 DB를 단일 PostgreSQL로 운영할까?](https://livewiki.com/ko/content/openai-800m-users-postgresql)
* [It’s 2026, Just Use Postgres | Tiger Data](https://www.tigerdata.com/blog/its-2026-just-use-postgres)
  * [2026년, 그냥 Postgres를 쓰자 (It's 2026. Just Use Postgr | GeekNews](https://news.hada.io/topic?id=26388)
* [RLS sounds great until it isn't | PlanetScale](https://planetscale.com/blog/rls-sounds-great-until-it-isnt)
  * PostgreSQL Row Level Security가 DB 레이어 접근 제어로 깔끔해 보이지만, 풋건·풀링 비호환·성능 함정으로 득보다 실이 많을 수 있다는 비판
* Vacuum
  * [베큠(VACUUM)을 실행해야되는 이유 그리고 성능 향상](http://blog.gaerae.com/2015/09/postgresql-vacuum-fsm.html)
  * [Visualizing PostgreSQL Vacuum Progress](http://dtrace.org/blogs/dap/2019/05/22/visualizing-postgresql-vacuum-progress/)
  * [Speeding up recovery and VACUUM in Postgres 14 - Microsoft Tech Community](https://techcommunity.microsoft.com/t5/azure-database-for-postgresql/speeding-up-recovery-and-vacuum-in-postgres-14/ba-p/2234071)
  * [**PostgreSQL 튜닝 - Autovacuum 최적화에 대하여**](https://nrise.github.io/posts/postgresql-autovacuum/)
  * [PostgreSQL Autovacuum 장애 대응기 (1). 29CM에서는 Amazon RDS for PostgreSQL를 사용하고… | by Jimin Lee | 29CM 기술블로그 | May, 2021 | Medium](https://medium.com/29cm/postgresql-autovacuum-%EC%9E%A5%EC%95%A0-%EB%8C%80%EC%9D%91%EA%B8%B0-1-8284955c0193)
  * [PostgreSQL Vacuum에 대한 거의 모든 것 | 우아한형제들 기술블로그](https://techblog.woowahan.com/9478/)
  * [How to Control Autovacuum Frequency in PostgreSQL - DEV Community](https://dev.to/farooquememon385/how-to-control-autovacuum-frequency-in-postgresql-4a65)
  * [VACUUM Is a Lie (About Your Indexes) | boringSQL](https://boringsql.com/posts/vacuum-is-lie/)

## PostgreSQL Library
* [Agg: Parallel aggregations for PostgreSQL](http://www.cybertec.at/en/products/agg-parallel-aggregations-postgresql/)
* [AlloyDB versus PostgreSQL: a performance review - Vettabase](https://vettabase.com/blog/alloydb-versus-postgresql/)
* [What is AlloyDB? - YouTube](https://www.youtube.com/watch?v=YODa-x0_3l0)
* [asyncpg -- A fast PostgreSQL Database Client Library for Python/asyncio](https://github.com/magicstack/asyncpg)
* [Biscuit is a specialized PostgreSQL index access method (IAM) designed for blazing-fast pattern matching on LIKE queries, with native support for multi-column searches. It eliminates the recheck overhead of trigram indexes while delivering significant performance improvements on wildcard-heavy queries](https://github.com/CrystallineCore/Biscuit)
  * [Biscuit - PostgreSQL에서 LIKE / ILIKE 패턴 검색을 고속화하기 위 | GeekNews](https://news.hada.io/topic?id=25649)
* [Bottled Water: Real-time integration of PostgreSQL and Kafka](http://www.confluent.io/blog/bottled-water-real-time-integration-of-postgresql-and-kafka/)
* [db9 — Serverless Postgres for AI Agents](https://db9.ai/)
  * 서버리스 PostgreSQL + 클라우드 파일 스토리지를 AI 에이전트용으로 결합. 내장 임베딩·벡터 검색·HTTP 확장·크론 스케줄링 지원
* [dms-psql-post-data: Ultimate Script to complete PostgreSQL-to-PostgreSQL Migration right after AWS DMS task done](https://github.com/sinwoobang/dms-psql-post-data)
* [DocumentDB - Open Source Document Database](https://documentdb.io/)
  * [documentdb: MongoDB-compatible database engine for cloud-native and open-source workloads. Built for scalability, performance, and developer productivity](https://github.com/documentdb/documentdb)
* EdgeDB
  * [EdgeDB—The next generation database](https://edgedb.com/)
  * [We Can Do Better Than SQL](https://edgedb.com/blog/we-can-do-better-than-sql/)
  * [EdgeDB - 개발자를 위한 차세대 오픈소스 ORDB | GeekNews](https://news.hada.io/topic?id=4602)
  * [My experience with EdgeDB · divan's blog](https://divan.dev/posts/edgedb/)
    * EdgeDB는 Postures 위에 만들어진 관계형/그래프 데이터베이스
    * SQL이 없고 EdgeQL이라는 자체 쿼리 언어가 있는데 이게 엄청 좋아서 다시는 SQL로 돌아가지 않을 생각
    * 요즘 추세대로 하나의 바이너리로 모든 걸 할 수 있어서 서버 설치, 데이터베이스 관리, 마이그레이션 모두 가능
    * 1년 전부터 사용하기 시작했는데 지금은 회사의 프로젝트도 EdgeDB로 바꾸고 있고 대부분의 경우 "It just works"를 경험, 다양한 기능을 소개
    * [EdgeDB 1년 사용 후기 - "다시는 SQL로 돌아가지 않을꺼야" | GeekNews](https://news.hada.io/topic?id=7052)
  * [All You Need to Know about EdgeDB | AppSignal Blog](https://blog.appsignal.com/2022/08/02/all-you-need-to-know-about-edgedb.html)
  * [Edge DB - 엘키의 주절 주절](https://elky84.github.io/2022/09/26/edgedb/)
* [ElectricSQL | Postgres sync engine](https://electric-sql.com/)
  * [Electric (Postgres 동기화 엔진) 베타 출시 | GeekNews](https://news.hada.io/topic?id=18239)
* [ElephantSQL - PostgreSQL as a Service](https://www.elephantsql.com/)
* [Envelope - Introducing a new paradigm in web application development written specifically for PostgreSQL developers!](http://envelope.xyz/)
* [Graphile | Powerful, Extensible and Performant GraphQL APIs Rapidly](https://www.graphile.org/)
  * [Beyond REST: Rapid Development With GraphQL Microservices | Netflix TechBlog](https://netflixtechblog.com/beyond-rest-1b76f7c20ef6)
* [GraphpostgresQL](https://github.com/solidsnack/GraphpostgresQL)
* [greenmask: PostgreSQL database anonymization and synthetic data generation tool](https://github.com/GreenmaskIO/greenmask)
  * [Open Source Data Anonymization Tool Empowering a Test Data Management](https://www.greenmask.io/)
  * [Greenmask - PostgreSQL DB 익명화 및 합성데이터 생성 도구 | GeekNews](https://news.hada.io/topic?id=17702)
* [Home - Full text search in milliseconds with PostgreSQL](https://blog.lateral.io/2015/05/full-text-search-in-milliseconds-with-postgresql/)
  * [Beyond REST: Rapid Development With GraphQL Microservices | Netflix TechBlog](https://netflixtechblog.com/beyond-rest-1b76f7c20ef6)
* [instantdb/instant: The realtime client-side database](https://github.com/instantdb/instant)
  * [InstantDB – "현대적인 Firebase" : 실시간 클라이언트측 DB 오픈소스 | GeekNews](https://news.hada.io/topic?id=16421)
* [GraphpostgresQL](https://github.com/solidsnack/GraphpostgresQL)
* [Home - Full text search in milliseconds with PostgreSQL](https://blog.lateral.io/2015/05/full-text-search-in-milliseconds-with-postgresql/)
* [Hydra / Query Postgres, Route to any Database](https://hydras.io/)
* [Kexi - an open source visual database applications creator, a long-awaited competitor for programs like MS Access or Filemaker](http://www.kexi-project.org/)
* [knex: A query builder for PostgreSQL, MySQL, CockroachDB, SQL Server, SQLite3 and Oracle, designed to be flexible, portable, and fun to use](https://github.com/knex/knex)
* [krahodb: An open-source database designed to support multi-master replication. It is designed on the top of PostgreSQL, providing bidirectional replication, as well as row filtering](https://github.com/timbira/krahodb)
* [Message DB - Microservice Native Event Store and Message Store for Postgres](https://github.com/message-db/message-db)
  * [Announcing Message DB: Event Store and Message Store for PostgreSQL](https://blog.eventide-project.org/articles/announcing-message-db/)
* [meteor-pg - Reactive PostgreSQL for Meteor](https://github.com/numtel/meteor-pg)
* [metricflow: MetricFlow allows you to define, build, and maintain metrics in code](https://github.com/transform-data/metricflow)
* [neon: The serverless open source alternative to AWS Aurora Postgres](https://github.com/neondatabase/neon)
  * [Neon - 서버리스 Postgres 오픈소스 | GeekNews](https://news.hada.io/topic?id=6658)
* [odyssey: Scalable PostgreSQL connection pooler](https://github.com/yandex/odyssey)
* [Ora2Pg : Migrates Oracle to PostgreSQL](https://www.ora2pg.com/)
* [orioledb: OrioleDB – building a modern cloud-native storage engine (... and solving some PostgreSQL wicked problems)  🇺🇦](https://github.com/orioledb/orioledb)
  * [OrioleDB Patent: now freely available to the Postgres community](https://supabase.com/blog/orioledb-patent-free)
    * [Postgres 커뮤니티에 이제 OrioleDB 특허가 자유롭게 공개됨 | GeekNews](https://news.hada.io/topic?id=23021)
* [pg2ch: Data streaming from postgresql to clickhouse via logical replication mechanism](https://github.com/mkabilov/pg2ch)
* [pgagroal - a high-performance protocol-native connection pool for PostgreSQL](https://agroal.github.io/pgagroal/)
* [pgBackRest - The Best Postgres Backup Tool with a very active community](https://www.migops.com/blog/2021/04/09/pgbackrest-the-best-postgres-backup-tool-with-a-very-active-community/)
* [pgcat - Enhanced PostgreSQL logical replication](https://github.com/kingluo/pgcat)
* [pgcat: Meow. PgBouncer rewritten in Rust, with sharding, load balancing and failover support](https://github.com/levkk/pgcat)
* [pgcli - Postgres CLI with autocompletion and syntax highlighting](https://github.com/dbcli/pgcli)
* [pg_easy_replicate: Easily setup logical replication and switchover to new database with minimal downtime](https://github.com/shayonj/pg_easy_replicate)
  * PostgreSQL 데이터베이스 간 논리적 복제를 간편하게 설정하는 CLI 도구
  * 소스 데이터베이스를 타깃 데이터베이스로 복제하고, 스위치오버(주 데이터베이스 변경)를 최소한의 다운타임으로 수행하는 데 중점
  * AWS, GCP 환경에서도 특수 사용자 권한을 지원, 복제 중 발생하는 스키마 변경(DDL) 관리 기능도 포함
* [pg_flame - A flamegraph generator for Postgres EXPLAIN ANALYZE output](https://github.com/mgartner/pg_flame)
* [pg_flo - Stream, transform, and route PostgreSQL data in real-time.](https://www.pgflo.io/)
  * [pg_flo – PostgreSQL 데이터를 실시간으로 스트리밍, 변환 및 재라우팅 | GeekNews](https://news.hada.io/topic?id=17585)
* [pgfutter - Import CSV and JSON into PostgreSQL the easy way](https://github.com/lukasmartinelli/pgfutter)
* [pg_graphql - PostgreSQL용 GraphQL 확장 | GeekNews](https://news.hada.io/topic?id=5493)
* [pglite: Lightweight Postgres packaged as WASM into a TypeScript library for the browser, Node.js, Bun and Deno](https://github.com/electric-sql/pglite)
  * [PGLite - 브라우저에서 Postgres 실행하기 | GeekNews](https://news.hada.io/topic?id=13555)
* [pgmemcache is a set of PostgreSQL user-defined functions that provide an interface to memcached](https://github.com/ohmu/pgmemcache/)
* [pgmicro: an in-process reimplementation of PostgreSQL, backed by a SQLite-compatible storage engine](https://github.com/glommer/pgmicro)
  * [pgmicro - SQLite 기반으로 만든 인-프로세스 PostgreSQL | GeekNews](https://news.hada.io/topic?id=28464)
  * PostgreSQL 구문을 실제 PG 파서로 파싱해 SQLite 바이트코드로 직접 컴파일. AI 에이전트·세션 스토어 등 임시 DB용. PG/SQLite 문법 동시 접속 지원
* [pg-migrator - PostgreSQL Migration Tool](https://github.com/aphel-bilisim-hizmetleri/pg-migrator)
* [pg-osc: Zero downtime schema changes in PostgreSQL](https://www.shayon.dev/post/2022/47/pg-osc-zero-downtime-schema-changes-in-postgresql/)
  * [Revolutionizing PostgreSQL Schema Changes with pg_osc - Mydbops | Blog](https://www.mydbops.com/blog/postgresql-schema-changes-with-pg_osc/)
* [PgQue – Zero-bloat Postgres queue. One SQL file to install, pg_cron to tick](https://github.com/NikolayS/pgque)
  * [PgQue – Bloat 없는 Postgres 큐 | GeekNews](https://news.hada.io/topic?id=28997)
  * Skype PgQ 아키텍처를 순수 PL/pgSQL로 재구현. C 확장·외부 데몬 없이 managed Postgres에서 바로 사용. SKIP LOCKED 큐의 dead tuple 누적 문제를 snapshot 기반으로 해결
* [PgQueuer is a Python library leveraging PostgreSQL for efficient job queuing](https://github.com/janbjorge/PgQueuer)
  * [PgQueuer – PostgreSQL을 작업 대기열로 이용하는 파이썬 라이브러리 | GeekNews](https://news.hada.io/topic?id=16377)
* [pg_replicate](https://github.com/supabase/pg_replicate)
  * [pg_replicate - Postgres의 복제를 위한 도구 | GeekNews](https://news.hada.io/topic?id=16300)
* [pgsemantic: Turn any PostgreSQL database into a semantic search engine](https://github.com/varmabudharaju/pgsemantic)
  * 기존 PostgreSQL에 60초 만에 시맨틱 검색 추가. DB 트리거로 임베딩 자동 동기화, 크로스 테이블 검색, MCP 도구 10종 제공
* [pg-shortkey: YouTube-like Short IDs as Postgres Primary Keys](https://github.com/turbo/pg-shortkey)
* [pgsql: Support GROUPING SETS, CUBE and ROLLUP](http://www.postgresql.org/message-id/E1YtRD5-0005Q7-SM@gemulon.postgresql.org)
* [pgsql: Create an infrastructure for parallel computation in PostgreSQL](http://www.postgresql.org/message-id/E1Ynu2T-0005iK-Gf@gemulon.postgresql.org)
* [pg_stat_monitor: PostgreSQL Statistics Collector](https://github.com/percona/pg_stat_monitor)
  * [Announcing pg_stat_monitor Tech Preview: Get Better Insights Into Query Performance in PostgreSQL - Percona Database Performance Blog](https://www.percona.com/blog/2020/10/14/announcing-pg_stat_monitor-tech-preview-get-better-insights-into-query-performance-in-postgresql/)
* [PG-Strom is an extension of PostgreSQL, works as custom-scan provider](https://wiki.postgresql.org/wiki/PGStrom)
* [pgTAP - a suite of database functions that make it easy to write TAP-emitting unit tests in psql scripts or xUnit-style test functions](http://pgtap.org/)
* [pg_timeseries: Simple and focused time-series tables for PostgreSQL, from Tembo](https://github.com/tembo-io/pg_timeseries/tree/main?tab=readme-ov-file#roadmap)
  * [Introducing pg_timeseries: Open-source time-series extension for PostgreSQL | Tembo](https://tembo.io/blog/pg-timeseries)
    * [pg_timeseries: PostgreSQL용 오픈소스 시계열 확장 기능 | GeekNews](https://news.hada.io/topic?id=14927)
* [PLV8 Documentation](https://plv8.github.io/)
  * [PLV8 - Postgres에서 Javascript 함수 사용하기 | GeekNews](https://news.hada.io/topic?id=15817)
* [PolarDB-for-PostgreSQL](https://github.com/alibaba/PolarDB-for-PostgreSQL)
  * [PolarDB for PostgreSQL | GeekNews](https://news.hada.io/topic?id=4362)
* [Pongo - Mongo but on Postgres and with strong consistency benefits](https://github.com/event-driven-io/Pongo)
  * [Pongo - Postgres 기반 Mongo with Strong Consistency | GeekNews](https://news.hada.io/topic?id=15742)
* [postgres: Unmodified Postgres with some useful plugins](https://github.com/supabase/postgres)
  * [유용한 확장을 포함한 Postgres Docker 이미지들 | GeekNews](https://news.hada.io/topic?id=4967)
* [Postgres.app – the easiest way to get started with PostgreSQL on the Mac](https://postgresapp.com/)
* [postgres.new: In-browser Postgres with an AI interface](https://supabase.com/blog/postgres-new)
  * [Postgres.new - AI 인터페이스를 갖춘 브라우저 내 Postgres | GeekNews](https://news.hada.io/topic?id=16310)
* [PostgresqlCO.NF: PostgreSQL configuration for humans](https://postgresqlco.nf/en/doc/param/)
* [PostgREST: REST API for any Postgres database](https://github.com/PostgREST/postgrest)
  * [PostgREST - a standalone web server that turns your PostgreSQL database directly into a RESTful AP](https://postgrest.org/)
  * [backend.sql + frontend.js =♥ - Polyglot.Network Blog](https://blog.polyglot.network/backend.sql-+-frontend.js-love)
* [Postico – a modern PostgreSQL client for the Mac](https://eggerapps.at/postico/)
* [postlite: Postgres wire compatible SQLite proxy](https://github.com/benbjohnson/postlite)
* [Psycopg - PostgreSQL driver for Python](https://www.psycopg.org/)
  * [Psycopg2 Tutorial](https://wiki.postgresql.org/wiki/Psycopg2_Tutorial)
  * [Error: pg_config executable not found](https://ohgyun.com/787)
  * [Akshay 🚀 on X: "Python is powerful! 🔥 You can execute SQL Queries using Python &amp; load the results in a Pandas DataFrame! 🐼 Check this out👇 https://t.co/juNBzz9CG8" / X](https://twitter.com/akshay_pachaar/status/1706949322494074908)
* [realtime: Listen to your to PostgreSQL database in realtime via websockets. Built with Elixir](https://github.com/supabase/realtime)
* [reshape: An easy-to-use, zero-downtime schema migration tool for Postgres](https://github.com/fabianlindfors/reshape)
  * [Reshape - 다운타임 없는 Postgres용 스키마 이관 도구 오픈소스 | GeekNews](https://news.hada.io/topic?id=5892)
* [Slinky - The easiest way to query your PostgreSQL data](https://www.slinkydb.com/)
* [sql_firewall - SQL Firewall Extension for PostgreSQL](https://github.com/uptimejp/sql_firewall)
* [stolon - PostgreSQL cloud native HA replication manager](https://github.com/sorintlab/stolon)
* [teable: ✨ A Super fast, Real-time, Professional, Developer friendly, No code database](https://github.com/teableio/teable)
  * [Teable - Postgres와 Airtable을 결합한 오픈소스 노코드 데이터베이스 | GeekNews](https://news.hada.io/topic?id=13768)
  * [Teable: Free Open Source No-Code PostgreSQL Database Platform - YouTube](https://www.youtube.com/watch?v=KkW1dlLfqWI)
* [ToroDB: A MongoDB-compatible, document-oriented database on top of PostgreSQL](http://www.8kdata.com/torodb/)
* [transqlate - 모든 SQL을 PostgreSQL Dialect로 변환(Transp | GeekNews](https://news.hada.io/topic?id=13978)
* [Vitesse X - A Speed Extension for PostgreSQL](http://vitessedata.com/)
* [Yoke - a Postgres redundancy/auto-failover solution that provides a high-availability PostgreSQL cluster that's simple to manage](https://github.com/nanopack/yoke)

# Query, SQL
* [Why the SQL Standard does not need another way to do GROUP BY](http://glennpaulley.ca/conestoga/2015/05/why-the-sql-standard-does-not-need-another-way-to-do-group-by/)
* [sql group by 응용 시험에 최소 1번 이상 통과한 사람과 그렇지 않은 사람 골라내기](https://codingdog.tistory.com/entry/sql-group-by-%EC%9D%91%EC%9A%A9-%EC%8B%9C%ED%97%98%EC%97%90-%EC%B5%9C%EC%86%8C-1%EB%B2%88-%EC%9D%B4%EC%83%81-%ED%86%B5%EA%B3%BC%ED%95%9C-%EC%82%AC%EB%9E%8C%EA%B3%BC-%EA%B7%B8%EB%A0%87%EC%A7%80-%EC%95%8A%EC%9D%80-%EC%82%AC%EB%9E%8C-%EA%B3%A8%EB%9D%BC%EB%82%B4%EA%B8%B0)
* [최대값 및 최소값 조회 (MAX, MIN 함수 대체방법)](https://sesok808.tistory.com/461)
* [**MySQL에서 ‘a’ = ‘a ‘가 true로 평가된다? | 우아한형제들 기술블로그**](https://techblog.woowahan.com/2559/)
  * [MySQL에서 'a' = 'a '가 true로 평가된다?](https://johngrib.github.io/wiki/sql-char-comparison/)
* [sql 기본 강좌# 개념 파악 및 공부법 안내](https://stricky.tistory.com/202)
* [sql 기본 강의 # select를 잘 이용하는 방법(1), 2편 -sTricky](https://stricky.tistory.com/204)
* [sql 기본 강의 # select를 잘 이용하는 방법(1), 3편 -sTricky](https://stricky.tistory.com/205)
* [sql 공부 강의 # 단일행 함수 잘 사용 하기(문자 함수) 4편 -sTricky](https://stricky.tistory.com/210)
* [sql 공부 강의 # 단일행 함수 잘 사용 하기(숫자 함수) 5편 -sTricky](https://stricky.tistory.com/217)
* [sql 공부 강의 # 단일행 함수 잘 사용 하기(날짜 함수) 6편 -sTricky](https://stricky.tistory.com/220)
* [sql 독학 강의 # 단일행 함수 잘 사용 하기(형 변환 함수) 7편 -sTricky](https://stricky.tistory.com/232)
* [sql 독학 강의 # 단일행 함수 잘 사용 하기(일반 함수) 8편 -sTricky](https://stricky.tistory.com/233)
* [sql 독학 강의 # 복수 행(window) 함수 잘 사용 하기(기본 사용법) 9편 -sTricky](https://stricky.tistory.com/240)
* [sql 독학 강의 # 복수 행(window) 함수 잘 사용 하기(group by) 10편 -sTricky](https://stricky.tistory.com/241)
* [sql 독학 강의 # mysql join (정의 및 종류) 11편 -sTricky](https://stricky.tistory.com/243)
* [sql 독학 강의 # Cartesian Product 카티션 곱 ansi SQL 문법 12편 -sTricky](https://stricky.tistory.com/245)
* [sql 독학 강의 # inner join with ansi SQL 13편 -sTricky](https://stricky.tistory.com/248)
* [sql 독학 강의 # 비등가 join with ansi SQL 14편 -sTricky](https://stricky.tistory.com/255)
* [sql 독학 강의 # outer join SQL 15편 -sTricky](https://stricky.tistory.com/260)
* [sql 독학 강의 # sub query 서브 쿼리 16편 -sTricky](https://stricky.tistory.com/265)
* [mysql update sql 독학 강의#17편 -sTricky](https://stricky.tistory.com/268)
* [mysql update sql 독학 강의#18편 -sTricky](https://stricky.tistory.com/277)
* [mysql delete sql 독학 강의#19편 -sTricky](https://stricky.tistory.com/282)
* [insert into on duplicate key MySQL merge SQL 독학 강의#20편 -sTricky](https://stricky.tistory.com/286)
* [MySQL DDL문 완전정복 SQL 독학 강의#21편 -sTricky](https://stricky.tistory.com/294)
* [MySQL data dictionary SQL 독학 강의#22편](https://stricky.tistory.com/296)
* [mysql 제약조건 알아보기 SQL 독학 강의#23편](https://stricky.tistory.com/308)
* [index 의 중요성과 이해 SQL 독학 강의#24편](https://stricky.tistory.com/310)
* [view 뷰에 대한 이해 SQL 독학 강의#25편](https://stricky.tistory.com/323)
* [주문 고객 상품 테스트용 데이터 생성 및 다운로드](https://stricky.tistory.com/230)
* [프로그래머스 SQL 코딩 테스트 select 문제 풀이](https://stricky.tistory.com/505)
* [프로그래머스 SQL 코딩 테스트 select 문제 풀이 #2](https://stricky.tistory.com/507)
* [프로그래머스 SQL 답 SUM, MAX, MIN 문제 풀이 #03](https://stricky.tistory.com/508)
* [SQL Correlated Subqueries - GeeksforGeeks](https://www.geeksforgeeks.org/sql-correlated-subqueries/)
* [Rain in Australia 캐글 날씨 데이터셋 다운로드 받아 mysql에 넣는 방법](https://stricky.tistory.com/448) DDL Datagrip
* [초보자도 준비하는 SQL 코딩 테스트 시리즈를 마치며...](https://wonit.tistory.com/448)
* [How to create a 1M record table with a single query | Anton Zhiyanov](https://antonz.org/random-table/) `with recursive`
* [(4) Asheq Reza's answer to What are some useful SQL queries you've found? - Quora](https://www.quora.com/What-are-some-useful-SQL-queries-youve-found/answer/Asheq-Reza)
* [Best practices for writing SQL queries](https://www.metabase.com/learn/building-analytics/sql-templates/sql-best-practices)
* [Master the SQL QUALIFY Statement: A Comprehensive Tutorial | DataCamp](https://www.datacamp.com/tutorial/qualify-the-sql-filtering-statement-you-never-knew-you-needed)
  * Row number, rank 등으로 필터링 하기 위해 sub query 를 만들었던 부분에서 훨씬 간편하게 사용 가능할 것으로 예상
* [sql-tutorial: E-Commerce Database v2.0 기반 SQL 튜토리얼](https://github.com/civilian7/sql-tutorial)
  * 30개 테이블, 687K+ 현실적 데이터, 22개 레슨 208개 연습문제. SQLite/MySQL/PostgreSQL 지원, 한/영 이중언어

## Query, SQL Join
* [SQL기초강좌(외부조인, outer join), 오라클, MySQL, 내부조인,외부조인,](http://www.slideshare.net/topcredu/sql-outer-join-mysql)
* [다양한 조인(JOIN) 기법](http://blog.ngelmaum.org/entry/lab-note-sql-join-method)
* [What's the difference between NOT EXISTS vs. NOT IN vs. LEFT JOIN WHERE IS NULL?](http://stackoverflow.com/questions/2246772/whats-the-difference-between-not-exists-vs-not-in-vs-left-join-where-is-null)
* [All about SQL JOINs](https://hackernoon.com/all-about-sql-joins-ced19ecc4c1d)
* [MSSQL JOIN의 종류설명 및 사용법 & 예제](https://coding-factory.tistory.com/87)
* [SQL Join](https://opentutorials.org/module/4118)
  * [SQL Join](https://www.youtube.com/playlist?list=PLuHgQVnccGMAG1O1BRZCT3wkD_aPmPylq)
* [Join 에 관해서 정리해 보겠습니다](https://developer88.tistory.com/331)
* [SQL의 핵심, 다양한 종류의 조인 : 네이버 블로그](https://blog.naver.com/codeitofficial/222019008042)
* [Say NO to Venn Diagrams When Explaining JOINs – Java, SQL and jOOQ](https://blog.jooq.org/2016/07/05/say-no-to-venn-diagrams-when-explaining-joins/)

# Realm
* [오픈소스 모바일 DB ‘렘’, 225억 투자 유치](http://www.bloter.net/archives/223748)

# Sharding
* [What is Sharding?](https://medium.com/@radixdlt/what-is-sharding-6ca10b72cbd1)
* [Database의 샤딩(Sharding)이란?](https://nesoy.github.io/articles/2018-05/Database-Shard)
* [NHN의 안과 밖: Sharding Platform](https://d2.naver.com/helloworld/14822) Spock Proxy, Gizzard, Cubrid Shard 비교
* [샤딩은 쉬워요 샤딩하세요](https://www.popit.kr/%ED%98%80%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8-charsyam%EC%9D%80-%EA%B5%AC%EB%9D%BC%EC%9F%81%EC%9D%B4-1-%EC%83%A4%EB%94%A9%EC%9D%80-%EC%89%AC%EC%9B%8C%EC%9A%94-%EC%83%A4%EB%94%A9%ED%95%98%EC%84%B8/) 실제로는 어렵다는 이야기
* [Sharding(샤딩)](https://jacking.tistory.com/1146)
* [샤딩과 파티셔닝의 차이점](http://theeye.pe.kr/archives/1917)
* [How we scaled Freshdesk (Part II) – The Sharding and Rebalancing techniques we used](https://freshdesk.com/product-updates/how-freshdesk-scaled-using-sharding-blog/)
* [Sharding: How Many Shards Are Safe?](https://medium.com/logos-network/sharding-how-many-shards-are-safe-bc361c487083)
* [DB분산처리를 위한 sharding | 우아한형제들 기술블로그](https://techblog.woowahan.com/2687/)
* [Database의 샤딩(Sharding)이란?](https://nesoy.github.io/articles/2018-05/Database-Shard)
* [Understanding Database Sharding | DigitalOcean](https://www.digitalocean.com/community/tutorials/understanding-database-sharding)
* [글로벌 칼럼 | DB 분산 처리 기법 '샤딩', "웬만하면 하지 마라" - ITWorld Korea](https://www.itworld.co.kr/news/200134) sharding

# SQLite
* [practice - python sqlite](https://github.com/hyunjun/practice/tree/master/python/test-sqlite3)
* [Appropriate Uses For SQLite](https://www.sqlite.org/whentouse.html)
* [Finding bugs in SQLite, the easy way](http://lcamtuf.blogspot.kr/2015/04/finding-bugs-in-sqlite-easy-way.html)
* [Don't test with SQLLite when you use Postgres in Production](http://michael.robellard.com/2015/07/dont-test-with-sqllite-when-you-use.html)
* [The SQLite Query Planner](https://www.sqlite.org/optoverview.html)
* [Code to transform Hillary's emails from raw PDF documents to a SQLite database](https://github.com/benhamner/hillary-clinton-emails)
* [Full Text Search with SQLite](http://blog.xojo.com/2014/03/14/full_text_search_with_sqlite/)
* [Install Python and Sqlite from Source](https://www.bluebill.net/2016/04/24/install-python-and-sqlite-from-source/)
  * 상황; virtualenv에서 pip3 install jupyter  성공 후 실행
  * 오류; `ModuleNotFoundError: No module named '_sqlite3'` + `ModuleNotFoundError: No module named 'pysqlite2'`
  * 원인; sqlite3가 제대로 설치되지 않음
  * 해결
    * 검색 결과 sqlite-devel or libsqlite3-dev를 설치 후 python3 재컴파일 혹은 setup.py의 path 수정
    * jupyter에서 간단히 할 일이 있어서 하려고 했던 건데 너무 일이 커져서 귀찮아서 여기서 중지
* [How To Corrupt An SQLite Database File](https://www.sqlite.org/howtocorrupt.html)
* [SQLite Is Serverless](https://www.sqlite.org/serverless.html)
* [Sharing an SQLite database across containers is surprisingly brilliant](https://medium.com/@rbranson/sharing-sqlite-databases-across-containers-is-surprisingly-brilliant-bacb8d753054)
* [SQLite As An Application File Format](https://sqlite.org/appfileformat.html)
* [How does SQLite work? Part 1: pages!](https://jvns.ca/blog/2014/09/27/how-does-sqlite-work-part-1-pages/)
* [How does SQLite work? Part 2: btrees! (or: disk seeks are slow don't do them!)](https://jvns.ca/blog/2014/10/02/how-does-sqlite-work-part-2-btrees/)
* [LPC-2019: SQLite on Linux](https://sqlite.org/lpc2019/doc/trunk/briefing.md)
* [SQLite 개념/구조/멀티 DB 실사용기 :: 메모장](https://ehdvudee.tistory.com/23)
* [SQLite as a document database](https://dgl.cx/2020/06/sqlite-json-support)
  * [SQLite를 도큐먼트DB로 사용하기 | GeekNews](https://news.hada.io/topic?id=3271)
* [Many Small Queries Are Efficient In SQLite](https://sqlite.org/np1queryprob.html)
  * SQLite에서는 작은 쿼리 수백개도 효율적 (sqlite.org)
  * 웹페이지 하나 표시하는데 200개의 SQL문장을 쓴다면 MySQL,PostgreSQL 같은 기존 C/S DB에겐 과도함
  * SQLite에서는 200개 이상의 쿼리도 별 문제 없음
  * → 복잡하고 큰 쿼리도 잘 효율적으로 실행하지만, 작은 쿼리가 많아도 효율적
  * → SQLite는 Client/Server 방식이 아니고 프로세스내에서 함수호출하는 방식이기에 N+1 Query Problem이 적용되지 않음
  * SQLite의 소스 타임라인을 표시하는 동적 웹페이지에서 사용하는 실제 SQL 문장 240여개를 볼 수 있음
* [SQLite is not a toy database | Anton Zhiyanov](https://antonz.org/sqlite-is-not-a-toy-database/)
  * SQLite를 토이 데이터베이스로 보는 사람도 많지만, 개발자가 아니어도 SQLite 활용 부문 많음
  * Console을 제공하므로 쉽게 조회 가능
  * CSV 파일도 임포트해서 SQL 문으로 조회 가능
  * 가상 테이블로 만들어서 조회하면 2배나 빠름
  * JSON 파일로 SQLite로 읽어서 조회 가능
  * 미디언, 퍼센타일 등의 값도 쉽게 조회 가능
  * Full-text 검색 지원
  * SQLite는 동시 엑세스를 지원하지 않는다는 오해도 있지만 write-ahead log 모드가 오래전에 추가되어 리더를 원하는 대로 추가 가능
* [What’s new in SQLite 3.35 | Anton Zhiyanov](https://antonz.org/sqlite-3-35/)
* [Cross-database queries in SQLite (and weeknotes)](https://simonwillison.net/2021/Feb/21/cross-database-queries/) Querying json data
* [CG/SQL: Easy, accurate SQLite code generation - Facebook Engineering](https://engineering.fb.com/open-source/cg-sql/)
* [DB Browser for SQLite](https://sqlitebrowser.org/)
* [SQLite the only database you will ever need in most cases](https://unixsheikh.com/articles/sqlite-the-only-database-you-will-ever-need-in-most-cases.html)
* [Exploring Tweets with SQLite + WASM - Divyendu's Blog](https://divu.in/experiments/wasm/twitter-sqlite)
* [Hosting SQLite databases on Github Pages - (or any static file hoster) - phiresky's blog](https://phiresky.github.io/blog/2021/hosting-sqlite-databases-on-github-pages/)
* [SQLite in production with WAL](https://victoria.dev/blog/sqlite-in-production-with-wal/)
* [The Untold Story of SQLite With Richard Hipp - CoRecursive Podcast](https://corecursive.com/066-sqlite-with-richard-hipp/)
  * [**SQLite의 알려지지 않은 이야기 | GeekNews**](https://news.hada.io/topic?id=4558)
* [Show HN: SQLite query inside a Bash function | Hacker News](https://news.ycombinator.com/item?id=27762201)
* [Using sqlite3 as a notekeeping document graph with automatic reference indexing](https://epilys.github.io/bibliothecula/notekeeping.html)
* [35% Faster Than The Filesystem](https://www.sqlite.org/fasterthanfs.html)
* [Hosting SQLite databases on Github Pages - (or any static file hoster) - phiresky's blog](https://phiresky.netlify.app/blog/2021/hosting-sqlite-databases-on-github-pages/)
* [MySQL을 SQLite로 변경 - 신현석(Hyeonseok Shin)](https://hyeonseok.com/blog/884)
* [Wesley Aptekar-Cassels | Consider SQLite](https://blog.wesleyac.com/posts/consider-sqlite)
* [Store SQLite in Cloudflare Durable Objects - Markus Ast](https://ma.rkusa.st/store-sqlite-in-cloudflare-durable-objects)
* [JSON improvements in SQLite 3.38.0](https://tirkarthi.github.io/programming/2022/02/26/sqlite-json-improvements.html)
* [SQLite in Go, with and without cgo](https://datastation.multiprocess.io/blog/2022-05-12-sqlite-in-go-with-and-without-cgo.html)
* [I'm All-In on Server-Side SQLite · Fly](https://fly.io/blog/all-in-on-sqlite-litestream/)
  * Go의 임베디드 키/밸류 데이터베이스인 BoltDB를 만든 Ben Johnson이 배포 서비스인 Fly.io에서 Litestream을 계속 작업
  * Litestream은 SQLite를 리플리케이션을 이용해서 유지할 수 있게 하는 프로젝트
  * BoltDB는 Go로 스키마를 작성해야 해서 마이그레이션이 어려운 등의 단점이 있었고 더 많은 프로그램에서 사용할 수 있도록 해야 할 작업을 고민하다가 SQLite이 이를 위해 존재한다는 결론
  * SQLite를 기본으로 사용하지 않는 이유는 스토리지 오류에 대한 복원력이고 규모에 따른 동시성 때문인데 SQLite에는 우리가 필요로 하는 기능의 99.9%가 있고 애플리케이션 바로 옆에 배치할 수 있어서 속도 이점
* [Why SQLite may become foundational for digital progress | VentureBeat](https://venturebeat.com/2022/05/20/why-sqlite-may-become-foundational-for-digital-progress/)
* [Temporary tables in SQLite](https://antonz.org/temp-tables/)
  * [SQLite의 Temporary Table 활용하기 | GeekNews](https://news.hada.io/topic?id=6581)
* [Cron-based backup - Litestream](https://litestream.io/alternatives/cron/)
* [One-liner for running queries against CSV files with SQLite | Simon Willison’s TILs](https://til.simonwillison.net/sqlite/one-line-csv-operations)
* [SQLite or PostgreSQL? It's Complicated!](https://www.twilio.com/blog/sqlite-postgresql-complicated)
* [SQLite Internals: Pages & B-trees · Fly](https://fly.io/blog/sqlite-internals-btree/)
* [Turning SQLite into a distributed database](https://univalence.me/posts/mvsqlite)
* [Proceedings of the VLDB Endowment](https://vldb.org/pvldb/volumes/15/paper/SQLite:%20Past,%20Present,%20and%20Future)
  * [SQLite: Past, Present, and Future | GeekNews](https://news.hada.io/topic?id=7327)
* [SQLite Forum: JSONB has landed](https://sqlite.org/forum/forumpost/fa6f64e3dc1a5d97)
* [Array columns in SQLite - DEV Community](https://dev.to/fractaledmind/array-columns-in-sqlite-15i0)
* [이 데이터베이스는 99.9%의 웹사이트에 완벽합니다 - YouTube](https://www.youtube.com/watch?v=ax-Q1iedXJA)
  * 155000 lines of code, 92000000 lines of test code (600 times)
* [First contact — brandur.org](https://brandur.org/atoms/gubk5w2)
  * [SQLite와의 First Contact | GeekNews](https://news.hada.io/topic?id=15816)
* [35% Faster Than The Filesystem](https://sqlite.org/fasterthanfs.html)
  * [SQLite: 파일 시스템보다 35% 더 빠름 | GeekNews](https://news.hada.io/topic?id=16044)
* [SQLite Transactions](https://reorchestrate.com/posts/sqlite-transactions/)
  * [SQLite의 트랜잭션 | GeekNews](https://news.hada.io/topic?id=16105)
* [Hybrid full-text search and vector search with SQLite | Alex Garcia's Blog](https://alexgarcia.xyz/blog/2024/sqlite-vec-hybrid-search/index.html)
  * [SQLite로 전문검색과 벡터검색의 하이브리드 구현하기 | GeekNews](https://news.hada.io/topic?id=17405)
* [Rearchitecting: Redis to SQLite | Wafris](https://wafris.org/blog/rearchitecting-for-sqlite)
  * [우리가 ‘Redis’에서 ‘SQLite’로 재설계한 이유 | 요즘IT](https://yozm.wishket.com/magazine/detail/2838/)
* [Disaggregated Storage - a brief introduction - blag](https://avi.im/blag/2024/disaggregated-storage/)
* [How bloom filters made SQLite 10x faster - blag](https://avi.im/blag/2024/sqlite-past-present-future/)
  * [Bloom 필터로 10배 빨라진 SQLite | GeekNews](https://news.hada.io/topic?id=18399)
* [SQLite JSON Superpower: Virtual Columns + Indexing - DB Pro Blog](https://www.dbpro.app/blog/sqlite-json-virtual-columns-indexing)
  * [SQLite JSON을 전체 인덱스 속도로 활용하는 방법: 생성된 컬럼을 이용한 고속 쿼리 | GeekNews](https://news.hada.io/topic?id=25041)
* [SQLite로 실제 쇼핑몰을 운영하며 배운 것들](https://ultrathink.art/blog/sqlite-in-production-lessons)
  * [SQLite로 실제 쇼핑몰을 운영하며 배운 것들 | GeekNews](https://news.hada.io/topic?id=28377)
  * 배포 파이프라인 동시성 문제로 인한 주문 손실 사고와 해결법, SQLite 프로덕션 운영 주의사항
* [absurd-sql: sqlite3 in ur indexeddb (hopefully a better backend soon)](https://github.com/jlongster/absurd-sql)
* [cr-sqlite: Convergent, Replicated SQLite. Multi-writer and CRDT support for SQLite](https://github.com/vlcn-io/cr-sqlite)
  * [Crsql - SQLite에 Multi-Writer, CRDT 기능을 추가하는 확장 | GeekNews](https://news.hada.io/topic?id=7843)
* [dbench: An unscientific benchmark of SQLite vs the file system (btrfs)](https://github.com/chrisdavies/dbench)
* [edge-sql - A serverless edge worker embedding SQLite using Cloudflare Workers and WASM](https://sql.lspgn.workers.dev/)
* [graphqlite: A SQLite extension that adds graph database capabilities with Cypher query language support and built-in graph algorithms](https://github.com/colliery-io/graphqlite)
  * [Introduction - GraphQLite Documentation](https://colliery-io.github.io/graphqlite/)
  * [GraphQLite - Cypher 쿼리 언어와 내장 그래프 알고리듬을 지원하는 SQLit | GeekNews](https://news.hada.io/topic?id=25913)
* [IceFireDB SQLite database - a decentralized SQLite database](https://github.com/IceFireDB/IceFireDB/tree/main/IceFireDB-SQLite)
* LiteFS [Introducing LiteFS · Fly](https://fly.io/blog/introducing-litefs/)
  * fly.io에서 Litestream의 아이디어를 확장한 LiteFS 공개
  * Litestream이 SQLite WAL 파일을 복사한다면 LiteFS는 각 트랜잭션을 검사하고 전달하는 역할
  * 이를 위해서 FUSE를 선택해서 앱과 데이터베이스 파일 사이에 파일 시스템 프락시 같은 걸 넣어서 트랜잭션을 리플리카에 복사 가능
  * [I Migrated from a Postgres Cluster to Distributed SQLite with LiteFS](https://kentcdodds.com/blog/i-migrated-from-a-postgres-cluster-to-distributed-sqlite-with-litefs)
    * Kent C. Dodds가 자신의 사이트를 PostgreSQL을 이용해서 fly.io 이용중
      * fly.io의 Litestream와 LiteFS를 알게 되어 SQLite로 이동
    * 이전에는 멀티리전 데이터베이스를 위해 primary 리전에 직접 write
      * SQLite는 로컬에 떠 있으므로 이 방법을 사용 불가
      * fly.io에서 지원하는 `fly-replay` 응답 헤더를 통해 primary 리전에서 처리되도록 하는 방법 사용
    * 단일 리전에서 동작하도록 마이그레이션 준비가 끝난 뒤에 LiteFS를 설정
      * `fly-replay` 응답 헤더를 통해 멀티 리전 처리 가능
      * 이 부분 외에는 멀티리전을 위한 코드의 영향은 없었음
* [Litestream - Streaming SQLite Replication](https://litestream.io/)
  * [litestream: Streaming S3 replication for SQLite](https://github.com/benbjohnson/litestream)
  * [Litestream - SQLite 스트리밍 복제 도구 | GeekNews](https://news.hada.io/topic?id=6438)
  * [Litestream v0.5.0 is Here · The Fly Blog](https://fly.io/blog/litestream-v050-is-here/)
    * [Litestream v0.5.0 | GeekNews](https://news.hada.io/topic?id=23422)
* [react-native-sqlite-storage - SQLite Native Plugin for React Native](https://github.com/andpor/react-native-sqlite-storage)
* [rqlite](https://rqlite.io/)
  * [rqlite: The lightweight, distributed relational database built on SQLite](https://github.com/rqlite/rqlite)
  * [7 years of open-source database development: lessons learned - Vallified](https://www.philipotoole.com/7-years-of-open-source-database-development-lessons-learned/)
    * [7년간의 오픈소스 DB 개발에서 배운 것 | GeekNews](https://news.hada.io/topic?id=4096)
  * [Building rqlite 9.0: Cutting Disk Usage by Half | Vallified](https://www.philipotoole.com/building-rqlite-9-0-cutting-disk-usage-by-half/)
    * [rqlite 9.0 개발중 - 디스크 사용량 절반으로 줄이기 | GeekNews](https://news.hada.io/topic?id=16231)
* [simple-graph: This is a simple graph database in SQLite, inspired by "SQLite as a document database"](https://github.com/dpapathanasiou/simple-graph)
* [soul: 🕉 A SQLite REST and realtime server](https://github.com/thevahidal/soul)
  * [SOUL - SQLite REST 및 실시간 서버 | GeekNews](https://news.hada.io/topic?id=13950)
* [SpatiaLite: SpatiaLite](https://www.gaia-gis.it/fossil/libspatialite/index)
* [sqlean: All the missing SQLite functions](https://github.com/nalgeon/sqlean)
* [SQLime - SQLite Playground](https://sqlime.org/)
  * [SQLime - 온라인 SQLite Playground | GeekNews](https://news.hada.io/topic?id=5153)
* [sqlite3 fiddle](https://sqlite.org/fiddle/)
* [sqlite3-to-mysql: Transfer data from SQLite to MySQL](https://github.com/techouse/sqlite3-to-mysql)
* [sqlite-data: A fast, lightweight replacement for SwiftData, powered by SQL and supporting CloudKit synchronization](https://github.com/pointfreeco/sqlite-data)
  * [SQLiteData - SwiftData의 빠르고 가벼운 대체제, SQL 기반이며 Clou | GeekNews](https://news.hada.io/topic?id=23297)
* [SQLite DB Browser - SQLite 비쥬얼 브라우저 오픈소스 | GeekNews](https://news.hada.io/topic?id=15765)
  * [DB Browser for SQLite](https://sqlitebrowser.org/)
  * [DB Browser for SQLite 3.13.0 릴리즈 | GeekNews](https://news.hada.io/topic?id=15977)
* [sqlite-graph: SQLite Graph Extension](https://github.com/agentflare-ai/sqlite-graph)
  * [SQLite-Graph - SQLite에 그래프DB 기능을 추가하는 확장 | GeekNews](https://news.hada.io/topic?id=24351)
* [sqlite-http: A SQLite extension for making HTTP requests purely in SQL](https://github.com/asg017/sqlite-http)
  * [Introducing sqlite-http: A SQLite extension for making HTTP requests / Alex Garcia / Observable](https://observablehq.com/@asg017/introducing-sqlite-http)
* [sqlite-lines: A SQLite extension for reading large files line-by-line (NDJSON, logs, txt, etc.)](https://github.com/asg017/sqlite-lines)
* [sqlitestudio.pl](http://sqlitestudio.pl/)
* [sqlite-studio: SQLite database explorer](https://github.com/frectonz/sqlite-studio)
  * [SQLite Studio - 싱글 바이너리 SQLite DB 탐색도구 | GeekNews](https://news.hada.io/topic?id=15415)
* [SQL OnLine IDE](https://sqliteonline.com/)
* [stanchion: A SQLite extension that brings column-oriented tables to SQLite](https://github.com/dgllghr/stanchion)
  * [Stanchion - SQLite에 컬럼 기반 테이블을 추가하는 확장 | GeekNews](https://news.hada.io/topic?id=13292)
* [syntaqlite: A parser, formatter, validator, and language server for SQLite SQL](https://lalitm.com/post/building-syntaqlite-ai/)
  * [syntaqlite](https://github.com/LalitMaganti/syntaqlite)
  * [8년의 갈망, 3개월의 완성 - AI가 바꾼 사이드 프로젝트의 공식 | GeekNews](https://news.hada.io/topic?id=28239)
  * [syntaqlite - SQLite 자체 문법과 토크나이저 기반의 SQL 파서·포매터·검증기·언어 서버 | GeekNews](https://news.hada.io/topic?id=28832)
  * SQLite 전용 SQL 파서·포매터·검증기·Language Server. SQLite 자체 문법과 토크나이저 기반
* [Turso - Databases for All](https://turso.tech/)
  * [Turso Database](https://github.com/tursodatabase)
  * [The SQLite Rewrite In Rust - YouTube](https://www.youtube.com/watch?v=PPjXM8G8ax0)
  * [Why We Created Turso, a Rust-Based Rewrite of SQLite - The New Stack](https://thenewstack.io/why-we-created-turso-a-rust-based-rewrite-of-sqlite/)
    * [Turso: A Rust-Based Rewrite of SQLite | Rust Jobs 🦀님이 토픽에 대해 올림 | LinkedIn](https://www.linkedin.com/posts/rustjobs-dev_turso-a-rust-based-rewrite-of-sqlite-activity-7383504170085085184-I0pV)
  * [diesel_turso: A Diesel backend and connection implementation for Turso Database, an in-process SQL database written in Rust, compatible with SQLite.](https://github.com/Choochmeque/diesel_turso)
* [wp-sqlite: WordPress running on an SQLite database](https://github.com/stokry/wp-sqlite)
  * [wp-sqlite - SQLite에서 Wordpress 실행하기 | GeekNews](https://news.hada.io/topic?id=6576)
* [ws4sqlite: Query sqlite via http](https://github.com/proofrock/ws4sqlite)

## SQLite Python
* [A simple Python script to document the SQLite databases](https://towardsdatascience.com/a-simple-python-script-to-document-the-sqlite-databases-7932aa462cd8)
* [Do You Know Python Has A Built-In Database? | by Christopher Tao | Towards Data Science](https://towardsdatascience.com/do-you-know-python-has-a-built-in-database-d553989c87bd)
* [Towards Inserting One Billion Rows in SQLite Under A Minute - blag](https://avi.im/blag/2021/fast-sqlite-inserts/)
* [파이썬 Python 코딩 - 전화번호부 만들기2 (SQLite DB 사용) - YouTube](https://www.youtube.com/watch?v=1JGWWH95O1g)
* [How to Use SQLite with Python](https://www.freecodecamp.org/news/sqlite-python-beginners-tutorial/)
* [Moving from Flat Files to SQLite in Python - YouTube](https://www.youtube.com/watch?v=_H5QcCu9saU)
* [SimpleSQLite - Python library to simplify the table creation and data insertion in SQLite database (Automatic table creation from data. Support various data type for insertion: dictionary/namedtuple/list/tuple) http://simplesqlite.readthedocs.org/en/stable/apis/simplesqlite.html](https://github.com/thombashi/SimpleSQLite)
* [SQLite-Image-Handler: Simple to use image handler for python sqlite3.](https://github.com/mozancetin/SQLite-Image-Handler)
  * [Simple to use image handler for python sqlite3](https://pythonawesome.com/simple-to-use-image-handler-for-python-sqlite3/)
* [sqlite-tutorial-pycon-2023](https://github.com/simonw/sqlite-tutorial-pycon-2023)
  * [Data analysis with SQLite and Python for PyCon 2023](https://simonwillison.net/2023/Apr/20/pycon-2023/)
  * [Data analysis with SQLite and Python, PyCon 2023 — Data analysis with SQLite and Python, PyCon 2023 557f94c documentation](https://sqlite-tutorial-pycon-2023.readthedocs.io/)

# TDD, Test
* [Unleashing Confidence in SQL Development through Unit Testing - Tobias Lampert (Lotum) - YouTube](https://www.youtube.com/watch?v=YRVTWwFFd8c)
* [SQLMesh](https://sqlmesh.com/)
* [sql-mock: A Python library to test your SQL models using mocked input data](https://github.com/DeepLcom/sql-mock)
* [sql-test-kit · GitLab](https://gitlab.com/ekinox-io/ekinox-libraries/sql-test-kit)
  * [SQL Test Kit, or how to unit test any SQL query by Victor Landeau - YouTube](https://www.youtube.com/watch?v=chB5f80U9jA)
    * [VidiGo SQL Test Kit, or how to unit test any SQL query by](https://vidigo.ai//chatbot/summary/Rk5j9GHqmMwP86E)
      * sql 쿼리 테스트를 위해 테이블의 구조와 스키마 정보 제공 필요
        * 이후 실제 쿼리 실행 없이도 sql 쿼리의 정확성을 검증 가능
      * 클라우드 서비스 제공업체의 변경 사항으로부터 독립적, 다양한 sql 방언에서 데이터 내부화 원칙을 사용하여 모든 select 쿼리를 테스트 가능
      * 단점으로 인터넷 접속 필요성과 테스트 속도 저하
    * [SQL 테스트 키트 또는 Victor Landeau의 모든 SQL 쿼리를 단위 테스트하는 방법 | 완벽한 영상요약, 릴리스에이아이 | Lilys AI](https://lilys.ai/digest/379887?sId=chB5f80U9jA)
      * 개발 중 발생할 수 있는 오류를 피하기 위해 개발 환경에서 단위 테스트 작성이 중요
        * 데이터 과학자로서 BigQuery에서 SQL 코드를 테스트하려는 노력
          * H2와 Testcontainers같은 도구 존재하나, BigQuery와 Amazon Redshift, Snowflake와 어울리지 않는다는 문제 직면
      * GCP에는 BigQuery의 SQL 방언을 해석할 수 있는 도구가 없어 개인이 작성한 Tinyquery 필요
        * BigQuery이 아닌 GCP에서 수행해야 하는 작업들이 Tinyquery에 의존
      * TinyQuery를 사용하면 모든 SQL 쿼리를 테스트는 불가능, 현재 BigQuery에서만 테스트 가능
        * 컴퓨터에서 실행할 수 있는 테스트를 작성하여 코드를 빠르게 확인하고, BigQuery에서 쿼리를 확인할 수 있는 방법인 'SQL Test Kit' 도입
        * SQL Test Kit을 사용하기 위해서는 테이블에 대한 정보를 프로그램에 알려야 하며, 이 정보를 활용하여 적합한 테스트 작성 가능
      * SQL Test Kit의 Qu interpolator를 사용하여 쿼리 내 데이터 보간 및 테스트 수행
        * 임시 테이블 구축 없이 테이블을 사용하는 쿼리를 실행하여 결과를 얻고, 이를 원래 예상 결과와 비교하여 버그 여부 확인
        * 최종적으로 데이터 보간을 통해 빠르게 쿼리 실행, Python 라이브러리를 활용하여 어떤 SELECT 쿼리든 테스트 가능, 클라우드 제공 업체의 변화에 독립적
      * 인터넷 액세스가 필요하며 단위 테스트 속도 저하
        * SQL로 인한 디버깅이 어렵지만, 단위 테스트를 통해 문제를 해결할 때 도움
