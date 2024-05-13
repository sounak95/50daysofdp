class Solution(object):

  def check(self, curr, prev):
    '''
    curr -> bade wala dabba
    prev -> chootte wala dabba
    '''
    if prev[0] <= curr[0] and prev[1] <= curr[1] and prev[2] <= curr[2]:
      return True
    return False

  def helper_so(self, cuboids):
    n = len(cuboids)
    next_row = [0 for _ in range(n + 1)]
    curr_row = [0 for _ in range(n + 1)]

    for curr_index in range(n - 1, -1, -1):
      for prev_index in range(curr_index - 1, -2, -1):
        include = 0
        if prev_index == -1 or self.check(cuboids[curr_index],
                                          cuboids[prev_index]):
          curr_height = cuboids[curr_index][2]
          include = curr_height + next_row[curr_index + 1]

        exclude = next_row[prev_index + 1]

        curr_row[prev_index + 1] = max(include, exclude)
      next_row = curr_row.copy()

    return next_row[0]

  def maxHeight(self, cuboids):
    for cuboid in cuboids:
      cuboid.sort()
    cuboids.sort()
    return self.helper_so(cuboids)
