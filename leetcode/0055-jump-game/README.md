# 55. Jump Game

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Topic](https://img.shields.io/badge/Topic-Dynamic_Programming-blue) ![Topic](https://img.shields.io/badge/Topic-Greedy-blue) ![Language](https://img.shields.io/badge/Language-python3-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 24 ms |
| Memory | 20.2 MB |
| Submission Date | 2026-10-26T12:20:03.464Z |
| Platform | leetcode |

## Problem Statement

<p>You are given an integer array <code>nums</code>. You are initially positioned at the array&#39;s <strong>first index</strong>, and each element in the array represents your maximum jump length at that position.</p>

<p>Return <code>true</code><em> if you can reach the last index, or </em><code>false</code><em> otherwise</em>.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>

<pre>
<strong>Input:</strong> nums = [2,3,1,1,4]
<strong>Output:</strong> true
<strong>Explanation:</strong> Jump 1 step from index 0 to 1, then 3 steps to the last index.
</pre>

<p>
```

**Example 2:**

```
</p>

<pre>
<strong>Input:</strong> nums = [3,2,1,0,4]
<strong>Output:</strong> false
<strong>Explanation:</strong> You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
</pre>

<p>&nbsp;</p>
```

## Constraints

- <code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code>
- <code>0 &lt;= nums[i] &lt;= 10<sup>5</sup></code>

## Solution

```py
class Solution:
    def canJump(self, nums: list[int]) -> bool:
        maxReach = 0
        for i in range(len(nums)):
            if(i>maxReach):
                return False
            maxReach = max(maxReach,i+nums[i])
        return True

       

```

[View on LeetCode](https://leetcode.com/problems/jump-game/)
