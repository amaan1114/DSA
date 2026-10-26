# 567. Permutation in String

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Topic](https://img.shields.io/badge/Topic-Hash_Table-blue) ![Topic](https://img.shields.io/badge/Topic-Two_Pointers-blue) ![Topic](https://img.shields.io/badge/Topic-String-blue) ![Topic](https://img.shields.io/badge/Topic-Sliding_Window-blue) ![Language](https://img.shields.io/badge/Language-python3-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 1664 ms |
| Memory | 19.3 MB |
| Submission Date | 2026-10-26T03:56:11.088Z |
| Platform | leetcode |

## Problem Statement

<p>Given two strings <code>s1</code> and <code>s2</code>, return <code>true</code> if <code>s2</code> contains a <span data-keyword="permutation-string">permutation</span> of <code>s1</code>, or <code>false</code> otherwise.</p>

<p>In other words, return <code>true</code> if one of <code>s1</code>&#39;s permutations is the substring of <code>s2</code>.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>

<pre>
<strong>Input:</strong> s1 = &quot;ab&quot;, s2 = &quot;eidbaooo&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> s2 contains one permutation of s1 (&quot;ba&quot;).
</pre>

<p>
```

**Example 2:**

```
</p>

<pre>
<strong>Input:</strong> s1 = &quot;ab&quot;, s2 = &quot;eidboaoo&quot;
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
```

## Constraints

- <code>1 &lt;= s1.length, s2.length &lt;= 10<sup>4</sup></code>
- <code>s1</code> and <code>s2</code> consist of lowercase English letters.

## Solution

```py
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        arr=[0]*26
        st=0
        end = len(s1)
        for i in s1:
            arr[ord(i)-97]+=1
        while end<=len(s2):
            s3 = s2[st:end]
            temp = [0] * 26
            for i in s3:
                temp[ord(i)-97]+=1
            if(arr==temp):
                return True
            st +=1
            end +=1
     
        return False


```

[View on LeetCode](https://leetcode.com/problems/permutation-in-string/)
