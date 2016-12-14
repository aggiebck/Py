n = 10

def foo(x):
    n = 3 + x
    x = n * 2
    return n, x

def bar(m):
    n = 4 + m
    a,b = foo(n)
    return a + 1, b * 10

b, a = bar(10)
print(a)
print(b)