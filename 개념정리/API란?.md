# API 디자인 패턴

## API 란?

- Application Programming Interface
-  웹 API : JSON, GET, POST...



## REST

- 로이 필딩이 제시한 API 디자인 패턴

###  핵심

- URL 은 정보를 표현
- 정보에 대한 행위는 HTTP Method로 표현

- URL과 HTTP Method를 이용해 정보를 가져온다

한줄요약 : HTTP URL 를 통해 자원을 명시하고, HTTP Method 를 통해 해당 자원에 대한 CRUD Operation를 적용하는 것

## 다른 API 디자인 패턴

### SOAP

- 현재는 거의 쓰이지 않음
- HTTP, HTTPS, SMTP 등의 프로토콜을 통해 XML 기반의 메시지를 주고받는 형식

### GraphQL

- Facebook 에서 만든 디자인 패턴
- REST를 사용하면서 생긴 불편함
  - URL 이 너무 많아진다
  - 사용자(기기) 별로 필요한 정보가 조금씩 다르다
    - Over-fetching, Under-Fetching
      - Over-fetching : 하나의 데이터만 받고 싶은데 여러개를 받아서 써야 함
      - Under 는 반대
- GraphQL 은 하나 or 소수의 엔드포인트 사용
- 요청 데이터에 따라 달라지는 결과 응답

