import numpy as np
class Solution:
    def getmatrixpower(self, mat, pow, mod)
        if pow == 0:
            return np.mat( [ [1,0,0], [0,1,0], [0,0,1]])
        ret = self.getmatrixpower(mat, pow//2, mod)
        ret = ret * ret % mod
        if pow % 2 == 1:
            ret = ret * mat % mod
        return ret
    
    def waysToStep(self, n):
        ans = [1, 1, 2]
        if n <= 2:
            return ans[n]
        mat = np.mat( [ [1,1,1], [1,0,0], [0,1,0] ])
        ret = self.getmatrixpower(mat, n-2, 1000000007)
        l = np.mat([[2], [1], [1]])
        ret = (ret * 1 % 1000000007)[0, 0]
        return int(ret)