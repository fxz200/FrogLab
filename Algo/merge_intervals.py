# 給你一個由「區間」組成的列表 intervals，每個區間為 [start, end]，
# 請你合併所有有重疊的區間，回傳一個新的區間列表。
# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]

def dev_merge_intervals(intervals):
    merge_intervals=[]
    intervals.sort()
    merge=0
    current = intervals[0]
    for i in range(1,len(intervals)):
        if merge==1:
            merge=0
        elif current[1]>=intervals[i][0]:
            merge_intervals.append([intervals[i-1][0],intervals[i][1]])
            merge=1
        else: merge_intervals.append(current)
        current=intervals[i]
    if current[1]!=merge_intervals[-1][1]:
        merge_intervals.append(current)
    return merge_intervals

def merge_intervals(intervals):
    intervals.sort()
    merged = [intervals[0]]
    for curr in intervals[1:]:
        pre=merged[-1] 
        if curr[0] <= pre[1]:
            pre[1]=max(pre[1],curr[1]) #取最大 避免[[1,5],[2,3]]
        else : merged.append(curr)
    return merged

#print(merge_intervals([[1,3],[2,6],[8,10],[15,18]]))
#print(merge_intervals([[1,4],[4,7]]))
print(merge_intervals([[1,4],[4,7],[6,9]]))
print(merge_intervals([[1,5], [2,3], [4,6]]))