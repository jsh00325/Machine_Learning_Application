import queue
dist = [[0, 1, 2, 1, 2, 3, 2, 3, 4], [1, 0, 1, 2, 1, 2, 3, 2, 3], [2, 1, 0, 3, 2, 1, 4, 3, 2], [1, 2, 3, 0, 1, 2, 1, 2, 3], [2, 1, 2, 1, 0, 1, 2, 1, 2], [3, 2, 1, 2, 1, 0, 3, 2, 1], [2, 3, 4, 1, 2, 3, 0, 1, 2], [3, 2, 3, 2, 1, 2, 1, 0, 1], [4, 3, 2, 3, 2, 1, 2, 1, 0]]
oob = [ [0, 3, 6], [2, 5, 8], [0, 1, 2], [6, 7, 8] ]
move_dist = [-1, 1, -3, 3]
NONE = -1

class State :
	def __init__(self, board, goal, depth = 0, parent = NONE) :
		self.board = board
		self.goal = goal
		self.depth = depth
		self.parent = parent

	def __str__(self) :
		return f'depth : {self.depth}\n' + '\n'.join([str(self.board[x:x+3]) for x in range(0, 9, 3)]) + '\n'
	
	# dir [(0, L), (1, R), (2, U), (3, D)]
	def move(self, dir) :
		blank, new_board = self.board.index(0), self.board[:]
		if not blank in oob[dir] :
			new_board[blank], new_board[blank + move_dist[dir]] = new_board[blank + move_dist[dir]], new_board[blank]
		return new_board
	
	def f(self) :
		return self.h2() + self.depth
	
	def h1(self) :
		ans = 0
		for i in range(9) :
			if self.board[i] == self.goal[i] :
				ans += 1
		return 9 - ans
	
	def h2(self) :
		return sum([dist[i][self.goal.index(self.board[i])] for i in range(9)])

	def __lt__(self, other) :
		return self.f() < other.f()
	def __gt__(self, other) :
		return self.f() > other.f()
	
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

pq = queue.PriorityQueue()
pq.put(State(puzzle, goal))

visit = []
visit.append(puzzle)

while not pq.empty() :
	cur = pq.get()

	if cur.board == goal :
		print("탐색 성공!")
		cur.printPath()
		break

	for dir in range(4) :
		nxt = cur.move(dir)
		if nxt == cur.board :
			continue
		if nxt in visit :
			continue
		pq.put(State(nxt, goal, cur.depth + 1, cur))
		visit.append(nxt)