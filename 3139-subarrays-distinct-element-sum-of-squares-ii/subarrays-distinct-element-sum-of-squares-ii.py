from typing import List
class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD=10**9+7
        n=len(nums)
        s1=[0]*(4*n)
        s2=[0]*(4*n)
        lazy=[0]*(4*n)
        def apply(node,l,r,v):
            length=r-l+1
            s2[node]=(s2[node]+2*v*s1[node]+length*v*v)%MOD
            s1[node]=(s1[node]+length*v)%MOD
            lazy[node]=(lazy[node]+v)%MOD
        def push(node,l,r):
            if lazy[node]==0 or l==r:
                return
            mid=(l+r)//2
            v=lazy[node]
            apply(node*2,l,mid,v)
            apply(node*2+1,mid+1,r,v)
            lazy[node]=0
        def update(node,l,r,ql,qr,v):
            if ql<=l and r<=qr:
                apply(node,l,r,v)
                return
            push(node,l,r)
            mid=(l+r)//2
            if ql<=mid:
                update(node*2,l,mid,ql,qr,v)
            if qr>mid:
                update(node*2+1,mid+1,r,ql,qr,v)
            s1[node]=(s1[node*2]+s1[node*2+1])%MOD
            s2[node]=(s2[node*2]+s2[node*2+1])%MOD
        last={}
        ans=0
        for i,x in enumerate(nums):
            left=last.get(x,-1)+1
            update(1,0,n-1,left,i,1)
            ans=(ans+s2[1])%MOD
            last[x]=i
        return ans