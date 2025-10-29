from lb_resouce_utils import *

debug = True
debug = False

# WoodRun is default has items None

# set_world_size(32)
# set_execution_speed(1000)
timer = get_time()
size = 32 #get_world_size()
rSize =  range(size)

finishCount = 10000000000

cost = 512
# use Leaderboards.Wood
def run():
	def droneAction():
		while num_items(Items.Wood) < finishCount or debug:
			for y in rSize:
				if (x + y) % 2 == 1:
					move(North)
					continue
				if get_water() < 0.8:
					use_item(Items.Water)

				if can_harvest():
					harvest()

				plant(Entities.Tree)
				c = get_companion()

				while not (c[0] == Entities.Grass and (c[1][0] + c[1][1]) % 2 == 1):
					harvest()
					plant(Entities.Tree)
					c = get_companion()
				move(North)

	for x in rSize:
		if num_drones() != max_drones():
			spawn_drone(droneAction)
		else:
			droneAction()
		move(East)
run()
quick_print('finished item counts:' + str(num_items(Items.Wood)))
quick_print('Wood tick: '+ str(get_tick_count()) + ', time: ' + str(get_time() - timer))

# History
#
# V1: x4マス区切りで混植grassになるまで刈り取る。yは1マスずつ開ける
# Wood tick: 3612131, time: 594.6
# V2: 完全市松で逆市松が混植Grassになるように調整する
# Wood tick: 1835048, time: 302.07