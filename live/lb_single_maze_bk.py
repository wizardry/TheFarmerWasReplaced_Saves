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
# 1回の攻略で得られるGoldは2048。616448
# 設計方針：
# わからん、左手法。通常攻略で使ったもの持ってくる
def run():
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
		harvest()
		return True

	clear()
	while not state['items']['gold'] > 616448:
		plant(Entities.Bush)
		substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
		use_item(Items.Weird_Substance, substance)
		action()
		state['iterator'] += 1
		state['items']['gold'] += 2048


def runV2():
	clear()
	size = 2
	needSubstanceCount = size * 2**5
	isClear = False
	def goal():
		global isClear
		if get_entity_type() == Entities.Treasure:
			if (state['items']['gold'] > 616448):
				harvest()
				isClear = True
				return True
			elif (state['iterator'] > 300):
				beforegold = num_items(Items.Gold)
				harvest()
				afterGold = num_items(Items.Gold)
				state['iterator'] = 0
				initMaze(size)
				return True
			else:
				use_item(Items.Weird_Substance, needSubstanceCount)
				return True
		return False

	def cycle():
		fin = False
		rightCycle = [North, East, South, West]
		leftCycle = [North, West, South, East]

		retryCount = [0,1]
		isGoaled = False
		while not isGoaled:
			for r in retryCount:
				for rc in rightCycle:
					move(rc)
					if (goal()):
						isGoaled = True
						break
				if isGoaled:
					break
			for r in retryCount:
				for lc in leftCycle:
					move(lc)
					if (goal()):
						isGoaled = True
						break
				if isGoaled:
					break
		state['iterator'] += 1
		state['items']['gold'] += 128

	initMaze(size)
	while not isClear:
		cycle()

run()

quick_print(num_items(Items.Gold), state)
quick_print('Maze_single tick counts', get_tick_count())

