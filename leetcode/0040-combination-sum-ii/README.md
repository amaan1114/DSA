# 40. Combination Sum II

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Topic](https://img.shields.io/badge/Topic-Backtracking-blue) ![Language](https://img.shields.io/badge/Language-python3-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 26 ms |
| Memory | 19.5 MB |
| Submission Date | 2026-10-21T05:23:53.554Z |
| Platform | leetcode |

## Problem Statement

<p>Given a collection of candidate numbers (<code>candidates</code>) and a target number (<code>target</code>), find all unique combinations in <code>candidates</code>&nbsp;where the candidate numbers sum to <code>target</code>.</p>

<p>Each number in <code>candidates</code>&nbsp;may only be used <strong>once</strong> in the combination.</p>

<p><strong>Note:</strong>&nbsp;The solution set must not contain duplicate combinations.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>

<pre>
<strong>Input:</strong> candidates = [10,1,2,7,6,1,5], target = 8
<strong>Output:</strong> 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
</pre>

<p>
```

**Example 2:**

```
</p>

<pre>
<strong>Input:</strong> candidates = [2,5,2,1,2], target = 5
<strong>Output:</strong> 
[
[1,2,2],
[5]
]
</pre>

<p>&nbsp;</p>
```

## Constraints

- <code>1 &lt;=&nbsp;candidates.length &lt;= 100</code>
- <code>1 &lt;=&nbsp;candidates[i] &lt;= 50</code>
- <code>1 &lt;= target &lt;= 30</code>

## Solution

```py
class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        ans = []
        candidates.sort()
        def back(arr,start):
            sum1 = sum(arr)
            if(sum1==target):
                ans.append(arr.copy())
                return
            if(sum1>target):
                return
            for i in range(start,len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                arr.append(candidates[i])
                back(arr,i+1)
                arr.pop()
        back([],0)
        return ans
```

[View on LeetCode](https://leetcode.com/problems/combination-sum-ii/)
