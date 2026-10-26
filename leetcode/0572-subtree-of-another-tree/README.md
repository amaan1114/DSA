# 572. Subtree of Another Tree

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen) ![Topic](https://img.shields.io/badge/Topic-Tree-blue) ![Topic](https://img.shields.io/badge/Topic-Depth--First_Search-blue) ![Topic](https://img.shields.io/badge/Topic-String_Matching-blue) ![Topic](https://img.shields.io/badge/Topic-Binary_Tree-blue) ![Topic](https://img.shields.io/badge/Topic-Hash_Function-blue) ![Language](https://img.shields.io/badge/Language-python3-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 72 ms |
| Memory | 20.6 MB |
| Submission Date | 2026-10-26T04:27:31.872Z |
| Platform | leetcode |

## Problem Statement

<p>Given the roots of two binary trees <code>root</code> and <code>subRoot</code>, return <code>true</code> if there is a subtree of <code>root</code> with the same structure and node values of<code> subRoot</code> and <code>false</code> otherwise.</p>

<p>A subtree of a binary tree <code>tree</code> is a tree that consists of a node in <code>tree</code> and all of this node&#39;s descendants. The tree <code>tree</code> could also be considered as a subtree of itself.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/28/subtree1-tree.jpg" style="width: 532px; height: 400px;" />
<pre>
<strong>Input:</strong> root = [3,4,5,1,2], subRoot = [4,1,2]
<strong>Output:</strong> true
</pre>

<p>
```

**Example 2:**

```
</p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/28/subtree2-tree.jpg" style="width: 502px; height: 458px;" />
<pre>
<strong>Input:</strong> root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
```

## Constraints

- The number of nodes in the <code>root</code> tree is in the range <code>[1, 2000]</code>.
- The number of nodes in the <code>subRoot</code> tree is in the range <code>[1, 1000]</code>.
- <code>-10<sup>4</sup> &lt;= root.val &lt;= 10<sup>4</sup></code>
- <code>-10<sup>4</sup> &lt;= subRoot.val &lt;= 10<sup>4</sup></code>

## Solution

```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        def isIdentical(s,t):
            if s is None and t is None:
                return True
            if s is None or t is None:
                return False

            return (s.val == t.val and
                    isIdentical(s.left, t.left) and
                    isIdentical(s.right, t.right))
        if subRoot is None:
            return True
        if root is None:
            return False

        if isIdentical(root, subRoot):
            return True

        return (self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))

```

[View on LeetCode](https://leetcode.com/problems/subtree-of-another-tree/)
