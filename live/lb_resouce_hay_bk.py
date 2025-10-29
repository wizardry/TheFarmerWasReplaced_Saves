from lb_single_utils import *

# singleMazeRun is default has items Weird_Substance 1B, Power 1B

# set_world_size(32)
# set_execution_speed(1)

size = 32 #get_world_size()
rSize =  range(size)
finishCount = 2000000000
# stateを更新してitemsで計測するのはコストが高いことが判明したので行わない。
# a += num => a = a + num => 2tick num_items(Items.hoge) => 1tick
state = {
	'finishCount': 0,
	'iterator': 0,
	'items': {
		'hay': 0,
	},
}
# use Leaderboards.Hay

def runV1():
	quick_print(get_world_size())
	isCompleted =  False
	def rowAction():
		while move(North):
			harvest()

	while not isCompleted:
		for x in rSize:
			if (max_drones() == num_drones()):
				while move(North) and not isCompleted:
					harvest()
					if (num_items(Items.Hay) > 2000000000):
						isCompleted = True
						break
			else:
				spawn_drone(rowAction)
			move(East)
	clear()
	return None

def runV2():
	isCompleted = False
	# map = [
		# (3, 3), (3, 10), (3, 17), (3, 24),
		# (10, 3), (10, 10), (10, 17), (10, 24),
		# (17, 3), (17, 10), (17, 17), (17, 24),
		# (24, 3), (24, 10), (24, 17), (24, 24),
		# (28, 6), (28, 13), (28,20), (28, 27),
		# (20, 29), (13, 29), (6, 29), (0 ,29)
	# ]
	map = [
		(0, 0), (0, 8), (0, 16), (0, 24),
		(3, 4), (3, 12), (3, 20), (3, 28),
		(7, 0), (7, 8), (7, 16), (7, 24),
		(11, 4), (11, 12), (11, 20), (11, 28),
		(15, 0), (15, 8), (15, 16), (15, 24),
		(19, 4), (19, 12), (19, 20), (19, 28),
		(23, 0), (23, 8), (23, 16), (23, 24),
		(27, 4), (27, 12), (27, 20), (27, 28),
	]

	def rowStepAction(pos, companionMap):
		mvTo(pos)
		companionMap = {}
		if can_harvest():
			num = num_items(Items.Hay)
			harvest()
			# quick_print('Hay', num_items(Items.Hay) - num)
		else:
			return True
			# quick_print('cont harvest', can_harvest())

		c = get_companion()
		# quick_print(index, (get_pos_x(), get_pos_y()), pos, c)
		# if (c == None):
		# 	pass
		if (c[1] in companionMap):
			return False
		companionMap[c[1]] = [c[0]]
		mvTo(c[1])
		harvest()
		if (c[0] == Entities.Carrot):
			if not (get_ground_type() == Grounds.Soil):
				till()
			if num_items(Items.Wood) > CARRORT_COST and num_items(Items.Hay) > CARRORT_COST:
				plant(c[0])
		else:
			plant(c[0])
		mvTo(pos)
		return True

	def rowAction(pos = (0, 0), index = None):
		measureMap = {}
		# quick_print(pos, index)
		while True:
			rowStepAction(pos, measureMap)

	def mainDoroneAction(pos = (0, 0), index = None):
		measureMap = {}
		# quick_print(pos, index)
		isCompleted = False
		while not isCompleted:
			if rowStepAction(pos, measureMap):
				if (num_items(Items.Hay) > finishCount):
					isCompleted = True
					break
		return True

	def rowActionWrapper():
		index = num_drones() - 1
		pos = map[index]
		# quick_print(num_drones(), index, pos,)
		rowAction(pos, index)

	for m in map:
		spawn_drone(rowActionWrapper)
		harvest() # tick合わせ。num_dorone()が重複する

	mainDoroneAction((0, 0))
	clear()
	return None

def runV3():
	isCompleted = False
	map = [
		(0, 0), (0, 8), (0, 16), (0, 24),
		(3, 4), (3, 12), (3, 20), (3, 28),
		(7, 0), (7, 8), (7, 16), (7, 24),
		(11, 4), (11, 12), (11, 20), (11, 28),
		(15, 0), (15, 8), (15, 16), (15, 24),
		(19, 4), (19, 12), (19, 20), (19, 28),
		(23, 0), (23, 8), (23, 16), (23, 24),
		(27, 4), (27, 12), (27, 20), (27, 28),
	]

	def stepAction(pos = (0, 0), companionMap = {}, index = 0):
		posIndex = index % 2
		poses = [pos, (pos[0], pos[1]+1)]
		nowPos = poses[posIndex]
		dirIndex = index % 2
		dir = [North, South][dirIndex]

		c = get_companion()
		if (c == None):
			till()
			c = get_companion()
		isSameTarget = c[1] in companionMap and companionMap[c[1]] == c[0]
		isPlantPos = c[1] in poses

		if (isSameTarget or isPlantPos):
			if not can_harvest():
				use_item(Items.Water)
			harvest()
			move(dir)
			index +=1
			return companionMap, index

		companionMap[c[1]] = [c[0]]
		mvTo(c[1])
		harvest()
		if (c[0] == Entities.Carrot):
			if not (get_ground_type() == Grounds.Soil):
				till()
			if num_items(Items.Wood) > CARRORT_COST and num_items(Items.Hay) > CARRORT_COST:
				plant(c[0])
		else:
			plant(c[0])
		mvTo(nowPos)
		if not can_harvest():
			use_item(Items.Water)
		harvest()
		move(dir)
		index += 1
		return companionMap, index

	def rowAction(pos = (0, 0)):
		companionMap = {}
		index = 0
		while True:
			_companionMap, _index = stepAction(pos, companionMap, index)
			companionMap = _companionMap
			index = _index

	def mainDoroneAction(pos = (0, 0)):
		companionMap = {}
		index = 0
		isCompleted = False
		while not isCompleted:
			_companionMap, _index = stepAction(pos, companionMap, index)
			companionMap = _companionMap
			index = _index
			if (num_items(Items.Hay) > finishCount):
				isCompleted = True
				break

		return True

	def rowActionWrapper():
		index = num_drones() - 1
		pos = map[index]
		# quick_print(num_drones(), index, pos,)
		rowAction(pos)

	for m in map:
		spawn_drone(rowActionWrapper)
		harvest() # tick合わせ。num_dorone()が重複する

	mainDoroneAction((0, 0))
	clear()
	return None


def run():
	runV1()

run()
quick_print('finished item counts:' + str(num_items(Items.Hay)))
quick_print('Hay tick: '+ str(get_tick_count()) + 'time :'+ str(get_tick_count()))

# History
#
# V1: dorone最大利用してwhile move(North)するだけ
# Hay tick: 48850517 time: 48850543
#