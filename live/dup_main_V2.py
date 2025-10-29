from util_dev import *
clear()
while True:
	initPosition()
	
	for i in range(3):
		for y in range(get_world_size()):
			if (can_harvest()):
				harvest()
			plantSunflower()
			move(North)
		move(East)

	for i in range(6):
		for y in range(get_world_size()):
			if (can_harvest()):
				harvest()
			plantGlass()
			move(North)
		move(East)
		
	for i in range(6):
		for y in range(get_world_size()):
			if (can_harvest()):
				harvest()
			plantTree()
			move(North)
		move(East)
			
	for i in range(7):
		for y in range(get_world_size()):
			if (can_harvest()):
				harvest()
			plantCarrot()
			move(North)
		move(East)
