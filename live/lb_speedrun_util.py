##-------------------------------use SpeedRunRankingModeUtils

def mvTo(pos = (0, 0), Spec=False):
	size = get_world_size()
	if (Spec):
		quick_print('from: ', (get_pos_x(), get_pos_y()))

	fromPos = (get_pos_x(), get_pos_y())
	toPos = pos
	horizontal = (pos[0] - fromPos[0]) % size
	horizontalRev = (fromPos[0] - pos[0])  % size

	vertical = (pos[1] - fromPos[1]) % size
	verticalRev = (fromPos[1] - pos[1])  % size

	if horizontal <= horizontalRev:
		for _ in range(horizontal):
			if (Spec):
				quick_print('east: ', get_pos_x())
			move(East)
	else:
		for _ in range(horizontalRev):
			if (Spec):
				quick_print('west: ', get_pos_x())
			move(West)

	if vertical <= verticalRev:
		for _ in range(vertical):
			if (Spec):
				quick_print('north: ', get_pos_y())
			move(North)
	else:
		for _ in range(verticalRev):
			if (Spec):
				quick_print('south: ', get_pos_y())
			move(South)
	if (Spec):
		quick_print('to: ', (get_pos_x(), get_pos_y()))
	# fpos = (get_pos_x(), get_pos_y())
	# quick_print('mvto',spos, fpos, pos, xdiff, xdir, ydiff, ydir)

def mvToTest():
	size = 5
	set_world_size(size)
	expects = [
		'West 1',
		'South 1',
		'East 2',
		'East 2, North 2',
		'North 2',
		'West1, South1'
	]
	it = [(4, 0), (0, 4), (0, 2), (2, 2), (2, 0), (4, 4)]
	for i in range(len(it)):
		mvTo((0, 0))
		mvTo(pos[i])
		quick_print(expects[i])

def mvToInDir(pos = (0, 0), vertical = North, hirozontal = East):
	now = get_pos_x(), get_pos_y()
	cantMove = False
	x = abs(pos[0] - now[0])
	y = abs(pos[1]- now[1])
	for _ in range(x):
		if can_move(hirozontal):
			move(hirozontal)
		else:
			cantMove = True
	for _ in range(y):
		if can_move(vertical):
			move(vertical)
		else:
			cantMove = True
	return not cantMove

# 配列を挿入ソートします
def memorySort(li):
	# gen index
	length = len(li)
	nl = []
	minV = min(li)
	for v in li:
		isInserted = False
		nllen = len(nl)
		for nli in range(nllen):
			if nl[nli] >= v:
				nl.insert(nli, v)
				isInserted = True
				break
		if not (isInserted):
			nl.insert(nllen, v)
	return nl

def debugHarvest(item):
	before = num_items(item)
	harvest()
	after = num_items(item)
	quick_print(after-before)

def initMaze(size):
	plant(Entities.Bush)
	substance = size * 2**(num_unlocked(Unlocks.Mazes) - 1)
	use_item(Items.Weird_Substance, substance)

def openingCheckeredLoop(size, wood = Entities.Bush):
	for x in range(size):
		for y in range(size):
			if can_harvest():
				harvest()
			if (x+y) % 2:
				plant(wood)
			elif (x >= size // 2):
				if (get_ground_type() == Grounds.Grassland):
					till()
				plant(Entities.Carrot)
			move(North)
		move(East)

def middleCheckeredLoop(size):
	# after unlocked sunflower, fertilizer
	for x in range(size):
		for y in range(size):
			if can_harvest():
				harvest()
			if (1 > y):
				if (get_ground_type() == Grounds.Grassland):
					till()
				plant(Entities.Sunflower)
			if (x+y) % 2:
				plant(Entities.Tree)
			elif (x >= size // 2):
				if (get_ground_type() == Grounds.Grassland):
					till()
				plant(Entities.Carrot)
			move(North)
		move(East)

def openingPumpkinHarvest(size):
	map = set()
	mvTo((0 ,0))
	for x in range(size):
		for y in range(size):
			if (get_ground_type() == Grounds.Grassland):
				till()
			plant(Entities.Pumpkin)
			move(North)
		move(East)

	for x in range(size):
		for y in range(size):
			if not can_harvest():
				if get_entity_type() == Entities.Dead_Pumpkin:
					plant(Entities.Pumpkin)
				map.add((x,y))
			move(North)
		move(East)

	while len(map) != 0:
		_map = set(map)
		for m in _map:
			mvTo(m)
			if not can_harvest():
				plant(Entities.Pumpkin)
			else:
				map.remove(m)

	harvest()

def pumpkinHarvest(size):
	# drone~4
	map = set()
	mvTo((0 ,0))
	def dronePlanter():
		for y in range(size):
			if (get_ground_type() == Grounds.Grassland):
				till()
			plant(Entities.Pumpkin)
			move(North)
	for x in range(size):
		if (max_drones() != num_drones()):
			spawn_drone(dronePlanter)
		else:
			dronePlanter()
		move(East)

	def droneMapping():
		_map = set()
		for y in range(size):
			if not can_harvest():
				if get_entity_type() == Entities.Dead_Pumpkin:
					plant(Entities.Pumpkin)
				_map.add((x,y))
			move(North)

		return _map

	drones = []
	results = []
	for x in range(size):
		if (max_drones() == num_drones()):
			results.append(droneMapping())
		else:
			drones.append(spawn_drone(droneMapping))
		move(East)

	for d in drones:
		# TODO: 同期通信 改善の余地あり
		results.append(wait_for(d))
	for r in results:
		for r2 in r:
			map.add(r2)

	while len(map) != 0:
		_map = set(map)
		for m in _map:
			mvTo(m)
			if not can_harvest():
				plant(Entities.Pumpkin)
			else:
				map.remove(m)

	harvest()




def polyPlant(entity):
	if (entity == Entities.Grass):
		if (get_ground_type() == Grounds.Soil):
			till()
	elif (entity == Entities.Carrot):
		if not (get_ground_type() == Grounds.Soil):
			till()
		plant(entity)
	else:
		plant(entity)

def polyHarvest(size):
	entity = [Entities.Grass, Entities.Tree, Entities.Carrot]
	for x in range(size):
		if not x % 4 == 0:
			move(East)
			continue
		for y in range(size):
			if can_harvest():
				if (num_items(Items.Fertilizer) > 5):
					use_item(Items.Fertilizer)
				harvest()

			target = entity[y % 3]
			polyPlant(target)
			c = get_companion()
			if not (c[1][0] == x):
				mvTo(c[1])
				polyPlant(c[0])
			mvTo((x,y + 1))
		move(East)

def polyHarvestV2(size):
	# drone~4count
	entity = [Entities.Grass, Entities.Tree, Entities.Carrot]

	def rowAction():
		for y in range(size):
			if can_harvest():
				harvest()

			target = entity[y % 3]
			polyPlant(target)
			c = get_companion()
			if c:
				if not (c[1][0] == x):
					mvTo(c[1])
					polyPlant(c[0])
			mvTo((x,y + 1))

	for x in range(size):
		if not x % 4 == 0:
			move(East)
			continue
		if (max_drones() != num_drones()):
			spawn_drone(rowAction)
		move(East)

def cactusHarvest(size):
	mvTo((0, 0))
	rSize = range(size)
	def initPlant():
		for x in rSize:
			if (get_ground_type() == Grounds.Grassland):
				till()
			plant(Entities.Cactus)
			use_item(Items.Fertilizer)

			move(East)
	drones = []
	for y in rSize:
		if num_drones() != max_drones():
			drones.append(spawn_drone(initPlant))
		else:
			initPlant()
		move(North)
	for d in drones:
		wait_for(d)
	# North | East
	def cactusSwap(axis):
		swapV = West
		if (axis != East):
			swapV = South
		pos = get_pos_x(), get_pos_y()
		now = measure()
		isSwapped = False
		target = measure(swapV)
		if (axis == East and pos[0] == 0) or (axis == North and pos[1] == 0):
			target = None

		if target:
			if (now < target):
				swap(swapV)
				isSwapped = True
		return isSwapped

	def rowAction(axis = East):
		initPos = get_pos_x(), get_pos_y()
		for a in rSize:
			while cactusSwap(axis):
				if (a == 0):
					break
				if axis == East:
					move(West)
				else :
					move(South)
			if axis == East:
				mvTo((a + 1, initPos[1]))
			else:
				mvTo((initPos[0], a + 1))
	mvTo((0,0))
	drones = []
	for x in rSize:
		if num_drones() != max_drones():
			drones.append(spawn_drone(rowAction))
		else:
			rowAction()
		move(North)
	for d in drones:
		wait_for(d)

	def northRowActionWrapper():
		rowAction(North)

	drones = []
	for y in rSize:
		if num_drones() != max_drones():
			drones.append(spawn_drone(northRowActionWrapper))
		else:
			northRowActionWrapper()
		move(East)
	for d in drones:
		wait_for(d)
	mvTo((0,0))

	harvest()

def runnerMaze():
	def checkTreasure():
		return get_entity_type() == Entities.Treasure

	def getDirection(lastPos):
		x = get_pos_x()
		y = get_pos_y()
		xdiff = lastPos[0]-x
		ydiff = lastPos[1]-y
		if (xdiff < 0 and ydiff == 0) :
			return 2
		elif (xdiff > 0 and ydiff == 0):
			return 4
		elif (xdiff == 0 and ydiff < 0):
			return 1
		elif (xdiff == 0 and ydiff > 0):
			return 3
		return 0

	def walkTo(direction):
		dirMap = [
			[West, North, East, South],
			[North, East, South, West],
			[East, South, West, North],
			[South, West, North, East]
		]
		dir = None
		for _dir in dirMap[direction - 1]:
			if can_move(_dir):
				dir = _dir
				break
		return move(dir)

	def action():
		lastPosition = [0, 0]

		while not checkTreasure():
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

	def setDrones():
		ws = get_world_size()
		quater = ws // 4
		droneMap = [
			[0, 0],
			[0, ws-1],
			[ws-1, 0],
			[ws-1, ws-1],
			[(ws-1)//2, (ws-1)//2],
			[quater, quater],
			[(ws-1) - quater, quater],
			[quater, (ws-1)-quater],
			[(ws-1)-quater, (ws-1)-quater],
		]
		pos = droneMap[num_drones() - 2]
		mvTo(pos)
		while not get_entity_type() == Entities.Hedge:
			pass
		return action()
	inited = False


	droneMaxCount = max_drones()
	if (droneMaxCount > 9):
		droneMaxCount = 9
	if (droneMaxCount == 1):
		action()
	else:
		for i in range(droneMaxCount):
			if (i == droneMaxCount - 1):
				# setTimeout()
				do_a_flip()
				pet_the_piggy()
				do_a_flip()
				pet_the_piggy()
				do_a_flip()
				initMaze(get_world_size())
				inited = True
				action()
			else:
				spawn_drone(setDrones)
		# while not (inited and measure() == None):
		# 	pass

def bulkMazeRunner():
	masterSize = get_world_size()
	# 4*4 / 5*5
	size = 4
	if (max_drones() > 25):
		size = 5
	mvTo((0,0))
	set_world_size(size)
	isCompleted = False
	maxCount = 300
	startItemCount = num_items(Items.Weird_Substance)
	upgradeCount = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
	afterCount = startItemCount - (upgradeCount * maxCount) + 200
	def checker():
		while num_items(Items.Weird_Substance) > afterCount :
			if get_entity_type() == Entities.Treasure:
				use_item(Items.Weird_Substance, upgradeCount)
		if get_entity_type() == Entities.Treasure:
			harvest()
	inited = False
	mvTo((0, 0), size)
	for x in range(size):
		for y in range(size):
			if (num_drones() != max_drones()):
				spawn_drone(checker)
			else:
				initMaze(size)
				checker()
				inited = True
			move(North)
		move(East)
	if not inited:
		initMaze(size)
	set_world_size(masterSize)



def dinoBasicRunner(size):
	clear()
	mvTo((0,0))
	change_hat(Hats.Dinosaur_Hat)
	canMove = True
	def cantMove():
		return can_move(North) == False and can_move(East) == False and can_move(South) == False and can_move(West) == False
	while canMove:
		i = 0
		for x in range(size):
			if (i == 0):
				success = mvToInDir((0, size - 1), North, East)
				if (not success or cantMove()):
					canMove = False
					break
			elif (x == (size -1)):
				success = mvToInDir((x, 0), South, East)
				if (not success or cantMove()):
					canMove = False
					break
				success = mvToInDir((0, 0), South, West)
				if (not success or cantMove()):
					canMove = False
					break

			elif (x % 2 == 1):
				success = mvToInDir((x, 1), South, East)
				if (not success or cantMove()):
					canMove = False
					break

			elif (x % 2 == 0):
				success = mvToInDir((x, size - 1), North, East)
				if (not success or cantMove()):
					canMove = False
					break

			i += 1
		if(cantMove()):
			canMove = False
	change_hat(Hats.Straw_Hat)


# Unlocks
# Unlocks.Auto_Unlock
# Unlocks.Cactus
# Unlocks.Carrots
# Unlocks.Costs
# Unlocks.Debug
# Unlocks.Debug_2
# Unlocks.Dictionaries
# Unlocks.Dinosaurs
# Unlocks.Expand
# Unlocks.Fertilizer
# Unlocks.Functions
# Unlocks.Grass
# Unlocks.Hats
# Unlocks.Import
# Unlocks.Leaderboard
# Unlocks.Lists
# Unlocks.Loops
# Unlocks.Mazes
# Unlocks.Megafarm
# Unlocks.Operators
# Unlocks.Plant
# Unlocks.Polyculture
# Unlocks.Pumpkins
# Unlocks.Senses
# Unlocks.Simulation
# Unlocks.Speed
# Unlocks.Sunflowers
# Unlocks.The_Farmers_Remains
# Unlocks.Timing
# Unlocks.Top_Hat
# Unlocks.Trees
# Unlocks.Utilities
# Unlocks.Variables
# Unlocks.Watering
