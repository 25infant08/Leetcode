class Node:
    def __init__(self, count=0):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None


class AllOne:

    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.nodes = {}

    def _insert_after(self, node, new_node):
        new_node.prev = node
        new_node.next = node.next
        node.next.prev = new_node
        node.next = new_node

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def inc(self, key: str) -> None:
        if key not in self.nodes:
            if self.head.next == self.tail or self.head.next.count != 1:
                node = Node(1)
                self._insert_after(self.head, node)
            else:
                node = self.head.next

            node.keys.add(key)
            self.nodes[key] = node
            return

        node = self.nodes[key]
        new_count = node.count + 1

        if node.next == self.tail or node.next.count != new_count:
            new_node = Node(new_count)
            self._insert_after(node, new_node)
        else:
            new_node = node.next

        new_node.keys.add(key)
        node.keys.remove(key)
        self.nodes[key] = new_node

        if not node.keys:
            self._remove(node)

    def dec(self, key: str) -> None:
        node = self.nodes[key]

        if node.count == 1:
            node.keys.remove(key)
            del self.nodes[key]

            if not node.keys:
                self._remove(node)

            return

        new_count = node.count - 1

        if node.prev == self.head or node.prev.count != new_count:
            new_node = Node(new_count)
            self._insert_after(node.prev, new_node)
        else:
            new_node = node.prev

        new_node.keys.add(key)
        node.keys.remove(key)
        self.nodes[key] = new_node

        if not node.keys:
            self._remove(node)

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""

        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""

        return next(iter(self.head.next.keys))
