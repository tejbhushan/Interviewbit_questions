class Solution:
    def __init__(self):
        self.ans = []
        self.tans = []

    def recur(self, sum, i, A, B):
        if sum == B:
            t = []
            if not self.tans in self.ans:
                for k in self.tans:
                    t.append(k)
                self.ans.append(t)
            return

        while i < len(A):
            if sum + A[i] <= B:
                sum += A[i]
                self.tans.append(A[i])
                self.recur(sum, i+1, A, B)
                sum -= A[i]
                self.tans.pop()
            i += 1

    def combinationSum(self, A, B):
        A.sort()
        self.recur(0, 0, A, B)
        return self.ans

s = Solution()
print(s.combinationSum([10,1,2,7,6,1,5], 8))
