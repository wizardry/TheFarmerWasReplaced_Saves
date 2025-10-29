from util_dev import *

def plantPumpkinV1(size):
	ci = 0
	startPosition = [get_pos_x(), get_pos_y()]
	if (startPosition[0] + size > get_world_size()):
		print("Error: x axis is world size over.")
	if (startPosition[1] + size > get_world_size()):
		print("Error: y axis is world size over.")
		
	canHarvestFlg = False
	checkColmuns = []
	for i in range(size):
		checkColmuns.append(False)
	while not canHarvestFlg:
		for x in range(size):
			hasDeadPumpForCol = False
			for y in range(size):
				if (checkColmuns[x] == True):
					continue
				initCondition(True)
				if (get_entity_type() == Entities.Dead_Pumpkin and ci != 0 ):
					hasDeadPumpForCol = True
				plant(Entities.Pumpkin)
				toMove(startPosition[0] + x, startPosition[1] + y + 1)
			if (hasDeadPumpForCol == False and ci != 0):
				checkColmuns[x] = True
			toMove(startPosition[0] + x + 1, startPosition[1])
		ci += 1
		if not includes(checkColmuns, False):
			canHarvestFlg = True
		toMove(startPosition[0], startPosition[1])
	toMove(startPosition[0], startPosition[1])
	return True

def plantPumpkin(size):
	startPosition = [get_pos_x(), get_pos_y()]
	if (startPosition[0] + size > get_world_size()):
		print("Error: x axis is world size over.")
		return False
	if (startPosition[1] + size > get_world_size()):
		print("Error: y axis is world size over.")
		return False
	
	def planting():
		toMove(startPosition[0], startPosition[1])
		for x in range(size):
			for y in range(size):
				initCondition(True)
				plant(Entities.Pumpkin)
				toMove(startPosition[0] + x, startPosition[1] + y + 1)
			toMove(startPosition[0] + x + 1, startPosition[1])
		toMove(startPosition[0], startPosition[1])

	def checkDead():
		map = {}
		toMove(startPosition[0], startPosition[1])
		for x in range(size):
			for y in range(size):
				# quick_print(can_harvest(), get_entity_type(), not (get_entity_type() == Entities.Pumpkin))
				if (get_entity_type() == Entities.Dead_Pumpkin):
					value = (get_pos_x(), get_pos_y())
					map[value] = value
				toMove(startPosition[0] + x, startPosition[1] + y + 1)
			toMove(startPosition[0] + x + 1, startPosition[1])
		return map

	def excludeDead(map):
		while not len(map) == 0:
			popKeys = []
			for m in map:
				toMove(m[0], m[1])
				if (get_entity_type() == Entities.Pumpkin and can_harvest()):
					popKeys.append(m)
					continue
				plant(Entities.Pumpkin)
			for k in popKeys:
				map.pop(k)
		return True
	planting()
	map = checkDead()
	excludeDead(map)
	toMove(startPosition[0], startPosition[1])
	harvest()
		
