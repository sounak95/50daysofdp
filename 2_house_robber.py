class Solution(object):
  def helper_recc(self, i, nums):
    if i>=len(nums):
      return 0

    include = nums[i] + self.helper_recc(i+2, nums)
    exclude = 0 + self.helper_recc(i+1, nums)

    return max(include, exclude)


  def rob_recc(self, nums):
    return self.helper_recc(0, nums)


  def helper_mem(self, dp, i, nums):
    if i>=len(nums):
      return 0
  
    if dp[i]!=-1:
      return dp[i]
  
    include = nums[i] + self.helper_mem(dp,i+2, nums)
    exclude = 0 + self.helper_mem(dp, i+1, nums)
  
    dp[i] = max(include, exclude)
  
    return dp[i]
  
  def rob_mem(self, nums):
    dp=[-1] * len(nums)
    return self.helper_mem(dp, 0, nums)


  def rob_tab(self, nums):
    n= len(nums)
    dp = [-1] * n
    dp[n-1] = nums[n-1]

    for i in range(n-2, -1 ,-1):
      temp_ans=0
      if i+2<n:
        temp_ans=dp[i+2]        
      include = nums[i] + temp_ans
      exclude =0 + dp[i+1]
      dp[i] = max(include, exclude)

    return dp[0]


  def rob(self, nums):
    n= len(nums)
    curr = nums[n-1] #i+1
    next = 0 #i+1
    for i in range(n-2, -1, -1):  
      include = nums[i] + next
      exclude = 0 + curr
      ans = max(include, exclude)

      next = curr
      curr = ans

    return curr
  