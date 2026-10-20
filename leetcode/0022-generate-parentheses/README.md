# 22. Generate Parentheses

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Topic](https://img.shields.io/badge/Topic-String-blue) ![Topic](https://img.shields.io/badge/Topic-Dynamic_Programming-blue) ![Topic](https://img.shields.io/badge/Topic-Backtracking-blue) ![Topic](https://img.shields.io/badge/Topic-Bracket_Sequences-blue) ![Language](https://img.shields.io/badge/Language-python3-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 95 ms |
| Memory | 19.4 MB |
| Submission Date | 2026-10-20T05:48:40.875Z |
| Platform | leetcode |

## Problem Statement

<p>Given <code>n</code> pairs of parentheses, write a function to <em>generate all combinations of well-formed parentheses</em>.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>
<pre><strong>Input:</strong> n = 3
<strong>Output:</strong> ["((()))","(()())","(())()","()(())","()()()"]
</pre><p>
```

**Example 2:**

```
</p>
<pre><strong>Input:</strong> n = 1
<strong>Output:</strong> ["()"]
</pre>
<p>&nbsp;</p>
```

## Constraints

- <code>1 &lt;= n &lt;= 8</code>

## Solution

```py
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        def check(par):
            arr=[]
            for i in par:
                if(len(arr)==0):
                    arr.append(i)
                    continue
                if(arr[-1]=='(' and i==')'):
                    arr.pop()
                else:
                    arr.append(i)
            if(len(arr)==0):
                return True
            else:
                return False
                        
        ans = []
        bracks=[]
        string="()"

        def back(arr,string):
            if(len(arr)==n*2):
                if(check(arr)):
                    ans.append("".join(arr))
                return
            for i in string:
                arr.append(i)
                back(arr,string)
                arr.pop()
        back([],string)

        return ans
```

[View on LeetCode](https://leetcode.com/problems/generate-parentheses/)
