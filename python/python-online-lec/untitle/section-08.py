from pkg.fibonacci import Fibonacci

Fibonacci.fib1(10)

print('ex2: ', Fibonacci.fib2(400))
print('ex2: ', Fibonacci().title)


from pkg.fibonacci import Fibonacci as fb


print('ex3: ', fb.fib1(400))



import pkg.cal as c

print('ex4:', c.add(2,4))

from pkg.cal import mul as m

print('ex5 : ', m(100,3))

import pkg.prints as p


p.prt1()
p.prr2()

