oob = [ [0, 3, 6], [2, 5, 8], [0, 1, 2], [6, 7, 8] ]
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

MaxDepth = 0
while True :
	stack, isFind = [State(puzzle, 0)], False
	while stack != [] :
		cur = stack.pop()

		if cur.depth > MaxDepth :
			continue

		if cur.board == goal :
			isFind = True
			break

		blank = cur.board.index(0)
		for dir in range(4) :
			if blank in oob[dir] :
				continue
			nxt_board = cur.board[:]
			nxt_board[blank], nxt_board[blank + move_dist[dir]] = nxt_board[blank + move_dist[dir]], nxt_board[blank]
			stack.append(State(nxt_board, cur.depth + 1))

	if isFind :
		print('탐색 성공!')
		print('depth : ', MaxDepth)
		break
	MaxDepth += 1