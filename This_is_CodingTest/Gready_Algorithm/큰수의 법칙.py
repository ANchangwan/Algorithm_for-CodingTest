import sys

N,M,K = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))
result = 0

array.sort()
first = array[N-1]
second = array[N-2]

while True:
    for i in range(K):
        if M == 0:
            break
        result += first
        M -= 1
    if M ==0:
        break
    result += second
    M -= 1
print(result)

