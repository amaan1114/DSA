# 518. Coin Change II

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Topic](https://img.shields.io/badge/Topic-Dynamic_Programming-blue) ![Topic](https://img.shields.io/badge/Topic-Knapsack_Problem-blue) ![Topic](https://img.shields.io/badge/Topic-Complete_Knapsack-blue) ![Language](https://img.shields.io/badge/Language-python3-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 2093 ms |
| Memory | 373.9 MB |
| Submission Date | 2026-11-02T04:31:24.560Z |
| Platform | leetcode |

## Problem Statement

<p>You are given an integer array <code>coins</code> representing coins of different denominations and an integer <code>amount</code> representing a total amount of money.</p>

<p>Return <em>the number of combinations that make up that amount</em>. If that amount of money cannot be made up by any combination of the coins, return <code>0</code>.</p>

<p>You may assume that you have an infinite number of each kind of coin.</p>

<p>The <strong>final</strong> answer is <strong>guaranteed</strong> to fit into a signed <strong>32-bit</strong> integer.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>

<pre>
<strong>Input:</strong> amount = 5, coins = [1,2,5]
<strong>Output:</strong> 4
<strong>Explanation:</strong> there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
</pre>

<p>
```

**Example 2:**

```
</p>

<pre>
<strong>Input:</strong> amount = 3, coins = [2]
<strong>Output:</strong> 0
<strong>Explanation:</strong> the amount of 3 cannot be made up just with coins of 2.
</pre>

<p>
```

**Example 3:**

```
</p>

<pre>
<strong>Input:</strong> amount = 10, coins = [10]
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
```

## Constraints

- <code>1 &lt;= coins.length &lt;= 300</code>
- <code>1 &lt;= coins[i] &lt;= 5000</code>
- All the values of <code>coins</code> are <strong>unique</strong>.
- <code>0 &lt;= amount &lt;= 5000</code>

## Solution

```py
class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        memo = {}
        def f(i,target):
            if(target==0):
                return 1
            if(i==len(coins)):
                return 0
            if((i,target) in memo):
                return memo[(i,target)]
            pick=0

            if(target>=coins[i]):
                pick = f(i,target-coins[i])
            skip = f(i+1,target)
            memo[(i,target)]=pick+skip
            return memo[(i,target)]
        return f(0,amount)


```

[View on LeetCode](https://leetcode.com/problems/coin-change-ii/)
