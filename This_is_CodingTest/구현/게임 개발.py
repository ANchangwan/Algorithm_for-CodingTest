import sys

n, m = map(int, sys.stdin.readline().split())
x, y, direction = map(int, sys.stdin.readline().split())
game_map = [[0 for _ in range(m)] for __ in range(n)]
game_map[x][y] = 1

array = []
for i in range(n):
    array.append(list(map(int, sys.stdin.readline().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global direction
    direction -=1
    if direction == -1:
        direction = 3


# 시뮬레이션 시작
count = 1
turn_time = 0

while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    if game_map[nx][ny] == 0 and array[nx][ny] == 0:
        game_map[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1

    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동하기
        if array[nx][ny] ==0:
            x = nx
            y = ny
        # 뒤가 바다로 막혀 있는 경우
        else:
            break
        turn_time = 0

print(count)

