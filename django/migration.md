## migration

`__init__.py`  파일이 없다면?



migration 커맨드 진행 시에 자동으로 진행하지 않는다.

`__init__.py` 파일을 만들거나, migration <app name> 으로 진행하면 된다.







- 장고 migration 은 DB에 무슨 값이 실제로 있는지는 고려하지 않는다.
  - 예시로, 필드를 하나 중간에 추가했을 때, 추가한 테이블에 기존 값이 하나도 없더라도 DB의 기존 값에 기본값을 설정하라고 강요한다.
  - 