array = [5,4,3,2,1]

def mergeSort(arr, low, high):
    cnt = 0
    if low >= high:
        return cnt
    
    mid = (low  + high)//2
    cnt += mergeSort(arr, low, mid)
    cnt += mergeSort(arr, mid+1, high)
    cnt += merge(arr, low, mid, high)
    return cnt


def merge(arr, low, mid, high):
    temp = []
    cnt = 0
    left = low
    right = mid+1
    
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1
            cnt += (mid - left + 1)
    
    while left <= mid:
        temp.append(arr[left])
        left += 1
    
    while right <= high:
        temp.append(arr[right])
        right += 1
    
    for i in range(low, high+1):
        arr[i] = temp[i-low]
    
    return cnt
        

def countInversion(arr):
    return mergeSort(array, 0, len(arr)-1)

    


print(countInversion(array))

    