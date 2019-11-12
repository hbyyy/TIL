'''
순차검색(Sequential Search)

문자열과 키 문자 1개를 받는 함수 구현
while문을 이용, 문자열에서 키 문자가 존재하는 index위치를 검사 후 해당 index를 리턴
찾지 못했을 경우 -1을 리턴
선택정렬(Selection sort)

[9, 1, 6, 8, 4, 3, 2, 0, 5, 7] 를 정렬한다.

정렬과정

리스트 중 최소값을 검색
그 값을 맨 앞의 값과 교체
나머지 리스트에서 위의 과정을 반복
해결방법

알고리즘 진행과정 그려보기
의사코드(Psuedo code) 작성
실제 코드 작성

'''

# sequance search

def seq_search(str, skey):
    counter = 0
    while True:
        if counter == len(str):
            counter = -1
            break
        elif str[counter] == skey:
            break
        else:
            counter += 1

    return counter

result = seq_search('asdfg', 'g')
print(result)

# selection sort

