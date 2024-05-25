nums1 = [1,2,3]
m = 3
nums2 = [2,5,6]
n = 3

def merge(nums1, nums2):
    m = 3
    n = 3
    i = 0
    j = 0
    k = 0
    ans = [0]*(len(nums1) + len(nums2))
    
    while i < m and j < n:
        if nums1[i] < nums2[j]:
            ans[k] = nums1[i]
            i += 1
            k += 1
        else:
            ans[k] = nums2[j]
            k += 1
            j += 1
    
    while i < m:
        ans[k] = nums1[i]
        i += 1
        k += 1
    
    while j < n:
        ans[k] = nums2[j]
        j += 1
        k += 1
    
    return ans
    

print(merge(nums1, nums2))