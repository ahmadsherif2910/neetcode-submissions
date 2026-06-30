class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = len(numbers)
        a = 0
        b=l-1

        while a <= b:
            if numbers[a]+numbers[b]==target:
                return [a+1,b+1]
            elif numbers[a]>numbers[b]:
                a+=1
            elif numbers[b]>numbers[a]:
                b-=1
            elif a==b:
                if numbers[a]<numbers[b+1]:
                    a+=1
                    b=l-1
                elif numbers[b]<numbers[a-1]:
                    a=0
                    b-=1


        