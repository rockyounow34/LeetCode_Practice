class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        mx = 0
        cw = 0
        for i in accounts:
            cw = sum(i)
            mx = max(cw,mx)
        return mx

            
        