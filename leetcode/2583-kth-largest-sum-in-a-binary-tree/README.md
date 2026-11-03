# 2583. Kth Largest Sum in a Binary Tree

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Topic](https://img.shields.io/badge/Topic-Tree-blue) ![Topic](https://img.shields.io/badge/Topic-Breadth--First_Search-blue) ![Topic](https://img.shields.io/badge/Topic-Sorting-blue) ![Topic](https://img.shields.io/badge/Topic-Binary_Tree-blue) ![Language](https://img.shields.io/badge/Language-python3-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 241 ms |
| Memory | 77.6 MB |
| Submission Date | 2026-11-03T09:30:13.333Z |
| Platform | leetcode |

## Problem Statement

<p>You are given the <code>root</code> of a binary tree and a positive integer <code>k</code>.</p>

<p>The <strong>level sum</strong> in the tree is the sum of the values of the nodes that are on the <strong>same</strong> level.</p>

<p>Return<em> the </em><code>k<sup>th</sup></code><em> <strong>largest</strong> level sum in the tree (not necessarily distinct)</em>. If there are fewer than <code>k</code> levels in the tree, return <code>-1</code>.</p>

<p><strong>Note</strong> that two nodes are on the same level if they have the same distance from the root.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/12/14/binaryytreeedrawio-2.png" style="width: 301px; height: 284px;" />
<pre>
<strong>Input:</strong> root = [5,8,9,2,1,3,7,4,6], k = 2
<strong>Output:</strong> 13
<strong>Explanation:</strong> The level sums are the following:
- Level 1: 5.
- Level 2: 8 + 9 = 17.
- Level 3: 2 + 1 + 3 + 7 = 13.
- Level 4: 4 + 6 = 10.
The 2<sup>nd</sup> largest level sum is 13.
</pre>

<p>
```

**Example 2:**

```
</p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/12/14/treedrawio-3.png" style="width: 181px; height: 181px;" />
<pre>
<strong>Input:</strong> root = [1,2,null,3], k = 1
<strong>Output:</strong> 3
<strong>Explanation:</strong> The largest level sum is 3.
</pre>

<p>&nbsp;</p>
```

## Constraints

- The number of nodes in the tree is <code>n</code>.
- <code>2 &lt;= n &lt;= 10<sup>5</sup></code>
- <code>1 &lt;= Node.val &lt;= 10<sup>6</sup></code>
- <code>1 &lt;= k &lt;= n</code>

## Solution

```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: TreeNode | None, k: int) -> int:
        arr = []
        def dfs(node,l):
            if(node == None):
                return
            if(len(arr)>l):
                arr[l]+=node.val
            else:
                arr.append(node.val)
            dfs(node.left,l+1)
            dfs(node.right,l+1)
        dfs(root,0)
        arr.sort()
        if(len(arr)>=k):
            return arr[-k]
        else:
            return -1
        


            
```

[View on LeetCode](https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/)
