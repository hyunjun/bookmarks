아키텍처를 알아야 앱 개발이 보인다
==================================
<img src="android_clean_code_through_dagger2_jetpack_rxjava/0.jpg" alt="title" width="400"/>

# 01장 안드로이드 애플리케이션 설계 소개 
## 2 애플리케이션의 설계 원칙
<img src="android_clean_code_through_dagger2_jetpack_rxjava/2.jpg" width="400"/>

> 단일 책임 원칙(Single Responsibility Principle)

<img src="android_clean_code_through_dagger2_jetpack_rxjava/3.jpg" width="400"/>

> 개방-폐쇄 원칙(Open Closed Principle)

<img src="android_clean_code_through_dagger2_jetpack_rxjava/4.jpg" width="400"/>

> 리스코프 치환 원칙(Liskov Substitution Principle)
>
> `공변성`의 예를 들면, List<? extends B>란 B를 상속받는 타입으로 이루어진 리스트가 있다면 List<C>를 사용할 수 있다는 내용이다. `반공변성`의 예를 들면, List<? extends B>란 리스트가 있을 때 List<A>를 사용할 수 있다는 것이다. 물론 A의 부모 타입으로도 치환이 가능하다.

<img src="android_clean_code_through_dagger2_jetpack_rxjava/5.jpg" width="400"/> <img src="android_clean_code_through_dagger2_jetpack_rxjava/6.jpg" width="400"/>

> 인터페이스 분리 원칙(Interface Segregation Principle)

<img src="android_clean_code_through_dagger2_jetpack_rxjava/7.jpg" width="400"/>

> 의존 역전 원칙(Dependency Inversion Principle)

## 3 클린 아키텍처
<img src="android_clean_code_through_dagger2_jetpack_rxjava/8.jpg" width="400"/> <img src="android_clean_code_through_dagger2_jetpack_rxjava/9.jpg" width="400"/> <img src="android_clean_code_through_dagger2_jetpack_rxjava/10.jpg" width="400"/> <img src="android_clean_code_through_dagger2_jetpack_rxjava/11.jpg" width="400"/>

## 6 권장하는 애플리케이션 설계
<img src="android_clean_code_through_dagger2_jetpack_rxjava/12.jpg" width="400"/> <img src="android_clean_code_through_dagger2_jetpack_rxjava/13.jpg" width="400"/> <img src="android_clean_code_through_dagger2_jetpack_rxjava/14.jpg" width="400"/>

## 7 안드로이드 애플리케이션 설계 패턴
<img src="android_clean_code_through_dagger2_jetpack_rxjava/15.jpg" width="400"/> <img src="android_clean_code_through_dagger2_jetpack_rxjava/16.jpg" width="400"/> <img src="android_clean_code_through_dagger2_jetpack_rxjava/17.jpg" width="400"/>

> MVC 디자인 패턴

<img src="android_clean_code_through_dagger2_jetpack_rxjava/18.jpg" width="400"/> <img src="android_clean_code_through_dagger2_jetpack_rxjava/19.jpg" width="400"/> <img src="android_clean_code_through_dagger2_jetpack_rxjava/20.jpg" width="400"/>

> MVP 디자인 패턴

<img src="android_clean_code_through_dagger2_jetpack_rxjava/21.jpg" width="400"/> <img src="android_clean_code_through_dagger2_jetpack_rxjava/22.jpg" width="400"/> <img src="android_clean_code_through_dagger2_jetpack_rxjava/23.jpg" width="400"/>

> MVVM 디자인 패턴

# 02장 Dagger2를 이용한 의존성 주입 기법
<img src="android_clean_code_through_dagger2_jetpack_rxjava/24.jpg" width="400"/> <img src="android_clean_code_through_dagger2_jetpack_rxjava/25.jpg" width="400"/> <img src="android_clean_code_through_dagger2_jetpack_rxjava/26.jpg" width="400"/>

> 의존성 주입(DI, Dependency Injection)

<img src="android_clean_code_through_dagger2_jetpack_rxjava/27.jpg" width="400"/> <img src="android_clean_code_through_dagger2_jetpack_rxjava/28.jpg" width="400"/> <img src="android_clean_code_through_dagger2_jetpack_rxjava/29.jpg" width="400"/>

> 제어의 역전(IoC, Inversion of Control)

<img src="android_clean_code_through_dagger2_jetpack_rxjava/30.jpg" width="400"/> <img src="android_clean_code_through_dagger2_jetpack_rxjava/31.jpg" width="400"/> <img src="android_clean_code_through_dagger2_jetpack_rxjava/32.jpg" width="400"/>

> Dagger2 RxJava 마블 다이어그램 Observable

# 05 나만 몰랐던 자바의 고급 기술
<img src="android_clean_code_through_dagger2_jetpack_rxjava/33.jpg" width="400"/>

> 리플렉션

<img src="android_clean_code_through_dagger2_jetpack_rxjava/34.jpg" width="400"/> <img src="android_clean_code_through_dagger2_jetpack_rxjava/35.jpg" width="400"/>

> Dynamic proxy