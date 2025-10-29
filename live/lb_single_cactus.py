from lb_single_utils import *

# singleCactusRun is default has items carrot 1B and power 1B

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

# 全面ソート = 131072
# 設計方針：
# Moveを行う際は必ずSwapも同時に行う。
# なぜならActionは重い処理でMoveのみを行っている場合同じ場所の移動が増えるからである
# また、そうした場合最も効果的だと思われるのはMappingを済ませた状態での遠距離移動が発生するSort
# したがって、bucket Sortで初回にDict上でSortが完了され、指定位置に対象を移動するロジックを採用する
def run():
	map = {}
	popedMap = set()
	popedSortedMap = set()
	mkeyMap = {0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[],}
	def getAllMeasure():
		return (measure(), [measure(North), measure(East), measure(South), measure(West)])
	# return Bool
	# swapとmapの設置まで行う
	# def plantingSwap ():
	# 	# now, south, west
	# 	pos = (get_pos_x(), get_pos_y())

	# 	ms = [measure(), measure(South), measure(West)]
	# 	if (ms[1] != None and ms[0] < ms[1] and pos[1] != 0):
	# 		swap(South)
	# 		_m = [ms[1], ms[0], ms[2]]
	# 		ms = _m
	# 		map[(pos[0], pos[1] - 1)] = ms[1]
	# 	if (ms[2] != None and ms[0] < ms[2] and pos[0] != 0):
	# 		swap(West)
	# 		_m = [ms[2], ms[1], ms[0]]
	# 		ms = _m
	# 		map[(pos[0] - 1, pos[1])] = ms[2]
	# 	map[pos] = ms[0]
	# throeDict = 'x' | 'y'
	def allSwap ():
		# now, south, west
		pos = (get_pos_x(), get_pos_y())
		m = measure()
		ms = [measure(North), measure(East), measure(South), measure(West)]
		if (ms[0] != None):
			if (pos[1] != size - 1):
				tagpos = (pos[0], pos[1] + 1)
				if not (tagpos in popedMap):
					if(m > ms[0]):
						swap(North)
						m, ms = getAllMeasure()
						map[tagpos] = ms[0]
		if (ms[1] != None):
			if (pos[0] != size - 1):
				tagpos = (pos[0] + 1, pos[1])
				if not (tagpos in popedMap):
					if(m > ms[1]):
						swap(East)
						m, ms = getAllMeasure()
						map[tagpos] = ms[1]
		if (ms[2] != None):
			if (pos[1] != 0):
				tagpos = (pos[0], pos[1] - 1)
				if not (tagpos in popedMap):
					if (m < ms[2]):
						swap(South)
						m, ms = getAllMeasure()
						map[tagpos] = ms[2]
		if (ms[3] != None):
			if (pos[0] != 0):
				tagpos = (pos[0] - 1, pos[1])
				if not (tagpos in popedMap):
					if (m < ms[3]):
						swap(West)
						m, ms = getAllMeasure()
						map[tagpos] = ms[3]
		map[pos] = m
	def throwSwap(direction):
		# [5,0]	に [4,4] のものを持ってきたいときなど大小判定を行いたくない移動がある
		# Northは原則通らないはず

		swap(direction)
		m, ms = getAllMeasure()
		map[(pos[0] + 1, pos[1])] = ms[1]

	# measureの入れ替えが面倒だが一つ手前のものをこのフェーズでswapしてしまってもよいのでは？
	for y in rSize:
		for x in rSize:
			till()
			plant(Entities.Cactus)
			allSwap()
			move(East)
		move(North)

	for pos in map:
		mkeyMap[map[pos]].append(pos)
	sortedMap = {}
	count = 0
	for m in mkeyMap:
		for pos in mkeyMap[m]:
			y = count // size
			x = count % size
			sortedMap[(x,y)] = m
			count += 1

	quick_print(map)
	quick_print(sortedMap)

	direction = [[West, East], [South, North]]
	throwAxises = ['x', 'y']
	for spos in sortedMap:
		mvTo(spos) # 本来不要のはずだがわかりやすくするために
		sortedMapMeasure = sortedMap[spos]
		# if (map[spos] == sortedMapMeasure):
		# 	map.pop(spos)
		# 	continue
		# find
		_pos = None
		for pos in map:
			if (map[pos] == sortedMapMeasure):
				_pos = pos
				break
		# 目的地にいく
#		mvTo(_pos)
		nowPos = (get_pos_x(), get_pos_y())
		for p in [0, 1]:
			diff = nowPos[p] - _pos[p]
			diffI = 0
			if (diff < 0):
				diffI = 1
			debugM = []
			for i in range(abs(diff)):
				if i >= abs(diff) - 2:
					allSwap()
				move(direction[p][diffI])
				debugM.append(measure())
		quick_print('targetmoved: ', get_pos_x(), get_pos_y(), pos, measure(), debugM)

		# x,y
		quick_print(map)
		# spos = 運ぶ場所、pos = 対象のmeasureがあるpos
		quick_print(spos, _pos)
		# 運びながら戻す
		for p in [0, 1]:
			diff = _pos[p] - spos[p]
			diffI = 0
			if (diff < 0):
				diffI = 1
			for i in range(abs(diff)):
				throwSwap(direction[p][diffI])
				move(direction[p][diffI])
		quick_print('rf:', get_pos_x(), get_pos_y(), spos)
		map.pop(spos)
		popedMap.add(spos)
	harvest()
run()
quick_print(num_items(Items.Cactus), state)
quick_print('Cactus_single tick counts', 'tick: '+ str(get_tick_count()), 'time: '+str(get_time()))

# v1(buble sort):
#   Cactus_single tick counts tick: 149945 time: 24.68
# v2(memory sort):
#   Cactus_single tick counts tick: 153548 time: 25.28
# v3(all dir swap) AvgはV1V2よりはやい こわれてる bk でまわしてたっぽい
#   Cactus_single tick counts tick: 157464 time: 25.92
# v4(all mapping backet sort)
#   Cactus_single tick counts tick: 148839 time: 24.5
# v5(shaker sort AIがノームより効率いいとかほざいてたので)
#   Cactus_single tick counts tick: 171488 time: 28.23 #激おそやないか死ねCopilot
