## Django Rest Framework

#### REST API란?

- REST API의 구성

  - 자원(Resource)    -    URI
  - 행위(Verb)    -    HTTP Method
  - 표현(Representations)
- REST API의 특징

  1. Uniform
     - Uniform Interface는 URI로 지정한 리소스에 대한 조작을 통일되고 한정적인 인터페이스로 수행하는 아키텍쳐 스타일을 말합니다
  2. Stateless
     - REST는 작업을 위한 상태정보를 따로 저장하고 관리하지 않는다.
     - 세션 정보나 쿠키정보를 병도로 저장하고 관리하지 않으며 들어오는 요청만을 단순히 처리한다.
  3. Self-descriptiveness(자체 표현 구조)
     - REST API 메시지만 보고도 쉽게 이해할 수 있는 자체 표현 구조로 되어있다.
  4. Client-server 구조
     - 서버는 API 제공, 클라이언트는 사용자 인증이나 컨텍스트 등을 직접 관리하는 구조로 각각 역할이 확실히 구분된다.
  5. Cacheable
     - HTTP 웹표준을 그대로 사용하므로 HTTP가 가진 캐싱 기능을 그대로 사용할 수 있다
  6. 계층형 구조
     - REST서버는 다중 계층으로 구성될 수 있으며 봥ㄴ, 로드 밸런싱, 암호화 계층을 추가해 구조상의 유연성을 둘 수 있다.
- HTTP Method


| Method | 역할                                                         |
| :----- | ------------------------------------------------------------ |
| POST   | POST를 통해 해당 URI를 요청하면 리소스를 생성                |
| GET    | GET을 통해 해당 리소스를 조회, 리소스를 조회하고 자세한 정보를 가져온다 |
| PUT    | PUT을 통해 해당 리소스를 수정                                |
| DELETE | DELETE를 통해 리소스를 삭제                                  |

​    



#### Django Rest Framework

- django를 백엔드로만 쓰려면 필요하다.
- DRF를 사용하면 프론트와 백엔드의 분리가 가능
  - 예시
    - backend - django 사용
    - frontend - React JS 사용
- DRF를 왜 쓰는가?    [django-rest-api의-필요성과-간단한-사용-방법]([https://medium.com/@whj2013123218/django-rest-api%EC%9D%98-%ED%95%84%EC%9A%94%EC%84%B1%EA%B3%BC-%EA%B0%84%EB%8B%A8%ED%95%9C-%EC%82%AC%EC%9A%A9-%EB%B0%A9%EB%B2%95-a95c6dd195fd](https://medium.com/@whj2013123218/django-rest-api의-필요성과-간단한-사용-방법-a95c6dd195fd))





## 200213 수업

### Django의  slash 처리

- APPEND_SLASH = True (settings)
  - slash가 안 붙은 url이 오면 붙인 주소로 리다이렉트하라고 요청을 보낸다.

trailling_slash



### assentication

- SessionAuthentication
  - 장고의 Authentication 방식
  - 헷갈리니 쓰지 않는걸 추천