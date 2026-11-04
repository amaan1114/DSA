# 72. Edit Distance

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Topic](https://img.shields.io/badge/Topic-String-blue) ![Topic](https://img.shields.io/badge/Topic-Dynamic_Programming-blue) ![Language](https://img.shields.io/badge/Language-python3-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 45 ms |
| Memory | 26.8 MB |
| Submission Date | 2026-11-04T08:32:23.470Z |
| Platform | leetcode |

## Problem Statement

<p>Given two strings <code>word1</code> and <code>word2</code>, return <em>the minimum number of operations required to convert <code>word1</code> to <code>word2</code></em>.</p>

<p>You have the following three operations permitted on a word:</p>

<ul>
	<li>Insert a character</li>
	<li>Delete a character</li>
	<li>Replace a character</li>
</ul>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>

<pre>
<strong>Input:</strong> word1 = &quot;horse&quot;, word2 = &quot;ros&quot;
<strong>Output:</strong> 3
<strong>Explanation:</strong> 
horse -&gt; rorse (replace &#39;h&#39; with &#39;r&#39;)
rorse -&gt; rose (remove &#39;r&#39;)
rose -&gt; ros (remove &#39;e&#39;)
</pre>

<p>
```

**Example 2:**

```
</p>

<pre>
<strong>Input:</strong> word1 = &quot;intention&quot;, word2 = &quot;execution&quot;
<strong>Output:</strong> 5
<strong>Explanation:</strong> 
intention -&gt; inention (remove &#39;t&#39;)
inention -&gt; enention (replace &#39;i&#39; with &#39;e&#39;)
enention -&gt; exention (replace &#39;n&#39; with &#39;x&#39;)
exention -&gt; exection (replace &#39;n&#39; with &#39;c&#39;)
exection -&gt; execution (insert &#39;u&#39;)
</pre>

<p>&nbsp;</p>
```

## Constraints

- <code>0 &lt;= word1.length, word2.length &lt;= 500</code>
- <code>word1</code> and <code>word2</code> consist of lowercase English letters.

## Solution

```py
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp={}
        def f(i,j):
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i
            if((i,j) in dp):
                return dp[(i,j)]
            if word1[i] == word2[j]:
                dp[(i,j)] = f(i + 1, j + 1)
            else:
                insert = 1 + f(i, j + 1)

                delete = 1 + f(i + 1, j)

                replace = 1 + f(i + 1, j + 1)

                dp[(i,j)] = min(insert, delete, replace)
            return dp[(i,j)]
        return f(0, 0)





```

[View on LeetCode](https://leetcode.com/problems/edit-distance/)
