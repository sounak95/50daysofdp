# https://leetcode.com/problems/longest-increasing-subsequence/


class Solution(object):

  def helper_recc(self, nums, curr, prev):
    if curr >= len(nums):
      return 0

    include = 0
    if prev == -1 or nums[curr] > nums[prev]:
      include = 1 + self.helper_recc(nums, curr + 1, curr)

    exclude = self.helper_recc(nums, curr + 1, prev)

    return max(include, exclude)

  def lengthOfLIS_recc(self, nums):
    return self.helper_recc(nums, 0, -1)

  def helper_mem(self, nums, curr, prev, dp):
    if curr >= len(nums):
      return 0

    if dp[curr][prev + 1] != -1:
      return dp[curr][prev + 1]

    include = 0
    if prev == -1 or nums[curr] > nums[prev]:
      include = 1 + self.helper_mem(nums, curr + 1, curr, dp)

    exclude = self.helper_mem(nums, curr + 1, prev, dp)

    dp[curr][prev + 1] = max(include, exclude)

    return dp[curr][prev + 1]

  def lengthOfLIS_mem(self, nums):
    n = len(nums)
    dp = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]
    return self.helper_mem(nums, 0, -1, dp)

  def lengthOfLIS_tab(self, nums):
    n = len(nums)
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    for curr_index in range(n - 1, -1, -1):
      for prev_index in range(curr_index - 1, -2, -1):
        include = 0
        if prev_index == -1 or nums[curr_index] > nums[prev_index]:
          include = 1 + dp[curr_index + 1][curr_index + 1]

        exclude = dp[curr_index + 1][prev_index + 1]

        dp[curr_index][prev_index + 1] = max(include, exclude)
    return dp[0][0]

  def lengthOfLIS(self, nums):
    n = len(nums)
    next_row = [0 for _ in range(n + 1)]
    curr_row = [0 for _ in range(n + 1)]

    for curr_index in range(n - 1, -1, -1):
      for prev_index in range(curr_index - 1, -2, -1):
        include = 0
        if prev_index == -1 or nums[curr_index] > nums[prev_index]:
          include = 1 + next_row[curr_index + 1]

        exclude = next_row[prev_index + 1]

        curr_row[prev_index + 1] = max(include, exclude)
      next_row = curr_row.copy()

    return next_row[0]
