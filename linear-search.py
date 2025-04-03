"""
Busca Linear Simples, sem ordenação
"""

def search(input_list: list, elemento: int) -> int:
    for index, value in enumerate(input_list):
        if value == elemento:
            return index

input_list = [3,1,4,6,12]
index = search(input_list, 3)
print(index)