import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n,m = map(int, input().split())
parent = [0] * (n+1)

for i in range(1,n+1):
    parent[i] = i

edges = []
result = 0

for _ in range(m):
    x,y,z = map(int,input().split())
    edges.append((z,x,y))

edges.sort()
total = 0

for edge in edges:
    cost,x,y = edge
    total += cost
    if find_parent(parent,x) != find_parent(parent,y):
        union_parent(parent,x,y)
        result += cost

print(total - result)
