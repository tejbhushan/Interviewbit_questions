class Solution:
    # @param A : integer
    # @param B : integer
    # @return a list of list of integers
    def __init__(self):
        self.lis = []
        self.lis1 = []

    def recur(self, i, A, B):
        if B == 0:
            tem = []
            for j in self.lis:
                tem.append(j)
            self.lis1.append(tem)
        else:
            while i <= A:
                # i += 1
                self.lis.append(i)
                self.recur(i+1, A, B-1)
                i += 1
                self.lis.pop()

    def combine(self, A, B):
        if A < B:
            return []
        else:
            self.recur(1, A, B)
        return self.lis1




s = Solution()
print(s.combine(2, 2))
