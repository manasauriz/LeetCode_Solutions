class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1, -1]
        l, r = 0, len(nums) - 1
        while l <= r:
            half = r - l // 2
            if nums[half] < target:
                l = half + 1
            elif nums[half] > target:
                r = half - 1
            else:
                for lh in range(half, -1, -1):
                    if nums[lh] != target: break
                    res[0] = lh
                for rh in range(half, len(nums)):
                    if nums[rh] != target: break
                    res[1] = rh
                break
        return res