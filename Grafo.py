class Grafo:
    def __init__(self, grafo):
        self.grafo = grafo

    def remover_ares(self, vert1, vert2):
        try:
            del self.grafo[vert1][vert2]
            del self.grafo[vert2][vert1]
            return "Falha informada."
        except KeyError:
            return "Conexão não existe."

    def dijkstra(self, src, dest):
        men_dist = {}
        antecessor = {}
        nao_visitado = self.grafo
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
            for filho, peso in self.grafo[minNode].items():
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
                return str(src) + " nao é conectavel com " + str(dest)
        caminho.insert(0, src)
        if men_dist[dest] != infinito:
            vazia = ""
            for l in range(len(caminho)):
                vazia += str(caminho[l]) + " "
            return vazia
