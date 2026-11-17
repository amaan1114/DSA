# 621. Task Scheduler

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Topic](https://img.shields.io/badge/Topic-Hash_Table-blue) ![Topic](https://img.shields.io/badge/Topic-Greedy-blue) ![Topic](https://img.shields.io/badge/Topic-Sorting-blue) ![Topic](https://img.shields.io/badge/Topic-Heap_(Priority_Queue)-blue) ![Topic](https://img.shields.io/badge/Topic-Counting-blue) ![Language](https://img.shields.io/badge/Language-python3-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 167 ms |
| Memory | 20.8 MB |
| Submission Date | 2026-11-17T04:38:25.481Z |
| Platform | leetcode |

## Problem Statement

<p>You are given an array of CPU <code>tasks</code>, each labeled with a letter from A to Z, and a number <code>n</code>. Each CPU interval can be idle or allow the completion of one task. Tasks can be completed in any order, but there&#39;s a constraint: there has to be a gap of <strong>at least</strong> <code>n</code> intervals between two tasks with the same label.</p>

<p>Return the <strong>minimum</strong> number of CPU intervals required to complete all tasks.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>

<div class="example-block" style="
    border-color: var(--border-tertiary);
    border-left-width: 2px;
    color: var(--text-secondary);
    font-size: .875rem;
    margin-bottom: 1rem;
    margin-top: 1rem;
    overflow: visible;
    padding-left: 1rem;
">
<p><strong>Input:</strong> <span class="example-io" style="
    font-family: Menlo,sans-serif;
    font-size: 0.85rem;
">tasks = [&quot;A&quot;,&quot;A&quot;,&quot;A&quot;,&quot;B&quot;,&quot;B&quot;,&quot;B&quot;], n = 2</span></p>

<p><strong>Output:</strong> <span class="example-io" style="
font-family: Menlo,sans-serif;
font-size: 0.85rem;
">8</span></p>

<p><strong>Explanation:</strong> A possible sequence is: A -&gt; B -&gt; idle -&gt; A -&gt; B -&gt; idle -&gt; A -&gt; B.</p>

<p>After completing task A, you must wait two intervals before doing A again. The same applies to task B. In the 3<sup>rd</sup> interval, neither A nor B can be done, so you idle. By the 4<sup>th</sup> interval, you can do A again as 2 intervals have passed.</p>
</div>

<p>
```

**Example 2:**

```
</p>

<div class="example-block" style="
    border-color: var(--border-tertiary);
    border-left-width: 2px;
    color: var(--text-secondary);
    font-size: .875rem;
    margin-bottom: 1rem;
    margin-top: 1rem;
    overflow: visible;
    padding-left: 1rem;
">
<p><strong>Input:</strong> <span class="example-io" style="
    font-family: Menlo,sans-serif;
    font-size: 0.85rem;
">tasks = [&quot;A&quot;,&quot;C&quot;,&quot;A&quot;,&quot;B&quot;,&quot;D&quot;,&quot;B&quot;], n = 1</span></p>

<p><strong>Output:</strong> <span class="example-io" style="
    font-family: Menlo,sans-serif;
    font-size: 0.85rem;
">6</span></p>

<p><strong>Explanation:</strong> A possible sequence is: A -&gt; B -&gt; C -&gt; D -&gt; A -&gt; B.</p>

<p>With a cooling interval of 1, you can repeat a task after just one other task.</p>
</div>

<p>
```

**Example 3:**

```
</p>

<div class="example-block" style="
    border-color: var(--border-tertiary);
    border-left-width: 2px;
    color: var(--text-secondary);
    font-size: .875rem;
    margin-bottom: 1rem;
    margin-top: 1rem;
    overflow: visible;
    padding-left: 1rem;
">
<p><strong>Input:</strong> <span class="example-io" style="
    font-family: Menlo,sans-serif;
    font-size: 0.85rem;
">tasks = [&quot;A&quot;,&quot;A&quot;,&quot;A&quot;, &quot;B&quot;,&quot;B&quot;,&quot;B&quot;], n = 3</span></p>

<p><strong>Output:</strong> <span class="example-io" style="
    font-family: Menlo,sans-serif;
    font-size: 0.85rem;
">10</span></p>

<p><strong>Explanation:</strong> A possible sequence is: A -&gt; B -&gt; idle -&gt; idle -&gt; A -&gt; B -&gt; idle -&gt; idle -&gt; A -&gt; B.</p>

<p>There are only two types of tasks, A and B, which need to be separated by 3 intervals. This leads to idling twice between repetitions of these tasks.</p>
</div>

<p>&nbsp;</p>
```

## Constraints

- <code>1 &lt;= tasks.length &lt;= 10<sup>4</sup></code>
- <code>tasks[i]</code> is an uppercase English letter.
- <code>0 &lt;= n &lt;= 100</code>

## Solution

```py

from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:

        freq = Counter(tasks)

        heap = [-count for count in freq.values()]
        heapq.heapify(heap)

        queue = deque()

        time = 0

        while heap or queue:

            time += 1

            if heap:
                count = heapq.heappop(heap)
                count += 1  

                if count != 0:
                    queue.append([count, time + n])

            if queue and queue[0][1] == time:
                count, available_time = queue.popleft()
                heapq.heappush(heap, count)

        return time

```

[View on LeetCode](https://leetcode.com/problems/task-scheduler/)
