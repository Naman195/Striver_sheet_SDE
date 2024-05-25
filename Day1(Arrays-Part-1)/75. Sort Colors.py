# nums = [2,0,2,1,1,0]
nums = [1]

def sortArr(nums):
    n = len(nums)
    zero = 0
    one = 0
    two = 0
    
    for i in nums:
        if i == 0:
            zero += 1
        
        elif i == 1:
            one += 1
        else:
            two += 1
    
    for i in range(n):
        while zero:
            nums[i] = 0
            zero -= 1
            i += 1
        while one:
            nums[i] = 1
            one -= 1
            i += 1
        while two:
            nums[i] = 2
            two -= 1
            i += 1
    print(nums)
        

sortArr(nums)        