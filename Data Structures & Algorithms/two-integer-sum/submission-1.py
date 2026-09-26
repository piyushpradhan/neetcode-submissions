class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted = []
        for i, num in enumerate(nums):
            sorted.append([num, i])
        
        sorted.sort()

        i, j = 0, len(nums) - 1
        while i < j:
            current = sorted[i][0] + sorted[j][0]
            if current == target:
                return [min(sorted[i][1], sorted[j][1]), max(sorted[i][1], sorted[j][1])]
            elif current < target: 
                i += 1
            else:
                j -= 1
        return []
