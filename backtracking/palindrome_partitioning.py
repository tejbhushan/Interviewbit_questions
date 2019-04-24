class Solution:
    # @param A : string
    # @return a list of list of strings
    def __init__(self):
        self.ans = []
        self.tans = []

    def palin(self, a):
        for i in range(len(a)/2):
            if not a[i] == a[len(a)-1- i]:
                return False
        return True

    def recur(self, j, A):
        if j > len(A):
            t = []
            for k in self.tans:
                t.append(k)
            self.ans.append(t)
            # print(len(self.tans))

        while j <= len(A):
            # print("f", A[i:j], i, j)
            if self.palin(A[0:j]):
                self.tans.append(A[0:j])
                self.recur(1, A[j:len(A)])
                self.tans.pop()
                # print("r", i, j, A[i:j])
            j += 1

    def partition(self, A):
        self.recur(1, A)
        return self.ans

s = Solution()
print(s.partition("abaa"))
