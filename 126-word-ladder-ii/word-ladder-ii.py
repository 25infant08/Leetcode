class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList = set(wordList) 
        result = []
        layer = set()
        layer.add(beginWord) 
        parent = defaultdict(set)
        while layer:
            new_layer = set()
            for word in layer:
                for i in range(len(beginWord)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        new = word[:i] + c + word[i + 1:]
                        if new in wordList and new != word:
                            parent[new].add(word)
                            new_layer.add(new)
            wordList -= new_layer
            layer = new_layer
        def build_path(last, lst):
            if last == beginWord:
                result.append(list(reversed(lst)))
                return
            for word in parent[last]:
                build_path(word, lst + [word])
        build_path(endWord, [endWord])
        return result