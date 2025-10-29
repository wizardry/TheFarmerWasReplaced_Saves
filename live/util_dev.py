# 水を閾値まで繰り返し使う
def useWater():
	while not get_water() > 0.8:
		use_item(Items.Water)
	return get_water()

# 肥料を使う
def useFer():
	if (get_ground_type() == Grounds.Soil):
		use_item(Items.Fertilizer)
	return num_items(Items.Fertilizer)

# 人参など植えるときに必要な耕しまとめ
def doTill():
	if not (get_ground_type() == Grounds.Soil):
		till()
	return get_ground_type() == Grounds.Soil

# 水あげたり耕したりをまとめてます
def initCondition(till = False, water = False, fer = False):
	if (water):
		useWater()
	if (fer):
		useFer()
	if (till):
		doTill()

# 疑似フィールドを表す配列をつくる。使わなかった。
def getFieldArray():
	field = []
	for x in range(get_world_size()):
		field.append([])
		for y in range(get_world_size()):
			field[y].append(None)
	return field

# 配列の中に指定のValueがあればTrueなければFalse
def includes(list, target):
	isExist = False
	for i in range(len(list)):
		if(target == list[i]):
			isExist = True
	return isExist

def n2AIncludes(obj, target):
	isExist = False
	for i in range(len(obj)):
		for ni in range(len(obj[i])):
			if(target == obj[i][ni]):
				isExist = True
	return isExist

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
	if horizontal <= horizontalRev:
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

# 指定の位置に移動
def toMove(x = 0, y = 0):
	wSize = get_world_size()
	if (x >= wSize):
		x -= wSize
	if (y >= wSize):
		y -= wSize
	xDirection = East
	yDirection = North
	now = [get_pos_x(), get_pos_y()]
	if (now[0] - x > 0):
		xDirection = West
	if (now[1] - y > 0):
		yDirection = South
	while get_pos_x() != x:
		move(xDirection)
	while get_pos_y() != y:
		move(yDirection)

# 指定位置に移動。移動方向を指定したい場合に利用
def movePosition(x = 0, y = 0, xVector = East, yVector = North):
	wSize = get_world_size()
	if (x >= wSize):
		x -= wSize
	if (y >= wSize):
		y -= wSize

	while get_pos_x() != x:
		if not (move(xVector)):
			break
	while get_pos_y() != y:
		if not (move(yVector)):
			break

# 初期値に移動
def initPosition():
	movePosition()


# ヒマワリを植える
def plantSunflower():
	initCondition(True)
	plant(Entities.Sunflower)

# 草を植える
def plantGlass():
	if not (get_ground_type() == Grounds.Grassland):
		till()
	pass

# 茂み・木を植える
def plantTree():
	if ((get_pos_x() % 2) + (get_pos_y() % 2) == 1):
		plant(Entities.Tree)
	else:
		plant(Entities.Bush)

# 人参を植える
def plantCarrot():
	initCondition(True)
	plant(Entities.Carrot)
	useFer()

# arg dorone[] 全てのdoroneが終わるまで待機する
def finishedAllDoroneAction(dorones):
	yFinished = False
	while not yFinished:
		flg = True
		for d in dorones:
			if not has_finished(d):
				flg = False
		if (flg):
			yFinished = True
	return True

def mvTo(pos = (0, 0)):
	# spos = (get_pos_x(), get_pos_y())
	xdiff = pos[0] - get_pos_x()
	ydiff = pos[1] - get_pos_y()
	if (xdiff == 0 and ydiff == 0):
		return True

	size = get_world_size() # world size
	th = size // 2 # size // 2

	xdir = East
	ydir = North
	if (xdiff > 0):
		if (xdiff > th):
			xdiff -= size
			xdir = West
	elif (xdiff < 0):
		if -xdiff < th:
			xdir = West
		else:
			xdiff += size
	if (ydiff > 0):
		if (ydiff > th):
			ydiff -= size
			ydir = South
	elif (ydiff < 0):
		if -ydiff < th:
			ydir = South
		else:
			ydiff += size

	for x in range(abs(xdiff)):
		move(xdir)
	for y in range(abs(ydiff)):
		move(ydir)
	# fpos = (get_pos_x(), get_pos_y())
	# quick_print('mvto',spos, fpos, pos, xdiff, xdir, ydiff, ydir)
