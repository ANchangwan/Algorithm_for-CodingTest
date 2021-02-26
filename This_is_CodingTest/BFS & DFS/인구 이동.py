from collections import deque

N,L,R = map(int, input().split()) # 맵 크기, 인구차이 L이상, R 이하

# 전체 나라의 정보(N * N)를 입력받기
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))


dx = [-1,0,1,0]
dy = [0,-1,0,1]

result = 0

# 특정 위치에서  출발하여 모든 연합을 체크한 뒤에 데이터 갱신
def process(x,y,index):
    # (x,y)의 위치와 연결된 나라(연합) 정보를 담는 리스트
    united = []
    united.append((x,y))

    # 너비 우선 탐색(BFS)을 위한 큐 자료구조 정의
    q = deque()
    q.append((x,y))
    union[x][y] = index # 현재 연합의 번호 할당
    summary = graph[x][y] # 현재 연합의 전체 인구 수
    count = 1 # 현재 연합의 국가 수
    # 큐가 빌 대까지 반복(BFS)
    while q:
        x,y = q.popleft()
        # 현재 위치에서 4가지 방향을 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 바로 옆에 있는 나라를 확인하여
            if 0 <= nx < N and 0 <= ny < N and union[nx][ny] == -1:
                # 옆에 있는 나라와 인구 차이가 L명 이상, R명 이하라면
                if L <= abs(graph[nx][ny] - graph[x][y]) <= R:
                    q.append((nx,ny))
                    # 연합에 추가
                    union[nx][ny] = index
                    summary += graph[nx][ny]
                    count +=1
                    united.append((nx,ny))
    for i, j in united:
        graph[i][j] = summary // count
    return count

total_count = 0

while True:
    union = [[-1] * N for _ in range(N)]
    index = 0
    for i in range(N):
        for j in range(N):
            if union[i][j] == -1:
                process(i,j,index)
                index += 1
    if index == N*N:
        break
    total_count +=1

print(total_count)