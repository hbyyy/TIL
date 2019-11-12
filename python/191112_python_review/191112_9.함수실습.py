# 1. 매개변수로 문자열을 받고, 해당 문자열이 red면 apple을, yellow면 banana를, green이면 melon을, 어떤 경우도 아닐 경우 I don't know를 리턴하는 함수를 정의하고, 사용하여 result변수에 결과를 할당하고 print해본다.

def fruit(color):
    'print fruits'
    return (lambda color:"apple" if color == 'red' else "banana" if color == 'yellow' else 'melon' if color == 'green' else "I don't know")(color)


inputcolor = 'yellow'
result = fruit(inputcolor)
print(result)


# 2. 번에서 작성한 함수에 docstring을 작성하여 함수에 대한 설명을 달아보고, help(함수명)으로 해당 설명을 출력해본다

help(fruit)

# 3. 한 개 또는 두 개의 숫자 인자를 전달받아, 하나가 오면 제곱, 두개를 받으면 두 수의 곱을 반환해주는 함수를 정의하고 사용해본다.

def cal(a, b = 0):
    if b == 0:
        return a * a
    else:
        return a * b

result = cal(2)
print(result)
result = cal(2,5)
print(result)

# 4. 두 개의 숫자를 인자로 받아 합과 차를 튜플을 이용해 동시에 반환하는 함수를 정의하고 사용해본다.

def q4(x, y):
    return (x+y, x-y)

re1 = q4(6,7)
print(re1)


# 5. 위치인자 묶음을 매개변수로 가지며, 위치인자가 몇 개 전달되었는지를 print하고 개수를 리턴해주는 함수를 정의하고 사용해본다.

def print_argsnum(*args):
    numOfargs = len(args)
    print(f'number of positional args : {numOfargs} ')
    return numOfargs

re2 = print_argsnum(2, 3, 5 ,'qasd')
print(re2)

# 6 람다함수와 리스트 컴프리헨션을 사용해 한 줄로 구구단의 결과를 갖는 리스트를 생성해본다.




gugu_list1 = [f'{x}x{y} = {x*y}' for x in range(2, 10) for y in range(1, 10) ]

# gugu_list2 = (lambda x :f'{x, y} = {x*y}')
print(gugu_list)
