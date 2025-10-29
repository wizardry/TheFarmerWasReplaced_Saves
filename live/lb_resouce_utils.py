##-------------------------------use RankingModeUtils

def mvTo(pos = (0, 0), size = 32, Spec=False):
	if (Spec):
		quick_print('from: ', (get_pos_x(), get_pos_y()))

	fromPos = (get_pos_x(), get_pos_y())
	toPos = pos
	horizontal = (pos[0] - fromPos[0]) % size
	horizontalRev = (fromPos[0] - pos[0])  % size

	vertical = (pos[1] - fromPos[1]) % size
	verticalRev = (fromPos[1] - pos[1])  % size
	if horizontal == 0:
		pass
	elif horizontal <= horizontalRev:
		for _ in range(horizontal):
			if (Spec):
				quick_print('east: ', get_pos_x())
			move(East)
	else:
		for _ in range(horizontalRev):
			if (Spec):
				quick_print('west: ', get_pos_x())
			move(West)
	if vertical == 0:
		pass
	elif vertical <= verticalRev:
		for _ in range(vertical):
			if (Spec):
				quick_print('north: ', get_pos_y())
			move(North)
	else:
		for _ in range(verticalRev):
			if (Spec):
				quick_print('south: ', get_pos_y())
			move(South)
	if (Spec):
		quick_print('to: ', (get_pos_x(), get_pos_y()))
	# fpos = (get_pos_x(), get_pos_y())
	# quick_print('mvto',spos, fpos, pos, xdiff, xdir, ydiff, ydir)
def mvToTest():
	size = 5
	set_world_size(size)
	expects = [
		'West 1',
		'South 1',
		'East 2',
		'East 2, North 2',
		'North 2',
		'West1, South1'
	]
	it = [(4, 0), (0, 4), (0, 2), (2, 2), (2, 0), (4, 4)]
	for i in range(len(it)):
		mvTo((0, 0), size)
		mvTo(pos[i], size, True)
		quick_print(expects[i])


# 配列を挿入ソートします
def memorySort(li):
	# gen index
	length = len(li)
	nl = []
	minV = min(li)
	for v in li:
		isInserted = False
		nllen = len(nl)
		for nli in range(nllen):
			if nl[nli] >= v:
				nl.insert(nli, v)
				isInserted = True
				break
		if not (isInserted):
			nl.insert(nllen, v)
	return nl

def debugHarvest(item):
	before = num_items(item)
	harvest()
	after = num_items(item)
	quick_print(after-before)

def initMaze(size):
	plant(Entities.Bush)
	substance = size * 2**(num_unlocked(Unlocks.Mazes) - 1)
	use_item(Items.Weird_Substance, substance)
