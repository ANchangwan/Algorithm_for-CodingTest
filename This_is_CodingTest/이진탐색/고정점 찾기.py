def binary_search(array,start,end):
    if start > end:
        return None

    mid = (start + end) // 2

    if array[mid] == mid:
        return mid

    if array[mid] > mid:
        return binary_search(array,mid + 1, end)

    else:
        return binary_search(array,start, mid + 1)

n = int(input())
array = list(map(int,input().split()))

index = binary_search(array,0,n-1)

if index == None:
    print(-1)
else:
    print(index)

# bisect 활용
from bisect import bisect_right


def fixed_count(array, point):
    right_index = bisect_right(array, point)
    return right_index - 1


n = int(input())
array = list(map(int, input().split()))
for i in range(len(array)):
    index = fixed_count(array, i)
    if array[i] == i:
        result = i
        break
    else:
        result = -1
        break
print(result)