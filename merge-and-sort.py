"""
Exemplo da Estratégia de Divisão e Conquista.
"""


def merge_sort(elementos: list) -> list:
    """
    Função que recebe uma lista não ordenada, então usando o 
    conceito de "divisão e conquitsa" fará a divisão da lista
    em sublistas, até que reste somente 1 elemento na lista. 
    Ao mesmo tempo fica responsável por invoncar a função merge,
    que irá juntar os elementos de forma ordenada.
    """
    # caso base - uma lista com um elemento
    if len(elementos) == 1:
        return elementos
    
    # encontrar o meio da lista (divisão inteira)
    mid = len(elementos) // 2

    # dividir a lista
    first = elementos[:mid]
    second = elementos[mid:]

    # caso recursivo - chamar a função até atingir caso base
    first_half = merge_sort(first)
    second_half = merge_sort(second)

    # ordenar e retornar a lista
    return merge(first_half, second_half)
    

def merge(first: list, second: list):
    """
    Função que junta as listas de forma ordenada
    """
    index1 = index2 = 0
    elementos = []

    #TODO: caso1 - ter elementos nas 2 listas 
    while index1 < len(first) and index2 < len(second):
        if first[index1] < second[index2]:
            elementos.append(first[index1])
            index1 += 1
        else:
            elementos.append(second[index2])
            index2 += 1

    #TODO: caso2 - haver elementos em uma das listas
    while index1 < len(first):
        elementos.append(first[index1])
        index1 += 1    

    while index1 < len(second):
        elementos.append(second[index2])
        index2 += 1    

    return elementos

elementos = [10,1,20,3,5,2,18,0]
print(merge_sort(elementos))