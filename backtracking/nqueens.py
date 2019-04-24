class Solution:
    # @param A : integer
    # @return a list of list of strings
    def __init__(self):
        self.ans = []
        self.tans = []

    def check_nqueen_condition(self, i, j):
        for r in range(len(self.tans)):
            if j == self.tans[r][1]:
                return False
            elif i == self.tans[r][0]:
                return False
            elif self.tans[r][0] - i == self.tans[r][1] - j:
                return False
            elif self.tans[r][0] + self.tans[r][1] == i + j:
                return False
        return True

    def recur(self, i, j, A):
        if i == A:
            t = []
            for k in self.tans:
                t.append(k)
            self.ans.append(t)
            return

        while j < A:
            if j == A:
                return
            if self.check_nqueen_condition(i, j):
                self.tans.append([i,j])
                self.recur(i+1, 0, A)
                self.tans.pop()
            # self.recur(i, j, A)
            j += 1

    def solveNQueens(self, A):
        if A == 1:
            return [["Q"]]
        elif A < 4:
            return []
        self.recur(0, 0, A)
        ans = []
        for an in self.ans:
            s = []
            for i in range(A):
                t =
                for j in range(A):
                    if [i,j] in an:
                        t+="Q"
                    else:
                        t+="."
                s.append(t)
            ans.append(s)
        # print(ans)
        return ans



a = Solution().solveNQueens(4)
