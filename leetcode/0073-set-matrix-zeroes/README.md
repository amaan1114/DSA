# 73. Set Matrix Zeroes

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Topic](https://img.shields.io/badge/Topic-Hash_Table-blue) ![Topic](https://img.shields.io/badge/Topic-Matrix-blue) ![Language](https://img.shields.io/badge/Language-python3-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 235 ms |
| Memory | 23.6 MB |
| Submission Date | 2026-10-28T09:04:43.155Z |
| Platform | leetcode |

## Problem Statement

<p>Given an <code>m x n</code> integer matrix <code>matrix</code>, if an element is <code>0</code>, set its entire row and column to <code>0</code>&#39;s.</p>

<p>You must do it <a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank">in place</a>.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/08/17/mat1.jpg" style="width: 450px; height: 169px;" />
<pre>
<strong>Input:</strong> matrix = [[1,1,1],[1,0,1],[1,1,1]]
<strong>Output:</strong> [[1,0,1],[0,0,0],[1,0,1]]
</pre>

<p>
```

**Example 2:**

```
</p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/08/17/mat2.jpg" style="width: 450px; height: 137px;" />
<pre>
<strong>Input:</strong> matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
<strong>Output:</strong> [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
</pre>

<p>&nbsp;</p>
```

## Constraints

- <code>m == matrix.length</code>
- <code>n == matrix[0].length</code>
- <code>1 &lt;= m, n &lt;= 200</code>
- <code>-2<sup>31</sup> &lt;= matrix[i][j] &lt;= 2<sup>31</sup> - 1</code>

## Solution

```py
class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        cols=len(matrix[0])
        rows = len(matrix)
        arr=[]
        for i in range(rows):
            for j in range(cols):
                if(matrix[i][j]==0):
                    arr.append([i,j])
        print(arr)
        for r, c in arr:
            for j in range(cols):
                matrix[r][j] = 0

            for i in range(rows):
                matrix[i][c] = 0
        
```

[View on LeetCode](https://leetcode.com/problems/set-matrix-zeroes/)
