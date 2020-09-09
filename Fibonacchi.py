def get_fib(num):
    a = 0
    b = 1
    for i in range(num):
       yield a
       temp = a
       a = b
       b = temp+b

for item in get_fib(20):
    print(item)
