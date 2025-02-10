class Solution:
    def jobScheduling(
        self, inicio: List[int], fim: List[int], lucro: List[int]
    ) -> int:
        @cache
        def dfs(i):
            if i >= n:
                return 0
            _, horarioFim, ganho = trabalhos[i]
            j = bisect_left(trabalhos, horarioFim, lo=i + 1, key=lambda x: x[0])
            return max(dfs(i + 1), ganho + dfs(j))

        trabalhos = sorted(zip(inicio, fim, lucro))
        n = len(lucro)
        return dfs(0)
