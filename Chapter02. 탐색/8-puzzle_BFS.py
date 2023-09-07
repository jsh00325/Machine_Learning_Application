oob = [ [0, 3, 6], [2, 5, 8], [0, 1, 2], [6, 7, 8] ]
move_dist = [-1, 1, -3, 3]
NONE = -1

class State :
	def __init__(self, board, depth, parent = NONE) :
		self.board = board
		self.depth = depth
		self.parent = parent

	def __str__(self) :
		return '\n'.join([str(self.board[x:x+3]) for x in range(0, 9, 3)]) + '\n'
	
	# dir [(0, L), (1, R), (2, U), (3, D)]
	def nxt_state(self, dir) :
		blank = self.board.index(0)
		new_board = self.board[:]

		if blank in oob[dir] :
			return new_board
		
		new_board[blank], new_board[blank + move_dist[dir]] = new_board[blank + move_dist[dir]], new_board[blank]
		return new_board
	
	def printPath(self) :
		if self.parent == NONE :
			return
		self.parent.printPath()
		print(self)

###################################################

puzzle, goal = [], []

with open("Chapter02. 탐색\8-puzzle input.txt", "r") as f :
	for _ in range(3) :
		puzzle += list(map(int, f.readline().split()))
	f.readline()
	for _ in range(3) :
		goal += list(map(int, f.readline().split()))

###################################################

queue, visit = [], []
queue.append(State(puzzle, 0))
visit.append(puzzle)

while queue != [] :
	cur = queue.pop(0)

	if cur.board == goal :
		print("탐색 성공!\n")
		cur.printPath()
		print(f'depth : {cur.depth}')
		break

	for dir in range(4) :
		nxt_board = cur.nxt_state(dir)
		if cur.board == nxt_board :
			continue
		if not nxt_board in visit :
			queue.append(State(nxt_board, cur.depth + 1, cur))
			visit.append(nxt_board)