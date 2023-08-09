class Solution:
    def singleNumber(self, nums: list[int]) -> int: 
        nums = sorted(nums)
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                i += 1
            else:
                return nums[i]
               
        return nums[0]
    
    
a = Solution()
print(a.singleNumber(nums = [2,2,1]))
print(a.singleNumber(nums = [4,1,2,1,2]))
print(a.singleNumber(nums = [1]))
