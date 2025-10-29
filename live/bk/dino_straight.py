from dino_util import *

size = get_world_size()
rSize = range(size)
# [(x, y), (x, y)...]
aPoses = []

def init():
	toMove()
	change_hat(Hats.Dinosaur_Hat)
	aPoses.append(measure())

def retire():
	change_hat(Hats.Wizard_Hat)
	aPoses = []
	toMove()
	return False

# dino do not move world size over
def getDir(_from, _to):
	xDir = East
	yDir = North
	if (_from[0] > _to[0]):
		xDir = West
	if (_from[1] > _to[1]):
		yDir = South
	return (xDir, yDir)
	
def dinoMoveInner(pos = (0, 0)):
	xMoved = False
	yMoved = False
	x = get_pos_x()
	y = get_pos_y()
	_d = getDir((x, y), pos)
	
	while not x == pos[0]:
		while move(_d[0]):
			x = get_pos_x()
			m = measure()
			if not m == None:
				aPoses.append(m)
			if (x == pos[0]):
				xMoved = True
				break
		if not xMoved:
			return False
					
	while not y == pos[1]:
		while move(_d[1]):
			y = get_pos_y()
			m = measure()
			if not m == None:
				aPoses.append(m)
			if (y == pos[1]):
				yMoved = True
				break
		if not yMoved:
			return False
				
	return True

def dinoMove(pos = (0, 0)):
	if not dinoMoveInner(pos):
		return retire()
	return True
	

def getNextApplePos():
	return aPoses[len(aPoses) - 1]

def firstCycle():
	# 初回は足元にある
	dinoMove((0, 0))
	dinoMove((0, 1))
	dinoMove((1, 1))
	dinoMove((1, 0))
	dinoMove((0, 0))
			
def cycle():
	t = []
	pos = getNextApplePos()
	length = len(aPoses)
	roadCount = size + pos[0] + size + pos[0]
	diff = roadCount - length
	repeatCount = 0
	beforeRepeat = 0
	afterRepeat = 0

	if (diff < 0):
		repeatCount = (diff // 32) + 1
	if (repeatCount != 0):
		if (pos[0] - repeatCount < 0):
			beforeRepeat = pos[0] + 0 # immutable
		else:
			beforeRepeat = pos[0] - repeatCount
		if (beforeRepeat < repeatCount):
			afterRepeat = repeatCount - beforeRepeat
				
	t.append(dinoMove((0, size - 1)))
	for _ in range(beforeRepeat):
		if (get_pos_x() % 2 == 1):
			t.append(dinoMove((get_pos_x(), 1)))
		else:
			t.append(dinoMove((get_pos_x(), size - 1)))
	if (get_pos_x() % 2 == 1):
		t.append(dinoMove((pos[0], 1)))
	else:
		t.append(dinoMove((pos[0], size - 1)))
	for _ in range(afterRepeat):
		if (get_pos_x() % 2 == 1):
			t.append(dinoMove((i, size - 1)))
		else:
			t.append(dinoMove((i, 1)))			
	if (get_pos_x() != pos[0] and get_pos_y() == size - 1):
		t.append(dinoMove((get_pos_x() + 1, 0)))
	else:
		t.append(dinoMove((get_pos_x(), 0)))
	t.append(dinoMove((0, 0)))
	return not False in t
				
def longest():
	t = []
	for x in rSize:
		if x == 0:
			t.append(dinoMove((0, size - 1)))
		elif x == (size -1):
			t.append(dinoMove((x, 0)))
			t.append(dinoMove((0, 0)))
		elif (x % 2 == 1):
			t.append(dinoMove((x, 1)))
		elif (x % 2 == 0):
			t.append(dinoMove((x, size - 1)))
	return not False in t
def run():
	init()
	firstCycle()
	while True:
		length = len(aPoses)
		if (length < 1000):
			t = cycle()
		else:
			t = longest()
		if not t:
			break
	return True
clear()
while True:
	run()
