import datetime


d = datetime.datetime.strptime('2020-1-1', '%Y-%m-%d')

c = datetime.datetime(2018, 5, 5)


q = d - c

e = datetime.datetime(2011, 2, 2)
f = datetime.datetime(2012, 2, 2)
print(type(e.day))
print((f-e).days)
print(type(e))
print(type(f))
print(type(f-e))
print(q)
print(type(q))
print(q.days)
print((f-e).days)

x = 3 if False else 2
print(x)

y = dict()
for q, w in zip([1,2,3],[4,5,6]):
    y[q] = w

print(y)
u = {q: y for q, y in zip([1, 2, 3], [4, 5, 6])}
print(u)
z = [*iter(u.items())]
print(z)
list1 = [1,2,3,4,5]
print(type(list1))
print(type(iter(list1)))
iter()