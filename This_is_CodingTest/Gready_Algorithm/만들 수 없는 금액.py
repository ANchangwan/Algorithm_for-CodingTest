import sys

N = map(int,sys.stdin.readline())
coin = list(map(int,sys.stdin.readline().split()))

coin.sort()

target = 1

for x in coin:
    if target < x:
        break
    target += x

print(target)
