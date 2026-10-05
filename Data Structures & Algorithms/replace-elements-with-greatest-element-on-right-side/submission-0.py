class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        my_list = []
        for index in range(len(arr)):
            if index == len(arr) - 1:
                my_list.append(-1)
            else:
                my_list.append(max(arr[index + 1:]))
        
        return my_list