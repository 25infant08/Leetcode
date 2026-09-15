from typing import List
class Solution:
    def boxDelivering(self, boxes: List[List[int]], portsCount: int, maxBoxes: int, maxWeight: int) -> int:
        n = len(boxes)
        prefix = [0] * (n + 1)
        change = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] + boxes[i - 1][1]
            if i > 1:
                change[i] = change[i - 1] + (boxes[i - 1][0] != boxes[i - 2][0])
        dp = [0] * (n + 1)
        q = [0] * (n + 1)
        head = tail = 0
        q[tail] = 0
        tail += 1
        for i in range(1, n + 1):
            while head < tail and (
                i - q[head] > maxBoxes or
                prefix[i] - prefix[q[head]] > maxWeight
            ):
                head += 1
            j = q[head]
            dp[i] = dp[j] + change[i] - change[j + 1] + 2
            while head < tail and dp[q[tail - 1]] - change[q[tail - 1] + 1] >= dp[i] - change[i]:
                tail -= 1
            q[tail] = i
            tail += 1
        return dp[n]