Network
=======
* [Metcalfe's law](https://en.wikipedia.org/wiki/Metcalfe%27s_law)
  * 네트워크의 효용성은 노드 간 컨넥션 수가 높을 수록 높으므로 노드 수의 제곱에 비례하게 된다는 법칙
  * 하지만 현실적으로는 모든 노드가 서로 컨넥션을 갖지 않는다
  * 따라서 크기가 작은 네트워크에서는 메칼프의 법칙이 성립하지만, 크기가 커지면 성립하지 않음
  * 일반적으로 노드 수가 많은 네트워크는 [complete graph](https://en.wikipedia.org/wiki/Complete_graph)도 아니고 각 컨넥션이 모두 같은 가치를 갖는것도 아니기 때문
* [How to handle CLOSE_WAIT state](http://docs.likejazz.com/close-wait/)
* [넷텐션, 중국의 치명적 '서버 혼잡붕괴'를 밝혀내다](http://m.khgames.co.kr/news/articleView.html?idxno=81843)
* [how DNS works](https://howdns.works/)
* [DNS 기초 지식 – 컴퓨터의 실체와 작동 원리 上](http://library.gabia.com/contents/domain/3979)
* [DNS 기초 지식 – 컴퓨터의 실체와 작동 원리](http://library.gabia.com/contents/domain/3985)
* [‘네임서버 설정’으로 알아보는 DNS: ② IP 주소와 호스트명 알아보기](http://library.gabia.com/contents/domain/4005)
* [‘네임서버 설정’으로 알아보는 DNS: ③ 네임서버 정보는 어디에서 얻을 수 있나](http://library.gabia.com/contents/domain/4009)
* [I don’t know DNS Caching](https://charsyam.wordpress.com/2017/12/22/%EC%9E%85-%EA%B0%9C%EB%B0%9C-i-dont-know-dns-caching/)
  * DNS Caching은 OS와 설정에 따라 다름. glibc의 getaddrinfo 자체에서 발생하는 이슈
* [DNS Caching in JVM](https://charsyam.wordpress.com/2017/12/27/%ec%9e%85-%ea%b0%9c%eb%b0%9c-dns-caching-in-jvm/)
* [Domain Name System (DNS): Untangling the Key Aspects](https://hackernoon.com/domain-name-system-dns-untangling-the-key-aspects-d86e39865d8c)
* [How to Identify and Prevent DNS Leaks](https://hackernoon.com/how-to-identify-and-prevent-dns-leaks-5fa659130a41)
* [An introduction to the Domain Name System](https://medium.freecodecamp.org/understanding-the-domain-name-servers-46c6bcf9afa3)
* [HAVING NO FUN WITH RUBYGEMS, SYSTEMD, DOCKER AND NETWORKING](https://www.fedux.org/articles/2015/09/09/having-no-fun-with-rubygems-systemd-docker-and-networking.html)
* [우리 집에서 구글까지 가는 길](https://evan-moon.github.io/2019/06/22/my-home-to-google/)
* [Pushing the Limits of Kernel Networking](http://rhelblog.redhat.com/2015/09/29/pushing-the-limits-of-kernel-networking/)
* [Non-Imperative Network Programming](https://github.com/mirage/mirage-decks/blob/master/slides/strangeloop15/content.md)
* [비트윈의 멀티티어 아키텍처를 위한 프레젠터 이야기](http://engineering.vcnc.co.kr/2015/11/presenter-multitier-architecture/)
* [Raw Sockets](http://intra97.tistory.com/201)
* [Haste Framework UDP(User Datagram Protocol)를 기반으로 빠르고 쉬운 개발을 위해 만들어진 게임 서버 프레임워크](https://github.com/nhnent/haste.framework)
  * [NDC2016 오픈 소스 '헤이스트' 배포! UDP를 사용해서 게임 서버 만들기](http://www.inven.co.kr/webzine/news/?news=155627&vtype=pc)
* [윈도우즈 소켓 통신 프로그램](http://ehclub.co.kr/category/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D%20%EA%B8%B0%EC%88%A0/%EC%9C%88%EB%8F%84%EC%9A%B0%EC%A6%88%20%EC%86%8C%EC%BC%93%20%ED%86%B5%EC%8B%A0%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%A8)
* [kakao의 Anycast 활용 사례 anycast, quagga, bgp, dns, devops](http://tech.kakao.com/2014/05/29/anycast/)
* [JAVA Network Programming](https://www.youtube.com/watch?v=HyZnrPjelsg)
* [표준 자바 소켓 프로그래밍 / 네트워크 프로그래밍](https://www.youtube.com/watch?v=_kUnut6zZE4)
* [냅스터 부터 P2P까지, PC와 모바일의 클라이언트-서버 모델](http://www.inven.co.kr/webzine/news/?news=164068)
* [동기, 비동기 / blocking, non-blocking](http://kineo2k.tistory.com/m/29)
* [Diffie-Hellman Key Exchange - 공개된 정보만으로 secret key 만들기](http://blog.seulgi.kim/2018/02/diffie-hellman-key-exchange.html)
* [보안 - Alice와 Bob](http://blog.seulgi.kim/2018/03/alice-and-bob_29.html)
* [How to drop 10 million packets per second](https://blog.cloudflare.com/how-to-drop-10-million-packets/)
* [LDAP 프토토콜 맛보기](https://medium.com/happyprogrammer-in-jeju/ldap-%ED%94%84%ED%86%A0%ED%86%A0%EC%BD%9C-%EB%A7%9B%EB%B3%B4%EA%B8%B0-15b53c6a6f26)

# Asynchronous
* [동기 I/O 와 비동기 I/O 의 성능 차이 (부록: Node.js 는 좋을게 없다.)](http://hamait.tistory.com/839)

# C
* [downman.tistory.com/category/응용/TCPIP](http://downman.tistory.com/category/%EC%9D%91%EC%9A%A9/TCPIP)
* [epoll 설명](http://blueheartscabin.blogspot.com/2013/08/c-epoll.html)

# Library
* Cicso packet tracer
  * [네트워크 장비 없이 공부하기 - Cisco Packet Tracer](https://www.youtube.com/watch?v=0f1viq6FjK4)
* [pcap 라이브러리](http://ehclub.co.kr/category/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D%20%EA%B8%B0%EC%88%A0/pcap%20%EB%9D%BC%EC%9D%B4%EB%B8%8C%EB%9F%AC%EB%A6%AC)
* [scapy - packet manipulation](http://www.secdev.org/projects/scapy)
* [SharkFest 2014 - Packet Analysis and Visualization with SteelScript](https://support.riverbed.com/apis/steelscript/SharkFest2014.slides.html)
* [HSTS — N26 hardcoded in your browser](https://mag.n26.com/hsts-n26-hardcoded-in-your-browser-fb2af97ed839)
* HTTP
  * [HTTP ERROR CODE](https://ukjin.tistory.com/2)
    * [HTTP codes as Valentine’s Day comics](https://medium.com/@hanilim/http-codes-as-valentines-day-comics-8c03c805faa0)
    * [301과 302 Redirect의 차이](https://nsinc.tistory.com/168)
    * [Apache 302 error 원인과 해결방법](https://blog.bsmind.co.kr/248)
  * [Android의 HTTP 클라이언트 라이브러리](http://d2.naver.com/helloworld/377316)
  * [나만 모르고 있던 – HTTP/2](http://www.popit.kr/%EB%82%98%EB%A7%8C-%EB%AA%A8%EB%A5%B4%EA%B3%A0-%EC%9E%88%EB%8D%98-http2/)
  * [HTTP란 무엇인가](https://www.zerocho.com/category/HTTP/post/5b344f3af94472001b17f2da)
  * [WEB2 - HTTP](https://opentutorials.org/course/3385)
  * **[HOW HTTPS WORKS](https://howhttps.works/)**
  * [프런트엔드 개발자가 알아야하는 HTTP 프로토콜 Part 1](https://joshua1988.github.io/web-development/http-part1/)
* [HTTP/3 explained](https://daniel.haxx.se/http3-explained/)
* HTTPS
  * [HTTPS로 보안 강화하기](https://blog.outsider.ne.kr/1149)
  * [HTTPS는 HTTP보다 빠르다](https://b.ssut.me/https-is-faster-than-http/)
  * [HTTPS 전환 후 서버 메모리는 안녕한가요?](http://d2.naver.com/helloworld/8842776)
  * [HTTPS 전환 과정에서 read timeout 오류 해결 과정](http://d2.naver.com/helloworld/1469717) apache prefork MPM -> apache nginx, epoll
  * [HTTPS explained with carrier pigeons](https://medium.freecodecamp.org/https-explained-with-carrier-pigeons-7029d2193351)
  * [How to add HTTPS to your website for free in 10 minutes, and why you need to do this now more than ever](https://medium.freecodecamp.org/free-https-c051ca570324)
  * [HTTPS와 SSL 인증서, SSL 동작방법](https://wayhome25.github.io/cs/2018/03/11/ssl-https/)
  * [How to get HTTPS working on your local development environment in 5 minutes](https://medium.freecodecamp.org/how-to-get-https-working-on-your-local-development-environment-in-5-minutes-7af615770eec)
  * [http에서 https로 변경 시 페이스북 like button 값 복구](https://www.popit.kr/https-%EB%B3%80%EA%B2%BD%EC%8B%9C-%ED%8E%98%EC%9D%B4%EC%8A%A4%EB%B6%81-like-button-%EA%B0%92-%EB%B3%B5%EA%B5%AC/)
  * [HTTPS에 대한 기초 이해](https://cheese10yun.github.io/https/)
  * [알아두면 쓸데없는 신비한 TLS 1.3](https://b.luavis.kr/server/tls-1.3)
  * [TLS 연결 디버깅: 인증서 오류를 찾아서](https://rein.kr/blog/archives/4525)
  * [TLS 연결 디버깅: Forward Secrecy 재확인하기](https://rein.kr/blog/archives/4529)
  * [HTTPS - 1. 그림으로 이해하는 HTTPS](https://www.youtube.com/watch?v=NhTstvC7DYY)
  * [HTTPS - 2. HTTPS의 Ciphersuite -1. 키 교환과 인증](https://www.youtube.com/watch?v=iEig3jlT45Y)
  * [How does SSL/TLS make HTTPS secure?](https://hackernoon.com/how-does-ssl-tls-make-https-secure-d247bd4e4cae)
* [unity5-networking-HLAPI-getting-started - An example implementation of HLAPI LAN server-client model.(managing connection with client)](https://github.com/ifndefdeadmau5/unity5-networking-HLAPI-getting-started)
* [uvloop: Blazing fast Python networking](http://magic.io/blog/uvloop-blazing-fast-python-networking/)

# TIME_WAIT
* [What is TIME_WAIT state?](http://docs.likejazz.com/time-wait/)
* [CLOSE_WAIT & TIME_WAIT 최종 분석](http://tech.kakao.com/2016/04/21/tcp-closewait-timewait/)
* [TIME_WAIT 상태란 무엇인가?](http://docs.likejazz.com/time-wait/)
* [로컬 포트 부족과 TIME_WAIT](https://www.popit.kr/%EB%A1%9C%EC%BB%AC-%ED%8F%AC%ED%8A%B8-%EB%B6%80%EC%A1%B1%EA%B3%BC-time-wait/)

# TCP
* [Fun with BPF, or, shutting down a TCP listening socket the hard way](http://pythonsweetness.tumblr.com/post/125005930662/fun-with-bpf-or-shutting-down-a-tcp-listening)
* [TCP/IP 네트워크 스택 이해하기](http://d2.naver.com/helloworld/47667)
* [프로그래밍 기술/TCPIP 프로토콜](http://ehclub.co.kr/category/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D%20%EA%B8%B0%EC%88%A0/TCPIP%20%ED%94%84%EB%A1%9C%ED%86%A0%EC%BD%9C)
* [좀비를 사용해서 정보수집을 해보자(TCP idle Scan)](https://www.youtube.com/watch?v=2-lRPpnT-tc)
* [IPv4 TCP Socket, Listen 에서 Accept 까지…](https://charsyam.wordpress.com/2018/01/09/%ec%9e%85-%ea%b0%9c%eb%b0%9c-ipv4-tcp-socket-listen-%ec%97%90%ec%84%9c-accept-%ea%b9%8c%ec%a7%80/)
* 리눅스 서버의 TCP 네트워크 성능을 결정짓는 커널 파라미터 이야기
  * [1편](http://meetup.toast.com/posts/53)
  * [2편](http://meetup.toast.com/posts/54)
  * [3편](http://meetup.toast.com/posts/55)
* [입개발 NAGLE 알고리즘과 TCP_CORK](https://charsyam.wordpress.com/2019/03/14/%EC%9E%85%EA%B0%9C%EB%B0%9C-nagle-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%EA%B3%BC-tcp_cork/)

# UDP
* [QUIC과 HTTP/3 - 1. UDP기반 전송 프로토콜의 대두](https://www.saturnsoft.net/network/2019/03/21/quic-http3-1/)
* [QUIC과 HTTP/3 - 2. 기존의 성능 개선 기법 및 한계](https://www.saturnsoft.net/network/2019/03/26/quic-http3-2)
