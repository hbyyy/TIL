## datetime

#### time module

```python
import time
```



- time모듈은 시간을 다루는 모듈이다
  - 프로그램의 실행 시간을 계산할 때 유용하게 사용한다.



```
time.time()
```

- 1970년 1월 1일 00시부터 현재까지 지난 시간을 초 단위로 보여준다.
  - UTC 표준 시를 지킨다
  - 이 시간을 **POSIX** 시간, **Epoch** 시간 이라고 한다. 



```python
time.gmtime([sec])
time.localtime([sec])

t1 = time.gmtime(10000)
t2 = time.localtime(10000)

time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=2, tm_min=46, tm_sec=40, tm_wday=3, tm_yday=1, tm_isdst=0)
time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=11, tm_min=46, tm_sec=40, tm_wday=3, tm_yday=1, tm_isdst=0)
```



- gmtime과 localtime 함수는 받은 인수(에포치 시간)를 struct_time 형태로 만들어 반환해 준다. 
  - gmtime() 은 UTC 표준시로 반환
  - localtime()은 사용자 현재 위치의 표준시로 반환
- 인수를 주지 않으면 현재 시간을 반환해준다

```python
time.strftime('포멧', [struct_time])
```

- 시간을 포멧에 맞게 출력해 준다.
- 2 번째 인자가 없으면 현재 시간을 포멧에 맞춰 반환해준다

| 코드 | 설명                                      | 예                                |
| ---- | :---------------------------------------- | --------------------------------- |
| %a   | 요일 줄임말                               | Sun, Mon, ... Sat                 |
| %A   | 요일                                      | Sunday, Monday, ..., Saturday     |
| %w   | 요일을 숫자로 표시, 월요일~일요일, 0~6    | 0, 1, ..., 6                      |
| %d   | 일                                        | 01, 02, ..., 31                   |
| %b   | 월 줄임말                                 | Jan, Feb, ..., Dec                |
| %B   | 월                                        | January, February, …, December    |
| %m   | 숫자 월                                   | 01, 02, ..., 12                   |
| %y   | 두 자릿수 연도                            | 01, 02, ..., 99                   |
| %Y   | 네 자릿수 연도                            | 0001, 0002, ..., 2017, 2018, 9999 |
| %H   | 시간(24시간)                              | 00, 01, ..., 23                   |
| %I   | 시간(12시간)                              | 01, 02, ..., 12                   |
| %p   | AM, PM                                    | AM, PM                            |
| %M   | 분                                        | 00, 01, ..., 59                   |
| %S   | 초                                        | 00, 01, ..., 59                   |
| %Z   | 시간대                                    | 대한민국 표준시                   |
| %j   | 1월 1일부터 경과한 일수                   | 001, 002, ..., 366                |
| %U   | 1년중 주차, 월요일이 한 주의 시작으로     | 00, 01, ..., 53                   |
| %W   | 1년중 주차, 월요일이 한 주의 시작으로     | 00, 01, ..., 53                   |
| %c   | 날짜, 요일, 시간을 출력, 현재 시간대 기준 | Sat May 19 11:14:27 2018          |
| %x   | 날짜를 출력, 현재 시간대 기준             | 05/19/18                          |
| %X   | 시간을 출력, 현재 시간대 기준             | '11:44:22                         |

