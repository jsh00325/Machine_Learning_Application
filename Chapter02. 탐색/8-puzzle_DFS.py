# 특정 방향으로 움직일 때, 빈칸의 위치로 옳지 않은 인덱스 저장
oob = [ [0, 3, 6], [2, 5, 8], [0, 1, 2], [6, 7, 8] ]

# 특정 방향으로 움직일 때, 증감하는 인덱스의 크기 저장
move_dist = [-1, 1, -3, 3]

class State :
	def __init__(self, board, depth) :
		self.board = board
		self.depth = depth

###################################################

puzzle, goal = [], []

with open("Chapter02. 탐색\8-puzzle input.txt", "r") as f :
	for _ in range(3) :
		puzzle += list(map(int, f.readline().split()))
	f.readline()
	for _ in range(3) :
		goal += list(map(int, f.readline().split()))

###################################################

stack, visit = [State(puzzle, 0)], [puzzle]

while stack != [] :
	cur = stack.pop()

	if cur.board == goal :
		print("탐색 성공!")
		print(f'depth : {cur.depth}')
		break

	blank = cur.board.index(0)
	for dir in range(4) :
		if blank in oob[dir] :
			continue

		nxt_board = cur.board[:]
		nxt_board[blank], nxt_board[blank + move_dist[dir]] = nxt_board[blank + move_dist[dir]], nxt_board[blank]

		if not nxt_board in visit:
			stack.append(State(nxt_board, cur.depth + 1))
			visit.append(nxt_board)