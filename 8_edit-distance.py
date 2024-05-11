class Solution(object):
  '''
  
  a b c
  a b c d e f
  
  '''

  def helper_recc(self, word1, word2, i, j):
    if i == len(word1):
      return len(word2) - j

    if j == len(word2):
      return len(word1) - i

    if word1[i] == word2[j]:
      return self.helper_recc(word1, word2, i + 1, j + 1)
    else:
      replace = 1 + self.helper_recc(word1, word2, i + 1, j + 1)
      remove = 1 + self.helper_recc(word1, word2, i + 1, j)
      insert = 1 + self.helper_recc(word1, word2, i, j + 1)
      ans = min(replace, min(remove, insert))
      return ans

  def minDistance_recc(self, word1, word2):
    return self.helper_recc(word1, word2, 0, 0)

  def helper_mem(self, word1, word2, i, j, dp):
    if i == len(word1):
      return len(word2) - j

    if j == len(word2):
      return len(word1) - i

    if dp[i][j] != -1:
      return dp[i][j]

    if word1[i] == word2[j]:
      dp[i][j] = self.helper_mem(word1, word2, i + 1, j + 1, dp)
    else:
      replace = 1 + self.helper_mem(word1, word2, i + 1, j + 1, dp)
      remove = 1 + self.helper_mem(word1, word2, i + 1, j, dp)
      insert = 1 + self.helper_mem(word1, word2, i, j + 1, dp)
      ans = min(replace, min(remove, insert))
      dp[i][j] = ans

    return dp[i][j]

  def minDistance_mem(self, word1, word2):
    dp = [[-1 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]

    return self.helper_mem(word1, word2, 0, 0, dp)

  def minDistance_tab(self, word1, word2):
    dp = [[-1 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]

    for row in range(len(word1) + 1):
      dp[row][len(word2)] = len(word1) - row

    for col in range(len(word2) + 1):
      dp[len(word1)][col] = len(word2) - col

    for i in range(len(word1) - 1, -1, -1):
      for j in range(len(word2) - 1, -1, -1):
        if word1[i] == word2[j]:
          dp[i][j] = dp[i + 1][j + 1]
        else:
          replace = 1 + dp[i + 1][j + 1]
          remove = 1 + dp[i + 1][j]
          insert = 1 + dp[i][j + 1]
          ans = min(replace, min(remove, insert))
          dp[i][j] = ans

    return dp[0][0]

  def minDistance(self, word1, word2):
    next = [0 for _ in range(len(word1) + 1)]
    curr = [0 for _ in range(len(word1) + 1)]

    for row in range(len(word1) + 1):
      next[row] = len(word1) - row

    # for col in range(len(word2) + 1):
    #   dp[len(word1)][col] = len(word2) - col

    for j in range(len(word2) - 1, -1, -1):
      curr[len(word1)] = len(word2) - j
      for i in range(len(word1) - 1, -1, -1):
        if word1[i] == word2[j]:
          curr[i] = next[i + 1]
        else:
          replace = 1 + next[i + 1]
          remove = 1 + curr[i + 1]
          insert = 1 + next[i]
          ans = min(replace, min(remove, insert))
          curr[i] = ans
      next = curr.copy()

    return next[0]
