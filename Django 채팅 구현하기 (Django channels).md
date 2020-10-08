## Django 채팅 구현하기 (Django channels)



### Socket 

- Socket Protocol을 사용한다

Http와 다른 점

- 계속 유지된다



#### Django는 기본적으로 Socket을 쓰는 걸 지원하지 않는다

- Django-Channels 를 사용한다.



### Process

#### 개발 단계

HTTP -> runserver -> Django

Websocket -> runserver -> Channels -> Layer(Redis)



### Django Channels

#### Installation

``` shell
pip install channels
```



#### settings

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'channels',
]

ASGI_APPLICATION = 'config.routing.application'	# 필수!
```

- routing.py 추가해 줘야 한다

```
from channels.routing import ProtocolTypeRouter

application = ProtocolTypeRouter({


})
```









