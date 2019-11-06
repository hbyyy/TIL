
for i in range(1, 100 +1):
    print(i)
    if i % 3 == 0:
        if i % 5 == 0:
            print('fizzbuzz')
        else:
            print('fizz')
    elif i % 5 == 0:
        print('buzz')
    
