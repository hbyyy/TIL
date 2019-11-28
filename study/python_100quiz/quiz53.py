# is_correct = 0
#
bracket_str1 = '(이것은 바른 문자열입니다)'
bracket_str2 = '(이것은 바르지 않은 문자열입니다()())'
#
# for i in list(bracket_str1):
#     if i == '(':
#         is_correct += 1
#     elif i == ')':
#         is_correct -= 1
#     else:
#         continue
#
# print('YES' if is_correct == 0 else "NO")
# 이렇게 풀었을 경우에는 ')(' 이런 문장이 와도 YES 라고 오답을 내게 된다.

temp_list = []
for i in list(bracket_str1):
    if


