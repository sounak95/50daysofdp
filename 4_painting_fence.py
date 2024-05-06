# https://www.geeksforgeeks.org/problems/painting-the-fence3727/1

MOD = 10**9 + 7
class Solution:

  def countWays_recc(self, n, k):
    '''
    if n == 1: In this case, each post can independently be painted with any of the k 
    colors. So there are k ways to paint a single post.
    '''
    if n == 1:
      return k
    '''
    if n == 2: For two posts, you have two scenarios:
    Paint both posts the same color: There are k choices for the first post and 1 way to match this color for the second post, yielding k.
    Paint both posts with different colors: There are k choices for the first post and k-1 choices for the second post, yielding k * (k - 1) ways.
    Combining both scenarios for two posts, you get k + k * (k - 1).

    '''
    if n == 2:
      return k + k * (k - 1)
    '''
    Last Post Different from the Second-to-Last Post:
If you choose a color for the last post that is different from the second-to-last post, you can freely pick any color from the remaining k-1 colors (since k is total colors, and you avoid one to ensure it's different).
Then, look at how you could have painted the rest of the fence up to the second-to-last post (n-1 posts in total). This gives the term self.countWays(n-1, k).

Last Two Posts Different from the Third-to-Last Post:
If you want the last two posts to be different from the third-to-last post, then these two posts can be colored in k-1 ways relative to the third-to-last post.
You then need to consider how the fence could have been painted up to the third-to-last post, which is self.countWays(n-2, k).

Combining the Scenarios:
You add these two scenarios together (self.countWays(n-1, k) for the scenario where only the last post needs to differ from its previous post, and self.countWays(n-2, k) for the scenario where the last two posts are treated as a unit different from the third-to-last post).
You multiply the sum of these possibilities by (k-1) because for each scenario, the new post(s) can be any of the remaining k-1 colors.

Formula:
Final Recursive Case: return (k-1) * (self.countWays(n-1, k) + self.countWays(n-2, k))
This means that for each way you can paint up to the previous posts (n-1 or n-2), you have k-1 choices for how to paint the next post or posts, ensuring no three consecutive posts are the same color.


'''

    return (k - 1) * (self.countWays_recc(n - 1, k) +
                      self.countWays_recc(n - 2, k))

  def helper_mem(self, dp, n, k):
    if n == 1:
      return k

    if n == 2:
      return k + k * (k - 1)

    if dp[n] != -1:
      return dp[n]

    dp[n] = (k - 1) * (self.helper_mem(dp, n - 1, k) +
                       self.helper_mem(dp, n - 2, k))

    return dp[n]

  def countWays_mem(self, n, k):
    dp = [-1] * (n + 1)
    return self.helper_mem(dp, n, k)

  def countWays_tab(self, n, k):
    dp = [-1] * (n + 1)
    dp[1] = k
    if n == 1:
      return dp[1]
    dp[2] = k + k * (k - 1)
    if n == 2:
      return dp[2]

    for i in range(3, n + 1):
      dp[i] = (k - 1) * (dp[i - 1] + dp[i - 2]) % MOD

    return dp[n]

  def countWays_SO(self, n, k):
    prev2 = k
    if n == 1:
      return prev2

    prev1 = k + k * (k - 1)
    if n == 2:
      return prev1

    for i in range(3, n+1):
      curr = (k-1) * (prev1+prev2) % MOD
      prev2 = prev1
      prev1=curr
      
    return prev1