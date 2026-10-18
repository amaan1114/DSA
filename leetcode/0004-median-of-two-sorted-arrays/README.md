# 4. Median of Two Sorted Arrays

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Topic](https://img.shields.io/badge/Topic-Binary_Search-blue) ![Topic](https://img.shields.io/badge/Topic-Divide_and_Conquer-blue) ![Language](https://img.shields.io/badge/Language-python3-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 4 ms |
| Memory | 19.4 MB |
| Submission Date | 2026-10-18T12:57:24.816Z |
| Platform | leetcode |

## Problem Statement

<p>Given two sorted arrays <code>nums1</code> and <code>nums2</code> of size <code>m</code> and <code>n</code> respectively, return <strong>the median</strong> of the two sorted arrays.</p>

<p>The overall run time complexity should be <code>O(log (m+n))</code>.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>

<pre>
<strong>Input:</strong> nums1 = [1,3], nums2 = [2]
<strong>Output:</strong> 2.00000
<strong>Explanation:</strong> merged array = [1,2,3] and median is 2.
</pre>

<p>
```

**Example 2:**

```
</p>

<pre>
<strong>Input:</strong> nums1 = [1,2], nums2 = [3,4]
<strong>Output:</strong> 2.50000
<strong>Explanation:</strong> merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
</pre>

<p>&nbsp;</p>
```

## Constraints

- <code>nums1.length == m</code>
- <code>nums2.length == n</code>
- <code>0 &lt;= m &lt;= 1000</code>
- <code>0 &lt;= n &lt;= 1000</code>
- <code>1 &lt;= m + n &lt;= 2000</code>
- <code>-10<sup>6</sup> &lt;= nums1[i], nums2[i] &lt;= 10<sup>6</sup></code>

## Solution

```py
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        low, high = 0, m

        while low <= high:
            mid1 = (low + high) // 2
            mid2 = (m + n + 1) // 2 - mid1

            if mid1 == 0:
                left1 = float('-inf')
            else:
                left1 = nums1[mid1 - 1]

            if mid1 == m:
                right1 = float('inf')
            else:
                right1 = nums1[mid1]

            if mid2 == 0:
                left2 = float('-inf')
            else:
                left2 = nums2[mid2 - 1]

            if mid2 == n:
                right2 = float('inf')
            else:
                right2 = nums2[mid2]

            if left1 <= right2 and left2 <= right1:
                if (m + n) % 2 == 0:
                    return (max(left1, left2) + min(right1, right2)) / 2
                else:
                    return float(max(left1, left2))

            elif left1 > right2:
                high = mid1 - 1
            else:
                low = mid1 + 1

```

[View on LeetCode](https://leetcode.com/problems/median-of-two-sorted-arrays/)
