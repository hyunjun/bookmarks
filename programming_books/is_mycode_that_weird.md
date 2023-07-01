내 코드가 그렇게 이상한가요?
=====================
<img src="is_mycode_that_weird/0.jpg" alt="title" width="400"/>

* 좋은 점
  * Java를 배우는 초보자에게 적합
  * 하나의 주제별로 code와 함께 볼 수 있어 좋은 code를 작성하기 위한 기술을 나눠서 습득 가능
  * code 관련 기술에 대해 주로 다루지만, software engineering에 대한 부분도 조금이라도 다루면서 전반적인 설계 관련된 영역을 제목처럼 '입문'하는데 충실하려고 노력
* 아쉬운 점
  * 저자는 Java를 사용했지만 다른 언어에도 적용이 가능할 거라고 하는데, 꼭 그렇지는 않음
    * e.g. 'static 메서드 오용', 당연히 static keyword가 Java와 일치하는 경우가 아니면 다른 언어에 적용할 수 없음
    * e.g. '인터페이스를 통한 조건 분기 해소', interface를 통해 OOP의 다형성을 구현하는 부분 자체는 좋지만 다른 언어에서 이에 일치하는 게 없으면 옮기기 어려움
  * (위와 유사할 수도 있으나) Java 언어의 설계 이념을 그대로 일반적인 부분으로 오해할 수 있음
    * e.g. '오류는 리턴 값으로 리턴하지 말고 예외 발생시키기' 오류를 return value로 처리하는 가 exception으로 처리하는 가 이 부분은 사실 어느 쪽이 무조건 옳다고 하기 어려운 부분으로 Java를 만든 James Gosling과 Delphi, C#으로 유명한 Anders Hejlsberg간의 논쟁이 유명하다
      * [artima - The Trouble with Checked Exceptions](https://www.artima.com/articles/the-trouble-with-checked-exceptions)
      * [artima - Failure and Exceptions](https://www.artima.com/articles/failure-and-exceptions)

<img src="is_mycode_that_weird/1.jpg" alt="title" width="400"/>

> 콘웨이 법칙(Conway's law)은 '시스템의 구조는 그것을 설계하는 조직의 구조를 닮아 간다'라는 법칙
>
> 콘웨이 법칙은 커뮤니케이션 비용 구조의 법칙... 팀 내부에서 이뤄지는 커뮤니케이션은 비용이 낮고, 팀 외부와의 커뮤니케이션은 비용이 높다는 비용 구조 자체가 시스템 구조에 영향을 준다는 것
>
> 역콘웨이 법칙(inverse Conway's law)... '소프트웨어의 구조를 먼저 설계하고,이후 소프트웨어의 구조에 맞게 조직을 편성한다'
>
> 역콘웨이 법칙을 표면적으로 내세우는 것만으로는 효과가 크지 않았습니다.
* 마지막에 짧게 나오긴 했지만 가장 마음에 드는 부분이라 따로 기록. 커뮤니케이션의 중요성은 어떤 업무에서도 빼놓을 수 없지만, 그 범위를 미리 예측할 수 없고, 문제점을 알아도 나중에 바꾸기 어려운 설계와 관련된 부분에서는 정말, 특히 중요하다.

* ’인사이트‘의 도서를 지원 받아 작성한 리뷰입니다