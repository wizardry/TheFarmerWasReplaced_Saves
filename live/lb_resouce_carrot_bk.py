from lb_resouce_utils import *

debug = False
# debug = True
# Carrot Run is default has items Wood 1B Hay 1B

# set_world_size(32)
# set_execution_speed(1000)
timer = get_time()
size = 32 #get_world_size()
rSize =  range(size)

finishCount = 2000000000
# startPoses = [(0, 0), (8, 0), (16, 0), (24, 0)]
COST = 512
# use Leaderboards.Carrots
def runV1():
	startPoses = [
		(0, 17), (0, 0),
		(4, 17), (4, 0),
		(8, 17), (8, 0),
		(12, 17), (12, 0),
		(16, 17), (16, 0),
		(20, 17), (20, 0),
		(24, 17), (24, 0),
		(28, 17), # (28, 0),
	]

	throwXPos = [0, 4, 8, 12, 16, 20, 24, 28]

	isCompleted = False
	def harvestAction(startPos, isOdd):
		mvTo(startPos)
		# {pos: entity}
		map = {}
		# get_companion()
		presentC = None
		index = 0
		thYpos = [16, 32]
		if (isOdd):
			thYpos = [-1, 17]
		toggleFlg = False

		def planter():
			moved = mvTo(presentC[1])
			harvest()
			palnted = plant(presentC[0])
			return moved and planted

		while True:
			if num_items(Items.Carrot) > finishCount and not debug:
				break
			if get_ground_type() == Grounds.Grassland:
				till()
				if num_items(Items.Water) > 16:
					use_item(Items.Water)
				plant(Entities.Carrot)

			dir = [North, South][toggleFlg]
			nowY = get_pos_y()
			if (dir == South):
				nextYpos = nowY - 1
				if nextYpos <= thYpos[0]:
					toggleFlg = False
			else:
				nextYpos = nowY + 1
				if nextYpos >= thYpos[1]:
					toggleFlg = True
			dir = [North, South][toggleFlg]


			if not can_harvest():
				if num_items(Items.Water) > 16:
					use_item(Items.Water)
				move(dir)
				index += 1
				continue

			presentC = get_companion()
			centity = presentC[0]
			cpos = presentC[1]
			if (cpos[0] in throwXPos):
				if can_harvest():
					harvest()

				# debugHarvest(Items.Carrot)
				plant(Entities.Carrot)
				move(dir)
				index += 1
				continue
			d = spawn_drone(planter)
			# ドローン最大数などで出せなかった場合
			if (d == None):
				continue

			# ここで詰まってるので要改良
			if (wait_for(d)):
				map[cpos] = centity

			if can_harvest():
				harvest()
				# debugHarvest(Items.Carrot)
				plant(Entities.Carrot)
			else:
				if num_items(Items.Water) > 16:
					use_item(Items.Water)
			move(dir)
			index += 1
		return True

	def harvester():
		posIndex = num_drones() - 2
		finish = harvestAction(startPoses[posIndex], posIndex % 2 == 1)
		return finish

	def mainHarvester():
		finish = harvestAction((28, 0), True)
		return finish
	# 0,0 は本体が回る
	for pos in startPoses:
		mvTo((pos[0], 0))
		spawn_drone(harvester)
		pass
	mvTo((28, 0))
	finish = mainHarvester()

	clear()
	return None
	throwXPos = [0, 4, 8, 12, 16, 20, 24, 28]

	def rowAction():
		for y in rSize:
			x = get_pos_x()
			def companioner():
				mvTo(c[1])
				harvest()
				plant(c[0])
			if not can_harvest():
				use_item(Items.Water)
			harvest()
			if (get_ground_type() == Grounds.Grassland):
				till()
			plant(Entities.Carrot)
			c = get_companion()
			if (c == None):
				move(North)
				continue
			if not c[1][0] in throwXPos:
				spawn_drone(companioner)
			move(North)

	while num_items(Items.Carrot) < finishCount or debug:
		for x in throwXPos:
			mvTo((x, 0))
			spawn_drone(rowAction)

	clear()
	return None
def runV2():
	throwXPos = [0, 4, 8, 12, 16, 20, 24, 28]

	def rowAction():
		for y in rSize:
			x = get_pos_x()
			def companioner():
				mvTo(c[1])
				harvest()
				plant(c[0])
			if not can_harvest():
				if (num_items(Items.Water) > 5):
					use_item(Items.Water)
			harvest()
			if (get_ground_type() == Grounds.Grassland):
				till()
			plant(Entities.Carrot)
			c = get_companion()
			if (c == None):
				move(North)
				continue
			if not c[1][0] in throwXPos:
				if spawn_drone(companioner) == None:
					quick_print('companioner dorone none', c)
			move(North)

	while num_items(Items.Carrot) < finishCount or debug:
		for x in throwXPos:
			mvTo((x, 0))
			if (num_drones() < max_drones() - 2):
				spawn_drone(rowAction)

	clear()
	return None
def runV3():
	def cellAction():
		y = get_pos_y()
		xavilablePos = [0, 4, 8, 12, 16, 20, 24, 28]
		while num_items(Items.Carrot) < finishCount or debug:
			for x in xavilablePos:
				if (get_ground_type() == Grounds.Grassland):
					till()
				if (get_entity_type() != Entities.Carrot):
					plant(Entities.Carrot)

				if get_water() < 0.5:
					use_item(Items.Water)

				# debugHarvest(Items.Carrot)
				harvest()

				plant(Entities.Carrot)

				c = get_companion()
				while not (c[0] == Entities.Grass and not (c[1][0] in xavilablePos)):
					harvest()
					plant(Entities.Carrot)
					c = get_companion()
				mvTo((x, y), size)

	for y in rSize:
		if num_drones() != max_drones():
			spawn_drone(cellAction)
		else:
			cellAction()
		move(North)

	clear()
	return None
def runV4():

	xavilablePos = [0, 4, 8, 12, 16, 20, 24, 28]
	def planter():
		y = get_pos_y()
		iy = num_drones()
		for iyy in range(iy):
			move(North)
		while True:
			for y in rSize:
				if (get_ground_type() == Grounds.Grassland):
					till()
				if get_water() < 0.5:
					use_item(Items.Water)

				plant(Entities.Carrot)

				c = get_companion()
				while not (c != None and c[0] == Entities.Grass and not (c[1][0] in xavilablePos)):
					harvest()
					plant(Entities.Carrot)
					c = get_companion()
				move(North)

	def harvester():
		y = get_pos_y()
		while num_items(Items.Carrot) < finishCount or debug:
			for y in rSize:
				c = get_companion()
				if (c != None and c[0] == Entities.Grass and not (c[1][0] in xavilablePos)):
					# debugHarvest(Items.Carrot)
					if can_harvest():
						harvest()
				move(North)

	for x in xavilablePos:
		mvTo((x, 0), size)
		spawn_drone(planter)
		spawn_drone(planter)
		spawn_drone(planter)
		if num_drones() != max_drones():
			spawn_drone(harvester)
		else:
			harvester()

	clear()
	return None
def runV5():
	# hh = [Hats.Gray_Hat, Hats.Green_Hat, Hats.Pumpkin_Hat, Hats.Purple_Hat]
	availablePos = [0, 8, 16, 24]
	xavailablePos = [0, 4, 8, 12, 16, 20, 24, 28]
	idnexes = [
		[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7],
		[1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7],
		[2, 0], [2, 1], [2, 2], [2, 3], [2, 4], [2, 5], [2, 6], [2, 7],
		[3, 0], [3, 1], [3, 2], [3, 3], [3, 4], [3, 5], [3, 6], [3, 7],
	]
	def cellAction(main = False):
		n = num_drones() - 2
		if (main):
			n = 31

		# change_hat(hh[n % 4])
		index = idnexes[n][0]
		xindex = idnexes[n][1]
		minY = availablePos[index]
		if index == 3:
			maxY = size - 1
		else:
			maxY = availablePos[index + 1] - 1
		rangeYs = [range(minY, maxY), range(maxY, minY, -1)]

		x = xavailablePos[xindex]

		toggleFlg = False
		mvTo((x, minY), size)
		while num_items(Items.Carrot) < finishCount or debug:

			for y in rangeYs[toggleFlg]:
				if (get_ground_type() == Grounds.Grassland):
					till()
				if (get_entity_type() != Entities.Carrot):
					plant(Entities.Carrot)
				if get_water() < 0.7:
					use_item(Items.Water)

				if not can_harvest():
					mvTo((x, y), size)
					continue
				# debugHarvest(Items.Carrot)
				harvest()

				a = plant(Entities.Carrot)
				c = get_companion()
				while not (c[0] == Entities.Grass and not (c[1][0] in xavailablePos)):
					harvest()
					plant(Entities.Carrot)
					c = get_companion()
				mvTo((x, y), size)
			toggleFlg = not toggleFlg
	for d in range(max_drones()):
		if num_drones() == max_drones():
			cellAction(True)
		else:
			spawn_drone(cellAction)
		pass
	clear()
	return None
runV1()
quick_print('finished item counts:' + str(num_items(Items.Carrot)))
quick_print('Carrots tick: '+ str(get_tick_count()) + ', time: ' + str(get_time() - timer))

# History
#
# V0: 各32台のドローンが上下往復をしながら混作を行う
#  -> 成長まで待機しっぱなしによる計測不能
# V0.1: Harvesterがqueueを入れてPlanterがQueueからcompanionを植える
#  -> スポーンしたドローンはスポーン時のglobal変数を複製し、イミュータブルに自身のスコープ内に変数をコピーするため
#     親に子の情報を伝えることが出来ず完全同期は断念した
# v1: 混作が収穫対象に被らないよう4xの一列を行き来する。また、ドローンがおいついてしまうと収穫後に混作取得しようとしてコケるので各半分を行き来する。混作を植えるのはドローンに任せる
# Carrots tick: 3364716, time: 553.87
# V2: 混作が被らない8列にMap処理など考えずにドローン処理させる
# Carrots tick: 3155181, time: 519.38

