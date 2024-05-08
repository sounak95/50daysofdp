# https://leetcode.com/problems/longest-common-subsequence/description/


class Solution(object):

  def helper_recc(self, text1, i, text2, j):
    if i >= len(text1):
      return 0

    if j >= len(text2):
      return 0

    if text1[i] == text2[j]:
      return 1 + self.helper_recc(text1, i + 1, text2, j + 1)

    else:
      return max(self.helper_recc(text1, i + 1, text2, j),
                 self.helper_recc(text1, i, text2, j + 1))

  def longestCommonSubsequence_recc(self, text1, text2):
    return self.helper_recc(text1, 0, text2, 0)

  def helper_mem(self, text1, i, text2, j, dp):
    if i >= len(text1):
      return 0

    if j >= len(text2):
      return 0

    if text1[i] == text2[j]:
      dp[i][j] = 1 + self.helper_mem(text1, i + 1, text2, j + 1, dp)

    else:
      dp[i][j] = max(self.helper_mem(text1, i + 1, text2, j, dp),
                     self.helper_mem(text1, i, text2, j + 1, dp))

    return dp[i][j]

  def longestCommonSubsequence_mem(self, text1, text2):
    dp = [[-1 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]

    return self.helper_mem(text1, 0, text2, 0, dp)

  def longestCommonSubsequence_tab(self, text1, text2):
    dp = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]

    for i in range(len(text1) - 1, -1, -1):
      for j in range(len(text2) - 1, -1, -1):
        if text1[i] == text2[j]:
          dp[i][j] = 1 + dp[i + 1][j + 1]
        else:
          dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

    return dp[0][0]

  def longestCommonSubsequence_so(self, text1, text2):
    next = [0 for _ in range(len(text1) + 1)]
    curr = [0 for _ in range(len(text1) + 1)]

    for j in range(len(text2) - 1, -1, -1):
      for i in range(len(text1) - 1, -1, -1):
        if text1[i] == text2[j]:
          curr[i] = 1 + next[i + 1]
        else:
          curr[i] = max(curr[i + 1], next[i])
      next = curr.copy()
    return curr[0]
