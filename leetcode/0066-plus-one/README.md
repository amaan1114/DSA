# 66. Plus One

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Topic](https://img.shields.io/badge/Topic-Math-blue) ![Language](https://img.shields.io/badge/Language-python3-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 0 ms |
| Memory | 19 MB |
| Submission Date | 2026-10-26T07:37:47.520Z |
| Platform | leetcode |

## Problem Statement

<p>You are given a <strong>large integer</strong> represented as an integer array <code>digits</code>, where each <code>digits[i]</code> is the <code>i<sup>th</sup></code> digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading <code>0</code>&#39;s.</p>

<p>Increment the large integer by one and return <em>the resulting array of digits</em>.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>

<pre>
<strong>Input:</strong> digits = [1,2,3]
<strong>Output:</strong> [1,2,4]
<strong>Explanation:</strong> The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
</pre>

<p>
```

**Example 2:**

```
</p>

<pre>
<strong>Input:</strong> digits = [4,3,2,1]
<strong>Output:</strong> [4,3,2,2]
<strong>Explanation:</strong> The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
</pre>

<p>
```

**Example 3:**

```
</p>

<pre>
<strong>Input:</strong> digits = [9]
<strong>Output:</strong> [1,0]
<strong>Explanation:</strong> The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
</pre>

<p>&nbsp;</p>
```

## Constraints

- <code>1 &lt;= digits.length &lt;= 100</code>
- <code>0 &lt;= digits[i] &lt;= 9</code>
- <code>digits</code> does not contain any leading <code>0</code>&#39;s.

## Solution

```py
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        ans=[]
        digit=0
        for i in digits:
            digit+=i
            digit = digit*10
        ansval = (digit//10)+1
        while ansval!=0:
            ans.append(ansval%10)
            ansval//=10
        return ans[::-1]

```

[View on LeetCode](https://leetcode.com/problems/plus-one/)
