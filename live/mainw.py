from util_dev import *

# { entity: [start_x_pos, end_x_pos] }
map = {
	Entities.Sunflower: (0, 3),
	Entities.Grass: (4, 13),
	Entities.Tree: (14, 18),
	Entities.Carrot: (19, 31)
}

def cellAction(entity):
#	quick_print(get_companion())
	if entity in [Entities.Sunflower, Entities.Carrot]:
		initCondition(True, True)
	else:
		initCondition(False, True)
	if (can_harvest()):
		harvest()
	if (entity == Entities.Tree):
		if ((get_pos_x() % 2) + (get_pos_y() % 2) == 1):
			plant(Entities.Tree)
		else:
			plant(Entities.Bush)
	else:
		plant(entity)

def columnAction():
	for y in range(get_world_size()):
		entity = None
		x = get_pos_x()
		for m in map:
			if(map[m][0] <= x and map[m][1] >= x):
				entity = m
		if (entity == None):
			print('Entity is None', x, y)
		else:
			cellAction(entity)
		toMove(get_pos_x(), get_pos_y() + 1)

def rowAction():
	for x in range(get_world_size()):
		if (num_drones() == max_drones()):
			columnAction()
		else:
			spawn_drone(columnAction)
		move(East)

def start():
	clear()
	while True:
		rowAction()

start()