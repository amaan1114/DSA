# 11. Container With Most Water

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Topic](https://img.shields.io/badge/Topic-Two_Pointers-blue) ![Topic](https://img.shields.io/badge/Topic-Greedy-blue) ![Language](https://img.shields.io/badge/Language-python3-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 52 ms |
| Memory | 29.6 MB |
| Submission Date | 2026-10-20T05:13:47.162Z |
| Platform | leetcode |

## Problem Statement

<p>You are given an integer array <code>height</code> of length <code>n</code>. There are <code>n</code> vertical lines drawn such that the two endpoints of the <code>i<sup>th</sup></code> line are <code>(i, 0)</code> and <code>(i, height[i])</code>.</p>

<p>Find two lines that together with the x-axis form a container, such that the container contains the most water.</p>

<p>Return <em>the maximum amount of water a container can store</em>.</p>

<p><strong>Notice</strong> that you may not slant the container.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>
<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg" style="width: 600px; height: 287px;" />
<pre>
<strong>Input:</strong> height = [1,8,6,2,5,4,8,3,7]
<strong>Output:</strong> 49
<strong>Explanation:</strong> The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
</pre>

<p>
```

**Example 2:**

```
</p>

<pre>
<strong>Input:</strong> height = [1,1]
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
```

## Constraints

- <code>n == height.length</code>
- <code>2 &lt;= n &lt;= 10<sup>5</sup></code>
- <code>0 &lt;= height[i] &lt;= 10<sup>4</sup></code>

## Solution

```py
class Solution:
    def maxArea(self, height: list[int]) -> int:
        max1 = 0
        low=0
        high = len(height)-1
        while low<high:
            arr = (high-low)*min(height[low],height[high])
            if(arr>max1):
                max1=arr
            if(height[low]<height[high]):
                low+=1
            else:
                high-=1
        return max1
        
```

[View on LeetCode](https://leetcode.com/problems/container-with-most-water/)
