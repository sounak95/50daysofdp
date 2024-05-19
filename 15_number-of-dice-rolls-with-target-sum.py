# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/description/
# pattern: explore all possible ways

MOD = 10**9 + 7


class Solution(object):

  def helper_recc(self, n, k, target, dice_count, curr_sum):
    if dice_count == n and curr_sum == target:
      return 1

    if dice_count == n and curr_sum != target:
      return 0

    if dice_count != n and curr_sum == target:
      return 0

    ans = 0
    for face in range(1, k + 1):
      if curr_sum + face < target:
        ans = ans + self.helper_recc(n, k, target, dice_count + 1,
                                     curr_sum + face)

    return ans

  def numRollsToTarget_recc(self, n, k, target):
    return self.helper_recc(n, k, target, dice_count=0, curr_sum=0)

  def helper_mem(self, n, k, target, dice_count, curr_sum, dp):
    if dice_count == n and curr_sum == target:
      return 1

    if dice_count == n and curr_sum != target:
      return 0

    if dice_count != n and curr_sum == target:
      return 0

    if dp[dice_count][curr_sum] != -1:
      return dp[dice_count][curr_sum]

    ans = 0
    for face in range(1, k + 1):
      if curr_sum + face <= target:
        ans = (ans + self.helper_mem(n, k, target, dice_count + 1,
                                     curr_sum + face, dp)) % MOD

    dp[dice_count][curr_sum] = ans
    return dp[dice_count][curr_sum]

  def numRollsToTarget_mem(self, n, k, target):
    dp = [[-1 for _ in range(target + 1)] for _ in range(n + 1)]
    return self.helper_mem(n, k, target, 0, 0, dp)

  def numRollsToTarget_tab(self, n, k, target):
    dp = [[0 for _ in range(target + 1)] for _ in range(n + 1)]

    dp[n][target] = 1

    for dice_count in range(n - 1, -1, -1):
      for curr_sum in range(target, -1, -1):
        ans = 0
        for face in range(1, k + 1):
          if curr_sum + face <= target:
            ans = (ans + dp[dice_count + 1][curr_sum + face]) % MOD
        dp[dice_count][curr_sum] = ans

    return dp[0][0]

  def numRollsToTarget(self, n, k, target):
    next_row = [0 for _ in range(target + 1)]
    curr_row = [0 for _ in range(target + 1)]

    next_row[target] = 1

    for dice_count in range(n - 1, -1, -1):
      for curr_sum in range(target, -1, -1):
        ans = 0
        for face in range(1, k + 1):
          if curr_sum + face <= target:
            ans = (ans + next_row[curr_sum + face]) % MOD
        curr_row[curr_sum] = ans
      next_row = curr_row.copy()

    return next_row[0]
