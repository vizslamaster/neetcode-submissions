class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_dictionary = {}

        for num in nums:
            if num in my_dictionary:
                return True
            else:
                my_dictionary[num] = 1
        
        return False