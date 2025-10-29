from cactus_util import *

clear()

while True:
	toMove()
	startPosition = [get_pos_x(), get_pos_y()]
	size = get_world_size()
	size = 8
	plantCactus(size)
	sortCactus(size)
	toMove(startPosition[0], startPosition[1])
	harvest()	
	