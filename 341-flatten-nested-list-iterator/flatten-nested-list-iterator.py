class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = []
        for item in reversed(nestedList):
            self.stack.append(item)
    def next(self) -> int:
        return self.stack.pop().getInteger()
    def hasNext(self) -> bool:
        while self.stack:
            top = self.stack[-1]
            if top.isInteger():
                return True
            self.stack.pop()
            nested = top.getList()
            for item in reversed(nested):
                self.stack.append(item)
        return False