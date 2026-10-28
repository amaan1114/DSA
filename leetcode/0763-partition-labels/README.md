# 763. Partition Labels

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Topic](https://img.shields.io/badge/Topic-Hash_Table-blue) ![Topic](https://img.shields.io/badge/Topic-Two_Pointers-blue) ![Topic](https://img.shields.io/badge/Topic-String-blue) ![Topic](https://img.shields.io/badge/Topic-Greedy-blue) ![Language](https://img.shields.io/badge/Language-python3-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 3 ms |
| Memory | 19.4 MB |
| Submission Date | 2026-10-28T13:05:51.163Z |
| Platform | leetcode |

## Problem Statement

<p>You are given a string <code>s</code>. We want to partition the string into as many parts as possible so that each letter appears in at most one part. For example, the string <code>&quot;ababcc&quot;</code> can be partitioned into <code>[&quot;abab&quot;, &quot;cc&quot;]</code>, but partitions such as <code>[&quot;aba&quot;, &quot;bcc&quot;]</code> or <code>[&quot;ab&quot;, &quot;ab&quot;, &quot;cc&quot;]</code> are invalid.</p>

<p>Note that the partition is done so that after concatenating all the parts in order, the resultant string should be <code>s</code>.</p>

<p>Return <em>a list of integers representing the size of these parts</em>.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>

<pre>
<strong>Input:</strong> s = &quot;ababcbacadefegdehijhklij&quot;
<strong>Output:</strong> [9,7,8]
<strong>Explanation:</strong>
The partition is &quot;ababcbaca&quot;, &quot;defegde&quot;, &quot;hijhklij&quot;.
This is a partition so that each letter appears in at most one part.
A partition like &quot;ababcbacadefegde&quot;, &quot;hijhklij&quot; is incorrect, because it splits s into less parts.
</pre>

<p>
```

**Example 2:**

```
</p>

<pre>
<strong>Input:</strong> s = &quot;eccbbbbdec&quot;
<strong>Output:</strong> [10]
</pre>

<p>&nbsp;</p>
```

## Constraints

- <code>1 &lt;= s.length &lt;= 500</code>
- <code>s</code> consists of lowercase English letters.

## Solution

```py
class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        hasht = {}
        for i in range(len(s)):
            hasht[s[i]] = i
        ans=[]
        start=0
        end=0
        for i in range(len(s)):
            end = max(end, hasht[s[i]])

            if i == end:
                ans.append(end - start + 1)
                start = i + 1

        return ans
            

            
                




```

[View on LeetCode](https://leetcode.com/problems/partition-labels/)
