import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)
start = 1
n,m = map(int,input().split())
graph = [[] * (n+1) for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append((b,1))
    graph[b].append((a,1))

def dijstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijstra(start)


hide_on_bush = 0
max_dist = 0
result = []


for i in range(1,n+1):
    if max_dist < distance[i]:
        hide_on_bush = i
        max_dist = distance[i]
        result = [hide_on_bush]
    elif max_dist == distance[i]:
        result.append(i)


print(hide_on_bush,max_dist,len(result))








