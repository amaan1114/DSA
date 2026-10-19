# 7. Reverse Integer

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Topic](https://img.shields.io/badge/Topic-Math-blue) ![Language](https://img.shields.io/badge/Language-python3-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 1 ms |
| Memory | 19.2 MB |
| Submission Date | 2026-10-19T06:29:33.328Z |
| Platform | leetcode |

## Problem Statement

<p>Given a signed 32-bit integer <code>x</code>, return <code>x</code><em> with its digits reversed</em>. If reversing <code>x</code> causes the value to go outside the signed 32-bit integer range <code>[-2<sup>31</sup>, 2<sup>31</sup> - 1]</code>, then return <code>0</code>.</p>

<p><strong>Assume the environment does not allow you to store 64-bit integers (signed or unsigned).</strong></p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>

<pre>
<strong>Input:</strong> x = 123
<strong>Output:</strong> 321
</pre>

<p>
```

**Example 2:**

```
</p>

<pre>
<strong>Input:</strong> x = -123
<strong>Output:</strong> -321
</pre>

<p>
```

**Example 3:**

```
</p>

<pre>
<strong>Input:</strong> x = 120
<strong>Output:</strong> 21
</pre>

<p>&nbsp;</p>
```

## Constraints

- <code>-2<sup>31</sup> &lt;= x &lt;= 2<sup>31</sup> - 1</code>

## Solution

```py
class Solution:
    def reverse(self, x: int) -> int:
        ans=0
        xcop = x
        x = abs(x)
        while x>0:
            lastval = x%10
            ans=ans*10+lastval
            x//=10
        if(xcop<0):
            if(-ans<-2147483648):
                return 0
            return -ans
        if(ans>2147483647):
            return 0
        return ans




```

[View on LeetCode](https://leetcode.com/problems/reverse-integer/)
