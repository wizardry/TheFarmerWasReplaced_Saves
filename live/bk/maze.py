from util_maze import *
# not looks for constants flag

def action():
	lastPosition = [0, 0]
	
	while not checkTreasure():
		quick_print(measure())
		if (measure() == None):
			break
		dir = getDirection(lastPosition)
		if (dir == None or dir == 0):
			lastPosition = [get_pos_x(), get_pos_y()]
			if not (walkTo(1)):
				print('Error: idk 1st')	
		else:
			lastPosition = [get_pos_x(), get_pos_y()]
			if not (walkTo(dir)):
				print('Error: idk')
	harvest()
	return True

def setDorones():
	ws = get_world_size()
	doroneMap = [
		[0, 0],
		[0, ws-1],
		[ws-1, 0],
		[ws-1, ws-1],
		[(ws-1)//2, (ws-1)//2],
	]
	pos = doroneMap[num_drones() - 2]
	toMove(pos[0], pos[1])
	while not get_entity_type() == Entities.Hedge:
		pass
	return action()
while True:
	clear()
	toMove()
		
	inited = False
	for i in range(5):
		if (i == 4):
			# setTimeout()
			do_a_flip()
			pet_the_piggy()
			do_a_flip()
			pet_the_piggy()
			do_a_flip()
			pet_the_piggy()
			pet_the_piggy()
			pet_the_piggy()
			init()
			inited = True
			action()
		else:
			spawn_drone(setDorones)
	while not (inited and measure() == None):
		pass
