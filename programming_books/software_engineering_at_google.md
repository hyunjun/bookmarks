# Software Engineering at Google 구글 엔지니어는 이렇게 일한다
<img src="software_engineering_at_google/title.jpg" alt="title" width="400"/>

<img src="software_engineering_at_google/0.jpg" alt="" width="400"/>

> 소프트웨어 엔지니어링software engineering은 단순히 코드를 작성하는 행위에 더하여, 시간의 흐름에 발맞춰 한 조직이 그 코드를 구축하고 유지보수하는 데 이용하는 모든 도구와 프로세스를 포괄합니다. 이것이 우리가 제안하는 소프트웨어 엔지니어링의 개념입니다.

## Part I 전제

### CHAPTER 1 소프트웨어 엔지니어링이란?
<img src="software_engineering_at_google/2.jpg" alt="" width="400"/>

> 프로그래밍과 소프트웨어 엔지니어링의 가장 큰 차이는 시간time, (규모) 확장scale, 실전에서의 트레이드오프trade-offs at play, 이렇게 세 가지라고 생각합니다. 소프트웨어 엔지니어링 프로젝트에서 엔지니어는 시간의 흐름과 언젠가 변경 change 가능성에 더 신경 써야 합니다. 소프트웨어 엔지니어링 조직은 만들어낼 소프트웨어 자체뿐 아니라 제작하는 조직까지 양 측면 모두에서의 확장과 효율에 더 집중해야 합니다. 마지막으로 소프트웨어 엔지니어는 대체로 수명과 성장 속도를 정밀하게 예측하기 어려운 상황에서, 결과에 더 큰 영향을 주는 보다 복잡한 결정을 내려야 합니다.
>
> 구글에서는 이따금 '소프트웨어 엔지니어링은 흐르는 시간 위에서 순간순간의 프로그래밍을 모두 합산한 것이다software engineering is programming integrated over time'라고 말하곤 합니다. 소프트웨어 엔지니어링에서 프로그래밍이 큰 비중을 차지하는 건 틀림없지만 프로그래밍은 결국 새로운 소프트웨어를 제작하는 수단입니다. 여러분이 이 차이를 받아들인다면 자연스럽게 프로그래밍 작업 (개발development)과 소프트웨어 엔지니어링 작업 (개발development + 수정modification + 유지보수maintenance)의 차이도 궁금할 것입니다. 시간이라는 요소가 더해지면서 프로그래밍에는 중요한 차원이 하나 늘어서 더 입체적으로 바뀝니다. 정육면체는 정사각형이 아니고 거리는 속도가 아니듯, 소프트웨어 엔지니어링은 프로그래밍이 아닌 것이죠.

<img src="software_engineering_at_google/3.jpg" alt="" width="400"/>

> 계획 세우기를 등한시하거나 소프트웨어를 더 잘 이해하려는 노력을 포기해서는 안 됩니다. 문제를 완벽하게 제거할 수는 없더라도 완화할 수는 있기 때문입니다.

<img src="software_engineering_at_google/4.jpg" alt="" width="400"/>

> 결국 엔지니어링 조직의 선택을 결정짓는 요인은 다음의 몇 가지로 압축됩니다.
>
> • 반드시 해야 하는 일(법적 요구사항 고객 요구사항)
>
> • 근거에 기반하여 당시 내릴 수 있는 최선의 선택(적절한 결정권자가 확정)
>
> 의사결정이 '내가 시켰으니까'가 되어서는 안 됩니다.

## Part II 문화

### CHAPTER 2 팀워크 이끌어내기
<img src="software_engineering_at_google/6.jpg" alt="" width="400"/>

> 사람은 완벽하지 않습니다. 그래서 인간을 '간헐적 버그들의 집합에 가깝다고 이야기하곤 하죠. 하지만 동료에 내재된 버그를 이해하려면, 무엇보다 여러분 내면에 서식하는 버그를 먼저 이해해야 합니다.
>
> 소프트웨어 개발은 '팀의 단합된 노력'의 결실. 그래서 엔지니어링팀이 (혹은 어떤 형태든 창의적 협업이 성공하려면 겸손, 존중, 신뢰라는 핵심 원칙에 맞게 여러분 자신의 행동을 바로잡아야

<img src="software_engineering_at_google/7.jpg" alt="" width="400"/>

> 천재 신화 The Genius Myth는 팀이 이룬 성공을 단 한 사람 (리더)에게 몰아주어 만들어지는 경향이 있습니다.

<img src="software_engineering_at_google/8.jpg" alt="" width="400"/>

> 현재의 데브옵스DevOps 철학은 '가능한 한 일찍 피드백하고, 가능한 한 일찍 테스트하고, 보안과 프로덕션 환경을 가능한 한 초기부터 고려한다'라는 목표를 천명하고 있습니다. 이 모두는 개발워크플로를 '원점 회귀shift lett'라는 아이디어에 녹아 있습니다. 즉, 문제를 빨리 찾을수록 고치는 비용이 낮아집니다.
>
> 빠른 피드백 루프는 코드 수준뿐 아니라 전체 프로젝트 수준에서도 이뤄져야 합니다.

### CHAPTER 3 지식 공유
<img src="software_engineering_at_google/9.jpg" alt="" width="400"/>

> 가장 중요한 사실은 조직에 배움의 문화가 자리 잡혀야 한다는 것이고, 그러려면 사람들에게 모르는 걸 인정할 수 있도록 돕는 심리적 안전Psychological safety을 제공해야 합니다.

<img src="software_engineering_at_google/10.jpg" alt="" width="400"/>

> 소프트웨어 엔지니어링에서 가장 중요한 요소는 사람입니다. 코드는 중요한 산출물이지만 제품 개발 전체를 보면 작은 부분에 지나지 않죠... 조직의 성패는 인력에 얼마나 투자해서 잘 키워내느냐에 달려 있습니다.

<img src="software_engineering_at_google/11.jpg" alt="" width="400"/>

> 배움에는 '무언가를 시도하다가 실패해도 안전하다'는 인식이 엄청나게 중요합니다. 건강한 환경에서라면 사람들은 질문을 던지고, 틀리고, 새로운 지식을 얻는 걸 편안하게 생각합니다. 이것이 구글이 모든 팀에 기본적으로 기대하는 바입니다. 우리 연구에 따르면 심리적 안전이 효과적인 팀을 이루는 데 가장 중요한 요인이었습니다."
>
> 심리적 안전 외에는 '신뢰성(dependability), '구조와 명확성(structure & clarity). 일의 의미(meaning of work). 일의 영향력(impact of work)이 중요한 요인

<img src="software_engineering_at_google/12.jpg" alt="" width="400"/>

> 일대일 도움은 밀도가 높지만 확장하는 데는 필연적으로 한계가 있습니다. 배우는 쪽에서도 상세 내용을 모두 다 기억하기란 쉽지 않습니다. 그러니 미래의 자신을 위해서라도 무언가를 일대일로 배울 때는 '기록하는 습관'을 기르세요. 여러분보다 나중에 들어오는 동료들도 여러분과 똑같은 질문을 할 가능성이 큽니다. 그들을 위해 기록해둔 지식을 공유하세요.

### CHAPTER 4 공정사회를 위한 엔지니어링
<img src="software_engineering_at_google/14.jpg" alt="" width="400"/>

> 모두와 '함께' 만들자... 모두를 위한 제품을 만드는 길은 무엇일까요? 바로 사용자와 함께 만드는 것입니다.

### CHAPTER 5 팀 이끌기
<img src="software_engineering_at_google/15.jpg" alt="" width="400"/>

> 여러분 스스로 '난 절대 관리자는 되지 않을 거야'라고 맹세했더라도 경력이 쌓이다보면 어느 순간 리더의 위치에 올라서 있는 자신을 발견하게 될 것입니다. 주어진 역할을 성공적으로 완수한 사람일수록 더 그렇죠.

<img src="software_engineering_at_google/16.jpg" alt="" width="400"/>

> 리더는 항상 무대 위에 있다고 생각하는 방법도 좋습니다. 여러분이 공식적인 리더의 위치에있다면 주변 사람들이 여러분의 일거수일투족을 항시 두 눈 똑바로 뜨고 쳐다보고 있다는 뜻입니다. 회의를 주재하거나 발언할 때는 당연하고, 메일에 답장하느라 컴퓨터 앞에 앉아 있을 때도 마찬가지입니다. 여러분의 몸짓, 사소한 이야기에 돌아오는 반응, 점심식사를 하며 보내는미묘한 신호들로부터 단서들을 얻어갑니다. 그들이 읽은 것이 자신감일까요 아니면 두려움일까요? 리더로서 여러분의 역할은 사람들을 고무시키는 것임을 명심하세요 관찰은 하루 24시간일주일 내내 이루어집니다. 아무리 사소한 것이라도 여러분이 내비치는 거의 모든 것이 무의식적으로 알려지고 팀에 전염됩니다.

### CHAPTER 6 성장하는 조직 이끌기
<img src="software_engineering_at_google/17.jpg" alt="" width="400"/>

> 늘 결정하라(Always Be Deciding)", "늘 떠나라(Always Be Leaving). 늘 확장하라(Aways Be Scaling)의 영어 첫 글자가 모두 'A'라서 3A

<img src="software_engineering_at_google/18.jpg" alt="" width="400"/>

> 관찰과 경청 95%, 절묘하고 시의적절한 개입 5% 이것이 좋은 관리입니다. 부하 리더들의 말을 경청하고 보고서는 건너뛰세요. 고객과 대화하세요.

<img src="software_engineering_at_google/19.jpg" alt="" width="400"/>

> 긴 코드 블록의 finally'절이 되는 것이죠.
>
> 조급함은 리더인 여러분의 효율을 갉아먹는 가장 큰 적입니다. 스스로를 완전한 반응형 모드로 전환해버리면 (거의 자동적으로 이렇게 됩니다) 삶 전체의 순간순간을 오로지 급한 일만 처리하면서 흘려보내게 됩니다. 멀리 보면 '중요하지 않은 일들임에도 말이죠. 리더로서 여러분은 '나만이 할 수 있는 일을 처리해야 함을 잊지 마세요.

### CHAPTER 7 엔지니어링 생산성 측정하기
<img src="software_engineering_at_google/20.jpg" alt="" width="400"/>

> 구글은 특히 소프트웨어 엔지니어링 측면에서 엔지니어링 생산성 자체에 집중하는 전문가팀을 별도로 꾸려두면 회사 성장 과정에서 아주 중요하고 값진 통찰을 얻을 수 있음을 알아냈습니다.

<img src="software_engineering_at_google/21.jpg" alt="" width="400"/>

> 단순히 추측에 맡기는 건 바라지 않지만, 그렇다고 의미 없는 측정을 하느라 시간과 자원을 낭비하지 말아야 합니다.

<img src="software_engineering_at_google/22.jpg" alt="" width="400"/>

> 구글은 지표를 만들 때 GSM이라는 프레임워크를 씁니다. GSM은 목표goal/신호signal/지표metric의 약자입니다.

## Part III 프로세스

### CHAPTER 8 스타일 가이드와 규칙
<img src="software_engineering_at_google/24.jpg" alt="" width="400"/>

> 규칙은 곧 법입니다. 제안이나 권장사항이 아닌, 엄격하고 꼭 지켜야 하는 법입니다. 코드 전반에서 따라야 하는 강제사항이라서 꼭 필요하여 승인된 경우를 제외하고는 무시할 수 없습니다.한편 지침guidance은 권장사항과 모범 사례를 말합니다. 따르면 편이 이득이라서 어지간하면 따르라고 권하지만, 규칙과 달리 다소 변형해 적용해도 괜찮습니다.

<img src="software_engineering_at_google/25.jpg" alt="" width="400"/>

> 규칙을 관리하는 목표는 '좋은' 행동을 장려하고 '나쁜'행동을 억제하기 위함입니다. '좋은'과 '나쁜'의 해석은 조직마다 차이가 있습니다. 관심사가 다르기 때문이죠. 좋음 나쁨은 주관적이고 무엇이 필요하냐에 따라 달라집니다.

<img src="software_engineering_at_google/26.jpg" alt="" width="400"/>

> 일관성은 규모를 확장하기 쉽게 도와줍니다. 조직 확장에는 도구 활용이 핵심이며 코드가 일관되면 코드를 이해하고 수정하고 생성하는 도구를 더 쉽게 만들 수 있습니다...
>
> 인력을 늘리는 데도 도움이 됩니다...
>
> 시간 관점에서도 탄력성을 보장합니다...

### CHAPTER 9 코드 리뷰
<img src="software_engineering_at_google/28.jpg" alt="" width="400"/>

> 우리는 코드가 그 자체로 부채임을 인정하고 잊지 말아야 합니다. 없어서는 안 될 부채이긴 하겠으나 존재만으로 어느 순간 누군가가 유지보수해야 할 대상이 되어버립니다. 마치 비행기의 연료처럼 비행기를 띄우려면 반드시 필요하지만, 그 자체가 하중을 늘려 부담으로 작용하죠.

<img src="software_engineering_at_google/29.jpg" alt="" width="400"/>

> '이 코드는 유지보수하기 쉬운가?', '내게 기술 부채를 안겨주나?''우리 팀원 중에 이 코드를 유지보수해줄 전문가가 있나?"

<img src="software_engineering_at_google/30.jpg" alt="" width="400"/>

> 구글은 아무리 작더라도 코드베이스를 수정하는 거의 모든 변경에 코드 리뷰를 요구합니다.

<img src="software_engineering_at_google/31.jpg" alt="" width="400"/>

> 프로세스 자체를 확장할 방법이 없습니다. 코드 리뷰를 작게 실행함으로써 확장성을 잃지 않는 것이죠.

### CHAPTER 10 문서자료
<img src="software_engineering_at_google/32.jpg" alt="" width="400"/>

> 구글에서 문서자료를 개선하고자 해본 시도 중 가장 성공적이었던 방법은 문서자료를 코드처럼 취급하여 엔지니어링 워크플로에 통합하는 것이었습니다.

<img src="software_engineering_at_google/33.jpg" alt="" width="400"/>

> 치트키는 없습니다. 하지만 우리는 오랜 경험에서 문서를 짧게 쓰는 게 유리하다는 사실을 알아냈습니다.

### CHAPTER 11 테스트 개요
<img src="software_engineering_at_google/35.jpg" alt="" width="400"/>

> 가장 단순한 테스트는 다음 요소들로 정의할 수 있습니다.
>
> • 테스트하려는 단 하나의 행위(주로 메서드나 API)
>
> • 특정한 입력(API에 전달하려는 값)
>
> • 관측 가능한 출력 혹은 동작
>
> • 통제된 조건(하나의 격리된 프로세스 등)

<img src="software_engineering_at_google/36.jpg" alt="" width="400"/>

> 문제들을 해결하고자 GWS의 테크 리드(TL)는 엔지니어 주도의 자동 테스트를 정책 차원에서 도입하기로 했습니다. 이 정책의 일환으로 모든 코드 변경에는 지속해서 실행할 수 있는 테스트가 반드시 딸려 있어야 했습니다. 정책 도입 1년 만에 긴급하게 코드를 수정해 배포하는 건수가 '절반'으로 줄었습니다.

<img src="software_engineering_at_google/37.jpg" alt="" width="400"/>

> 그래서 테스트에서의 해법은 단 하나, 바로 '자동화'뿐입니다.

<img src="software_engineering_at_google/38.jpg" alt="" width="400"/>

> 테스트 피라미드 / 테스트 스위트 안티패턴 아이스크림 콘, 모래시계

### CHAPTER 12 단위 테스트
<img src="software_engineering_at_google/39.jpg" alt="" width="400"/>

> 테스트의 가장 중요한 목적은 물론 버그 예방입니다. 그다음으로 중요한 목적을 꼽자면 엔지니어의 생산성 개선입니다. 범위가 더 넓은 테스트들과 비교하여 단위 테스트는 생산성을 끌어올리는 훌륭한 수단이 될 수 있는 특성을 많이 지니고 있습니다.

<img src="software_engineering_at_google/40.jpg" alt="" width="400"/>

> 이상적인 테스트라면 변하지 않아야 합니다. 한 번 작성한 후로는 대상 시스템의 요구사항이 바뀌지 않는 한 절대 수정할 일이 없어야 합니다.

### CHAPTER 13 테스트 대역
* [Test Double at XUnitPatterns.com](http://xunitpatterns.com/Test%20Double.html)

<img src="software_engineering_at_google/42.jpg" alt="" width="400"/>

> 구글이 어렵게 깨우친 교훈 하나는 테스트 대역을 쉽게 만들어주는 모의 객체 프레임워크를 과용하면 위험하다는 것입니다

<img src="software_engineering_at_google/43.jpg" alt="" width="400"/>

> 실제 구현을 선호하는 테스트 방식을 고전적 테스트classical test라고 하며, 반대로 모의 객체 프레임워크를 선호하는 테스트 방식은 모의 객체 중심주의 테스트mockist test라고 합니다." (초기 모의 객체 프레임워크들의 창시자들'을 포함하여) 소프트웨어 업계에는 모의 객체를 예찬하는 사람도 있지만 구글은 모의 객체 중심주의는 확장하기 어렵다고 결론지었습니다. 모의 객체 중심주의에서는 엔지니어들이 대상 시스템을 엄격한 지침에 따라 설계해야 합니다. 하지만 구글의 엔지니어 대부분은 고전적인 테스트에 더 적합한 방식으로 코드를 작성해왔습니다.
* [Mocks, Fakes, Stubs and Dummies at XUnitPatterns.com](http://xunitpatterns.com/Mocks,%20Fakes,%20Stubs%20and%20Dummies.html)
* [Mocks Aren't Stubs](https://martinfowler.com/articles/mocksArentStubs.html)
* [Mock Objects: A Brief History of Mock Objects](http://www.mockobjects.com/2009/09/brief-history-of-mock-objects.html)
* [Mock Roles, not Objects](http://jmock.org/oopsla2004.pdf)

### CHAPTER 14 더 큰 테스트
<img src="software_engineering_at_google/45.jpg" alt="" width="400"/> <img src="software_engineering_at_google/46.jpg" alt="" width="400"/> <img src="software_engineering_at_google/47.jpg" alt="" width="400"/>

> 단위 테스트로는 위험 요인을 충분히 해소하기 어려운 대표적인 영역 다섯 가지
>
> 1) 부정확한 테스트 대역
>
> 2) 설정 문제
>
> 3) 과부하 시 나타나는 문제
>
> 4) 예기치 못한 동작, 입력, 부작용
>
> 5) 창발적 행위'와 '진공 효과'
* [Hyrum's Law](https://www.hyrumslaw.com/)

<img src="software_engineering_at_google/48.jpg" alt="" width="400"/>

> 높은 신뢰성: 결과가 불규칙하면 안 되며 유용한 성공/실패 신호를 제공해야 합니다.
>
> 빠른 속도: 개발자 워크플로를 방해하지 않을 정도로 빨라야 합니다.
>
> 높은 확장성: 구글은 변경되는 코드에 영향을 받는 모든 테스트를 서브밋 직전과 직후에 효율적으로 실행할 수 있어야 합니다.
>
> 좋은 단위 테스트라면 이상의 특징을 모두 갖춰야 합니다.
>
> 더 큰 테스트가 극복해야 할 과제가 두 가지 더 있습니다.
>
> 첫 번째는 소유권 문제입니다...
>
> 두 번째 과제는 표준화 혹은 표준화 부족입니다...

<img src="software_engineering_at_google/49.jpg" alt="" width="400"/> <img src="software_engineering_at_google/50.jpg" alt="" width="400"/>

### CHAPTER 15 폐기
<img src="software_engineering_at_google/52.jpg" alt="" width="400"/>

> 코드 '자체'는 가치를 창출하지 않습니다. 가치를 만들어내는 건 바로 '기능'입니다. 사용자의 요구에 부합하는 기능은 자산입니다. 이 기능을 구현하는 코드는 그저 목적지로 가기 위한 수단인것이죠. 똑같은 기능을 하는 두 코드가 있습니다. 하나는 이해하기 쉽게 짜여서 유지보수도 문제가 없는 한 줄짜리이고, 다른 하나는 1만 줄이나 되는 난해한 스파게티 코드입니다. 우리는 전자를 선호합니다. 코드 자체는 비용을 낳기 때문에 기능이 같다면 코드 자체는 단순할수록 좋습니다.
>
> 따라서 우리는 얼마나 많은 코드를 작성하느냐나 코드베이스가 얼마나 큰가가 아니라, 단위 코드당 얼마나 많은 기능을 제공하느냐에 집중하여 이 지표를 극대화해야 합니다. 더 많은 기능을 제공하길 기대하면서 코드의 양만 늘려서는 안 됩니다. 오히려 지나친 코드나 더 이상 필요 없는 시스템들을 제거해야 하죠. 이때 필요한 것이 바로 폐기 정책과 절차입니다.

<img src="software_engineering_at_google/53.jpg" alt="" width="400"/>

> '언젠가는 폐기하게 될 시스템을 설계한다'라는 개념이 소프트웨어 엔지니어링 시각에서는 생소할 수 있지만 다른 엔지니어링 분야에서는 흔한 일입니다.

## Part IV 도구

### CHAPTER 16 버전 관리와 브랜치 관리
<img src="software_engineering_at_google/56.jpg" alt="" width="400"/>

> 경영진이 엔지니어의 일을 '소프트웨어 엔지니어링'이 아닌 '소프트웨어 개발'로만 생각해도 VCS를 주저하게 됩니다. 코드를 작성해 론칭한 후에도 오랜 기간 중단 없이 작동하며 가치를 창출하도록 관리하는 일로 봐주지 않고 앉아서 그저 코드만 작성하는 일로 바라본다는 뜻입니다. 엔지니어 업무의 핵심을 프로그래밍으로 인식하여 코드와 시간의 상호작용을 제대로 이해하지 못한다면 '실수를 되돌리기 위해 이전 버전으로 돌아간다'라는 기능은 이상하고 값비싼 사치로 느껴질 수 있습니다.

<img src="software_engineering_at_google/57.jpg" alt="" width="400"/>

> 구글의 DORA DevOps Research and Assessment 조직의 연구 결과에 따르면 최고 수준의 기술 조직에는 릴리스 브랜치조차 없습니다. 트렁크로부터 하루에도 몇 번씩 릴리스할 수 있는 지속적 배포continuous deployment (CD)가 잘 자리 잡은 조직에서는 대체로 릴리스 브랜치를 건너뜁니다. 수정사항을 적용해 다시 배포하는 게 훨씬 쉽기 때문이죠. 그래서 별도 브랜치를 두고 병합할 코드를 선별하는 일은 모두 불필요한 오버헤드인 셈입니다.

<img src="software_engineering_at_google/58.jpg" alt="" width="400"/>

> 개발자가 '이 구성요소는 어떤 버전을 사용해야 하죠?'라고 묻는 상황을 만들지 않아야 합니다.
>
> 이 말이 곧 '원-버전 규칙One-Version Rule' 입니다.

### CHAPTER 17 Code Search
<img src="software_engineering_at_google/60.jpg" alt="" width="400"/>

> 대체로 사람은 지연시간이 200밀리초보다 짧기만 하면 UI가 빠르다고 느낍니다. 하지만 1초가 넘어가면 주의가 분산되기 시작하죠. 여기서 10초가 더 흐르면 전혀 다른 일을 하기 시작하여 생산성을 급격히 떨어뜨릴 가능성이 큽니다.
* [Best Practices for Response Times and Latency · Tendrl/documentation Wiki](https://github.com/Tendrl/documentation/wiki/Best-Practices-for-Response-Times-and-Latency)

### CHAPTER 18 빌드 시스템과 빌드 철학
<img src="software_engineering_at_google/62.jpg" alt="" width="400"/>

> 외부 의존성 관리는 훨씬 어렵다는 것입니다

<img src="software_engineering_at_google/63.jpg" alt="" width="400"/>

> 때로는 엔지니어의 힘과 유연성을 제한해야 생산성을 높일 수 있다
>
> 작은 모듈 방식이 굵직한 모듈 방식보다 잘 확장됨

### CHAPTER 19 Critique: 구글의 코드 리뷰 도구
<img src="software_engineering_at_google/65.jpg" alt="" width="400"/>

> 리뷰어가 변경을 거부하려면 반드시 유용한 피드백을 함께 줘야 합니다. 부정적인 피드백은 구체적인 수정사항을 반드시 포함해야 합니다.

### CHAPTER 20 정적 분석

### CHAPTER 21 의존성 관리
<img src="software_engineering_at_google/66.jpg" alt="" width="400"/>

> 의존성 관리 문제는 정의하는 것부터가 쉽지 않습니다... 의존성 하나를 관리하는 방법이 중요한 게 아닙니다. 수많은 의존성들로 구성된 네트워크와 그 네트워크에 미래에 일어날 변화까지 고려해 관리하는 방법을 강구해야 합니다.

<img src="software_engineering_at_google/67.jpg" alt="" width="400"/>

> 프로그래밍 측면에서 보면 직접 처음부터 새로 짜는 것보다 기존 인프라를 재활용하는 게 분명히 더 낫습니다. 두말하면 잔소리고, 기술이 진보할 수 있는 근본에 속합니다.

<img src="software_engineering_at_google/68.jpg" alt="" width="400"/>

> • 의존성 관리보다는 되도록 버전 관리가 되도록 합니다. 더 많은 코드를 조직 내로 가져와 투명성과 통제력을 높인다면 문제가 훨씬 단순해집니다.
>
> • 소프트웨어 엔지니어링 프로젝트에서 의존성 추가는 공짜가 아닙니다. 의존성 네트워크에서의 신뢰 관계를 지속하는 문제는 매우 복잡합니다. 여러분의 조직에 의존성을 임포트할 때는 장기 지원 비용까지 고려해서 신중하게 결정해야 합니다.
>
> • 의존성 역시 하나의 계약입니다. 주는 게 있고 받는 게 있죠. 계약에서는 제공자와 소비자 모두 일정한 권리와 의무를 갖습니다. 제공자가 제시하는 내용에는 지금 당장뿐 아니라 미래에 대한 약속도 명확하게 포함되어야 합니다.

### CHAPTER 22 대규모 변경
<img src="software_engineering_at_google/69.jpg" alt="" width="400"/>

> 구글은 일찍이 코드베이스 전반을 전면적으로 건드리는 변경을 원자적으로 수행한다는 아이디어를 포기했습니다. 우리 경험에 따르면 코드베이스와 엔지니어 수가 늘어날수록 원자적으로 수행할 수 있는 변경의 크기는 거꾸로 줄어듭니다. 영향받는 모든 프리서브밋 검사와 테스트를 수행하기가 어렵고, 서브밋 전에 변경에 포함된 파일 전부가 최신 버전인지도 확신할 수 없게 됩니다. 기반 인프라를 계속 개선시켜야 하는데 전면적인 변경은 점점 어려워지면서, 우리는 대규모 변경을 바라보는 관점을 바꾸고 이를 현실에서 실행할 방법을 개발해내야 했습니다.

<img src="software_engineering_at_google/70.jpg" alt="" width="400"/>

> 소프트웨어가 철저하게 테스트된다면 변경해도 이상이 생기지 않으리라는 믿음이 생깁니다. 시스템이 얼마나 오래되었고 복잡한지는 문제되지 않습니다.

<img src="software_engineering_at_google/71.jpg" alt="" width="400"/>

> 모든 변경은 테스트되어야 합니다 (프로세스 이야기는 잠시 후에 하겠습니다). 하지만 변경의 덩치가 커지면 제대로 테스트하기가 훨씬 어렵습니다.

### CHAPTER 23 지속적 통합
* [Continuous Integration](https://www.martinfowler.com/articles/continuousIntegration.html)

<img src="software_engineering_at_google/73.jpg" alt="" width="400"/>

> 지속적 통합: 빠르게 진화하는 복잡한 생태계 전체를 지속적으로 조립하고 테스트하는 개발 방식

<img src="software_engineering_at_google/74.jpg" alt="" width="400"/>

<img src="software_engineering_at_google/75.jpg" alt="" width="400"/>

> 우리는 프로덕션 시스템이 환경 변화에 어떻게 반응하는지 이해하기 위해 모니터링&경보 시스템을 이용합니다. 마찬가지로 CI는 소프트웨어가 환경 변화에 어떻게 적응하는지를 알려줍니다. 프로덕션 모니터링에는 수동 경보와 가동 중인 시스템의 능동 프로버를 이용합니다. 이에 반해 CI는 변경된 소프트웨어를 배포하기 전에 단위 테스트와 통합 테스트를 수행합니다. 두 영역을 잘 비교해보면 한 영역에서 쌓은 지식을 다른 영역에도 적용할 수 있습니다.

### CHAPTER 24 지속적 배포
<img src="software_engineering_at_google/76.jpg" alt="" width="400"/>

> 에릭 레이먼드의 성당과 시장에서 에릭 리스의 린스타트업까지 오랜 기간 성공적으로 살아남은 조직들은 하나같이 아이디어를 빠르게 실천하고 고객의 손에 최대한 빨리 전달하고 그들의 피드백에 신속하게 대응하는 능력을 갖췄습니다. 마틴 파울러는 '소프트웨어 개발에서 가장 큰 위험은 결국은 쓸데없는 무언가를 만들어내는 것입니다. 동작하는 소프트웨어를 조기에 그리고 더 자주 고객 손에 쥐어준다면 실제로 어느 정도의 가치가 있는지를 빠르게 확인할 수 있습니다'라고 했습니다."
* [ContinuousDelivery](https://martinfowler.com/bliki/ContinuousDelivery.html)

<img src="software_engineering_at_google/77.jpg" alt="" width="400"/> <img src="software_engineering_at_google/78.jpg" alt="" width="400"/>

> 지속적 배포continuous delivery (CD) 그리고 애자일 방법론의 핵심 교리는 작은 변경들을 자주 배포할수록 품질이 높아진다는 것입니다. '빠를수록 안전하다 faster is safer'라는 말이죠.
>
> • 민첩성: 자주 작게 릴리스합니다.
>
> • 자동화: 잦은 릴리스에 수반되는 반복 작업 부담을 줄이거나 없앱니다.
>
> • 격리: 변경을 격리하여 문제를 쉽게 해결할 수 있도록 모듈화된 아키텍처를 지향합니다.
>
> • 신뢰성: 비정상 종료와 지연시간 같은 주요 상태 지표를 측정하고 꾸준히 개선합니다.
>
> • 데이터 중심 의사 결정: A/B 실험으로 상태 지표를 비교하여 품질을 높입니다.
>
> • 단계적 출시: 변경을 모두에게 동시에 출시하지 않고 소수의 사용자부터 이용해보게 합니다.

<img src="software_engineering_at_google/79.jpg" alt="" width="400"/>

> 릴리스 비용이 늘고 위험이 커지면 '본능적'으로 릴리스 주기를 늦춰 안정성을 확보할 기간을 늘리려 합니다. 하지만 이렇게 해서 얻는 안도감은 짧은 기간만 유지될 뿐, 멀리 보면 팀의 속도가 느려지고 팀과 고객 모두를 좌절시키는 선택입니다. '답'은 비용을 줄이고, 규율을 강화하고, 위험에 점진적으로 대응하는 것입니다. 당장의 안정을 위한 프로세스 수정에 저항하고 장기적인 아키텍처 개선에 투자해야 하는 게 핵심입니다. 눈앞의 안정만 추구한다면 낡은 개발 프로세스로 회귀하기 쉽습니다. 예를 들어, 배우고 반복할 여지를 거의 남기지 않는 계획 중심 모델로 되돌리고, 개발 프로세스를 더 철저하게 관리 감독하고, 위험 평가를 수행하여 위험이 낮은 (주로 가치도 적은) 기능을 선호하게 됩니다.
>
> 구글의 역사를 보면 종종 제품을 단순히 마이그레이션하는 수준이 아니라 처음부터 다시 짜는 게 올바른 선택이었습니다.

<img src="software_engineering_at_google/80.jpg" alt="" width="400"/>

> 완벽한 바이너리는 없습니다.프로덕션에 새로운 변경을 릴리스할 때마다 무언가를 결정하고 절충해야 합니다. 핵심 성과 지표key performance indicator (KPI)와 명확한 문턱값을 활용하면 비록 완벽하지는 않더라도 기능을 출시할 수 있습니다. 자칫 논란으로 이어질 결정에 확실한 근거가 되어주는 것이죠.
>
> 릴리스가 다가오면 어느 시점부터 여러분은 완고한 자세로 개발자와 그들이 들고 온 새로운 기능을 외면해야 합니다. 그 시점 이후로는 아무리 애원하고 구걸해도 이번 릴리스에 껴주지 않아야 합니다.

<img src="software_engineering_at_google/81.jpg" alt="" width="400"/>

> '늘 배포하라Always Be Deploying' 정책은 여러 측면에서 개발자 속도를 높여줍니다.

### CHAPTER 25 서비스형 컴퓨트
<img src="software_engineering_at_google/83.jpg" alt="" width="400"/>

> 이때 컴퓨트 인프라는 강력한 종속lock-in 요인임을 충분히 감안하여 선택해야 합니다.

<img src="software_engineering_at_google/84.jpg" alt="" width="400"/>

> 프레임워크의 핵심적 특징은 제어 반전 Inversion of control (IOC)