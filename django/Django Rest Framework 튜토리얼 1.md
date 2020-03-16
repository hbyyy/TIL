# Django Rest Framework Tutorial (1)



> Django 는 REST API 를 만들 수 있는 **Django REST Framework(DRF)** 가 존재한다. Django는 기본적으로 풀스택 프레임워크로 동작하지만, **DRF**를 사용한다면 클라이언트와 분리된 완전한 백엔드 프레임워크로 동작하게 만들 수 있다.  
>
> Django는 백엔드에서 실제로 HTML 코드를 만들어 클라이언트에 전달해주는 동작으로 서비스를 구현한다. 하지만, DRF는 직렬화한 데이터(주로 JSON 형식이 많이 쓰인다) 를 클라이언트에 보내주는 역할을 한다.
>
> 이 포스트에서는 [Django REST Framework tutorial](https://www.django-rest-framework.org/tutorial/1-serialization/) 을 따라가며 한글로 번역하고, 기본적인 DRF의 사용법을 정리할 것이다.



들어가기에 앞서, 이 튜토리얼은 간단한 코드 하이라이팅 웹 API를 구현하는 식으로 진행된다.



## 프로젝트 설정



프로젝트를 만들기 전에, 먼저 가상환경을 설정해준다. 

`pyenv` 를 이용한 설정

```shell
pyenv virtualenv 3.7.5 drf-tutorial-env
pyenv local drf-tutorial-env
```

다음으로, 필요한 패키지들을 설치해 준다.

```shell
pip install django
pip install djangorestframework
pip install pygments			# 코드 하이라이팅을 위한 패키지
```



필요한 패키지 설치 후, Django Project를 생성하고, app을 만들어 준다. 

```shell
django-admin startproject tutorial	# 프로젝트 생성
cd tutorial
./manage.py startapp snippets		# app 생성
```



**`tutorial/settings.py`**

```python
INSTALLED_APPS = [
    'rest_framework',
    'snippets.apps.SnippetsConfig',
    ...,
    ...,
]
```



### Snippet 모델 구현

Snippet 모델에는 created, title, code, linenos, language, style 6가지 필드가 존재한다.

튜토리얼에서는 코드 하이라이팅 기능을 구현하기 위해 pygments 패키지를 사용한다.

**`snippets/models.py`**

```python
from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

# pygments에서 지원하는 모든 언어 정보를 가져온다.
LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
# pygments에서 지원하는 모든 코드 스타일들을 가져온다.
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ['created']
```

모델 구현 후에는 *makemigrations*, *migrate* 를 진행해 주자.



### Serializer 구현

**serializer** 는 DRF의 핵심이다. serializer는 파이썬 클래스 인스턴스 형식의 데이터(snippet)를 직렬화하여 JSON 같은 데이터 형식으로 표현해 주거나, 반대로 JSON 같은 데이터 형식의 데이터를 파이썬 클래스 인스턴스 형식의 데이터로 역 직렬화 해주는 역할을 한다.

  **serializer**  의 구현은  django form과 비슷한 면이 있다. 다음의 코드를 보자

- serializer.py 파일을 만들어 준다.

**`snippets/serializer.py`**

```python
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(required=True, style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    def create(self, validated_data):
        """
        validation을 통과한 validated_data로 새로운 snippet instance 를 생성힌디.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        validation을 통과한 validated_data로 이미 존재하는 snippet instance를 변경한다.
        변경을 요청하지 않은 데이터는 기존 instance의 데이터를 넣는다.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance

```

첫번째로, 직렬화와 역 직렬화를 하는 필드들을 정의해준다. 필드들은 form과 같이 필드를 정의할 때 **default**, **read_only** 등등의 **validation flag**를 포함해 선언한다.

**style** flag 는 django form의 widget처럼 HTML로 렌더링 하는 방법을 설정해 줄 수 있다.  

필드들의 자세한 정보는 [여기](https://www.django-rest-framework.org/api-guide/fields/)를 참조하자. 

다음으로, **`create()`**, **`update()`** 메소드는 **`serializer.save()`** 를 실행할 때 동작할 코드들을 정의해 주는 것이다.



### Serialization, Deserialization 테스트

이제 지금까지 구현한 Snippet model과  Serializer를 이용하여 직렬화, 역 직렬화를 테스트 해보자.

1. Serialization

```python
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


snippet = Snippet.objects.create(code='foo = "bar"\n')                   snippet = Snippet.objects.create(code='print("Hello world!")\n')

# serializer를 만들고 생성한 snippet instance를 넣어준다.
# serializer가 snippet instance를 python dictionary 형태로 변환해 준다.
serializer = SnippetSerializer(snippet)                                 
serializer.data                                                         # {'id': 3, 'title': '', 'code': 'print("Hello world!")\n', 'linenos': False, 'language': 'python', 'style': 'friendly'}

# python 데이터 형태를 JSON으로 변환
content = JSONRenderer().render(serializer.data)
content                                                                 # b'{"id":3,"title":"","code":"print(\\"Hello world!\\")\\n","linenos":false,"language":"python","style":"friendly"}'

```

2. Deserialization

```python
import io

# 데이터 스트림을 파이썬 기본 데이터 형으로 변환해 준다.
stream = io.BytesIO(content)
data = JSONParser().parse(stream)
data
# {'id': 3, 'title': '', 'code': 'print("Hello world!")\n', 'linenos': False, 'language': 'python', 'style': 'friendly'}

serializer = SnippetSerializer(data=data)
serializer.is_valid()
# True
serializer.validated_data
# OrderedDict([('title', ''),
             ('code', 'print("Hello world!")'),
             ('linenos', False),
             ('language', 'python'),
             ('style', 'friendly')])

# serializer 정의 시에 정의해 준 동작 실행 (create)
serializer.save()

```



- serializer에 queryset을 넣어 줄 수도 있다. 이 경우 `many=True` 옵션을 지정해 주어야 한다.

```python
serializer = SnippetSerializer(Snippet.objects.all(), many=True)
```



### ModelSerializers 사용

Django의 ModelForm처럼, Serializer도 ModelSerializers를 사용할 수 있다 이것을 사용한다면 훨씬 간편하게 serializer를 만들 수 있다.

**`snippets/serializer.py`**

```python
class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']
```

간단하게 serializer 가 구현되었다. create()와 update()같은 메소드들은 기본적으로 구현이 되어 있다.



ModelSerializer의 구현 내용은 다음과 같이 확인할 수 있다.

```python
serializer = SnippetSerializer()                                         
print(repr(serializer))                                                        
# SnippetSerializer():
#    id = IntegerField(read_only=True)
#    title = CharField(allow_blank=True, max_length=100, required=False)
#    code = CharField(required=True, style={'base_template': 'textarea.html'})
#    linenos = BooleanField(required=False)
#    language = ChoiceField(choices=[
#    .....
```







**`serializer.save()`** method를 잠깐 확인해 보자.

**`BaseSerializer`**

```python
....
def save(self. **kwargs):
	...
	    if self.instance is not None:
            self.instance = self.update(self.instance, validated_data)
            assert self.instance is not None, (
                '`update()` did not return an object instance.'
            )
        else:
            self.instance = self.create(validated_data)
            assert self.instance is not None, (
                '`create()` did not return an object instance.'
            )

        return self.instance
```

