class Solution:
    # @param A : integer
    # @param B : integer
    # @return a strings
    def __init__(self):
        self.ans = []
        self.tans = []

    def recur(self, i, j, ar, A):
        if j == A:
            k = ""
            for t in ar:
                k+=str(t)
            self.ans.append(k)
            return
        while j < A:
            ar[i], ar[j] = ar[j], ar[i]
            self.recur(i+1,i+1, ar, A)
            ar[j], ar[i] = ar[i], ar[j]
            j+=1


    def getPermutation(self, A, B):
        self.recur(0, 0, [i+1 for i in range(A)], A)
        self.ans.sort()
        return self.ans[B-1]

print(Solution().getPermutation(9, 1))
