# https://leetcode.com/problems/guess-number-higher-or-lower-ii/


class Solution(object):

  def helper_recc(self, s, e):
    if s >= e:
      return 0

    ans = float('inf')
    for i in range(s, e):
      ans = min(
          ans, i + max(self.helper_recc(s, i - 1), self.helper_recc(i + 1, e)))
    return ans

  def getMoneyAmount_recc(self, n):
    return self.helper_recc(1, n)

  def helper_mem(self, s, e, dp):
    if s >= e:
      return 0

    if dp[s][e] != -1:
      return dp[s][e]

    ans = float('inf')
    for i in range(s, e):
      ans = min(
          ans, i +
          max(self.helper_mem(s, i - 1, dp), self.helper_mem(i + 1, e, dp)))
    dp[s][e] = ans
    return dp[s][e]

  def getMoneyAmount_mem(self, n):
    dp = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]
    return self.helper_mem(1, n, dp)

  def getMoneyAmount(self, n):
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    for start_index in range(n - 1, -1, -1):
      for end_index in range(1, n + 1):
        if start_index > end_index:
          continue
        ans = float('inf')
        for i in range(start_index, end_index):
          ans = min(ans, i + max(dp[start_index][i - 1], dp[i + 1][end_index]))

          dp[start_index][end_index] = ans
    return dp[1][n]
