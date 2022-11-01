코딩을 지탱하는 기술
====================
<img src="technologies_that_supports_coding/0.jpg" alt="title" width="400"/>

<img src="technologies_that_supports_coding/1.jpg" width="400"/>

* static typed language가  dynamic typed language에 비해 더 안전하다는 주장에 대한 반박

<img src="technologies_that_supports_coding/2.jpg" width="400"/> <img src="technologies_that_supports_coding/3.jpg" width="400"/>

> 협력적 멀티태스크
>
> 선점적 멀티태스크 - 일정 시간에 교대한다

<img src="technologies_that_supports_coding/4.jpg" width="400"/>

> 경합 상태의 3가지 조건

<img src="technologies_that_supports_coding/5.jpg" width="400"/> <img src="technologies_that_supports_coding/6.jpg" width="400"/>

> 공유하지 않는다 - 프로세스와 액터 모델

<img src="technologies_that_supports_coding/7.jpg" width="400"/>

> 변경하지 않는다 - const, val, Immutable

<img src="technologies_that_supports_coding/8.jpg" width="400"/> <img src="technologies_that_supports_coding/9.jpg" width="400"/>

> 끼어들지 않는다

<img src="technologies_that_supports_coding/10.jpg" width="400"/>

> 10.5 락의 문제점과 해결책

<img src="technologies_that_supports_coding/11.jpg" width="400"/> <img src="technologies_that_supports_coding/12.jpg" width="400"/> <img src="technologies_that_supports_coding/13.jpg" width="400"/> <img src="technologies_that_supports_coding/14.jpg" width="400"/>

> 트랜잭션 메모리 (Transactional memory)

<img src="technologies_that_supports_coding/15.jpg" width="400"/>

> Alan Kay '객체 지향'이란 용어에 대해 질문을 받은 그는
>
> '형에 반대하지는 않지만, 고생하지 않는 형 시스템을 본적이 없다'
>
> 'Simula의 상속 방법은 좋지 않다'
>
> '객체 지향이란 상태를 가진 객체가 메시지를 주고 받아서 커뮤니케이션하는 프로그램이다'
>
> 형이나 상속에 대한 부정적인 입장

<img src="technologies_that_supports_coding/16.jpg" width="400"/> <img src="technologies_that_supports_coding/17.jpg" width="400"/>

> 클래스란?

<img src="technologies_that_supports_coding/18.jpg" width="400"/>

> 클로저
>
> 함수를 함수 안에 정의하고,내포할 수 있는 정적 스코프가 있어서 함수를 반환값으로 사용하거나 변수에 대입하여 사용한다는 개념
>
> 어떤 standard ML 학습서. 자유 변수를 포함한 식을 '열린 식'이라고 부르고, 그 자유 변수의 바인딩을 조합함으로 해당 식을 닫고 있기 때문

<img src="technologies_that_supports_coding/19.jpg" width="400"/> <img src="technologies_that_supports_coding/20.jpg" width="400"/>

> 사람의 인지 능력에 한계가 있기 때문에 영향 범위가 너무 크면 이해할 수 없게 된다. 영향 범위가 작은 쪽이 이해하기 편하다.

<img src="technologies_that_supports_coding/21.jpg" width="400"/>

> 리스코프의 치환 원칙

<img src="technologies_that_supports_coding/22.jpg" width="400"/>

> 클래스 상속과 형 구조의 정합성을 유지하기가 얼마나 어려운지

<img src="technologies_that_supports_coding/23.jpg" width="400"/> <img src="technologies_that_supports_coding/24.jpg" width="400"/> <img src="technologies_that_supports_coding/25.jpg" width="400"/>

> 해결책 1: 다중 상속을 금지한다
>
> 위임, 의존성 주입(Dependency Injection)
>
> 인터페이스

<img src="technologies_that_supports_coding/26.jpg" width="400"/> <img src="technologies_that_supports_coding/27.jpg" width="400"/> <img src="technologies_that_supports_coding/28.jpg" width="400"/> <img src="technologies_that_supports_coding/29.jpg" width="400"/>

> 해결책 2: 메소드 해결 순서를 고민한다
>
> 깊이 우선 탐색의 문제점
>
> C3 선형화로 순서를 정한다

<img src="technologies_that_supports_coding/30.jpg" width="400"/> <img src="technologies_that_supports_coding/31.jpg" width="400"/> <img src="technologies_that_supports_coding/32.jpg" width="400"/>

> 해결책 3: 처리를 섞는다
>
> 믹스-인

<img src="technologies_that_supports_coding/33.jpg" width="400"/> <img src="technologies_that_supports_coding/34.jpg" width="400"/> <img src="technologies_that_supports_coding/35.jpg" width="400"/> <img src="technologies_that_supports_coding/36.jpg" width="400"/>

> 해결책 4: 트레이트
>
> goto가 강력했지만 무대에서 사라져간 역사를 기억. 기능이 강력하다고 반드시 편리한 것만은 아니다.