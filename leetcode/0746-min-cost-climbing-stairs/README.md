# 746. Min Cost Climbing Stairs

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Topic](https://img.shields.io/badge/Topic-Dynamic_Programming-blue) ![Language](https://img.shields.io/badge/Language-python3-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 9 ms |
| Memory | 20.8 MB |
| Submission Date | 2026-10-29T09:20:31.082Z |
| Platform | leetcode |

## Problem Statement

<p>You are given an integer array <code>cost</code> where <code>cost[i]</code> is the cost of <code>i<sup>th</sup></code> step on a staircase.</p>

<p>Once you pay the cost, you can either climb <strong>one</strong> or <strong>two</strong> steps.</p>

<p>You can either start from the step with index 0, or the step with index 1.</p>

<p>Return the <strong>minimum</strong> cost to reach the top of the staircase, which is the position just past the last step (index <code>cost.length</code>).</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>

<pre>
<strong>Input:</strong> cost = [10,<u>15</u>,20]
<strong>Output:</strong> 15
<strong>Explanation:</strong> You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.
</pre>

<p>
```

**Example 2:**

```
</p>

<pre>
<strong>Input:</strong> cost = [<u>1</u>,100,<u>1</u>,1,<u>1</u>,100,<u>1</u>,<u>1</u>,100,<u>1</u>]
<strong>Output:</strong> 6
<strong>Explanation:</strong> You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.
</pre>

<p>&nbsp;</p>
```

## Constraints

- <code>2 &lt;= cost.length &lt;= 1000</code>
- <code>0 &lt;= cost[i] &lt;= 999</code>

## Solution

```py
class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
            n = len(cost)
            dp=[-1]*(n+1)
            def jump(i):
                if(i<=1):
                    return 0
                if(dp[i]!=-1):
                    return dp[i]
                climb1 = jump(i-1)+cost[i-1]
                climb2 = jump(i-2)+cost[i-2]
                ans = min(climb1,climb2)
                dp[i] = ans
                return dp[i]
            return jump(n)
```

[View on LeetCode](https://leetcode.com/problems/min-cost-climbing-stairs/)
