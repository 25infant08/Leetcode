class Solution:
    def hasMatch(self, string: str, pattern: str) -> bool:
        left_part, right_part = pattern.split('*')
        left_idx = string.find(left_part)
        right_idx = string.find(right_part, left_idx + len(left_part))
        return left_idx != -1 and right_idx != -1