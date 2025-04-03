class Vertex:
    def __init__(self, label: str, target_distance: int):
        self.label = label
        self.target_distance = target_distance
        self.adjacent = []
        self.visited = False

    def add_adjacent(self, adjacent):
        self.adjacent.append(adjacent)

    def list_adjacent(self):
        for adjacent in self.adjacent:
            print(f"{adjacent.vertex.label} - {adjacent.cost}")

class Adjacent:
    def __init__(self, vertex: Vertex, cost: int):
        self.vertex = vertex
        self.cost = cost

class Graph:
    porto_uniao = Vertex("Porto União", 203)
    paulo_frontin = Vertex("Paulo Frontin", 172)
    canoinhas = Vertex("Canoinhas", 141)
    tres_barras = Vertex("Três Barras", 131)
    sao_mateus_do_sul = Vertex("São Mateus do Sul", 123)
    irati =  Vertex("Irati", 139)
    curitiba = Vertex("Curitiba", 0)
    palmeira = Vertex("Palmeira", 59)
    mafra = Vertex("Mafra", 94)
    campo_largo = Vertex("Campo Largo", 27)
    balsa_nova = Vertex("Balsa Nova", 41)
    lapa = Vertex("Lapa", 74)
    tijucas_do_sul = Vertex("Tijucas do Sul", 56)
    araucaria = Vertex("Araucária", 23)
    sao_jose_dos_pinhas = Vertex("São José dos Pinhais", 13)
    contenda = Vertex("Contenda", 39)

    porto_uniao.add_adjacent(Adjacent(paulo_frontin, 46))
    porto_uniao.add_adjacent(Adjacent(sao_mateus_sul, 87))
    porto_uniao.add_adjacent(Adjacent(canoinha, 78))

    paulo_frontin.add_adjacent(Adjacent(irati, 75))
    paulo_frontin.add_adjacent(Adjacent(porto_uniao,46))

    irati.add_adjacent(Adjacent(palmeira, 75))
    irati.add_adjacent(Adjacent(sao_mateus_sul, 57))
    irati.add_adjacent(Adjacent(paulo_frontin, 75))

    sao_mateus_sul.add_adjacent(Adjacent(porto_uniao, 87))
    sao_mateus_sul.add_adjacent(Adjacent(irati,  57))
    sao_mateus_sul.add_adjacent(Adjacent(tres_barras, 43))
    sao_mateus_sul.add_adjacent(Adjacent(palmeira, 77))
    sao_mateus_sul.add_adjacent(Adjacent(lapa, 60))
    
    tres_barras.add_adjacent(Adjacent(canoinha, 12))
    tres_barras.add_adjacent(Adjacent(sao_mateus_sul, 43))

    canoinha.add_adjacent(Adjacent(porto_uniao, 78))
    canoinha.add_adjacent(Adjacent(tres_barras, 12))
    canoinha.add_adjacent(Adjacent(mafra, 66))

    mafra.add_adjacent(Adjacent(canoinha, 60))
    mafra.add_adjacent(Adjacent(lapa, 57))
    mafra.add_adjacent(Adjacent(tijucas_do_sul, 99))

    lapa.add_adjacent(Adjacent(mafra, 57))
    lapa.add_adjacent(Adjacent(sao_mateus_sul, 60))
    lapa.add_adjacent(Adjacent(contenda,26))

    contenda.add_adjacent(Adjacent(balsa_nova, 19))
    contenda.add_adjacent(Adjacent(araucaria, 18))
    contenda.add_adjacent(Adjacent(lapa, 26))

    araucaria.add_adjacent(Adjacent(contenda, 18))     
    araucaria.add_adjacent(Adjacent(curitiba, 37))

    palmeira.add_adjacent(Adjacent(irati, 75))
    palmeira.add_adjacent(Adjacent(campo_largo, 55))
    palmeira.add_adjacent(Adjacent(sao_mateus_sul, 77))

    tijucas_do_sul.add_adjacent(Adjacent(mafra, 99))
    tijucas_do_sul.add_adjacent(Adjacent(sao_jose_dos_pinhais, 49))
    
    campo_largo.add_adjacent(Adjacent(palmeira, 55))
    campo_largo.add_adjacent(Adjacent(curitiba, 29))
    campo_largo.add_adjacent(Adjacent(balsa_nova,22))

    sao_jose_dos_pinhais.add_adjacent(Adjacent(tijucas_do_sul, 49))
    sao_jose_dos_pinhais.add_adjacent(Adjacent(curitiba, 15))
