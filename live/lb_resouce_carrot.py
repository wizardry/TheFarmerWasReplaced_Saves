from lb_resouce_utils import *

debug = False
# debug = True
# Carrot Run is default has items Wood 1B Hay 1B

# set_world_size(32)
set_execution_speed(100)
timer = get_time()
size = 32 #get_world_size()
rSize =  range(size)

finishCount = 2000000000

COST = 512
# use Leaderboards.Carrots
def run():
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
run()
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
# Carrots tick: 2832896, time: 466.33
# V3: companionがGrassでなければ成長前に刈り取る
# Carrots tick: 2406020, time: 396.06
# V4: 混作機と収穫機にわけて8列で動かす。なお列数を下げれば下げるほど遅くなる
# Carrots tick: 2252396, time: 370.74
# V5 V3ロジックで横移動から移動の無駄を減らすため各32台が上下移動するように変更
# Carrots tick: 1643633, time: 270.53 <- 20251029T0:29 WR13!
