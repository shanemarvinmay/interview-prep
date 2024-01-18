# Solution Explained!
* *This is a slightly modified version of [votrubac's solution](https://leetcode.com/problems/find-the-pivot-integer/solutions/2851991/sqrt-binary-search-dp/).*
## Main Idea in a Nutshel
* We can get the sum from 1 to x in a simple fomula (found below).
* So can find where the sum from 1...x = 1...n - 1...x + x
  * We add x at the end becaues 1...n - 1...x = x+1...n and we need x.
* We try to find x by doing a binary search from 1 to n
  * returning -1 if we can't find a valid x

## Formula 
### Sumation $$\sum_{1}^n = \frac{n(n + 1)}{2}$$
So...

$$ \frac{x(x + 1)}{2} = \frac{n(n + 1)}{2} - \frac{x(x + 1)}{2} + x $$
$$ \frac{x(x + 1)}{2} + \frac{x(x + 1)}{2} - x = \frac{n(n + 1)}{2} $$
$$ x(x + 1) - x = \frac{n(n + 1)}{2} $$
$$ x^2 + x - x = \frac{n(n + 1)}{2} $$
$$ x^2 = \frac{n(n + 1)}{2} $$ 
$$ x^2 = \sum_{1}^n $$ 

## Time Complexity $O(log(n))$

## Putting It All Together in Code!
```python
class Solution:
    def pivotInteger(self, n: int) -> int:
        n_summation = n * (n + 1) / 2
        l, r = 1, n

        while l < r:
            mid = (l + r) // 2

            if mid * mid == n_summation:
                return mid
            elif mid * mid > n_summation:
                r = mid
            else:
                l = mid + 1
        
        if l * l == n_summation:
            return l
        return -1
```