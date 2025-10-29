def deque_new():
	return {"data": []}

def deque_append(dq, value):
	dq["data"].append(value)

def deque_appendleft(dq, value):
	dq["data"].insert(0, value)

def deque_pop(dq):
	if not dq["data"]:
		print('IndexError("pop from empty deque")')
	return dq["data"].pop()

def deque_popleft(dq):
	if not dq["data"]:
		print('IndexError("pop from empty deque")')
	return dq["data"].pop(0)

def deque_len(dq):
	return len(dq["data"])

def deque_get(dq, idx):
	return dq["data"][idx]

def deque_contains(dq, item):
	return item in dq["data"]

def deque_iter(dq):
	return iter(dq["data"])



N = 32
DIRS = [(0,1),(1,0),(0,-1),(-1,0)]

def game_init(ap):
	snake = deque_new()
	deque_append(snake, (0,0))   # 初期位置
	state = {
		"snake": snake,
		"item": ap,           # 初回は足元
		"next_item": measure()   # 次のアイテムを先読み
	}
	return state

def in_bounds(x, y):
	return 0 <= x < N and 0 <= y < N

def bfs(state, start, goal):
	q = deque_new()
	deque_append(q, start)
	prev = {start: None}

	occupied = set(state["snake"]["data"])
	# ゴールは通過可能にする
	if goal in occupied:
		occupied.remove(goal)

	while deque_len(q) > 0:
		x, y = deque_popleft(q)
		if (x,y) == goal:
			# 経路復元
			path = []
			while (x,y) != start:
				path.append((x,y))
				x,y = prev[(x,y)]
			return path[::-1]

		for dx, dy in DIRS:
			nx, ny = x+dx, y+dy
			if in_bounds(nx, ny) and (nx,ny) not in occupied and (nx,ny) not in prev:
				prev[(nx,ny)] = (x,y)
				deque_append(q, (nx,ny))
	return None

def game_step(state):
	snake = state["snake"]
	head = deque_get(snake, 0)
	path = bfs(state, head, state["item"])
	if not path:
		retire()
		return False

	# 次の一歩
	nx, ny = path[0]
	move(nx, ny)
	deque_appendleft(snake, (nx,ny))

	# アイテム取得判定
	if (nx,ny) == state["item"]:
		state["item"] = state["next_item"]
		state["next_item"] = measure()
	else:
		deque_pop(snake)  # 尻尾を縮める

	return True

def retire():
	change_hat(Hats.The_Farmers_Remains)
	clear()
	return False

def game_run():
	clear()
	change_hat(Hats.Dinosaur_Hat)
	ap = measure()
	move(North)
	state = game_init(ap)
	while True:
		if not game_step(state):
			break
game_run()