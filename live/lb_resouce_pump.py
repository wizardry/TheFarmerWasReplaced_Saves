from lb_resouce_utils import *

debug = True
# debug = False

# PumpkinRun is default has items None

# set_execution_speed(1000)
timer = get_time()
size = 32 #get_world_size()
# set_world_size(size)
rSize =  range(size)

finishCount = 200000000

cost = 512
# use Leaderboards.Pumpkin
def run():
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
					if measure() == measure(East):
						harvest()

	for x in rSize:
		if num_drones() != max_drones():
			spawn_drone(droneAction)
		else:
			droneAction(True)
		move(East)

	return None
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