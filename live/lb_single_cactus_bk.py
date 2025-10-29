from lb_single_utils import *

# singlePumpkinRun is default has items carrot 1B and power 1B

set_world_size(8)
# set_execution_speed(1)

notRankingFlg = False

size = 8 #size
rSize =  range(size)

state = {
	'finishCount': 0,
	'iterator': 0,
}

# use Leaderboards.Pumpkin_Single
# finish is num_items(Items.Pumpkin) >= 131072

# pupkin 1 = 512, 2x2 = 4096
# 設計方針：
# 8x8を最大効率で収穫を繰り返すのがよさそう

def run():
	startPosition = (0, 0)
	def plantCactus():
		for x in rSize:
			for y in rSize:
				till()
				plant(Entities.Cactus)
				move(North)
			move(East)
		mvTo()

	def singleSort(vector):
		if (North == vector):
			if(get_pos_y() == size - 1):
				return False
		if (South == vector):
			if(get_pos_y() == 0):
				return False
		if (East == vector):
			if(get_pos_x() == size - 1):
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
		for a in rSize:
			isSorted = singleSort(vector)
			if (isSorted):
				for a2 in range(a):
					move(reverseMap[vector])
					if not (singleSort(vector)):
						move(vector)
						break
					else:
						if (vector in [North, South]):
							mvTo((startPosition[0], startPosition[1] + a - (a2 + 1)))
						else:
							mvTo((startPosition[0] + a - (a2 + 1), startPosition[1]))

			if (vector in [North, South]):
				yy = a + 1
				if (yy >= size):
					yy -= 1
				mvTo((startPosition[0], yy))
			else:
				xx = a + 1
				if (xx >= size):
					xx -= 1

				mvTo((xx, startPosition[1]))
	def sortCactus():
		for x in rSize:
			mvTo((x, 0))
			columnSort(size, North)
		mvTo((startPosition[0], startPosition[1]))
		for y in rSize:
			mvTo((0, y))
			columnSort(size, East)
	plantCactus()
	sortCactus()
	harvest()

def runV2():
	# { y: measure[]}
	yms = {}
	xms = {}

	# plant and genMapping
	# measureの入れ替えが面倒だが一つ手前のものをこのフェーズでswapしてしまってもよいのでは？
	for y in rSize:
		for x in rSize:
			till()
			plant(Entities.Cactus)
			m = measure()
			# 一方向のSortをするともう一方向のmapは崩壊するためx軸のみMapを作成する
			if not (y in xms):
				xms[y] = []
			xms[y].append(m)
			move(East)
		move(North)
	# wip
	# (before: i[], v[])
	# (before: (i, v)[])
	# (before: {i, v}[] )
	def indexOf(v, l):
		for i in range(len(l)):
			if v == l[i]:
				return i
		return None
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


	# axis x sorting
	for y in rSize:
		horizonValues = xms[y]
		sortedValues = memorySort(horizonValues)
		for x in rSize:
			# value = horizonValues[y]
			value = horizonValues[0]
			ans = sortedValues[x]
			if not (x in yms):
				yms[x] = []
			yms[x].append(ans)

			if (ans == value):
				horizonValues.pop(0)
				move(East)
				continue

			popedTargetIndex = indexOf(ans, horizonValues)
			mvTo((popedTargetIndex + x, y))
			moveCount = -popedTargetIndex
			direction = West
			if moveCount > 0:
				direction = East

			for i in range(abs(moveCount)):
				swap(West)
				move(direction)
			t = horizonValues[popedTargetIndex]
			horizonValues.pop(popedTargetIndex)
			# horizonValues.insert(x, t)

			move(East)
		move(North)

	# axis y sorting
	for x in rSize:
		verticalValues = yms[x]
		sortedValues = memorySort(verticalValues)
		for y in rSize:
			# value = verticalValues[y]
			value = verticalValues[0]
			ans = sortedValues[y]

			if (ans == value):
				verticalValues.pop(0)
				move(North)
				continue
			popedTargetIndex = indexOf(ans, verticalValues)
			mvTo((x, popedTargetIndex + y))
			moveCount = -popedTargetIndex
			direction = South
			if moveCount > 0:
				direction = North

			for i in range(abs(moveCount)):
				swap(South)
				move(direction)
			t = verticalValues[popedTargetIndex]
			verticalValues.pop(popedTargetIndex)
			# verticalValues.insert(y, t)

			move(North)
		move(East)
	harvest()

def runV3():
	# dir = West | South

	def sortDescSwap(dir = West):
		m = measure()
		cm = measure(dir)
		if (m < cm):
			return swap(dir)
		return False
	def sortAscSwap(dir = East):
		m = measure()
		cm = measure(dir)
		if (None in [m, cm]):
			return False
		if (m > cm):
			return swap(dir)
		return False

	def rowSort(v, i):
		indexMap = [West, South]
		posMap = (get_pos_x(), get_pos_y())
		for i2 in range(i):
			sorteds = []
			sorteds.append(sortDescSwap(West))
			sorteds.append(sortAscSwap(East))
			sorteds.append(sortDescSwap(South))
			sorteds.append(sortAscSwap(North))
			if not (True in sorteds):
				break
			move(indexMap[v])
		mvTo(posMap)

	# measureの入れ替えが面倒だが一つ手前のものをこのフェーズでswapしてしまってもよいのでは？
	for y in rSize:
		for x in rSize:
			till()
			plant(Entities.Cactus)
			# ついでにソートできるのをしちゃう
			if (x != 0):
				sortDescSwap(West)
			if (x != size - 1):
				sortAscSwap(East)
			if (y != 0):
				sortDescSwap(South)
			if (y != size - 1):
				sortAscSwap(North)
			move(East)
		move(North)

	for v in [0, 1]:
		dirMap = [East, North]
		swapDirMap = [West, South]
		for i in rSize:
			for i2 in rSize:
				rowSort(v, i2)
				move(dirMap[v])
			move(dirMap[not v]) # 0,1 のBool反転
	harvest()

def runV4():
	map = {}
	mkeyMap = {0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[],}
	# measureの入れ替えが面倒だが一つ手前のものをこのフェーズでswapしてしまってもよいのでは？
	for y in rSize:
		for x in rSize:
			till()
			plant(Entities.Cactus)
			m = measure()
			map[(x,y)] = m
			mkeyMap[m].append((x,y))
			move(East)
		move(North)

	sortedMap = {}
	count = 0
	for m in mkeyMap:
		for pos in mkeyMap[m]:
			y = count // size
			x = count % size
			sortedMap[(x,y)] = m
			count += 1

	direction = [[West, East], [South, North]]
	for spos in sortedMap:
		# find
		_pos = None
		for pos in map:
			if (map[pos] == sortedMap[spos]):
				_pos = pos
				break
		mvTo(_pos)
		# x,y
		for p in [0, 1]:
			diff = _pos[p] - spos[p]
			diffI = 0
			if (diff < 0):
				diffI = 1
			for i in range(abs(diff)):
				swap(direction[p][diffI])
				map[(get_pos_x(), get_pos_y())] = measure()
				move(direction[p][diffI])
		map.pop(spos)
	harvest()

def runV5():
	for x in rSize:
		for y in rSize:
			till()
			plant(Entities.Cactus)
			move(North)
		move(East)

	axises = [[East, West], [North, South]]
	for v in [0, 1]:
		for x in rSize:
			isComp = False
			# defPos = [(0,x), (x,0)]
			# mvTo(defPos[x])
			while not isComp:
				for l in [0, 1]:
					isFilterling = False
					for y2 in rSize:
						cp = measure(axises[v][l])
						np = measure()
						f = [np > cp, np < cp]
						f2 = [y2 == size - 1, y2 == 0]
						if (f[l] and not f2[l]):
							swap(axises[v][l])
							isFilterling = True
						move(axises[v][l])
					if (not isFilterling):
						isComp = True
						break
			move(axises[not v][0])
	harvest()

clear()
runV2()

quick_print(num_items(Items.Cactus), state)
quick_print('Cactus_single tick counts', 'tick: '+ str(get_tick_count()), 'time: '+str(get_time()))

# v1: Cactus_single tick counts tick: 149945 time: 24.68


