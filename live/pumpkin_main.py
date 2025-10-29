from pumpkin_util import * 

clear()
dList = {
	(0, 0),
	(0, 7),
	(0, 14),
	(0, 21),
	(7, 0),
	(7, 7),
	(7, 14),
	(7, 21),
	(14, 0),
	(14, 7),
	(14, 14),
	(14, 21),
	(21, 0),
	(21, 7),
	(21, 14),
	(21, 21),
}
dPos = []
for l in dList:
	dPos.append(l)
def actionWrapper():
	plantPumpkin(6)
while True:
	if True:
		dorones = {}
		toMove(0, 0)
		dMax = max_drones() - 1
		lMax = len(dList)
		max = dMax
		if dMax > lMax:
			max = lMax
		for i in range(max):
			target = dPos[i]
			toMove(target[0], target[1])
			dorones[target] = spawn_drone(actionWrapper)
		while True:
			for d in dorones:
				if (has_finished(dorones[d])):
					toMove(d[0], d[1])
					dorones[d] = spawn_drone(actionWrapper)
								
	else:
		plantPumpkin(get_world_size())
