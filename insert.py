def insert(vertice, path):
    grafo = {x: {} for x in range(1, vertice + 1)}
    with open(path, "r") as file:
        for y in file.readlines():
            vert1, vert2, peso = y.split()
            grafo[int(vert1)][int(vert2)] = int(peso)
    return grafo