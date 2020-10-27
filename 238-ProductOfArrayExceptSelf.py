# Time Complexity O(n), where n is len(nums)
# It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array)
# fits in a 32 bit integer
# Space Complexity 0(1)
class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        output = []
        
        # para cada num em nums, multiplicar os anteriores a num
        p = 1
        for num in nums:
            output.append(p)
            p *= num
        
        # para cada outnum em output, multiplicar os posteriores a outnum
        p = 1
        for outnum in range(n-1,-1,-1):
            output[outnum] *= p
            p *= nums[outnum]
        
        return output
