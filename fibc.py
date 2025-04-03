"""
Exemplo Fibonacci Interativo.
"""


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b

    return a


#print(f"F(4) = {fib(4)}")
#print(f"F(5) = {fib(5)}")
#print(f"F(6) = {fib(6)}")
print(f"F(6) = {fib(10000)}")
