class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        largest = -1

        for i in range(len(arr) - 1, -1, -1):

            current = arr[i]

            arr[i] = largest

            if current > largest:
                largest = current

        return arr