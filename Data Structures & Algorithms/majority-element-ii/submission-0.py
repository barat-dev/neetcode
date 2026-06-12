class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        result = []
        majority_count = len(nums) // 3
        for key, value in count.items():
            if value > majority_count :
                result.append(key)
        
        return result