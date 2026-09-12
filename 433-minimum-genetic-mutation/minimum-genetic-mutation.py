from typing import List
from collections import deque
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank = set(bank)
        queue = deque([(startGene, 0)])
        visited = {startGene}
        genes = "ACGT"
        while queue:
            gene, mutations = queue.popleft()
            if gene == endGene:
                return mutations
            for i in range(8):
                for char in genes:
                    next_gene = gene[:i] + char + gene[i + 1:]
                    if next_gene in bank and next_gene not in visited:
                        visited.add(next_gene)
                        queue.append((next_gene, mutations + 1))
        return -1