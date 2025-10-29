from util_dev import *
from errors import *
# サボテンを植えるまでを実行します。
# ソートは実行しません

def plantCactus(size):
	startPosition = [get_pos_x(), get_pos_y()]
	checkOverSizeFromWorld(size, size)
	dorones = []
	def columnActionWrapper():
		x = get_pos_x()
		for y in range(size):
			initCondition(True)
			plant(Entities.Cactus)
			toMove(startPosition[0] + x, startPosition[1] + y + 1)
					
	for x in range(size):
		if (max_drones() == num_drones() or x == size - 1):
			columnActionWrapper()
		else:
			dorones.append(spawn_drone(columnActionWrapper))
		toMove(startPosition[0] + x + 1, startPosition[1])
	finishedAllDoroneAction(dorones)
	toMove(startPosition[0], startPosition[1])

def singleSort(vector):
	if (North == vector):
		if(get_pos_y() == get_world_size() - 1):
			return False
	if (South == vector):
		if(get_pos_y() == 0):
			return False
	if (East == vector):
		if(get_pos_x() == get_world_size() - 1):
			return False
	if (West == vector):
		if(get_pos_x() == 0):
			return False
			
	now = measure()
	compare = measure(vector)
	if (compare == None or now == None):
		return False
	if (now > compare):
		swap(vector)
		return True
	return False

def columnSort(size, vector):
	completed = False
	startPosition = [get_pos_x(), get_pos_y()]
	reverseMap = {
		North: South,
		South: North,
		East: West,
		West: East,
	}
	for a in range(size):
		isSorted = singleSort(vector)
		if (isSorted):
			for a2 in range(a):
				move(reverseMap[vector])
				if not (singleSort(vector)):
					move(vector)
					break
				else:
					if (includes([North, South], vector)):
						toMove(startPosition[0], startPosition[1] + a - (a2 + 1))
					else:
						toMove(startPosition[0] + a - (a2 + 1), startPosition[1])
			
		if (includes([North, South], vector)):
			toMove(startPosition[0], startPosition[1] + a + 1)
		else:
			toMove(startPosition[0] + a + 1, startPosition[1])


def sortCactusV1(size):
	startPosition = [get_pos_x(), get_pos_y()]
	for x in range(size):
		columnSort(size, North)
		toMove(startPosition[0] + x + 1, startPosition[1])
	toMove(startPosition[0], startPosition[1])
	for y in range(size):
		columnSort(size, East)
		toMove(startPosition[0], startPosition[1] + y + 1)

def sortCactus(size):
	startPosition = [get_pos_x(), get_pos_y()]
	dorones = []
	def northSort():
		columnSort(size, North)
	for x in range(size):
		if (num_drones() == max_drones() or x == size - 1):
			northSort()
		else:
			dorones.append(spawn_drone(northSort))
		toMove(startPosition[0] + x + 1, startPosition[1])
	toMove(startPosition[0], startPosition[1])
	finishedAllDoroneAction(dorones)

	dorones = []
	def eastSort():
		columnSort(size, East)
		
	for y in range(size):
		if (num_drones() == max_drones() or y == size - 1):
			columnSort(size, East)
		else:
			dorones.append(spawn_drone(eastSort))
		toMove(startPosition[0], startPosition[1] + y + 1)
	finishedAllDoroneAction(dorones)
