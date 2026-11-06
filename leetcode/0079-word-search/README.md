# 79. Word Search

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Topic](https://img.shields.io/badge/Topic-String-blue) ![Topic](https://img.shields.io/badge/Topic-Backtracking-blue) ![Topic](https://img.shields.io/badge/Topic-Depth--First_Search-blue) ![Topic](https://img.shields.io/badge/Topic-Matrix-blue) ![Language](https://img.shields.io/badge/Language-python3-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 4955 ms |
| Memory | 19.3 MB |
| Submission Date | 2026-11-06T07:00:26.678Z |
| Platform | leetcode |

## Problem Statement

<p>Given an <code>m x n</code> grid of characters <code>board</code> and a string <code>word</code>, return <code>true</code> <em>if</em> <code>word</code> <em>exists in the grid</em>.</p>

<p>The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/04/word2.jpg" style="width: 322px; height: 242px;" />
<pre>
<strong>Input:</strong> board = [[&quot;A&quot;,&quot;B&quot;,&quot;C&quot;,&quot;E&quot;],[&quot;S&quot;,&quot;F&quot;,&quot;C&quot;,&quot;S&quot;],[&quot;A&quot;,&quot;D&quot;,&quot;E&quot;,&quot;E&quot;]], word = &quot;ABCCED&quot;
<strong>Output:</strong> true
</pre>

<p>
```

**Example 2:**

```
</p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/04/word-1.jpg" style="width: 322px; height: 242px;" />
<pre>
<strong>Input:</strong> board = [[&quot;A&quot;,&quot;B&quot;,&quot;C&quot;,&quot;E&quot;],[&quot;S&quot;,&quot;F&quot;,&quot;C&quot;,&quot;S&quot;],[&quot;A&quot;,&quot;D&quot;,&quot;E&quot;,&quot;E&quot;]], word = &quot;SEE&quot;
<strong>Output:</strong> true
</pre>

<p>
```

**Example 3:**

```
</p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/15/word3.jpg" style="width: 322px; height: 242px;" />
<pre>
<strong>Input:</strong> board = [[&quot;A&quot;,&quot;B&quot;,&quot;C&quot;,&quot;E&quot;],[&quot;S&quot;,&quot;F&quot;,&quot;C&quot;,&quot;S&quot;],[&quot;A&quot;,&quot;D&quot;,&quot;E&quot;,&quot;E&quot;]], word = &quot;ABCB&quot;
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
```

## Constraints

- <code>m == board.length</code>
- <code>n = board[i].length</code>
- <code>1 &lt;= m, n &lt;= 6</code>
- <code>1 &lt;= word.length &lt;= 15</code>
- <code>board</code> and <code>word</code> consists of only lowercase and uppercase English letters.

## Solution

```py
class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        ans = [False]

        def backtrack(i, j, k):
            if k == len(word):
                return True

            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
                return False

            if board[i][j] != word[k]:
                return False

            temp = board[i][j]
            board[i][j] = '#'

            found = (
                backtrack(i+1, j, k+1) or
                backtrack(i-1, j, k+1) or
                backtrack(i, j+1, k+1) or
                backtrack(i, j-1, k+1)
            )

            board[i][j] = temp

            return found

        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j, 0):
                    return True

        return False
```

[View on LeetCode](https://leetcode.com/problems/word-search/)
