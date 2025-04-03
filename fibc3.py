"""
Exemplo de Fibonacci utilizando uma arquitrtura de algoritmo Top-down, com memorização.
"""



def fib(n):
    if n == 0 or n == 1:
        return n
    
    if memory[n] is not None:
        return memory[n]
    
    memory[n] = fib(n - 1) + fib(n - 2)
    return memory[n]

memory = [None] * 100000
for n in range(100000):
    print(fib(n), end = " ")