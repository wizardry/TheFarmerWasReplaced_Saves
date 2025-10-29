from lb_resouce_utils import *

debug = True
debug = False

# WoodRun is default has items None

# set_world_size(32)
# set_execution_speed(1000)
timer = get_time()
size = 32 #get_world_size()
rSize =  range(size)

finishCount = 10000000000

cost = 512
# use Leaderboards.Wood
def runV1():
	availableYPos = [0, 8, 16, 24]
	availableXPos = [0, 4, 8, 12, 16, 20, 24, 28]
	posMas = []
	for id in range(max_drones()):
		for x in availableXPos:
			for y in availableYPos:
				posMas.append((x, y))

	def droneAction(main = False):
		n = num_drones()
		index = n - 2
		if (main):
			index = 31
		initPos = posMas[index]
		minY = initPos[1]
		maxY = initPos[1] + (size / len(availableYPos)) - 1
		x = initPos[0]
		flg = False
		yRange = [range(minY, maxY), range(maxY, minY, -1)]

		mvTo(initPos, size)
		# init plant
		for y in yRange[flg]:
			if (x + y) % 2 == 1:
				continue
			mvTo((x, y), size)
			plant(Entities.Tree)
			c = get_companion()
			while c[0] != Entities.Grass and (c[1][0] in availableXPos or (c[1][0] + c[1][1]) % 2):
				harvest()
				plant(Entities.Tree)
				c = get_companion()
		flg = not flg
		while num_items(Items.Wood) < finishCount or debug:
			for y in yRange[flg]:
				if (x + y) % 2 == 1:
					continue

				mvTo((x, y))

				if not can_harvest() and get_entity_type() == Entities.Tree:
					continue

				if get_water() < 0.8:
					use_item(Items.Water)

				harvest()

				plant(Entities.Tree)
				c = get_companion()
				while c[0] != Entities.Grass and (c[1][0] in availableXPos or (c[1][0] + c[1][1]) % 2):
					harvest()
					plant(Entities.Tree)
					c = get_companion()
			flg = not flg

	for d in range(max_drones()):
		if num_drones() != max_drones():
			spawn_drone(droneAction)
		else:
			droneAction(True)

def runV2():
	def droneAction():
		while num_items(Items.Wood) < finishCount or debug:
			for y in rSize:
				if (x + y) % 2 == 1:
					move(North)
					continue
				if get_water() < 0.8:
					use_item(Items.Water)

				if can_harvest():
					harvest()

				plant(Entities.Tree)
				c = get_companion()

				while not (c[0] == Entities.Grass and (c[1][0] + c[1][1]) % 2 == 1):
					harvest()
					plant(Entities.Tree)
					c = get_companion()
				move(North)

	for x in rSize:
		if num_drones() != max_drones():
			spawn_drone(droneAction)
		else:
			droneAction()
		move(East)

run()
quick_print('finished item counts:' + str(num_items(Items.Wood)))
quick_print('Wood tick: '+ str(get_tick_count()) + ', time: ' + str(get_time() - timer))

# History
#
# V1: