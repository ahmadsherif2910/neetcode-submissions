class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in range(len(matrix)):
            if target <= matrix[row][-1]:
                nums = matrix[row]
                i = 0   
                j=len(nums)-1
                while i<=j:
                    m=((j-i)//2)+i
                    print(i,j,m)
                    if nums[m]==target:
                        return True
                    elif nums[m]<target:
                        i=m+1
                    elif nums[m]>target:
                        j=m-1
                return False
        return False