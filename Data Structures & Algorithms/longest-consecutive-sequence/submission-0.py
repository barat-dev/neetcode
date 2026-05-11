class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums.sort()

        longest = 1
        consecutive = 1
        prev = nums[0]
        for i in range(1, len(nums)):
            if prev == nums[i]:
                continue # duplicate
            
            if (prev + 1) == nums[i]:
                consecutive += 1
            else:
                consecutive = 1

            longest = max(longest, consecutive)  
            prev = nums[i]

        return longest