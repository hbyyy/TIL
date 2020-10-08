# YAML (.yml)

> **야믈** 이라고 읽는다!





## YAML 이란

- 사람이 쉽게 읽을 수 있는 데이터 직렬화 양식이다.

>현재는 주로 XML과 JSON이 데이터 직렬화에 사용되고, YAML 은 '가벼운 마크업 언어' 로 사용하려고 하고 있다.

- **리스트, 해쉬 데이터구조 직렬화** 에 강하다



## 문법

`#` :  주석

`---` : 문서의 **시작** (선택사항)

`...` : 문서의 **끝** (선택사항)



- 기본 표현은 `key : value` 로 표현, : 뒤에는 공백문자가 와야 한다.

```yaml
key : value
key:
    key_1:
    	key_2:
    		...
```



#### objects 표현

```yaml
key:
  key: value
  key: value
# or
key: {
  key: value
  key: value
}
```



#### list 표현

```yaml
key:
  - item
  - item
  
# or

key: [
  item, item
]
```



#### json과 yaml 비교



##### json

```json
{
    "basic_list": [
        "apple",
        "banana",
        "orange"
    ],
    "basic_list2": [
        "apple",
        "banana",
        "orange"
    ],
    ...
    
    "object_list": [
        {
            "name": "test1",
            "category": "test1"
        },
        {
            "name": "test2",
            "category": "test2"
        }
    ],
    "basic_objects": {
        "time": "11:11:11",
        "date": "2020-09011"
    }
}
```



##### yaml

```yaml
---
basic_list:
- apple
- banana
- orange

basic_list2: [
  apple,
  banana,
  orange
]

object_list:
- name: test1
  categoty: test1
- name: test2
  category: test2

basic_object:
  time: '11:11:11'
  date: '2020-09-11'
...
```

