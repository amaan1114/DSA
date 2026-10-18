# Runtime: 4 ms
# Memory: 19.4 MB

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
