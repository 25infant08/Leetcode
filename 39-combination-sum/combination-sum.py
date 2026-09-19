class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        def backtrack(start, target, path):
            if target == 0:
                ans.append(path[:])
                return
            for i in range(start, len(candidates)):
                x = candidates[i]
                if x > target:
                    break
                path.append(x)
                backtrack(i, target - x, path)
                path.pop()
        backtrack(0, target, [])
        return ans