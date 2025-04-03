def fatorial(n: int) -> int:
    # caso base: Fatorial de 0 que é 1
    if n == 0:
        return 1

    # caso recursivo
    return n * fatorial(n-1)

print(fatorial(10))