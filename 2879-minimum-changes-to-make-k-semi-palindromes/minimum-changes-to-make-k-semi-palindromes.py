class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n=len(s)
        cost=[[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(i+2,n+1):
                m=j-i
                best=float('inf')
                for d in range(1,m):
                    if m%d==0:
                        c=0
                        for x in range(d):
                            a=list(range(i+x,j,d))
                            for p in range(len(a)//2):
                                if s[a[p]]!=s[a[-1-p]]:
                                    c+=1
                        best=min(best,c)
                cost[i][j-1]=best
        dp=[[float('inf')]*(k+1) for _ in range(n+1)]
        dp[0][0]=0
        for i in range(1,n+1):
            for t in range(1,k+1):
                for j in range(i-2,-1,-1):
                    if dp[j][t-1]!=float('inf'):
                        dp[i][t]=min(dp[i][t],dp[j][t-1]+cost[j][i-1])
        return dp[n][k]