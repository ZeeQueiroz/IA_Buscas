DISTANCIA = 0
PREDECESSOR = 1
INFINITO = float("inf")

mapa = {
    "A": {"B": 4, "C": 3},
    "B": {"A": 4, "C": 5, "D":2},
    "C": {"A": 3, "B": 5, "D": 1, "E":3},
    "D": {"B": 2, "C": 1, "E": 3},
    "E": {"C": 3, "D": 4}
}

tabela = {
    "A": [0, None],
    "B": [INFINITO, None],
    "C": [INFINITO, None],
    "D": [INFINITO, None],
    "E": [INFINITO, None],
}

def pega_distancia_mais_curta(tabela: dict, vertex: str) -> int:
    return tabela[vertex][DISTANCIA]

def define_distancia_mais_curta(tabela: dict, vertex: str, distancia: int):
    tabela[vertex][DISTANCIA] = distancia

def define_predecessor(table: dict, vertex: str, predecessor: str):
    tabela[vertex][PREDECESSOR] = predecessor

def pega_distancia(mapa: dict, primeiro_vertex: str, segundo_vertex: str):
    return mapa[primeiro_vertex][segundo_vertex]

def pega_proximo_vertex(tabela: dict, vistado: list):
    nao_visitado = list(
        set(
            tabela.keys()
        ).difference(vistado)
    )

    min_vertex = nao_visitado[0]
    min_distancia = tabela[nao_visitado[0]][DISTANCIA]

    for vertex in nao_visitado:
        if tabela[vertex][DISTANCIA] < min_distancia:
            min_vertex = vertex
            min_distancia = tabela[vertex][DISTANCIA]

    return min_vertex

def acha_caminho_mais_curto(mapa: dict, tabela: dict, origem: str = "A"):
    visitado = []
    atual = origem
    comeco = origem

    while True:
        adjacente_vertex = mapa[atual]

        if set(adjacente_vertex).issubset(set(visitado)):
            ...
        else:
            nao_visitado = set(adjacente_vertex).difference(set(visitado))

            for vertex in nao_visitado:
                distancia_do_comeco = pega_distancia_mais_curta(tabela, vertex)

                if distancia_do_comeco == INFINITO and atual == comeco:
                    distancia_total = pega_distancia(mapa, vertex, atual)
                else:
                    distancia_total = pega_distancia_mais_curta(tabela, atual)
                    distancia_total += pega_distancia(mapa, atual, vertex)

                if distancia_total < distancia_do_comeco:
                    define_distancia_mais_curta(tabela, vertex, distancia_total)
                    define_predecessor(tabela, vertex, atual)
                
        visitado.append(atual)

        if len(visitado) == len(tabela.keys()):
            break

        atual = pega_proximo_vertex(tabela, visitado)

    return tabela

resultado = acha_caminho_mais_curto(mapa, tabela)
print(resultado)