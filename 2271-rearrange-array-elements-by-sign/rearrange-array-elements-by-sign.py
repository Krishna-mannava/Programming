class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        num = [0]*n
        k,j = 1,0
        for i in range(n):
            if(nums[i]>0):
                num[j] = nums[i]
                j += 2
            else:
                num[k] = nums[i]
                k += 2
        return num

            
                