# https://leetcode.com/problems/coin-change/description/
'''
                         solve([1, 2, 5], 11)
                         /         |         \
                        /          |          \
             solve([1,2,5], 10)   solve([1,2,5], 9)  solve([1,2,5], 6)
                 /      |      \       /      |      \        /     |    \
                /       |       \     /       |       \      /      |     \
solve([1,2,5],9) solve([1,2,5],8) solve([1,2,5],5) ...  solve([1,2,5],5) ...
    /     |     \        and so on...
   /      |      \
 ...     ...     ...

'''


class Solution(object):

  def helper_recc(self, coins, amount):
    if amount == 0:
      return 0

    mini = float('inf')

    for i in range(len(coins)):
      recAns = 0
      if amount - coins[i] >= 0:
        recAns = self.helper_recc(coins, amount - coins[i])
        if recAns != float('inf'):
          ans = 1 + recAns
          mini = min(ans, mini)
    return mini

  def coinChange_recc(self, coins, amount):
    ans = self.helper_recc(coins, amount)
    if ans == float('inf'):
      return -1
    else:
      return ans

  def helper_mem(self, dp, coins, amount):
    if amount == 0:
      return 0

    if dp[amount] != -1:
      return dp[amount]

    mini = float('inf')

    for i in range(len(coins)):
      recAns = 0
      if amount - coins[i] >= 0:
        recAns = self.helper_mem(dp, coins, amount - coins[i])
        if recAns != float('inf'):
          ans = 1 + recAns
          mini = min(ans, mini)
    dp[amount] = mini

    return dp[amount]

  def coinChange_mem(self, coins, amount):
    n = amount
    dp = [-1] * (n + 1)
    ans = self.helper_mem(dp, coins, amount)
    if ans == float('inf'):
      return -1
    else:
      return ans

  def coinChange_tab(self, coins, amount):
    n = amount
    dp = [float('inf')] * (n + 1)
    if amount == 0:
      return 0

    dp[0] = 0

    for amt in range(1, n + 1):
      mini = float('inf')
      for i in range(len(coins)):
        recAns = 0
        if amount - coins[i] >= 0:
          recAns = dp[amt - coins[i]]
          if recAns != float('inf'):
            ans = 1 + recAns
            mini = min(ans, mini)
      dp[amt] = mini

    if dp[amount] == float('inf'):
      return -1
    else:
      return dp[amount]
