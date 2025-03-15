class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) < len(nums2):
            small = nums1
            big = nums2
        else:
            small = nums2
            big = nums1

        first, second = 0, 0
        merged = [] 
        while (first < len(small)) and (second < len(big)):
            if small[first] < big[second]:
                merged.append(small[first])
                first += 1
            else:
                merged.append(big[second])
                second += 1
        merged = merged + small[first:]
        merged = merged + big[second:]

        median = merged[len(merged)//2] if len(merged) % 2 != 0 else (merged[len(merged)//2] + merged[(len(merged)//2) - 1]) / 2
        return float(median)