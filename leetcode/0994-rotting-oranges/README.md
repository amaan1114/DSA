# 994. Rotting Oranges

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Topic](https://img.shields.io/badge/Topic-Breadth--First_Search-blue) ![Topic](https://img.shields.io/badge/Topic-Matrix-blue) ![Language](https://img.shields.io/badge/Language-python3-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 4 ms |
| Memory | 19.2 MB |
| Submission Date | 2026-10-20T05:43:28.344Z |
| Platform | leetcode |

## Problem Statement

<p>You are given an <code>m x n</code> <code>grid</code> where each cell can have one of three values:</p>

<ul>
	<li><code>0</code> representing an empty cell,</li>
	<li><code>1</code> representing a fresh orange, or</li>
	<li><code>2</code> representing a rotten orange.</li>
</ul>

<p>Every minute, any fresh orange that is <strong>4-directionally adjacent</strong> to a rotten orange becomes rotten.</p>

<p>Return <em>the minimum number of minutes that must elapse until no cell has a fresh orange</em>. If <em>this is impossible, return</em> <code>-1</code>.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/02/16/oranges.png" style="width: 650px; height: 137px;" />
<pre>
<strong>Input:</strong> grid = [[2,1,1],[1,1,0],[0,1,1]]
<strong>Output:</strong> 4
</pre>

<p>
```

**Example 2:**

```
</p>

<pre>
<strong>Input:</strong> grid = [[2,1,1],[0,1,1],[1,0,1]]
<strong>Output:</strong> -1
<strong>Explanation:</strong> The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
</pre>

<p>
```

**Example 3:**

```
</p>

<pre>
<strong>Input:</strong> grid = [[0,2]]
<strong>Output:</strong> 0
<strong>Explanation:</strong> Since there are already no fresh oranges at minute 0, the answer is just 0.
</pre>

<p>&nbsp;</p>
```

## Constraints

- <code>m == grid.length</code>
- <code>n == grid[i].length</code>
- <code>1 &lt;= m, n &lt;= 10</code>
- <code>grid[i][j]</code> is <code>0</code>, <code>1</code>, or <code>2</code>.

## Solution

```py
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        minute=0
        while True:
            rotten = []
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    if(grid[i][j]==1):
                        if(j>0):
                            if(grid[i][j-1]==2):
                               rotten.append((i,j))
                        if(j<len(grid[i])-1):
                            if(grid[i][j+1]==2):
                                rotten.append((i,j))
                        if(i>0):
                            if(grid[i-1][j]==2):
                                rotten.append((i,j))
                        if(i<len(grid)-1):
                            if(grid[i+1][j]==2):
                                rotten.append((i,j))
            if(len(rotten)==0):
                break
            for i,j in rotten:
                grid[i][j]=2
            minute+=1
        for i in grid:
            for j in i:
                if(j==1):
                    return -1
        return minute
                           



```

[View on LeetCode](https://leetcode.com/problems/rotting-oranges/)
