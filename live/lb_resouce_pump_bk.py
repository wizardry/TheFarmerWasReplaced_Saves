from lb_resouce_utils import *

debug = True
debug = False

# PumpkinRun is default has items None

# set_world_size(32)
# set_execution_speed(1000)
timer = get_time()
size = 32 #get_world_size()
rSize =  range(size)

finishCount = 200000000

cost = 512
# use Leaderboards.Pumpkin
def runV1():
	deads = []
	deadsIndex = 0
	def rowPlanter():
		for y in rSize:
			if (get_ground_type() == Grounds.Grassland):
				till()
			plant(Entities.Pumpkin)
			move(North)
	def rowChecker():
		_deads = set()
		x = get_pos_x()
		for y in rSize:
			if not can_harvest():
				_deads.add((x,y))
				if get_entity_type() == Entities.Dead_Pumpkin:
					plant(Entities.Pumpkin)
			move(North)
		return _deads
	def riser():
		n = num_drones() - 2
		m = max_drones() - 1
		length = len(deads)
		rang = length // m
		slice = [n*rang, (n*rang)+rang]
		if (n + 1 == m):
			slice[1] = None
		targets = deads[slice[0]:slice[1]]
		res = targets[0:]
		while len(targets) != 0:
			_targets = targets[0:]
			for target in _targets:
				mvTo(target, size)
				if not can_harvest():
					if get_water() < 0.5:
						use_item(Items.Water)
					if get_entity_type() == Entities.Dead_Pumpkin:
						plant(Entities.Pumpkin)
				else:
					targets.remove(target)
		return res

	# planting
	while num_items(Items.Pumpkin) < finishCount or debug:
		for y in rSize:
			if num_drones() != max_drones():
				spawn_drone(rowPlanter)
			else:
				rowPlanter()
			move(East)

		# check
		drones = []
		for y in rSize:
			if num_drones() != max_drones():
				drones.append(spawn_drone(rowChecker))
			else:
				rowChecker()
			move(East)
		_drones = drones[0:]
		for d in _drones:
			res = wait_for(d)
			for r in res:
				deads.append(r)
			drones.remove(d)

		# rise
		while len(deads) != 0:
			_deads = deads[0:]
			length = len(deads)
			rang = max_drones() - 1
			loop = length
			drones = []

			if length < rang:
				loop = rang
			for _ in range(loop):
				if num_drones() != max_drones():
					drones.append(spawn_drone(riser))

			while len(drones) != 0:
				_drones = set()
				for d in drones:
					_drones.add(d)
					res = wait_for(d)
					for r in res:
						if r in deads:
							deads.remove(r)
				for d in _drones:
					drones.remove(d)
		# harvest()
		debugHarvest(Items.Pumpkin)
def runV2(): #inbag
	index = 0
	initPoses = [
		[(0, 0), (9, 0), (0, 9), (9, 9),],
		[(0, 11), (9, 11), (0, 20), (9, 20),],
		[(0, 22), (9, 22), (0, 31), (9, 31),],
		[(11, 0), (20, 0), (11, 9), (20, 9),],
		[(11, 11), (20, 11), (11, 20), (20, 20),],
		[(11, 22), (22, 22), (11, 31), (20, 31),],
		[(22, 0), (20, 0), (22, 9), (20, 9),],
		[(22, 11), (20, 11), (22, 20), (20, 20),],
		[(22, 22), (22, 22), (22, 31), (20, 31),],
	]
	def planter(main = False, size = 10):
		group = initPoses[index // 4]
		groupIndex = index % 4
		initPos = group[groupIndex]
		# mvToInDir(initPos)
		minY = group[0][1]
		maxY = group[3][1]
		minX = group[0][0]
		maxX = group[3][0]

		quick_print(index, group, groupIndex, initPos, size)
		quick_print(' >:',main,minY,maxY,minX,maxX)
		initDirs = [
			(East, North),
			(West, North),
			(East, South),
			(West, South),
		][groupIndex]
		revDirs = [
			(West, South),
			(East, South),
			(West, North),
			(East, North),
		][groupIndex]
		yDirFlg = 0
		xDirFlg = 0
		while num_items(Items.Pumpkin) < finishCount or debug:
			mvTo(initPos, 32)
			for x in range(size):
				for y in range(size):
					if (get_pos_x() == 0 and get_pos_y() == 10):
						pass
					if (get_ground_type() == Grounds.Grassland):
						till()
					plant(Entities.Pumpkin)
					if y == size - 1:
						yDirFlg = not yDirFlg
					else:
						move([initDirs, revDirs][yDirFlg][1])
				if x == size - 1:
					xDirFlg = not xDirFlg
				else:
					move([initDirs, revDirs][xDirFlg][0])

			map = set()
			for x in range(size):
				for y in range(size):
					if get_water() < 0.5:
						use_item(Items.Water)
					if not can_harvest():
						map.add((get_pos_x(), get_pos_y()))
						plant(Entities.Pumpkin)
					if y == size - 1:
						yDirFlg = not yDirFlg
					else:
						move([initDirs, revDirs][yDirFlg][1])
				if x == size - 1:
					xDirFlg = not xDirFlg
				else:
					move([initDirs, revDirs][xDirFlg][0])


			while len(map) != 0:
				_map = set(map)
				for p in _map:
					mvTo(p)
					if can_harvest():
						map.remove(p)
					else:
						plant(Entities.Pumpkin)
			harvest()

	for d in range(max_drones()):
		if num_drones() != max_drones():
			spawn_drone(planter)
		else:
			planter(True)
		index += 1
def runV3():
	def droneAction(main = False):
		while num_items(Items.Pumpkin) < finishCount or debug:
			for y in rSize:
				if not can_harvest() and get_water() < 0.5:
					use_item(Items.Water)
				if (get_ground_type() == Grounds.Grassland):
					till()
				p = plant(Entities.Pumpkin)
				move(North)
			if main:
				harvest()

	for x in rSize:
		if num_drones() != max_drones():
			spawn_drone(droneAction)
		else:
			droneAction(True)
		move(East)

	return None
def runV4():
	set_world_size(16)

	def droneAction(main = False):
		while num_items(Items.Pumpkin) < finishCount or debug:
			for y in rSize:
				if not can_harvest() and get_water() < 0.5:
					use_item(Items.Water)
				if (get_ground_type() == Grounds.Grassland):
					till()
				p = plant(Entities.Pumpkin)
				move(North)
			if main:
				harvest()

	def droneRevAction(main = False):
		while num_items(Items.Pumpkin) < finishCount or debug:
			for y in rSize:
				if not can_harvest() and get_water() < 0.5:
					use_item(Items.Water)
				if (get_ground_type() == Grounds.Grassland):
					till()
				p = plant(Entities.Pumpkin)
				move(South)
			if main:
				harvest()
	for x in range(16):
		if num_drones() != max_drones():
			spawn_drone(droneAction)
		else:
			droneAction(True)
		move(East)
	move(South)
	for x in range(16):
		if num_drones() != max_drones():
			spawn_drone(droneAction)
		else:
			droneAction(True)
		move(East)

	return None

def runV5():
	set_world_size(8)
	def droneAction():
		while True:
			if (get_ground_type() == Grounds.Grassland):
				till()
			if not can_harvest():
				if get_water() < 0.5:
					use_item(Items.Water)
			plant(Entities.Pumpkin)
			move(North)

	for y in range(8):
		for x in range(8):
			spawn_drone(droneAction)
			move(East)
			if (num_drones() == max_drones()):
				break
		move(North)
		if (num_drones() == max_drones()):
			break

	# main drone action
	while num_items(Items.Pumpkin) < finishCount or debug:
		if can_harvest():
			debugHarvest(Items.Pumpkin)
	return None
def runV6(): #多分V6
	def finish()
		return num_items(Items.Pumpkin) < finishCount or debug:
	if debug:
		clear()
	def droneAction(main = False):
		ms = []
		x = get_pos_x()

		while finish():
			notReadies = set()
			for i in rSize:
				notReadies.add((x,i))
			while len(notReadies) != 0:
				_r = set(notReadies)
				for pos in _r:
					mvTo(pos)
					if (get_ground_type() == Grounds.Grassland):
						till()
					plant(Entities.Pumpkin)
					if main:
						m = measure()
						me = measure(East)
						if m == me:
							harvest()
							break
					if not can_harvest():
						if get_water() < 0.5:
							use_item(Items.Water)
						if len(notReadies) == 1:
							use_item(Items.Fertilizer)
					else:
						notReadies.remove(pos)
	for x in rSize:
		if num_drones() != max_drones():
			spawn_drone(droneAction)
		else:
			droneAction(True)
		move(East)

def runV7():
	def finish():
		return num_items(Items.Pumpkin) < finishCount or debug
	if debug:
		clear()
	completedRow = set()
	notCompletedRow = set()
	# どうせDead_Pumpkinは出るのでメインはドローン出しに専念する
	# map {(x,y)}を作ると重いのでmeasureが単一であるかどうかだけを返す
	def droneAction(isNorth = True):
		x = get_pos_x()
		fail = set()
		for y in rSize:
			if (get_ground_type() == Grounds.Grassland):
				till()
			if not can_harvest():

				plant(Entities.Pumpkin)
				fail.add(y)
				if get_water() < 0.5 and len(notCompletedRow) < 10:
					use_item(Items.Water)
				if len(notCompletedRow) == 1:
					use_item(Items.Fertilizer)
			move([North, South][isNorth])
		quick_print(fail, len(fail))
		return x,len(fail)
	def droneActionWrapperN():
		res = droneAction(True)
		return res
	def droneActionWrapperS():
		res = droneAction(False)
		return res
	def mainDroneAction():
		while finish():
			initpos = get_pos_x()
			notCompletedRow = set()
			drones = []
			for x in rSize:
				notCompletedRow.add((initpos + x) % size)
			while len(notCompletedRow) != 0:
				xes = set(notCompletedRow)
				for x in xes:
					mvTo((x,0), size)
					m = measure()
					ms = measure(South)
					if m == ms and m != None:
						harvest()
						notCompletedRow = set()
						break
					if num_drones() != max_drones():
						drones.append(spawn_drone(droneActionWrapperS))
					if num_drones() != max_drones():
						drones.append(spawn_drone(droneActionWrapperN))
					_d = list(drones)
					for d in _d:
						if has_finished(d):
							pos, length = wait_for(d)
							if length == 0 and pos in notCompletedRow:
								notCompletedRow.remove(pos)
							drones.remove(d)

	mainDroneAction()


run()
quick_print('finished item counts:' + str(num_items(Items.Pumpkin)))
quick_print('Pumpkin tick: '+ str(get_tick_count()) + ', time: ' + str(get_time() - timer))

# History
#
# V1: 32x32 巨大カボチャの作成
# Pumpkin tick: 6171170, time: 1015.84
# V2: 10x10 サイズのカボチャを各地に作成。1か所につき5台のドローンを並行稼働する
# Pumpkin tick: 5709587, time: 939.86 ややバグありだが相当遅いので断念
# V3 32列で植え、合否に関わらずmainがharvestする
# Pumpkin tick: 3693961, time: 608.07
# V4 2方向から植えて合否にかかわらず毎回左下のみharvestする
# Pumpkin tick: 8585257, time: 1413.23
# V5 6x6サイズに敷き詰めて真下だけ判定する。本体は残り4マスの状態を取り動的に上に行く
# 30minutes ~ 測定不能 5x5でmeasureで同一個体か確かめる方法も同様
# V6 V3と同等だがmeasure同一値が6回続けば収穫するロジックを全ドローンにつめた
# Pumpkin tick: 3628662, time: 597.32
# V7 上下にドローンを出してクロスで植える
# Pumpkin tick: 5887692, time: 969.18