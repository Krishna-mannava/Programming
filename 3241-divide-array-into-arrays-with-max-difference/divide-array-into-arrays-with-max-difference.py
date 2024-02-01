class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        if(len(nums)<3):
            return []
        result = []
        nums.sort()
        for i in range(0,len(nums),3):
            if ((nums[i+2] - nums[i]) <= k):
                result.append(nums[i:i+3])
            else:
                return []
        return result
            
        