def findDuplicate(nums):
       
    mp = {}
    for i in nums:
        mp[i] = mp.get(i, 0)+1
        
    for key, value in mp.items():
        if value> 1:
            return key
def repeatedNumber(A):
    ans = []
        
    x = findDuplicate(A)
    ans.append(x)
    arr = list(set(A))
    print(arr)
    
    a = len(A)
    print(a)
    tot = (a*(a+1))//2
    print(tot)
    z = tot - sum(arr)
    ans.append(z)
    return ans

arr = [3, 1 ,2 ,5, 3]
print(repeatedNumber(arr)) 

       
        
       