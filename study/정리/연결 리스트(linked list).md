### 연결 리스트(linked list)

#### 연결 리스트란?

- 각 노드가 데이터와 포인터를 가지고 한 줄로 연결되어 있는 방식이다.

![연결 리스트에 대한 이미지 검색결과](https://miro.medium.com/max/1332/1*JG-58S8EMxVXrk7cKAaK8w.png)

- 노드 : 데이터와 포인터가 들어있는 데이터 구조

- 포인터 :  다음 노드의 주소값을 가지고 있다 (다음 노드를 가리키로 있다)
  - 파이썬에서는 객체를 가리키고 있는 변수라고 생각하면 된다.

- head : 시작 노드
  - 따로 지정해주어야 한다. 지정해주지 않으면 어디가 시작인지 알 수 없다.
- tail : 마지막 노드
  - 포인터는 아무것도 가리키고 있지 않는다. 

#### 연결 리스트의 추가, 삭제

![연결 리스트 추가에 대한 이미지 검색결과](https://dojang.io/pluginfile.php/710/mod_page/content/21/unit74-5.png)



- 어느 지점이든 바로 노드를 추가하거나 삭제할 수 있다. 

#### 연결 리스트의 검색

![연결 리스트에 대한 이미지 검색결과](https://miro.medium.com/max/1332/1*JG-58S8EMxVXrk7cKAaK8w.png)

- 연결 리스트는 배열처럼 특정 인덱스에 바로 접근이 불가능하다. 위의 그림에서 T를 찾아가려면 head 노드부터 순차적으로 탐색해야 한다.



#### 연결 리스트의 종류

1.  이중 연결 리스트

   ![](https://s3.ap-northeast-2.amazonaws.com/opentutorials-user-file/module/1335/2949.png)

이중 연결 리스트는 양쪽으로 모두 연결되어 있는 연결 리스트이다.

- 장점
  - 데이터를 가져와야 할 때 양쪽 끝에서부터 접근이 가능하므로 탐색해야하는 노드가 반으로 줄어든다.
  - 단일 연결 리스트와 달리 앞뒤로 이동하며 탐색이 가능하다.
- 단점
  - 포인터가 하나 더 늘어 노드의 크기가 더 커진다.
  - 구현이 조금 더 복잡해진다.

2. 원형 연결 리스트

   ![원형 연결 리스트에 대한 이미지 검색결과](http://mblogthumb1.phinf.naver.net/20150628_268/posnopi13_1435483108794UMBOe_PNG/%C4%B8%C3%B3.PNG?type=w420)

원형 연결 리스트는 마지막 노드가 head를 가리키는 계속 순환할 수 있는 연결 리스트이다.

## 참조

이미지 1 : (https://medium.com/wasd/c-c-%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%EC%97%B0%EA%B2%B0-%EB%A6%AC%EC%8A%A4%ED%8A%B8-1-41a312399a8f)



이미지 2 : (https://dojang.io/mod/page/view.php?id=6460)



(https://opentutorials.org/module/1335/8940)