# 54. Spiral Matrix

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Topic](https://img.shields.io/badge/Topic-Matrix-blue) ![Topic](https://img.shields.io/badge/Topic-Simulation-blue) ![Language](https://img.shields.io/badge/Language-python3-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 0 ms |
| Memory | 19.2 MB |
| Submission Date | 2026-10-25T13:56:08.985Z |
| Platform | leetcode |

## Problem Statement

<p>Given an <code>m x n</code> <code>matrix</code>, return <em>all elements of the</em> <code>matrix</code> <em>in spiral order</em>.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/13/spiral1.jpg" style="width: 242px; height: 242px;" />
<pre>
<strong>Input:</strong> matrix = [[1,2,3],[4,5,6],[7,8,9]]
<strong>Output:</strong> [1,2,3,6,9,8,7,4,5]
</pre>

<p>
```

**Example 2:**

```
</p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/13/spiral.jpg" style="width: 322px; height: 242px;" />
<pre>
<strong>Input:</strong> matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
<strong>Output:</strong> [1,2,3,4,8,12,11,10,9,5,6,7]
</pre>

<p>&nbsp;</p>
```

## Constraints

- <code>m == matrix.length</code>
- <code>n == matrix[i].length</code>
- <code>1 &lt;= m, n &lt;= 10</code>
- <code>-100 &lt;= matrix[i][j] &lt;= 100</code>

## Solution

```py
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        ans = []
        left =0
        right = len(matrix[0])-1
        top = 0
        bottom = len(matrix)-1
        while top<=bottom and left<=right:
            for i in range(left,right+1):
                ans.append(matrix[top][i])
            top+=1
            for i in range(top,bottom+1):
                ans.append(matrix[i][right])
            right-=1
            if top <= bottom:
                for i in range(right,left-1,-1):
                    ans.append(matrix[bottom][i])
                bottom-=1
            if left<=right:
                for i in range(bottom,top-1,-1):
                    ans.append(matrix[i][left])
                left+=1
        return ans
            

```

[View on LeetCode](https://leetcode.com/problems/spiral-matrix/)
