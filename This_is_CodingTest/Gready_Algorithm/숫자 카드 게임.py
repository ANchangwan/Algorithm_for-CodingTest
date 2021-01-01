import sys
import time

m,n = map(int,sys.stdin.readline().split())
result = 0
card = []

for i in range(m):
        card.append(list(map(int,sys.stdin.readline().split())))
        min_value = min(card)

result = max(min_value)
print(result)
