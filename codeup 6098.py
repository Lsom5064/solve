"""
영일이는 생명과학에 관심이 생겨 왕개미를 연구하고 있었다.

왕개미를 유심히 살펴보던 중 특별히 성실해 보이는 개미가 있었는데,
그 개미는 개미굴에서 나와 먹이까지 가장 빠른 길로 이동하는 것이었다.

개미는 오른쪽으로 움직이다가 벽을 만나면 아래쪽으로 움직여 가장 빠른 길로 움직였다.
(오른쪽에 길이 나타나면 다시 오른쪽으로 움직인다.)

이에 호기심이 생긴 영일이는 그 개미를 미로 상자에 넣고 살펴보기 시작하였다.

미로 상자에 넣은 개미는 먹이를 찾았거나, 더 이상 움직일 수 없을 때까지
오른쪽 또는 아래쪽으로만 움직였다.

미로 상자의 구조가 0(갈 수 있는 곳), 1(벽 또는 장애물)로 주어지고,
먹이가 2로 주어질 때, 성실한 개미의 이동 경로를 예상해보자.

단, 맨 아래의 가장 오른쪽에 도착한 경우, 더 이상 움직일 수 없는 경우, 먹이를 찾은 경우에는
더이상 이동하지 않고 그 곳에 머무른다고 가정한다.

미로 상자의 테두리는 모두 벽으로 되어 있으며,
개미집은 반드시 (2, 2)에 존재하기 때문에 개미는 (2, 2)에서 출발한다.
"""

maze = []
for i in range(10):
    maze.append(list(map(int,input().split())))
currentX,currentY = 1,1
maze[currentX][currentY]=9
for i in range(100):
    if currentX==9 and currentY ==9:
        break
    elif maze[currentX+1][currentY]==1 and maze[currentX][currentY+1]==1:
        break
    elif maze[currentX][currentY+1]==2:
        maze[currentX][currentY+1]=9
        break

    elif maze[currentX][currentY+1]==0:
        maze[currentX][currentY+1]=9
        currentY+=1

    elif maze[currentX+1][currentY]==2:
        maze[currentX+1][currentY]=9
        break

    elif maze[currentX+1][currentY]==0:
        maze[currentX+1][currentY]=9
        currentX+=1
for row in maze:
    for cell in row:
        print(cell,end=" ")
    print()
