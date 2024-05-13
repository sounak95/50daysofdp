# https://leetcode.com/problems/russian-doll-envelopes/


class Solution(object):

  def check(self, curr, prev):
    '''
    curr -> bade wala dabba
    prev -> chootte wala dabba
    '''
    if prev[0] < curr[0] and prev[1] < curr[1]:
      return True
    return False

  def helper_so(self, envelopes):
    n = len(envelopes)
    next_row = [0 for _ in range(n + 1)]
    curr_row = [0 for _ in range(n + 1)]

    for curr_index in range(n - 1, -1, -1):
      for prev_index in range(curr_index - 1, -2, -1):
        include = 0
        if prev_index == -1 or self.check(envelopes[curr_index],
                                          envelopes[prev_index]):
          include = 1 + next_row[curr_index + 1]

        exclude = next_row[prev_index + 1]

        curr_row[prev_index + 1] = max(include, exclude)
      next_row = curr_row.copy()

    return next_row[0]

  def maxEnvelopes(self, envelopes):
    envelopes.sort()
    return self.helper_so(envelopes)
