from lb_resouce_utils import *

# HayRun is default has items None

# set_world_size(32)
# set_execution_speed(1000)
timer = get_time()
size = 32 #get_world_size()
rSize =  range(size)

finishCount = 2000000000

# stateを更新してitemsで計測するのはコストが高いことが判明したので行わない。
# a += num => a = a + num => 2tick num_items(Items.hoge) => 1tick

CARRORT_COST = 512
# use Leaderboards.Hay
def run():
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
run()
quick_print('finished item counts:' + str(num_items(Items.Hay)))
quick_print('Hay tick: '+ str(get_tick_count()) + ', time: ' + str(get_time() - timer))

# History
#
# V1: dorone最大利用してwhile move(North)するだけ
# Hay tick: 48850517 time: 48850543
# V2: 32台がそれぞれの持ち場を設定して混作する。 なぜかrunしたときに倍速がうまくのらない
# Hay tick: 2347352, time: 386.4
# V3: V2を各上下移動させた
# Hay tick: 1451462, time: 238.93
# NOTE: PlanterとHarvesterにDoroneの役割を分けるとか？
# 平均2マス移動plant戻りとしてHayは2マス移動で成長しきるため概算値10~12台が常に動かせるなら強いかも
# harvesterがplanterをspawnすれば管理が楽そう