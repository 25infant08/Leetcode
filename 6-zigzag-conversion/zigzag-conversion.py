class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1 or numRows>=len(s):
            return s
        rows=[""]*numRows
        curr=0
        down=False
        for ch in s:
            rows[curr]+=ch
            if curr==0 or curr==numRows-1:
                down =not down
            curr+=1 if down else -1
        return "".join(rows)