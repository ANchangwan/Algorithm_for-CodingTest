#만약 M의 크기가 100억 이상이라면
import sys
n,m,k = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))

first = array[n-1]
second = array[n-2]

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k+1))*k
count += M % (K + 1)

result = 0
result += (count) * first # 가장 큰 수 더하기
result += (m - count) * second # 두번째로 큰 수 더하기

print(result)