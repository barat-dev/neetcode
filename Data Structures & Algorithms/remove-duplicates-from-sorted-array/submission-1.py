class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r, n = 0, 0, len(nums)

        while r < n:
            nums[l] = nums[r]
            while r < n and nums[l] == nums[r]:
                r += 1
            l+=1
        return l
