from lb_resouce_utils import *

debug = True
debug = False

# DinoRun is default has items None

# set_world_size(32)
# set_execution_speed(1000)
timer = get_time()
size = 32 #get_world_size()
rSize =  range(size)

finishCount = 33488928

cost = 512
# use Leaderboards.Dino
def run():
	return None

run()
quick_print('finished item counts:' + str(num_items(Items.Bone)))
quick_print('Dino tick: '+ str(get_tick_count()) + ', time: ' + str(get_time() - timer))

# History
#
# V1: