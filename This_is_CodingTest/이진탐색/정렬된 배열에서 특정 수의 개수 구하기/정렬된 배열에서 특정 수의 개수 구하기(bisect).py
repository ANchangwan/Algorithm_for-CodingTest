# 1
from bisect import bisect_left,bisect_right

def count_by_range(array,left_value,right_value):
    right_index = bisect_right(array,right_value)
    left_index = bisect_left(array,left_value)
    return right_index - left_index


n, x = map(int, input().split())
array = list(map(int,input().split()))

count = count_by_range(array,x,x)

if count == 0:
    print(-1)
else:
    print(count)
    
    

# 2
from bisect import bisect_right, bisect_left
n, target = map(int, input().split())
data = list(map(int, input().split()))

right = bisect_right(data, target)
left = bisect_left(data, target)
result = right - left

if result:
    print(result)
else:
    print(-1)

