class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        prefix = defaultdict(int)
        for num in nums: 
            if not prefix[num]:
                prefix[num] = prefix[num - 1] + prefix[num + 1] + 1
                prefix[num - prefix[num - 1]] = prefix[num]
                prefix[num + prefix[num + 1]] = prefix[num] 
                longest = max(longest, prefix[num])

        return longest



                
                