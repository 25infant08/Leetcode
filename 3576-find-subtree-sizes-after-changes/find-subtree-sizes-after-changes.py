class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n=len(parent)
        children=[[] for _ in range(n)]
        for i in range(1,n):
            children[parent[i]].append(i)
        last=[-1]*26
        new_parent=[-1]*n
        def dfs(u):
            c=ord(s[u])-97
            old=last[c]
            if old!=-1:
                new_parent[u]=old
            else:
                new_parent[u]=parent[u]
            last[c]=u
            for v in children[u]:
                dfs(v)
            last[c]=old
        dfs(0)
        tree=[[] for _ in range(n)]
        for i in range(1,n):
            tree[new_parent[i]].append(i)
        ans=[1]*n
        def calc(u):
            for v in tree[u]:
                ans[u]+=calc(v)
            return ans[u]
        calc(0)
        return ans