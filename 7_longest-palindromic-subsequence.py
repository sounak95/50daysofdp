class Solution(object):

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

  def longestPalindromeSubseq(self, s):
    reversed_s = ''.join(reversed(s))
    return self.longestCommonSubsequence_so(s, reversed_s)
