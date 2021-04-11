def dijkstra(grafo, src, dest):
    men_dist = {}
    antecessor = {}
    nao_visitado = grafo
    infinito = float("inf")
    caminho = []
    for node in nao_visitado:
        men_dist[node] = infinito
    men_dist[src] = 0

    while nao_visitado:
        minNode = None
        for node in nao_visitado:
            if minNode is None:
                minNode = node
            elif men_dist[node] < men_dist[minNode]:
                minNode = node

        for filho, peso in grafo[minNode].items():
            if peso + men_dist[minNode] < men_dist[filho]:
                men_dist[filho] = peso + men_dist[minNode]
                antecessor[filho] = minNode
        nao_visitado.pop(minNode)

    atual = dest
    while atual != src:
        try:
            caminho.insert(0, atual)
            atual = antecessor[atual]
        except KeyError:
            print(str(dest) + " não é alcançavel por " + str(src))
            break
    caminho.insert(0, src)
    if men_dist[dest] != infinito:
        print("O menor caminho é: ", end="")
        print(*caminho, sep=" ")
