class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i, j = 0, 0
        arr = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                arr.append(nums1[i])
                i += 1
            else:
                arr.append(nums2[j])
                j += 1
        arr.extend(nums1[i:])
        arr.extend(nums2[j:])
        res = len(arr)
        if res % 2 != 0:
            k = res // 2
            return arr[k]
        else:
            k = res // 2
            return ((arr[k-1] + arr[k]) / 2.0)