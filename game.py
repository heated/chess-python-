import sys
from board import *

class Chess(object):
	"""a game with two players!"""
	def __init__(self):
		self.initializeBoard()

	def turn(self):
		while True:
			moveString = self.prompt_move()
			# TODO catch bad input
			move = self.parseMove(moveString)
			valid = self.board.tryMove(move)
			if valid:
				break;
			else:
				print 'Invalid move!'
		# wait for input

		# tell board input


	def play(self):
		while not self.is_over():
			turn()

		# print board

	# return pair of cells?
	def parseMove(self, input):
		# TODO catch bad input
		start_row = int(input[0])
		start_col = input[1]
		end_row = int(input[2])
		end_col = input[3]
		return [[start_row, start_col], [end_row, end_col]]


	def prompt_move(self):
		print 'Sir, your orders?'
		return sys.stdin.readline()

	def initializeBoard(self):
		self.board = Board()

if __name__ == "__main__":
    game = Chess()
    game.turn()