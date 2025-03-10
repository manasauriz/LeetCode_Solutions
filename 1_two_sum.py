class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tups = sorted(enumerate(nums), key = lambda x: x[1])
        first, last = 0, len(tups) - 1
        while True:
            sum = tups[first][1] + tups[last][1]
            if sum == target:
                return [tups[first][0], tups[last][0]]
            elif sum < target:
                first += 1
            elif sum > target:
                first = 0
                last -= 1

    def half(self, iter):
        l = len(iter)
        if l == 2:
            return 0
        if l == 3:
            return 1
        return int(l/2) if l % 2 == 0 else int((l - 1)/2)