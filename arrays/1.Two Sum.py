class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_to_index = {}
        
        for index, num in enumerate(nums):
            remainder = target - num
            if remainder in num_to_index:
                return [num_to_index[remainder], index]
            
            num_to_index[num] = index
      