class Solution:
    def maxProbability(
        self,
        n: int,
        arestas: List[List[int]],
        probSucesso: List[float],
        noInicial: int,
        noFinal: int,
    ) -> float:
        grafo: List[List[Tuple[int, float]]] = [[] for _ in range(n)]
        for (a, b), p in zip(arestas, probSucesso):
            grafo[a].append((b, p))
            grafo[b].append((a, p))
        
        filaPrioridade = [(-1, noInicial)]
        distancias = [0] * n
        distancias[noInicial] = 1
        
        while filaPrioridade:
            prob, noAtual = heappop(filaPrioridade)
            prob = -prob
            if distancias[noAtual] > prob:
                continue
            for vizinho, p in grafo[noAtual]:
                if (novaProb := prob * p) > distancias[vizinho]:
                    distancias[vizinho] = novaProb
                    heappush(filaPrioridade, (-novaProb, vizinho))
        
        return distancias[noFinal]
