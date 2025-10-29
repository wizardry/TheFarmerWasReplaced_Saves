from lb_single_utils import *
debug = True
debug = False
# set_world_size(8)
# set_execution_speed(100000)
# set_execution_speed(2)
timer = get_time()

def run():
	size = 3
	rSize =  range(size)
	finishCount = 100000000
	set_world_size(size)
	carrotCost = 512
	map = {
		(0, 2): Entities.Bush,
		(1, 2): Entities.Bush,
		(2, 1): Entities.Bush,
		(2, 0): Entities.Bush,
	}
	for x in rSize:
		if(x == 2):
			break
		for y in rSize:
			plant(Entities.Bush)
			move(North)
		move(East)
	while not (num_items(Items.Hay) > finishCount and not debug):
		# debugHarvest(Items.Hay)
		harvest()

		if get_water() < 0.5:
			use_item(Items.Water)

		c = get_companion()

		while c[0] != Entities.Bush or c[1][0] == 2:
			# quick_print('while')
			# debugHarvest(Items.Hay)
			harvest()
			c = get_companion()

		move(North)
run()

quick_print('finished item counts:' + str(num_items(Items.Hay)))
quick_print('Hay_Single tick: '+ str(get_tick_count()) + ', time: ' + str(get_time() - timer))

# History
#
# use lb_single_util
# formtted to match other lb files
# V0 ?
# Hay_Single tick: ?, time: 400~
# V1 混作を被ってもよいが場所は固定になるよう以下ポジションで収穫する
# [(0, 0), (0, 4), (2, 6), (2, 2), (4, 0), (4, 4), (6, 6), (6, 2)]
# Hay_Single tick: 2176661, time:358.31
# V2 縦一列で毎回今作を行う。Hay間の移動距離を少なくかつ、成長をまたなくてよいためワールド端を利用した縦一列に限定する
# 咥え3マスは距離が遠いのでharvestしてキャンセルする
# Hay_Single tick: 3300117, time: 543.21
# V2 でx = 0 だった場合も無視する => Hay_Single tick: 3139967, time: 324.4
# V3 V2をもとに縦一列ではなく前後して回収する。それにより縦の混作率を上げる
# Hay_Single tick: 1781905, time: 293.3
# V5 V3の不要ifや妥協Errorによるmin化
# Hay_Single tick: 1714397, time: 282.18
# NOTE: V5 より早く行うことを考えると混作先に向かうとき、帰るときに収穫する必要がある
# しかし、その場合、tillの相互を行う必要、混作対象でなければ微々たるものという課題がある
# V5の行き帰りに収穫するようにした => MvToにharvest()直付けすると time: 357.52 ~　遅い
# V6 worldサイズを小さくした
# Hay_Single tick: 1695808, time: 279.16
# V7 ワールドサイズ3x3で0,0の1マス収穫のみ * 2点座標だと遅かった
# Hay_Single tick: 1412582, time: 232.53
# V7.1 水を0.9未満だったら上げるようにした。waterがあがれば最大0.1秒で成長する
# Hay_Single tick: 1410923, time: 232.26
# フル混作としても1秒間で6～8回収穫を目標にする必要がある
# 200tick 0.07秒として、移動、収穫、植える、移動、収穫が発生すると0.27 = 4回しかできない
# 毎回4回行動で収穫していると5分かかる。
# 3x3で全部Bush植えて1マスを混作運ゲーすると？
# v8 運ゲーを高速で回すのにcompanionを成長前収穫して高速に回す。
# Hay_Single tick: 1203152, time: 198.06


