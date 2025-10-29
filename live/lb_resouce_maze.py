from lb_resouce_utils import *

debug = True
debug = False

# MazeRun is default has items None

# set_world_size(32)
# set_execution_speed(1000)
timer = get_time()
size = 32 #get_world_size()
rSize =  range(size)

finishCount = 9863168

cost = 512
# use Leaderboards.Maze
def run():
	return None

run()
quick_print('finished item counts:' + str(num_items(Items.Gold)))
quick_print('Maze tick: '+ str(get_tick_count()) + ', time: ' + str(get_time() - timer))

# History
#
# V1: