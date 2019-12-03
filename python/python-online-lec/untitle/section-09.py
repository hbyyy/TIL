# # 파일 읽기 쓰기
# # 읽기 : r, 쓰기 : w, 추가 모드(파일 생성 또는 추가): a
#
# f = open('./resource/review.txt', 'r')
# content = f.read()
# print(content)
# f.close()
#
# print('=========================================')
# print('=========================================')
# print('=========================================')
# print('=========================================')
#
# with open('./resource/review.txt', 'r') as f:
#     c = f.read()
#     print(c)
#
# print('=========================================')
# print('=========================================')
#
#
# with open('./resource/review.txt', 'r') as f:
#     for c in f:
#         print(c.strip())
#
# print('=========================================')
# print('=========================================')
#
# with open('./resource/review.txt', 'r') as f:
#     content = f.read()
#     print(">", content)
#     content = f.read()
#     print(">2", content)
#
# print('=========================================')
# print('=========================================')
#
# with open('./resource/review.txt', 'r') as f:
#     line = f.readline()
#     while line:
#         print(line, end='%%%')
#         line = f.readline()
#
# print('=========================================')
# print('=========================================')
#
# with open('./resource/review.txt', 'r') as f:
#     contents = f.readlines()    # 리스트로 반환(공백문자 포함해서)
#     for line in contents:
#         print(line, end='*******')
#
# print('=========================================')
# print('=========================================')
#
# score = []
# with open('./resource/score.txt', 'r') as f:
#     for line in f:
#         score.append(int(line))
#     print(score)
#
# print('average: {:6.3}'.format(sum(score)/len(score)))
#
# print('=========================================')
# print('=========================================')
#
# #파일 쓰기
#
# with open('./resource/test1.txt', 'w') as f:
#     f.write('niceman\n')
#
# print('=========================================')
# print('=========================================')
#
# with open('./resource/test1.txt', 'a') as f:
#     f.write('niceman\n')
#
#
# print('=========================================')
# print('=========================================')
#
# from random import randint
#
# with open('./resource/test2.txt', 'w') as f:
#     for cnt in range(5):
#         f.write(str(randint(0, 50)))
#         f.write('\n')
#
#
# print('=========================================')
# print('=========================================')
#
#
# with open('./resource/test2.txt', 'w') as f:
#     list1 = ['Kim\n', 'park\n', 'heo\n']
#     f.writelines(list1)             #리스트를 파일에 저장
#
#
# print('=========================================')
# print('=========================================')
#
#
# with open('./resource/test2.txt', 'w') as f:
#     print('Test contents 1!', file=f)
#
#
#
# f = open('./resource/review.txt', 'r')
# content = f.read()
# print(content)
# print(dir(f))
# f.close()
#
#
# # with 문은 문이 끝나면 자동으로 close 해준다
# with open('./resource/review.txt', 'r') as f:
#     c = f.read()
#     print(c)
#     print(iter(c))
#
# print('==============================')
# print('==============================')
#
# # 한번에 읽어옴
# with open('./resource/review.txt', 'r') as f:
#     c = f.read()
#     print(c)
#     c = f.read()
#     print(c)
#
# print('==============================')
# print('==============================')
#
# with open('./resource/review.txt', 'r') as f:
#     c = f.readline()
#     print(c)
#     c = f.readline()
#     print(c)
#     while c:
#         print(c)
#         c = f.readline()
#
#
# print('==============================')
# print('==============================')
#
#
# with open('./resource/review.txt', 'r') as f:
#     c = f.readlines()
#     for line in c:
#         print(line)
#
# print('==============================')
# print('==============================')
#
#
# with open('./resource/score.txt', 'r') as f:
#     score = []
#     #f는 이터레이터, Next이용해 하나씩 뽑아 쓸 수 있다.
#     print(f)
#     for line in f:
#         score.append(int(line))
#     print(score)
#
#
# print('==============================')
# print('==============================')
#
#
# with open('./resource/test3.txt', 'w') as f:
#     f.write('niceman\n')
#
#
# print('==============================')
# print('==============================')
#
#
# with open('./resource/test3.txt', 'a') as f:
#     f.write('good man\n')
#
# print('==============================')
# print('==============================')
#
#
# print('==============================')
# print('==============================')
#
# with open('./resource/test3.txt', 'a') as f:
#     list = ['Kim\n', 'Park\n', 'Cho\n']
#     f.writelines(list)
#
#
# print('==============================')
# print('==============================')
#
# with open('./resource/test3.txt', 'a') as f:
#     print('Test content1', file=f, seq='', end='')
#     print('Test content2', file=f, seq='', end='')
#
#
#
# with open('./resource/test4.txt', 'a') as f:
#     f.write('Test content1')
#     f.write('Test content2')

lines = '''111111111111\
222222222222\
333333333333\
444444444444\
555555555555'''
print(lines)

fout = open('./resource/relativity', 'wt')
size = len(lines)
offset = 0
chunk = 10

while True:
    if offset > size:
        break
    print(fout.write(lines[offset:offset+chunk]))
    offset += chunk

fout.close()

# try:
#     fout = open('./resource/relativity', 'xt')
#     fout.write('adadadad')
# except FileExistsError:
#     raise FileExistsError('relativity file already exist!')


f = open('./resource/testtest2', 'wb')
bdata = bytes(range(256))
f.write(bdata)
print(len(bdata))
f.close()

f = open('./resource/testtest2', 'rb')
print(f.tell())
print(f.seek(255))
bdata = f.read()
print(len(bdata))
print(bdata[0])

