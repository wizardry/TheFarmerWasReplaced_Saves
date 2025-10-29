from sunflower_util import *

clear()
mvTo((0, 0))
def action():
	while True:
		for y in range(get_world_size()):
			if get_ground_type() == Grounds.Grassland:
				till()
			plant(Entities.Sunflower)
			if (can_harvest()):
				harvest()
			move(North)

while True:
	for x in range(get_world_size()):
		if (num_drones() != max_drones()):
			spawn_drone(action)
		else:
			action()
		move(East)
