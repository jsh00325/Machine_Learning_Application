line_index = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
POS_INF, NEG_INF = 99999, -99999

class Board :
	def __init__(self) : 
		self.board = ['.'] * 9
		self.empty = 9
		
	def __str__(self) :
		return '\n'.join(['|{}|'.format('|'.join([self.board[3*i + x] for x in range(3)])) for i in range(3)]) + '\n'
	
	def getChild(self) :
		return [p for p in range(9) if self.board[p] == '.']
	
	def move(self, pos, player) :
		if (pos in range(9)) and (self.board[pos] == '.') :
			self.board[pos] = player
			self.empty -= 1

	def check_win(self, player) :
		for line in line_index :
			if all([self.board[x] == player for x in line]) :
				return True
		return False
	
	def evaluate(self) :
		if self.check_win('X') :
			return 1
		elif self.check_win('O') :
			return -1
		else :
			return 0
		
	def gameover(self) :
		return self.check_win('X') or self.check_win('O') or self.empty == 0

def minimax(cur, maxPlayer) :
	idx = -1

	if cur.gameover() :
		return -1, cur.evaluate()
	
	if maxPlayer :
		value = NEG_INF

		for p in cur.getChild() :
			cur.board[p] = 'X'
			cur.empty -= 1
			_, score = minimax(cur, False)
			cur.board[p] = '.'
			cur.empty += 1

			if score > value :
				idx, value = p, score
	else :
		value = POS_INF
		
		for p in cur.getChild() :
			if cur.board[p] != '.' :
				continue

			cur.board[p] = 'O'
			cur.empty -= 1
			_, score = minimax(cur, True)
			cur.board[p] = '.'
			cur.empty += 1

			if score < value :
				idx, value = p, score
	return idx, value

board, player = Board(), 'X'
while True :
	print(board)

	if board.gameover() :
		break

	i, v = minimax(board, player == 'X')
	board.move(i, player)

	player = ('X' if player == 'O' else 'O')

if board.evaluate() == 1 :
	print('X win!')
elif board.evaluate() == -1 :
	print('O win!')
else :
	print('Draw!')