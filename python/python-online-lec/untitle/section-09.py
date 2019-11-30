# 파일 읽기 쓰기
# 읽기 : r, 쓰기 : w, 추가 모드(파일 생성 또는 추가): a

f = open('./resource/review.txt', 'r')
content = f.read()
print(content)
f.close()

print('=========================================')
print('=========================================')
print('=========================================')
print('=========================================')

with open('./resource/review.txt', 'r') as f:
    c = f.read()
    print(c)

print('=========================================')
print('=========================================')


with open('./resource/review.txt', 'r') as f:
    for c in f:
        print(c.strip())

print('=========================================')
print('=========================================')

with open('./resource/review.txt', 'r') as f:
    content = f.read()
    print(">", content)
    content = f.read()
    print(">2", content)

print('=========================================')
print('=========================================')

with open('./resource/review.txt', 'r') as f:
    line = f.readline()
    while line:
        print(line, end='%%%')
        line = f.readline()

print('=========================================')
print('=========================================')

with open('./resource/review.txt', 'r') as f:
    contents = f.readlines()    # 리스트로 반환(공백문자 포함해서)
    for line in contents:
        print(line, end='*******')

print('=========================================')
print('=========================================')

score = []
with open('./resource/score.txt', 'r') as f:
    for line in f:
        score.append(int(line))
    print(score)

print('average: {:6.3}'.format(sum(score)/len(score)))

print('=========================================')
print('=========================================')

#파일 쓰기

with open('./resource/test1.txt', 'w') as f:
    f.write('niceman\n')

print('=========================================')
print('=========================================')

with open('./resource/test1.txt', 'a') as f:
    f.write('niceman\n')


print('=========================================')
print('=========================================')

from random import randint

with open('./resource/test2.txt', 'w') as f:
    for cnt in range(5):
        f.write(str(randint(0, 50)))
        f.write('\n')


print('=========================================')
print('=========================================')


with open('./resource/test2.txt', 'w') as f:
    list1 = ['Kim\n', 'park\n', 'heo\n']
    f.writelines(list1)             #리스트를 파일에 저장


print('=========================================')
print('=========================================')


with open('./resource/test2.txt', 'w') as f:
    print('Test contents 1!', file=f)


