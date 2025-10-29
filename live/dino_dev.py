from dino_util import *

clear()
while True:
	toMove()
	change_hat(Hats.Dinosaur_Hat)
	canMove = True
	
	def cantMove():
		return can_move(North) == False and can_move(East) == False and can_move(South) == False and can_move(West) == False
	while canMove:
		i = 0
		size = get_world_size()
		for x in range(size):
			if (i == 0):
				movePosition(0, size - 1, East, North)
				if (cantMove()):
					canMove = False
					break
			elif (x == (size -1)):
				movePosition(x, 0, East, South)
				if (cantMove()):
					canMove = False
					break
				movePosition(0, 0, West, South)
				if (cantMove()):
					canMove = False
					break
	
			elif (x % 2 == 1):
				movePosition(x, 1, East, South)
				if (cantMove()):
					canMove = False
					break
					
			elif (x % 2 == 0):
				movePosition(x, size - 1, East, North)
				if (cantMove()):
					canMove = False
					break
					
			i += 1
			
		if(cantMove()):
			canMove = False
	change_hat(Hats.Traffic_Cone)