# https://leetcode.com/problems/partition-equal-subset-sum
# pattern: include exclude

class Solution(object):

  def helper_recc(self, index, sum, target, nums):
    if index >= len(nums):
      return 0
    if sum > target:
      return 0
    if sum == target:
      return 1

    include = self.helper_recc(index + 1, sum + nums[index], target, nums)
    exclude = self.helper_recc(index + 1, sum, target, nums)

    return include or exclude

  def canPartition_recc(self, nums):
    target = 0
    for num in nums:
      target += num

    if target % 2 != 0:
      return False

    target = target // 2
    return self.helper_recc(0, 0, target, nums)

  def helper_mem(self, index, sum, target, nums, dp):
    if index >= len(nums):
      return 0
    if sum > target:
      return 0
    if sum == target:
      return 1

    if dp[index][sum] != -1:
      return dp[index][sum]

    include = self.helper_mem(index + 1, sum + nums[index], target, nums, dp)
    exclude = self.helper_mem(index + 1, sum, target, nums, dp)

    dp[index][sum] = include or exclude
    return dp[index][sum]

  def canPartition_mem(self, nums):
    target = 0
    for num in nums:
      target += num

    if target % 2 != 0:
      return False

    target = target // 2
    dp = [[-1 for _ in range(target + 1)] for _ in range(len(nums) + 1)]

    return self.helper_mem(0, 0, target, nums, dp)

  def canPartition_tab(self, nums):
    target = 0
    for num in nums:
      target += num

    if target % 2 != 0:
      return False

    target = target // 2
    dp = [[0 for _ in range(target + 1)] for _ in range(len(nums) + 1)]

    for index in range(len(nums) + 1):
      dp[index][target] = 1

    for index in range(len(nums) - 1, -1, -1):
      for sum in range(target, -1, -1):
        include = 0
        if sum + nums[index] <= target:
          include = dp[index + 1][sum + nums[index]]
        exclude = dp[index + 1][sum]
        dp[index][sum] = include or exclude

    return dp[0][0]

  def canPartition(self, nums):
    target = 0
    for num in nums:
      target += num

    if target % 2 != 0:
      return False

    target = target // 2

    next_row = [0 for _ in range(target + 1)]
    curr_row = [0 for _ in range(target + 1)]

    next_row[target] = 1
    curr_row[target] = 1

    for index in range(len(nums) - 1, -1, -1):
      for sum in range(target, -1, -1):
        include = 0
        if sum + nums[index] <= target:
          include = next_row[sum + nums[index]]
        exclude = next_row[sum]
        curr_row[sum] = include or exclude
      next_row = curr_row.copy()

    return next_row[0]
