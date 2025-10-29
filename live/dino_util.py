from util_dev import *

apples = []

def dm(pos = (0, 0)):
	_pos = (get_pos_x(), get_pos_y())
	dir = (East, North)
	
	for i in range(1):
		diff = pos[i] - _pos[i]
		step = 1
		_dir = [West, South]	
		if (diff < 0):
			dir[i] = _dir[i]
			step = -1
		for x in range(_pos[i], pos[i], step):
			if not (move(dir[i])):
				return False
			next = measure()
			if not (next == None):
				apples.append(next)
	return True

def initPos():
	dm()

def getNextApple():
	return apples[len(apples) - 1]

def checkCanMove(start = (0, 0),target = (0, 0), end = None):
	a = getNextApple()
	if (end == None):
		end = start
	goWay = (abs(a[0]-start[0]), abs(a[1]-start[1]))
	endWay = (abs(start[0]-end[0]), abs(start[1]-end[1]))
	distance = (goway[0] + endWay[0], goway[1] + endWay[1])
	length = len(apples)
	return distance > length

def getDistance(poses = []):
	total = 0
	for i in range(len(poses)):
		if (i == 0):
			continue
		for i2 in range(1):
			total += abs(poses[i][i2] - poses[i -1][i2])
	return total
			
def t1Action():
	apples.append(measure())
	dm((1, 1))
	dm()

# 現在地からリンゴまで行き、一番近い画面端に移動する
def t2Action():
	moves = []
	pos = (get_pos_x(), get_pos_y())
	ap = getNextApple()
	# North, East, South, West
	# dirs = [North, East, South, West]
	poses = [(ap[0], size - 1), (size - 1, ap[1]), (ap[0], 0), (0, ap[1])]

	edges = [ap[1] - (size-1), ap[0] - (size - 1), ap[1], ap[0]]
	isEastEdge = ap[0] > threshold
	isNorthEdge = ap[1] > threshold
	_xdi = 1
	xA = edges[1]
	if not (isEastEdge):
		_xdi = 3
		xA = edges[3]

	_ydi = 0
	yA = edges[0]
	if not (isNorthEdge):
		_ydi = 2
		yA = edges[2]
	d = _xdi
	if (xA > yA):
		d = _ydi
	endPos = poses[d]
	if (checkCanMove(pos, ap, endPos)):
		moves.append(dm(ap))
		moves.append(dm(endPos))
	return False in moves

# 必ず(0, 0)からスタートしリンゴを取得して(0, 0)にもどる
def t3Action():
	moves = []
	moves.append(dm())
	
	ap = getNextApple()
	ways = [
		(0, 0),
		(0, size-1),
		ap,
		(0, 0),
	]
	distance = getDistance(ways)
	
	if (distance > len(apples) + 1):
		for way in ways:
			moves.append(dm(way))
	else:
		return False
	return False in moves
	
# 必ず(0, 0)からスタートしリンゴを取得する前後で距離調整を行い(0, 0)にもどる
# 距離調整を行うため y = 0 は帰り道としてかならず空ける
def t4Action():
	moves = []
	moves.append(dm())
	
	ap = getNextApple()
	