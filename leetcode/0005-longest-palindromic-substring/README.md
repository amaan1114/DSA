# 5. Longest Palindromic Substring

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Topic](https://img.shields.io/badge/Topic-Two_Pointers-blue) ![Topic](https://img.shields.io/badge/Topic-String-blue) ![Topic](https://img.shields.io/badge/Topic-Dynamic_Programming-blue) ![Topic](https://img.shields.io/badge/Topic-Manacher-blue) ![Language](https://img.shields.io/badge/Language-python3-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 229 ms |
| Memory | 19.2 MB |
| Submission Date | 2026-10-19T06:19:30.182Z |
| Platform | leetcode |

## Problem Statement

<p>Given a string <code>s</code>, return <em>the longest</em> <span data-keyword="palindromic-string"><em>palindromic</em></span> <span data-keyword="substring-nonempty"><em>substring</em></span> in <code>s</code>.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>

<pre>
<strong>Input:</strong> s = &quot;babad&quot;
<strong>Output:</strong> &quot;bab&quot;
<strong>Explanation:</strong> &quot;aba&quot; is also a valid answer.
</pre>

<p>
```

**Example 2:**

```
</p>

<pre>
<strong>Input:</strong> s = &quot;cbbd&quot;
<strong>Output:</strong> &quot;bb&quot;
</pre>

<p>&nbsp;</p>
```

## Constraints

- <code>1 &lt;= s.length &lt;= 1000</code>
- <code>s</code> consist of only digits and English letters.

## Solution

```py
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(s,i,j):
            while i>=0 and j<len(s) and s[i]==s[j]:
                i-=1
                j+=1
            return s[i+1:j]
    
        max1=0
        ans=''
        if(len(s)==1):
            ans=s
            return ans
        for i in range(len(s)-1):
            a = expand(s,i,i)
            b = expand(s,i,i+1)
            if len(a) > len(ans):
                ans = a
            if len(b) > len(ans):
                ans = b
        return ans
        


        
```

[View on LeetCode](https://leetcode.com/problems/longest-palindromic-substring/)
