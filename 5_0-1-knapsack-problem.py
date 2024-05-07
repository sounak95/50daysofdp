# https://www.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1


class Solution:

  #Function to return max value that can be put in knapsack of capacity W.

  def helper_recc(self, W, wt, val, n, i):
    if i == n:
      return 0

    include = 0
    if wt[i] <= W:
      include = val[i] + self.helper_recc(W - wt[i], wt, val, n, i + 1)

    exclude = self.helper_recc(W, wt, val, n, i + 1)

    return max(include, exclude)

  def knapSack_recc(self, W, wt, val, n):
    return self.helper_recc(W, wt, val, n, 0)

  def helper_mem(self, W, wt, val, n, i, dp):
    if i == n:
      return 0

    if dp[W][i] != -1:
      return dp[W][i]

    include = 0
    if wt[i] <= W:
      include = val[i] + self.helper_mem(W - wt[i], wt, val, n, i + 1, dp)

    exclude = self.helper_mem(W, wt, val, n, i + 1, dp)

    dp[W][i] = max(include, exclude)

    return dp[W][i]

  def knapSack_mem(self, W, wt, val, n):
    dp = [[-1 for _ in range(n + 1)] for _ in range(W + 1)]

    return self.helper_mem(W, wt, val, n, 0, dp)

  def knapSack_tab(self, W, wt, val, n):
    dp = [[-1 for _ in range(n + 1)] for _ in range(W + 1)]

    for row in range(W + 1):
      dp[row][n] = 0

    for w in range(W + 1):
      for j in range(n - 1, -1, -1):
        include = 0
        if wt[j] <= w:
          include = val[j] + dp[w - wt[j]][j + 1]

        exclude = dp[w][j + 1]

        dp[w][j] = max(include, exclude)

    return dp[W][0]

  def knapSack_so1(self, W, wt, val, n):
    next = [0 for _ in range(W + 1)]
    curr = [-1 for _ in range(W + 1)]

    for j in range(n - 1, -1, -1):
      for w in range(W + 1):
        include = 0
        if wt[j] <= w:
          include = val[j] + next[w - wt[j]]

        exclude = next[w]

        curr[w] = max(include, exclude)

      next = curr.copy()

    return curr[W]

  def knapSack_so2(self, W, wt, val, n):
    next = [0 for _ in range(W + 1)]

    for j in range(n - 1, -1, -1):
      for w in range(W, -1, -1):
        include = 0
        if wt[j] <= w:
          include = val[j] + next[w - wt[j]]

        exclude = next[w]

        next[w] = max(include, exclude)

    return next[W]
