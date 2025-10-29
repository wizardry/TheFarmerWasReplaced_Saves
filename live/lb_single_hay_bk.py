from lb_single_utils import *

set_world_size(8)
# set_execution_speed(1)
timer = get_time()
size = 8
rSize =  range(size)

finishCount = 100000000
targets = [(0, 0), (0, 4), (2, 6), (2, 2), (4, 0), (4, 4), (6, 6), (6, 2)]
# targets = [(0,0), (4,4)]
def finish():
	# return True
	return num_items(Items.Hay) > finishCount

def runV2():

	def finish():
		# return False
		return num_items(Items.Hay) > finishCount

	map = {}
	index = 0
	while not finish():
		# ほかの混作で耕されていた場合に戻す,収穫してHayにしておく
		if (get_ground_type() == Grounds.Soil):
			till()
		if (get_entity_type() != Entities.Grass):
			harvest()
		c = get_companion()

		returnPos = [get_pos_x(), get_pos_y()]
		isSameTarget = c[1] in map and map[c[1]] == c[0]
		isFar = (c[1][0] in [0,1,2,6,7]) and abs(c[1][1] - returnPos[1]) < 3

		if (isSameTarget or isFar):
			harvest()
			move(North)
			index +=1
			continue
		map[c[1]] = c[0]
		# before move
		mvTo(c[1])
		harvest()
		if (c[0] == Entities.Carrot):
			if (get_ground_type() != Grounds.Soil):
				till()
			carrotCost = 512
			if num_items(Items.Wood) > carrotCost and num_items(Items.Hay) > carrotCost:
				plant(c[0])
		else:
			plant(c[0])

		# hay
		mvTo(returnPos)
		if can_harvest():
			harvest()
		else:
			continue
		move(North)
		index += 1

def runV1():
	map = {}
	index = 0
	while not finish():
		initPos = targets[index % len(targets)]
		mvTo(initPos)

		if can_harvest():
			harvest()
		else:
			pass

		c = get_companion()
		if (c[1] in map and map[c[1]] == c[0]):
			index +=1
			continue
		map[c[1]] = c[0]

		mvTo(c[1])
		harvest()
		if (c[0] == Entities.Carrot):
			if (get_ground_type() != Grounds.Soil):
				till()
			carrotCost = 512
			if num_items(Items.Wood) > carrotCost and num_items(Items.Hay) > carrotCost:
				plant(c[0])
		else:
			plant(c[0])
		index += 1

def runV3():
	def finish():
		return False
		return num_items(Items.Hay) > finishCount

	map = {}
	index = 0
	while not finish():
		bn = num_items(Items.Hay)

		# ほかの混作で耕されていた場合に戻す,収穫してHayにしておく
		if (get_ground_type() == Grounds.Soil):
			till()
		if (get_entity_type() != Entities.Grass):
			harvest()
		c = get_companion()

		returnPos = [get_pos_x(), get_pos_y()]
		isSameTarget = c[1] in map and map[c[1]] == c[0]
		isFar = (c[1][0] in [0, 3, 5])

		if (isSameTarget or isFar):
			harvest()
			move(North)
			index +=1

			continue
		map[c[1]] = c[0]
		# before move
		mvTo(c[1])
		harvest()
		if (c[0] == Entities.Carrot):
			if (get_ground_type() != Grounds.Soil):
				till()
			carrotCost = 512
			if num_items(Items.Wood) > carrotCost and num_items(Items.Hay) > carrotCost:
				plant(c[0])
		else:
			plant(c[0])

		# hay
		mvTo(returnPos)
		if can_harvest():
			harvest()

		else:
			continue
		move(North)
		index += 1

def runV4():
	carrotCost = 512

	def finish():
		# return False
		return num_items(Items.Hay) > finishCount

	map = {}
	index = 0
	while not finish():
		bn = num_items(Items.Hay)
		posIndex = index % 4
		poses = [(0, 0), (0, 1), (0, 2), (0, 1)]
		nowPos = poses[posIndex]
		dirIndex = index % 4
		dir = [North, North, South, South][dirIndex]

		# ほかの混作で耕されていた場合に戻す,収穫してHayにしておく
		if (get_ground_type() == Grounds.Soil):
			till()
		if (get_entity_type() != Entities.Grass):
			harvest()
		c = get_companion()

		isSameTarget = c[1] in map and map[c[1]] == c[0]
		if (c[1][0] > 4):
			xdiff = nowPos[0] - c[1][0] + size
		else:
			xdiff = nowPos[0] - c[1][0]
		if (c[1][1] > 4):
			ydiff = nowPos[1] - c[1][1] + size
		else:
			ydiff = nowPos[1] - c[1][1]
		isFar = abs(xdiff) + abs(ydiff) > 2
		isPlantPos = c[1] in poses

		if (isSameTarget or isFar or isPlantPos):
			if not can_harvest():
				use_item(Items.Water)
			harvest()
			quick_print('same: ', num_items(Items.Hay) - bn)
			move(dir)
			index +=1
			continue
		map[c[1]] = c[0]
		# before move
		mvTo(c[1])
		# before companion target harvest
		harvest()
		if (c[0] == Entities.Carrot):
			if (get_ground_type() != Grounds.Soil):
				till()
			if num_items(Items.Wood) > carrotCost and num_items(Items.Hay) > carrotCost:
				plant(c[0])
		else:
			plant(c[0])

		# hay

		mvTo(nowPos)
		if not can_harvest():
			use_item(Items.Water)
		harvest()
		quick_print('las: ', num_items(Items.Hay) - bn)

		move(dir)
		index += 1
def runV5():
	carrotCost = 512
	map = {}
	index = 0
	# while True:
	while not num_items(Items.Hay) > finishCount:
		posIndex = index % 2
		poses = [(0, 0), (0, 1)]
		nowPos = poses[posIndex]
		dirIndex = index % 2
		dir = [North, South][dirIndex]

		c = get_companion()

		isSameTarget = c[1] in map and map[c[1]] == c[0]
		isPlantPos = c[1] in poses

		if (isSameTarget or isPlantPos):
			if not can_harvest():
				use_item(Items.Water)
			harvest()
			move(dir)
			index +=1
			continue
		map[c[1]] = c[0]
		# before move
		mvTo(c[1])
		# before companion target harvest
		harvest()
		if (c[0] == Entities.Carrot):
			if (get_ground_type() != Grounds.Soil):
				till()
		plant(c[0])

		# hay
		mvTo(nowPos)
		if not can_harvest():
			use_item(Items.Water)

		harvest()
		move(dir)

def runV6():
	size = 4
	rSize =  range(size)

	finishCount = 100000000
	set_world_size(size)
	carrotCost = 512
	map = {}
	index = 0
	# while True:
	while not num_items(Items.Hay) > finishCount:
		posIndex = index % 2
		poses = [(0, 0), (0, 1)]
		nowPos = poses[posIndex]
		dirIndex = index % 2
		dir = [North, South][dirIndex]
		mvTo(nowPos, size)
		c = get_companion()
		if (c == None):
			continue
		isSameTarget = c[1] in map and map[c[1]] == c[0]
		isPlantPos = c[1] in poses
		if (isSameTarget or isPlantPos):
			if not can_harvest():
				use_item(Items.Water)
			while not can_harvest():
				use_item(Items.Fertilizer)
				pass
			debugHarvest(Items.Hay)
			move(dir)
			index +=1
			continue
		map[c[1]] = c[0]
		# before move
		mvTo(c[1], size)
		# before companion target harvest
		harvest()
		if (c[0] == Entities.Carrot):
			if (get_ground_type() != Grounds.Soil):
				till()
		plant(c[0])

		# hay
		mvTo(nowPos, size)
		if not can_harvest():
			use_item(Items.Water)
		while not can_harvest():
			quick_print('wait')
			use_item(Items.Fertilizer)
			pass
		debugHarvest(Items.Hay)
		# harvest()
		move(dir)
		index += 1
def runV7():
	size = 3
	rSize =  range(size)
	finishCount = 100000000
	set_world_size(size)
	carrotCost = 512
	map = {}
	poses = [(0, 0), (0, 0)]
	now = (0,0)
	flg = False
	while num_items(Items.Hay) < finishCount or debug:

		def hav():
			# if not can_harvest():
			# 	return False

			# while not can_harvest():
			# 	if num_items(Items.Water) > 0:
			# 		use_item(Items.Water)

			if not can_harvest():
				quick_print('-------------cant')
				return False
				# use_item(Items.Fertilizer)
			# debugHarvest(Items.Hay)
			harvest()
			return True
		hav()
		if num_items(Items.Water) > 0 and get_water() < 0.9:
			use_item(Items.Water)
		c = get_companion()
		if not (c[1] in poses):
			if c[1] in map and map[c[1]] == c[0]:
				hav()
				mvTo(now, size)
				continue
			if c[0] == Entities.Carrot and carrotCost > num_items(Items.Wood):
				hav()
				mvTo(now, size)
				continue
			mvTo(c[1], size)
			harvest()
			if not c[1] in map:
				till()
			plant(c[0])
			map[c[1]] = c[0]
			nearly = [
				((0 - c[1][0]) % size) + ((0 - c[1][1]) % size),
				((2 - c[1][0]) % size) + ((2 - c[1][1]) % size)
			]
			flg = nearly[0] > nearly[1]
			now = poses[flg]
			mvTo(now, size)

runV1()


quick_print('finished item counts:' + str(num_items(Items.Hay)))
quick_print('Hay_Single tick: '+ str(get_tick_count()) + ', time: ' + str(get_time() - timer))

# History
#
# use lb_single_util
# formtted to match other lb files
# V1 Hay_Single tick: ?, time: 400~
# V1 Hay_Single tick: 2176661, time:358.31
#