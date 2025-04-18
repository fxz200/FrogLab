# tickets = [5,1,1,1], k = 0 #8
# tickets = [2,3,2], k = 2 #6

#[2,3,2] => [1,2,1] => [0,1,0]
# 3 + 3
#[5,1,1,1] => [4,0,0,0] => [3,0,0,0] => [2,0,0,0] => [1,0,0,0] => [0,0,0,0,0]
#   4+1+1+1+1


def timeRequiredToBuy(tickets,k) -> int:
    count=0
    for i in range(len(tickets)):
        if i<=k:
            count+= min(tickets[i],tickets[k])
        else:
            count += min(tickets[i],tickets[k]-1)
    return count


print(timeRequiredToBuy([5,1,1,1],0))#8
print(timeRequiredToBuy([2,3,2],2))#6