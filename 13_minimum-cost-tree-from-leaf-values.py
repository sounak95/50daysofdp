class Solution(object):

  def helper_recc(self, s, e, maxi):
    if s > e:
      return 0
    if s == e:
      return 0

    ans = float('inf')
    for i in range(s, e):
      ans = min(
          ans, maxi[(s, i)] * maxi[(i + 1, e)] + self.helper_recc(s, i, maxi) +
          self.helper_recc(i + 1, e, maxi))

    return ans

  def mctFromLeafValues_recc(self, arr):
    maxi = {}

    for i in range(len(arr)):
      maxi[(i, i)] = arr[i]
      for j in range(i + 1, len(arr)):
        maxi[(i, j)] = max(arr[j], maxi[(i, j - 1)])

    s = 0
    e = len(arr) - 1

    return self.helper_recc(s, e, maxi)

  def helper_mem(self, s, e, maxi, dp):
    if s > e:
      return 0
    if s == e:
      return 0

    if dp[s][e] != -1:
      return dp[s][e]

    ans = float('inf')
    for i in range(s, e):
      ans = min(
          ans,
          maxi[(s, i)] * maxi[(i + 1, e)] + self.helper_mem(s, i, maxi, dp) +
          self.helper_mem(i + 1, e, maxi, dp))

    dp[s][e] = ans
    return dp[s][e]

  def mctFromLeafValues_mem(self, arr):
    maxi = {}

    for i in range(len(arr)):
      maxi[(i, i)] = arr[i]
      for j in range(i + 1, len(arr)):
        maxi[(i, j)] = max(arr[j], maxi[(i, j - 1)])

    s = 0
    e = len(arr) - 1
    n = len(arr)
    dp = [[-1 for _ in range(n)] for _ in range(n)]
    return self.helper_mem(s, e, maxi, dp)

  def mctFromLeafValues(self, arr):
    maxi = {}

    for i in range(len(arr)):
      maxi[(i, i)] = arr[i]
      for j in range(i + 1, len(arr)):
        maxi[(i, j)] = max(arr[j], maxi[(i, j - 1)])

    s = 0
    e = len(arr) - 1
    n = len(arr)
    dp = [[0 for _ in range(n)] for _ in range(n)]

    for s in range(n - 1, -1, -1):
      for e in range(0, n):
        if s >= e:
          continue

        ans = float('inf')
        for i in range(s, e):
          ans = min(ans,
                    maxi[(s, i)] * maxi[(i + 1, e)] + dp[s][i] + dp[i + 1][e])
        dp[s][e] = ans

    return dp[0][n - 1]
