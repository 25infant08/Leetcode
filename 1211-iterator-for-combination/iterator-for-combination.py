class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        self.characters = characters
        self.k = combinationLength
        self.n = len(characters)
        self.indices = list(range(self.k))
        self.finished = False
    def next(self) -> str:
        result = ''.join(
            self.characters[i] for i in self.indices
        )
        i = self.k - 1
        while i >= 0 and self.indices[i] == self.n - self.k + i:
            i -= 1
        if i < 0:
            self.finished = True
        else:
            self.indices[i] += 1
            for j in range(i + 1, self.k):
                self.indices[j] = self.indices[j - 1] + 1
        return result
    def hasNext(self) -> bool:
        return not self.finished