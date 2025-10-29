from util_dev import *
from errors import *

def initPlantSunflower(xSize = get_world_size(), ySize = get_world_size()):
	now = [get_pos_x(), get_pos_y()]
	checkOverSizeFromWorld(xSize, ySize)
	
	for x in range(xSize):
		for y in range(ySize):
			initCondition(True)
			plant(Entities.Sunflower)
			toMove(now[0] + x, now[1] + y + 1)
		toMove(now[0] + x + 1, now[1])


# private
def harvestSunflowerCell():
	if (can_harvest()):
		harvest()
		return True
	return False

# private
# skipするならcacheをいれないといけない
def harvestSunflowerColmun(ySize):
	y1stPos = get_pos_y()
	for y in range(ySize):
		_harvested = harvestSunflowerCell()
		plant(Entities.Sunflower)
		toMove(get_pos_x(), y1stPos + y + 1)
	return True

def harvestSunflower(xSize = get_world_size(), ySize = get_world_size()):
	now = [get_pos_x(), get_pos_y()]
	for x in range(xSize):
		harvestSunflowerColmun(ySize)
		toMove(now[0] + x + 1, now[1])
