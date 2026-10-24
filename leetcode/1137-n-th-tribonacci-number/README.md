# 1137. N-th Tribonacci Number

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen) ![Topic](https://img.shields.io/badge/Topic-Math-blue) ![Topic](https://img.shields.io/badge/Topic-Dynamic_Programming-blue) ![Topic](https://img.shields.io/badge/Topic-Memoization-blue) ![Language](https://img.shields.io/badge/Language-python3-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 0 ms |
| Memory | 19.1 MB |
| Submission Date | 2026-10-24T07:44:04.207Z |
| Platform | leetcode |

## Problem Statement

<p>The Tribonacci sequence T<sub>n</sub> is defined as follows:&nbsp;</p>

<p>T<sub>0</sub> = 0, T<sub>1</sub> = 1, T<sub>2</sub> = 1, and T<sub>n+3</sub> = T<sub>n</sub> + T<sub>n+1</sub> + T<sub>n+2</sub> for n &gt;= 0.</p>

<p>Given <code>n</code>, return the value of T<sub>n</sub>.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>

<pre>
<strong>Input:</strong> n = 4
<strong>Output:</strong> 4
<strong>Explanation:</strong>
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
</pre>

<p>
```

**Example 2:**

```
</p>

<pre>
<strong>Input:</strong> n = 25
<strong>Output:</strong> 1389537
</pre>

<p>&nbsp;</p>
```

## Constraints

- <code>0 &lt;= n &lt;= 37</code>
- The answer is guaranteed to fit within a 32-bit integer, ie. <code>answer &lt;= 2^31 - 1</code>.

## Solution

```py
class Solution:
    def tribonacci(self, n: int) -> int:
        arr=[-1]*(n+1)
        def transv(n):
            if n == 0:
                return 0
            elif n == 1 or n == 2:
                return 1

            elif arr[n] != -1:
                return arr[n]
            else:
                arr[n] = transv(n-3) + transv(n-2) + transv(n-1)
                return arr[n]

        return transv(n)

```

[View on LeetCode](https://leetcode.com/problems/n-th-tribonacci-number/)
