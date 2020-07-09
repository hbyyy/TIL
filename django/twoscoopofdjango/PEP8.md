# 코딩 스타일

## 임포트시 지켜야할 규칙

- 임포트를 할 때는 다음과 같은 규칙을 따른다
  1. 표준 라이브러리
  2. 연관 외부 라이브러리
  3. 로컬 애플리케이션, 라이브러리에 한정된 임포트



예시로, 장고 프로젝트에서는 다음과 같이 임포트한다.

```python
# 표준 라이브러리
import os
from math import sqrt
# 코어 장고 임포트
from django.db import models
...
# 서드파티앱 임포트
from django_extentions.db.models import TimeStampedModel
# 프로젝트앱 임포트,
from .model import User
```



- 명시적 성격의 상대 임포트 이용

 프로젝트 앱을 임포트 해야할 때, 상대경로로 임포트 하는것이 좋다.

- 만약 앱을 재사용해야 할 때, 앱의 이름을 바꿔야 한다면?
  - 하드 코딩된 임포트는 코드를 다 변경해야할 것이다!
  - 즉, 상대 경로로 쓰는게 **이식성과 재사용성**에서 더 좋다! 



- 장고 코딩 스타일 가이드

https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/#imports



