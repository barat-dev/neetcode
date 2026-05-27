class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        res = []
        
        for i in range(len(nums)):
            if nums[i] in res:
                continue
            else:
                res.append(nums[i])
        

        k = len(res)
        nums[:k] = res
        return k