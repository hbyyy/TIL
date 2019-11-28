str1 = 'asdaasdadad'
lasd = str1.split('a')
print(lasd)

for idx, item in enumerate(lasd[:]):
    if lasd[idx] == '':
        del lasd[idx]


print(lasd)
