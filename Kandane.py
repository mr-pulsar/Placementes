def maxSubArray(nums):
    max1= nums[0]    
    current= 0        
    for i in nums:
        current = max(i, current + i)
        max1 = max(max1, current)
    return max1
a=[1,2,3,-1]
print(maxSubArray(a))    