import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n,m,c = map(int, input().split()) # n 도시의 개수, m 통로의 개수, c 출발 위치

graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(n+1):
    x,y,z = map(int,input().split())
    graph[x].append((y,z)) # x -> y, 전달 시간

def dijstra(c):
    q = []
    heapq.heappush(q,(0,c))
    distance[c] = 0

    while q:
        dist, now = heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = i[1] + dist
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijstra(c)

count = 0
max_distance = 0

for d in distance:
    if d != INF:
        count += 1
        max_distance = max(max_distance,d)


print(count-1,max_distance)