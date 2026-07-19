class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        mx = 0
        cw = 0
        n = len(accounts)
        for i in range(n):
            if(n==1):
                return sum(accounts[i][:])
            if(cw>mx):
                mx = cw
            cw = sum(accounts[i][:])
        return mx
            
        