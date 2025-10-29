from lb_single_utils import *

# singleMazeRun is default has items Weird_Substance 1B, Power 1B

set_world_size(8)
# set_execution_speed(1)
notRankingFlg = False

size = 8 #get_world_size()
rSize =  range(size)

state = {
	'finishCount': 0,
	'iterator': 0,
	'items': {
		'gold': 0,
	},
}
# use Leaderboards.Maze_Single
# finish is num_items(Items.Gold) >= 616448
# 1回の攻略で得られる8x8でGoldは2048。616448
# 強化倍率x32
# 設計方針：
# わからん、左手法。通常攻略で使ったもの持ってくる

# こわれてるよ
def run():
	isClear = False
	def checkTreasure():
		return get_entity_type() == Entities.Treasure

	def getDirection(lastPos):
		x = get_pos_x()
		y = get_pos_y()
		xdiff = lastPos[0]-x
		ydiff = lastPos[1]-y
		if (xdiff < 0 and ydiff == 0) :
			return 2
		elif (xdiff > 0 and ydiff == 0):
			return 4
		elif (xdiff == 0 and ydiff < 0):
			return 1
		elif (xdiff == 0 and ydiff > 0):
			return 3
		return 0

	def walkTo(direction):
		dirMap = [
			[West, North, East, South],
			[North, East, South, West],
			[East, South, West, North],
			[South, West, North, East]
		]
		dir = None
		for _dir in dirMap[direction - 1]:
			if can_move(_dir):
				dir = _dir
				break
		return move(dir)

	def action():
		global isClear
		lastPosition = [0, 0]

		while not checkTreasure():
			if (measure() == None):
				break
			dir = getDirection(lastPosition)
			if (dir == None or dir == 0):
				lastPosition = [get_pos_x(), get_pos_y()]
				if not (walkTo(1)):
					print('Error: idk 1st')
			else:
				lastPosition = [get_pos_x(), get_pos_y()]
				if not (walkTo(dir)):
					print('Error: idk')
		if (state['items']['gold'] > 616448):
			harvest()
			isClear = True
		elif state['iterator'] > 300:
			harvest()
			state['items']['gold'] += 288
			state['iterator'] = 0
			initMaze(3)
		else:
			use_item(Items.Weird_Substance, 3*2**5)
			state['iterator'] += 1
			state['items']['gold'] += 512

		return True

	while not isClear:
		action()
initMaze(3)
run()
quick_print(num_items(Items.Gold), state)
quick_print('Maze_single tick counts', get_tick_count())

# v1: 左手法
# Maze_single tick counts 4652138
# v2: 2*2網羅型
# Maze_single tick counts 4501541