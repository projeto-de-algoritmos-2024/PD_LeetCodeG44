class Solution:
    def findCheapestPrice(
        self, n: int, voos: List[List[int]], origem: int, destino: int, paradas: int
    ) -> int:
        @cache
        def dfs(cidade, paradasRestantes):
            if cidade == destino:
                return 0
            if paradasRestantes <= 0:
                return float("inf")
            paradasRestantes -= 1
            melhorPreco = float("inf")
            for proxCidade, preco in grafo[cidade]:
                melhorPreco = min(melhorPreco, dfs(proxCidade, paradasRestantes) + preco)
            return melhorPreco

        grafo = defaultdict(list)
        for origemVoo, destinoVoo, preco in voos:
            grafo[origemVoo].append((destinoVoo, preco))
        
        melhorPreco = dfs(origem, paradas + 1)
        return -1 if melhorPreco >= float("inf") else melhorPreco
