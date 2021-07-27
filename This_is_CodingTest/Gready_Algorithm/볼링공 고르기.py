
# 1
import sys
import time



n, m = map(int, sys.stdin.readline().split())
ball = list(map(int, sys.stdin.readline().split()))

count = 0
ball.sort()

for x in ball:
    for y in ball:
        if x != y and x <= y:
            count += 1

end = time.time()

print(end-start)
print(count)

# 2
import sys

n, m = map(int,sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))

# 1부터 10까지의 무게를 담을 수 있는 리스트
array = [0] * 11

for x in data:
    # 각 무게에 해당하는 볼링공의 개수 카운트
    array[x] += 1

result = 0
# 1부터 m까지의 각 무게에 대하여 처리
for i in range(1,m+1):
    n -= array[i]
    result += array[i] * n

print(result)

# 3
from collections import Counter

n,m = map(int, input().split())

data = list(map(int, input().split()))

num_dict = Counter(data)

result = 0
for i in num_dict.keys():
    n-= num_dict[i]
    result += num_dict[i] * n

print(result)



