# 문제

# 캐슬 디펜스는 성을 향해 몰려오는 적을 잡는 턴 방식의 게임이다. 게임이 진행되는 곳은 크기가 N×M인 격자판으로 나타낼 수 있다. 격자판은 1×1 크기의 칸으로 나누어져 있고, 각 칸에 포함된 적의 수는 최대 하나이다. 격자판의 N번행의 바로 아래(N+1번 행)의 모든 칸에는 성이 있다.

# 성을 적에게서 지키기 위해 궁수 3명을 배치하려고 한다. 궁수는 성이 있는 칸에 배치할 수 있고, 하나의 칸에는 최대 1명의 궁수만 있을 수 있다. 각각의 턴마다 궁수는 적 하나를 공격할 수 있고, 모든 궁수는 동시에 공격한다. 궁수가 공격하는 적은 거리가 D이하인 적 중에서 가장 가까운 적이고, 그러한 적이 여럿일 경우에는 가장 왼쪽에 있는 적을 공격한다. 같은 적이 여러 궁수에게 공격당할 수 있다. 공격받은 적은 게임에서 제외된다. 궁수의 공격이 끝나면, 적이 이동한다. 적은 아래로 한 칸 이동하며, 성이 있는 칸으로 이동한 경우에는 게임에서 제외된다. 모든 적이 격자판에서 제외되면 게임이 끝난다. 

# 게임 설명에서 보다시피 궁수를 배치한 이후의 게임 진행은 정해져있다. 따라서, 이 게임은 궁수의 위치가 중요하다. 격자판의 상태가 주어졌을 때, 궁수의 공격으로 제거할 수 있는 적의 최대 수를 계산해보자.

# 격자판의 두 위치 (r1, c1), (r2, c2)의 거리는 |r1-r2| + |c1-c2|이다.
# 입력

# 첫째 줄에 격자판 행의 수 N, 열의 수 M, 궁수의 공격 거리 제한 D가 주어진다. 둘째 줄부터 N개의 줄에는 격자판의 상태가 주어진다. 0은 빈 칸, 1은 적이 있는 칸이다.
# 출력

# 첫째 줄에 궁수의 공격으로 제거할 수 있는 적의 최대 수를 출력한다.




# 공격 규칙:

# D 칸 이내에서 가장 가까운 적을 공격
# 여러 적이 동일한 거리에 있을 경우, 가장 왼쪽의 적을 공격
# 모든 궁수는 동시에 공격
# 공격받은 적은 게임에서 제외

# 적의 이동:

# 궁수의 공격 후, 적은 아래로 한 칸씩 이동
# 성의 위치로 이동한 적은 게임에서 제외

# 목표:

# 궁수의 위치를 최적으로 배치하여, 궁수가 공격으로 제거할 수 있는 적의 최대 수를 구하기


from itertools import combinations      # 귀찮으니 combination
import copy

N, M, D = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
# 입력: 격자판의 크기 N, M과 궁수의 공격 거리 D
# 게임판 정보 입력 받기 (0: 빈 칸, 1: 적)


# 두 점 사이의 거리
def distance(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

# 궁수가 공격하는 함수
def attack(archers, board):
    targets = []  # 공격 대상들

    for archer in archers:
        min_distance = D + 1    # 최소 거리 초기값 (D보다 크게)
        target = None           # 공격 대상이 아직 지정되지 않음

        for i in range(N):      # 모든 적에 대해서
            for j in range(M):
                if board[i][j] == 1 and distance((N, archer), (i, j)) <= D:     # 적이 있고, 거리가 D 이하일 경우
                    # 가장 가까운 적을 찾거나, 거리가 같으면 가장 왼쪽의 적을 찾기
                    if distance((N, archer), (i, j)) < min_distance or (distance((N, archer), (i, j)) == min_distance and j < target[1]):
                        min_distance = distance((N, archer), (i, j))
                        target = (i, j)

        # 반복문에서 target에 궁수가 공격할 적의 위치를 저장
        if target:
            targets.append(target)

    count = 0                       # 죽인 적의 수
    for target in set(targets):     # 중복 제거 후 공격
        if board[target[0]][target[1]] == 1:
            count += 1
            board[target[0]][target[1]] = 0  # 적 제거
    return count

# 적들을 아래로 한 칸씩 이동시키는 함수
def move_enemies(board):
    for i in range(N-1, 0, -1):
        board[i] = board[i-1]
    board[0] = [0]*M            # 가장 위의 줄

max_enemies = 0                 

# 가능한 궁수의 모든 조합에 대해
for archers in combinations(range(M), 3):
    b = copy.deepcopy(board)        # board를 수정하지 않고 복사본 생성
    count = 0                       # 해당 조합에서 죽인 적의 수

    # 아직 적이 남아있다면 b에는 1값이 남아있을 것
    while sum(map(sum, b)):
        count += attack(archers, b)     # 궁수가 공격
        move_enemies(b)                 # 적 이동

    max_enemies = max(max_enemies, count)  

print(max_enemies)