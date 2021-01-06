import sys
import time

n, k = map(int,sys.stdin.readline().split())
count = 0

while n>=k:
    while n % k !=0:
        n-=1
        count += 1
    n //= k
    count += 1





print(count)
