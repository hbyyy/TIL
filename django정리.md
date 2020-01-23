## path()

### **`path(route, view, kwargs=None, name=None)`**

2개인 필수 인수인 **route**와 **view**가 존재

##### route

URL 패턴을 가진 문자열

장고는 urlpatterns 의 첫번째 요소부터 시작하여 일치하는 패턴을 찾을 때까지 요청된 URL을 리스트의 순서대로 비교한다.

패턴은 GET이나 POST 의 매개 변수들이나 도메인 이름은 검색하지 않는다

##### view

Django 에서 일치하는 패턴을 찾으면, **HttpRequest** 객체를 첫번째 인수로 하고, 경로로 부터 캡처된 값을 키워드 인수로하여 특정한 view 함수를 호출한다.

##### name

URL 에 이름을 지으면 어디에서나 명확하게 참조가 가능해진다.

##### kwargs

```python
urlpatterns = [
    path('blog/<int:year>/', views.year_archive, {'foo': 'bar'}),
]
```

이런 식으로 사용한다면 장고는,

```python
views.year_archive(request, year=2005, foo='bar')
```

을 호출할 것이다.





## admin



## field 

##### null과 blank의 차이



null=True라면, 값 자체가 없는 것이다.

blank=True이면 빈 값을 허용한다는 것이다. -> **값 자체는 존재!**





*  장고는 멀티 키로 기본키를 설ㅈㅇ할 수 없다



## 191218 수업

```python

class Manufacturer(models.Model):
    name = models.CharField('제조사명', max_length=20)

    def __str__(self):
        return self.name


class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    name = models.CharField('차량명', max_length=20)

    def __str__(self):
        return self.name
    
p.get_shirt_size_displlay()
```



**템플릿 네임스페이싱**

`polls/templates/polls`라고 만들 필요 없이, 그냥 `polls/templates`에 넣어도 되지 않을까하고 생각할지도 모르지만 이것은 별로 좋은 생각이 아닙니다. Django는 이름이 일치하는 첫번째 템플릿을 선택하는데, 만약 동일한 템플릿 이름이 다른 어플리케이션에 있을 경우 Django는 이 둘 간의 차이를 구분하지 못합니다. Django에게 정확한 템플릿을 지정하기 위해서 가장 편리한 방법은 *이름공간*으로 구분짓는 것인데, 어플리케이션의 이름으로 된 디렉토리에 이러한 템플릿들을 넣으면 됩니다.



## 200107

```python
In [1]: User                                                                                                                                                                    
Out[1]: members.models.User

In [2]: user = User(username='qwer')                                                                                                                                            

In [3]: user.set_password('1234')                                                                                                                                               

In [4]: user.save()                                                                                                                                                             
# 잘못된 사용, create_user를 사용해야 한다.
# create를 사용한다면 , password에 빈 값이 들어가서 실제 db에는 패스워드에 빈 값이 저장된다.
In [5]: user = User.objects.create(username='qwert')                                                                          
In [6]: user.set_password('1234')                                   
In [7]: user.save()                                                                                                                                                             
    
# create_user를 사용하면 password를 처음에 입력하지 않으면, set_unusable_password()가 자동으로 설정되는 것 같다. 실제 DB에는 해싱된 어떤 값이 저장된다.
In [8]: user = User.objects.create_user(username='asdf')             
In [9]: user.set_password('1234')                                   
In [10]: user.save()                                                                                                                                                            

In [11]: from django.contrib.auth.hashers import *                                                                                                                              

In [12]: passwd = make_password('1234')                                                                                                                                         

In [13]: passwd                                                                                                                                                                 
Out[13]: 'pbkdf2_sha256$150000$wjouaZlPkm9C$0HWV+SJ9RbPQbaKaXvmqHdSTTerHyQGeQ3LlSNCDuVE='

In [14]: user = User.objects.get(username='asd')                                    

In [15]: user.password                                                              
Out[15]: '1234'

In [16]: user.set_password(passwd)                                                  

In [17]: user.save()                                                                

In [18]: user.check_password('1234')                                                
Out[18]: False

In [19]: user.check_password(passwd)                                                
Out[19]: True

In [20]: check_password('1234',passwd)                                              
Out[20]: True

In [21]: user.password = 'pbkdf2_sha256$150000$wjouaZlPkm9C$0HWV+SJ9RbPQbaKaXvmqHdST
    ...: TerHyQGeQ3LlSNCDuVE='                                                      

In [22]: user.save()                                                                

In [23]: User.objects.get(username='1234')   
```



### 200107 수업_migration

- manage.py makemigrations <app>

  모델클래스의 변경사항을 migrations으로 생성

- manage.py migrate <app> 

  - migrations 변경사항을 실제로 db에 적용



- showmigrations
  - 마이그레이션 적용 현황을 보여줌



* DB에 django_migrations

  * 마이그레이션한 정보를 기록해 둔다.

  

#### 마이그레이션 파일을 지웠을 때



프로젝트에서 마이그레이션 파일을 삭제하고 showmigrations를 하면

마이그레이션이 없다고 나온다.

하지만 DB의 django_migrations에는 마이그레이션 정보가 그대로 저장되어 있다.

기록상에 문제가 생김 ( 없는 마이그레이션이 적용되었다고 DB에 기록이 되어있다.)

* 마이그레이션 파일을 지워야 한다면 꼭 마이그레이션 적용사항을 지우고 삭제해야 한다!

  ex)  migrate members zero -> 마이그레이션 initial 까지 모두 적용 취소

  

manage.py migrate <appname> 0001 -> 0001로 마이그레이션 되돌림



마이그레이션 파일 번호는 0001부터 하나씩 올라간다.

협업 중 같은 번호의 마이그레이션 파일이 생긴다면, 충돌이 생김

-> dependency를 수정하여 해결할 수 있음





수정해야 할 상황이 온다?

migration을 전 단계로(initial로 돌리는게 좋을 듯) 돌려놓고, 파일을 받아와서 마이그레이션을 수정한다. 이렇게 적용해야 오류를 피할 수 있다.



#### 같은 번호가 생긴다?

같은 번호가 있는 마이그레이션을 지우고

db 삭제하고

마이그레이션





실제 개발시 DB 사용?

운영 DB - Prodect		-> 주기적으로 백업 해놓음

개발 DB - Dev



개발자1 개발자2 개발자3

local1    local2    local3		( 운영  db의 백업을 가져옴)





## 200108 수업

#### Form class

- form tag와 button tag는 직접 만들어줘야 한다.
  - form action이 뭔지, method가 뭔지는 알수 없으므로 알아서 작성해야 한다.



* form에서 file을 보낼 때
  * `<form action="" method="post", enctype="multipart/form-data">` 
    * enctype을 꼭 추가해 주어야 한다
  * 보낸 파일은 request.FILES 에 있다.



- FileField > ImageFiled
  - FileField.url 이라는 속성이 존재한다.



#### form에서 이미지를 한번에 여러 개 올리게 하기

- ```python
  class PostCreateForm(forms.Form):
      image = forms.ImageField(widget=forms.ClearableFileInput(
          attrs={'multiple': True}))
  ```

- 

- QueryDict.getlist(key, default=None)
  - 해당하는 key를 가지고 있는 딕셔너리의 리스트를 가져온다.
  - 해당하는 key의 값이 없다면 빈 리스트를 반환(default값을 지정해주지 않았을 때)



- settings의 ALLOWED_HOSTS
  - ALLOWED_HOSTS = [허용할 ip 주소 ex) 'localhost', '학원ip', ]

- runserver 시 runserver 0.0.0.0:8000 으로 하면, 모든 들어오는 연결을 허용





* 외부에서 받은 데이터를 검증할 떄 장고에서는 보통 form 클래스 안에서 진행한다.





## 200109



#### form validation



1. `to_python()`
   - field의 내룡을 python에 맞게 바꾼다



* `Field.clean()`
  * field가 가진 메서드
    * to_python, validate, run_validate 수행
* `forms.clean()`
  *  clean()을 수행해 통과한 데이터들을 모아서 돌려줌
    * cleaned_data 로 모아서 돌려준다
    * 이것을 오버라이딩 해서 기능을 추가할 수 있다.

- clean() 실행 어떻게 되나?

  ```
  class LoginForm
  	username(CharField)
  		1. to_python
  		2. validate
  		3. run_validators()
  			통과시 return value1
  	password
  		...
  			통과시 return value2
  		
  	self.cleaned_data
  		'username': value1
  		'password': value2
  	
  	4. Form.clean()
      	하는일 없음(cleaned_date를 처음으로 사용할 수 있는 시점)
      5. 모든 필드명에 대해서
       (있다면) Form.clean_<필드명>을 실행
  		
  	
  ```

  

  * 기본적인 방법

```python
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            form.login(request)
            return redirect('posts:post_list')
        
    else:
        form = LoginForm()

    context = {
        'form': form,
    }

    return render(request, 'members/login.html', context)
```





* `form.non_field_error`
  * clean()에서 온 오류를 모아서 줌
* `form.field명.errors`
  * clean_field명 에서 발생한 오류를 모아서 줌





* 시프트 + 컨트롤 + F
  * 전체 코드에서 찾기





* form의 clean_<field>를 사용

```python
    def clean_email(self):
        email_check = User.objects.filter(email=self.cleaned_data['email']).exists()
        if email_check is True:
            raise forms.ValidationError('이미 존재하는 email입니다')
        else:
            return self.cleaned_data['email']

    def clean_username(self):
        username_check = User.objects.filter(username=self.cleaned_data['username']).exists()
        if username_check is True:
            raise forms.ValidationError('이미 존재하는 username입니다')
        else:
            return self.cleaned_data['username']

    def save(self):

        return User.objects.create_user(
            username=self.cleaned_data['username'],
            # username=self.cleaned_username(),
            password=self.cleaned_data['password'],
            name=self.cleaned_data['name'],
            email=self.cleaned_data['email']
            # email=self.clean_email()
        )
```

view에서 is_valid()가 실행되면,

실행 후 clean_<field명> 을 모두 실행, 그 후 clean()을 실행

clean_field는 에러를 발생시키거나, cleaned_data['해당필드']를 리턴해줘야 한다.

- clean_field를 실행한 후 cleaned_data['해당 필드']값을 덮어쓰기 떄문에 데이터가 바뀌지 않는다고 해도 리턴해줘야 한다.
- clean_field에서 에러가 발생하면 forms.errors에 `{필드명 : 에러내용}` 식으로 저장된다.
- clean()에서 발생한 오류는 field.non_field_errors()에 저장된다.
- clean() 함수도 오버라이딩 한다면, cleaned_data 자체를 리턴해 주어야 한다.
  - super().clean()을 실행한 후, 커스텀하는 방법이 있다.





## 200113

#### save() method

- forms.Modelform에 기본적으로 존재하는 method
  - Form에는 기본적으로 있지 않다



기본적인 save() 메소드는 현재 폼에 있는 데이터를 DB에 저장시킨다. save()는 키워드 인자 commit=True 를 가지고 있는데, False로 설정한다면 실제 DB에는 저장하지 않은 상태로 객체를 리턴해 준다.이 옵션을 이용해 DB에 실제로 저장하기 전에 처리를 해 줄 수 있다.



##### 주의사항

기본값은 create()를 해 준다. 기본 User 모델을 상속받아 사용할 때에는 create_user() 를 사용해야 하기 때문에, save() method를 오버라이딩 해 주어야 한다.



```python
In [1]: from members.form import *                                                                                                      
In [2]: from members.forms import *                                                                                                                                            
In [3]: form = SignupForm(data={ 
   ...: 'username': 'e', 
   ...: 'name': 'e', 
   ...: 'password': '1234' 
   ...: })                                                                                                                                                                      

In [4]: form.is_valid()                                                                                                                                                       
Out[4]: False

In [5]: form.errors                                                                                                                                                             
Out[5]: {'username': ['이미 존재하는 아이디입니다']}

In [6]: form.field                                                                                                                       
In [7]: form.fields                                                                                                                                                             
Out[7]: 
OrderedDict([('username', <django.forms.fields.CharField at 0x7f3b00e92290>),
             ('name', <django.forms.fields.CharField at 0x7f3b00e92c90>),
             ('password', <django.forms.fields.CharField at 0x7f3b00e92450>)])

                           

In [11]: for field in form: 
    ...:   print(field.errors) 
    ...:                                                                                                                                                                        
<ul class="errorlist"><li>이미 존재하는 아이디입니다</li></ul>


In [12]: print(form)                                                                                                                                                           
<tr><th><label for="id_username">Username:</label></th><td><ul class="errorlist"><li>이미 존재하는 아이디입니다</li></ul><input type="text" name="username" value="e" class="forlaceholder="아이디를 입력하세요" maxlength="150" required id="id_username"><br><span class="helptext">Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</sp/tr>
<tr><th><label for="id_name">Name:</label></th><td><input type="text" name="name" value="e" class="form-control" placeholder="닉네임을 입력하세요" maxlength="20" required id="i/td></tr>
<tr><th><label for="id_password">Password:</label></th><td><input type="password" name="password" class="form-control" placeholder="비밀번호를 입력하세요" maxlength="128" requi_password"></td></tr>

In [13]: for field in form: 
    ...:   print(field.errors) 
    ...:                                                                                                                                                                        
<ul class="errorlist"><li>이미 존재하는 아이디입니다</li></ul>



In [14]: for field in form: 
    ...:   for error in field.errors: 
    ...:       print(field.errors) 
    ...:                                                                                                                                                                        
<ul class="errorlist"><li>이미 존재하는 아이디입니다</li></ul>

In [15]: for field in form: 
    ...:   for error in field.errors: 
    ...:       print(error) 
    ...:        
    ...:                                                                                                                                                                        
이미 존재하는 아이디입니다

```



* form.errors

* for field in form

* for error in field.errors

  * 위 세가지의 출력 다르니 확인해보자

  

## 200115



#### OAuth (소셜 로그인)

- 작동 방식

1. 소셜로 로그인 요청
2. 서버가 소셜 주소로 리다이렉트
3. callback URL을 통해 collback token을 보내줌(Accessc token)
4. 이 토큰으로 소셜 서버에 요청을 하면 유니크한 id를 보내준다.
5. 이 유니크id 값으로 아이디를 만듬
6. 다음에 이 토큰으로 오는 요청이 있으면, 어떤 유저인지 알 수가 있다.
7. 





## 200116

#### 장고 커스텀 커맨드 만들기

https://docs.djangoproject.com/en/3.0/howto/custom-management-commands/#module-django.core.management

```python
class Command(BaseCommand):
    def handle(self, *args, **options):
        post_count = Post.objects.count()
        comment_count = PostComment.objects.count()
        tag_count = Tag.objects.count()

        self.stdout.write(f'post_count: {post_count}, comment_count: {comment_count}, tag_count: {tag_count}')
```

- 인자가 없으면 handle만 저으이해 줌으로 간단하게 만들 수 있다.

```
myapp/
    __init__.py
    models.py
    management/
        commands/
            _private.py		# ./manage.py 했을 때 명령어가 안 뜨게 함
            commandname.py	# ./manage.py <py파일 이름(커맨드명)> <인자>
    tests.py
    views.py
```

- 위의 구조를 꼭 지켜서 만들어 줘야 한다.





#### cron

어떤 작업을 주기적으로 실행해야 할 떄 사용한다

- 가상환경에서 돌아갈 수 있도록 실행명령을 절대경로로 잘 알려줘야 한다.

ex)

```shell
~/.pyenv/versions/wps-instagram-env/bin/python #프로젝트에서 사용하고 있는 가상환경의 파이썬 ~/projects/wps12th/python/instagram/app/manage.py	#
```



- cron은 출력 결과를 따로 보여주지는 않는다 (백단에서 돌아가므로)
  - 출력 결과를 텍스트로 저장해서 출력하는 식으로 해야한다

- crontap -e 로 설정할 수 있음





#### 네이버 로그인

ClientId: 			공개값

​	네이버 로그인 버튼

`<a herf="....client_id=<ClientID>"/>`

ClientSecret:	비공개값

​	token + secret -> access_token







#### requests 모듈 사용법

- response = requests.get(url, **kwargs)
  - headers=<커스텀 헤더>	-> 커스텀 헤더를 추가할 수 있다.
- response.text : response 값(string)
- response.status_code : 





## 200119

#### url encoding

한글 사이트인 경우(예시: yes24) 한글로 검색을 한다면, 

```
# 파이썬 검색 시
http://www.yes24.com/searchcorner/Search?keywordAd=&keyword=&domain=ALL&qdomain=%C0%FC%C3%BC&query=%C6%C4%C0%CC%BD%E3

%C6%C4%C0%CC%BD%E3 = 파이썬
```

이런 식으로 인코딩해서 검색을 한다



이유로는, url에는 아스키 코드만 가능하다. 그러므로 한글은 