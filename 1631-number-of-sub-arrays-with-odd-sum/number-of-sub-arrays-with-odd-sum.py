class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        mod=10**9+7
        odd=0
        even=1
        s=0
        ans=0
        for x in arr:
            s+=x
            if s%2:
                ans+=even
                odd+=1
            else:
                ans+=odd
                even+=1
        return ans%mod