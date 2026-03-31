class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search(numbers,target):
            left = 0
            right = len(numbers) - 1

            while left <= right:
                mid = (right + left) // 2
                # print(f"{left}, {mid}, {right}")
                if numbers[mid] == target:
                    return True

                elif numbers[mid] > target:
                    # print("update right")
                    right = mid - 1

                elif numbers[mid] < target:
                    # print("updating left")
                    left = mid + 1

                # mid = (right - left) // 2

            return False
        # iterate in the matrix to find all rows: O(m)
        row = 0
        
        Found = False

        while not Found and row < len(matrix):
            val = search(matrix[row],target)
            Found = val
            row += 1
        return Found



        





