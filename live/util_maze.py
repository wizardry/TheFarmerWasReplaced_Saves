from util_dev import *

def init():
	plant(Entities.Bush)
	substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
	use_item(Items.Weird_Substance, substance)


def checkTreasure():
	return get_entity_type() == Entities.Treasure


# 1. ドローンの方角を知るためには最後の位置と現在地を比較すればよい
# 2. 上右下左の優先順で都度判定し進む
# 3. 上1 右2 下3 左4として北が正面としてどこを向いているか返すものとする。移動失敗時には0を返す

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

# 意味無し
def adjustColumnWall():
	toMove()
	size = get_world_size()
	rSize = range(size)
	for x in rSize:
		for y in rSize:
			if x % 2 == 1:
				continue
			if y == 0 or y == (size - 1):
				move(North)
				continue
			plant(Entities.Bush)
			move(North)
		move(East)
	toMove()

	
