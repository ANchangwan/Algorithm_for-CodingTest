import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

start = int(input())
graph = [[] for _ in range(n+1)]
n,m = map(int, input().split())
distance = [INF] * (n + 1)

for i in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

def dijstra(start):
    q = []

    heapq.heappush(q,(0,start))
    distance[start] = 0
    for i in graph[start]:
        dist, now = heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijstra(start)

for i in range(n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])