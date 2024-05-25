intervals = [[1,3],[2,6],[8,10],[15,18]]

def merge(intervals):
    intervals.sort(key = lambda x: x[0])
    prevInterval = intervals[0]
    res = []
    
    for i in range(1, len(intervals)):
        currInterval = intervals[i]
        if currInterval[0] <= prevInterval[1]:
            prevInterval[1] = max(currInterval[1], prevInterval[1])
        else:
            res.append(prevInterval)
            prevInterval = currInterval
    res.append(prevInterval)
    return res

print(merge(intervals))
            
        