from typing import List
from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        if endWord not in words:
            return 0
        queue = deque([(beginWord, 1)])
        visited = {beginWord}
        while queue:
            word, steps = queue.popleft()
            if word == endWord:
                return steps
            for i in range(len(word)):
                for char in "abcdefghijklmnopqrstuvwxyz":
                    next_word = word[:i] + char + word[i + 1:]
                    if next_word in words and next_word not in visited:
                        visited.add(next_word)
                        queue.append((next_word, steps + 1))
        return 0