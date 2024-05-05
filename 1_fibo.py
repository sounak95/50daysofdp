# https://leetcode.com/problems/fibonacci-number/

class Solution(object):
  def fib_rec(self, n):
      """
      :type n: int

      :rtype: int
      """
    if n==0:
      return 0

    if n==1:
      return 1

    return self.fib(n-1) + self.fib(n-2)

  def helper_mem(self, dp, n):
    if n==0:
      return 0

    if n==1:
      return 1

    if dp[n]!=-1:
      return dp[n]

    dp[n] = self.helper_mem(dp, n-1) +  self.helper_mem(dp, n-2)

    return dp[n]
    

  def fib_mem(self, n):
    dp= [-1] * (n+1)
    return self.helper_mem(dp, n)

  def fib_tab(self, n):
    if n==0:
        return 0
    if n==1:
        return 1
    dp= [-1] * (n+1)
    
    dp[0] =0
    dp[1] = 1
    
    for i in range(2, n+1):
      dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]

  def fib(self, n):
    if n==0:
      return 0
    if n==1:
      return 1

    prev=0
    curr=1
    for i in range(2, n+1):
      ans = prev+ curr
      prev= curr
      curr=ans
    return curr
    