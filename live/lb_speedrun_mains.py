from lb_speedrun_util import *

def unlockSpeedAction():
	speedUnlockCost = 20
	for i in range(speedUnlockCost + 1):
		harvest()
	unlock(Unlocks.Speed)

def unlockExpandAction():
	expandUnlockCost = 30
	for i in range(expandUnlockCost + 1):
		while not can_harvest():
			pass
		harvest()
	unlock(Unlocks.Expand)

def unlockPlantAction():
	plantUnlockCost = 50
	for i in range(plantUnlockCost + 1):
		while not can_harvest():
			pass
		harvest()
	unlock(Unlocks.Plant)

def unlockExpand2Action():
	# 混作の可能性があるが検知できない。混作だった場合5倍の収穫となるため以降num_itemsを使う
	# Hayは移動するよりその場で刈った方が早いので、縦軸に *+* で植える
	# wood
	expand2UnlockCost = 20
	# Bush = 3.2sec ~ 4.8sec
	# Grass = 0.5sec
	plant(Entities.Bush)
	move(North)
	plant(Entities.Bush)
	move(North)
	while num_items(Items.Wood) < expand2UnlockCost:
		# Bush成長までGrassを狩る
		# 上下に植えるのでGrass収穫時にmaybe 0.92secかかっている
		for g in range(4):
			while not can_harvest():
				pass
			harvest()
		move(South)
		while not can_harvest():
			pass
		harvest()
		plant(Entities.Bush)
		move(South)
		while not can_harvest():
			pass
		harvest()
		plant(Entities.Bush)
		move(South)
	unlock(Unlocks.Expand)

def unlockSpeed2Action():
	speed2UnlockCost = 20
	# Bush = 3.2sec ~ 4.8sec
	# Grass = 0.5sec
	plant(Entities.Bush)
	move(North)
	plant(Entities.Bush)
	move(North)
	move(East)
	plant(Entities.Bush)
	move(East)
	plant(Entities.Bush)
	move(East)
	while num_items(Items.Wood) < speed2UnlockCost:
		# Bush成長までGrassを狩る
		# 上下に植えるのでGrass収穫時にmaybe 1.82secかかっている
		for g in range(3):
			while not can_harvest():
				pass
			harvest()
		move(South)
		while not can_harvest():
			pass
		harvest()
		plant(Entities.Bush)
		move(South)
		while not can_harvest():
			pass
		harvest()
		plant(Entities.Bush)
		move(South)
		move(East)
		while not can_harvest():
			pass
		harvest()
		plant(Entities.Bush)
		move(East)
		while not can_harvest():
			pass
		harvest()
		plant(Entities.Bush)
		move(East)
	unlock(Unlocks.Speed)

def unlockCarrotAction():
	# FYI:
	# Speedが3になったことでcan_harvestで待つより移動した方が収穫が早くなった
	# 5回Hay収穫の差分 Speed2:for2.51 while2.27 Speed3:for1.67 while2.18
	unlockWoodCost = 50
	clear()
	# util variableにsizeを入れておいてexpand時に更新する　でもいいかも
	size = get_world_size()
	while num_items(Items.Wood) < unlockWoodCost:
		for x in range(size):
			for y in range(size):
				if can_harvest():
					harvest()
				if (x+y) % 2:
					plant(Entities.Bush)
				move(North)
			move(East)
	unlock(Unlocks.Carrots)

def unlockExpand3Action():
	# Carrotのためバッファをいれておく
	unlockCost = {'Wood': 30+10, 'Carrot': 20}

	size = get_world_size()
	while num_items(Items.Wood) < unlockCost['Wood'] or num_items(Items.Carrot) < unlockCost['Carrot']:
		openingCheckeredLoop(size)
	unlock(Unlocks.Expand)

def unlockSpeed3Action():
	# Carrotのためバッファをいれておく
	unlockCost = {'Wood': 50 + 10, 'Carrot': 50}

	size = get_world_size()
	while num_items(Items.Wood) < unlockCost['Wood'] or num_items(Items.Carrot) < unlockCost['Carrot']:
		openingCheckeredLoop(size)
	unlock(Unlocks.Speed)

def unlockTreeAction():
	# Carrotのためバッファをいれておく
	unlockCost = {'Wood': 50 + 10, 'Carrot': 70}

	size = get_world_size()
	while num_items(Items.Wood) < unlockCost['Wood'] or num_items(Items.Carrot) < unlockCost['Carrot']:
		openingCheckeredLoop(size)
	unlock(Unlocks.Trees)

def unlockGrass2Action():
	# Carrotのためバッファをいれておく
	unlockCost = 300

	size = get_world_size()
	while num_items(Items.Hay) < unlockCost:
		openingCheckeredLoop(size, Entities.Tree)
	unlock(Unlocks.Grass)

def unlockExpand4Action():
	unlockCost = {'Wood': 100 + 10, 'Carrot': 50}

	size = get_world_size()
	while num_items(Items.Wood) < unlockCost['Wood'] or num_items(Items.Carrot) < unlockCost['Carrot']:
		openingCheckeredLoop(size, Entities.Tree)
	unlock(Unlocks.Expand)

def unlockCarrot2Action():
	unlockCost = {'Wood': 250 + 10}

	size = get_world_size()
	while num_items(Items.Wood) < unlockCost['Wood']:
		openingCheckeredLoop(size, Entities.Tree)
	unlock(Unlocks.Carrots)

def unlockWaterAction():
	unlockCost = {'Wood': 50 + 10}

	size = get_world_size()
	while num_items(Items.Wood) < unlockCost['Wood']:
		openingCheckeredLoop(size, Entities.Tree)
	unlock(Unlocks.Watering)

def unlockGrass3Action():
	unlockCost = {'Wood': 500 + 10}

	size = get_world_size()
	while num_items(Items.Wood) < unlockCost['Wood']:
		openingCheckeredLoop(size, Entities.Tree)
	unlock(Unlocks.Grass)

def unlockTree2Action():
	unlockCost = {'Hay': 300 + 10}

	size = get_world_size()
	while num_items(Items.Hay) < unlockCost['Hay']:
		openingCheckeredLoop(size, Entities.Tree)
	unlock(Unlocks.Trees)

def unlockFertilizerAction():
	unlockCost = {'Wood': 500 + 10}

	size = get_world_size()
	while num_items(Items.Wood) < unlockCost['Wood']:
		openingCheckeredLoop(size, Entities.Tree)
	unlock(Unlocks.Fertilizer)

def unlockCarrot3Action():
	unlockCost = {'Wood': 1250 + 10}

	size = get_world_size()
	while num_items(Items.Wood) < unlockCost['Wood']:
		openingCheckeredLoop(size, Entities.Tree)
	unlock(Unlocks.Carrots)

def unlockSpeed4Action():
	unlockCost = {'Carrot': 500 + 10}

	size = get_world_size()
	while num_items(Items.Carrot) < unlockCost['Carrot']:
		openingCheckeredLoop(size, Entities.Tree)
	unlock(Unlocks.Speed)

def unlockWater2Action():
	unlockCost = {'Wood': 200 + 10}

	size = get_world_size()
	while num_items(Items.Wood) < unlockCost['Wood']:
		openingCheckeredLoop(size, Entities.Tree)
	unlock(Unlocks.Watering)

def unlockPumpkinAction():
	unlockCost = {'Wood': 500 + 10, 'Carrot': 200}

	size = get_world_size()
	while num_items(Items.Wood) < unlockCost['Wood'] or num_items(Items.Carrot) < unlockCost['Carrot']:
		openingCheckeredLoop(size, Entities.Tree)
	unlock(Unlocks.Pumpkins)

def unlockGrass4Action():
	unlockCost = {'Wood': 2500}

	size = get_world_size()
	while num_items(Items.Wood) < unlockCost['Wood']:
		openingCheckeredLoop(size, Entities.Tree)
	unlock(Unlocks.Grass)

def unlockSunflowerAction():
	unlockCost = {'Carrot': 500}

	size = get_world_size()
	while num_items(Items.Carrot) < unlockCost['Carrot']:
		openingCheckeredLoop(size, Entities.Tree)
	unlock(Unlocks.Sunflowers)

def unlockFertilizer2Action():
	unlockCost = {'Wood': 1500}

	size = get_world_size()
	while num_items(Items.Wood) < unlockCost['Wood']:
		middleCheckeredLoop(size)
	unlock(Unlocks.Fertilizer)


def unlockTree3Action():
	unlockCost = {'Hay': 1200}

	size = get_world_size()
	while num_items(Items.Hay) < unlockCost['Hay']:
		middleCheckeredLoop(size)
	unlock(Unlocks.Trees)

def unlockPumpkin2Action():
	unlockCost = {'Carrot': 1000 + 50}

	size = get_world_size()
	while num_items(Items.Carrot) < unlockCost['Carrot']:
		middleCheckeredLoop(size)
	unlock(Unlocks.Pumpkins)

def unlockWater3Action():
	unlockCost = {'Wood': 800 + 50}

	size = get_world_size()
	while num_items(Items.Wood) < unlockCost['Wood']:
		middleCheckeredLoop(size)
	unlock(Unlocks.Watering)

def unlockCarrot4Action():
	unlockCost = {'Wood': 6250 + 50}

	size = get_world_size()
	while num_items(Items.Wood) < unlockCost['Wood']:
		middleCheckeredLoop(size)
	unlock(Unlocks.Carrots)

def unlockExpand5Action():
	unlockCost = {'Pumpkin': 1000 + 50}

	size = get_world_size()
	needCarrotCount = unlockCost['Pumpkin'] / get_cost(Entities.Pumpkin)[Items.Carrot]

	while num_items(Items.Carrot) < needCarrotCount:
		middleCheckeredLoop(size)

	clear()
	while num_items(Items.Pumpkin) < unlockCost['Pumpkin']:
		openingPumpkinHarvest(size)
	unlock(Unlocks.Expand)

def unlockTree4Action():
	clear()
	unlockCost = {'Hay': 4800 + 50}

	size = get_world_size()
	while num_items(Items.Hay) < unlockCost['Hay']:
		middleCheckeredLoop(size)
	unlock(Unlocks.Trees)

def unlockSpeed5Action():
	unlockCost = {'Carrot': 1000 + 50}

	size = get_world_size()
	while num_items(Items.Carrot) < unlockCost['Carrot']:
		middleCheckeredLoop(size)
	unlock(Unlocks.Speed)
	clear()

def unlockPolycultureAction():
	unlockCost = {'Pumpkin': 3000 + 50}

	size = get_world_size()
	needCarrotCount = unlockCost['Pumpkin'] / get_cost(Entities.Pumpkin)[Items.Carrot]

	while num_items(Items.Carrot) < needCarrotCount:
		middleCheckeredLoop(size)

	clear()
	while num_items(Items.Pumpkin) < unlockCost['Pumpkin']:
		openingPumpkinHarvest(size)
	unlock(Unlocks.Polyculture)
	clear()

def unlockGrass5Action():
	unlockCost = {'Wood': 12500}

	size = get_world_size()
	while num_items(Items.Wood) < unlockCost['Wood']:
		middleCheckeredLoop(size)
	unlock(Unlocks.Grass)

def unlockFertilizer3Action():
	unlockCost = {'Wood': 9000}

	size = get_world_size()
	while num_items(Items.Wood) < unlockCost['Wood']:
		middleCheckeredLoop(size)
	unlock(Unlocks.Fertilizer)

def unlockExpand6Action():
	unlockCost = {'Pumpkin': 8000 + 50}

	size = get_world_size()
	needCarrotCount = unlockCost['Pumpkin'] / get_cost(Entities.Pumpkin)[Items.Carrot]
	clear()
	while num_items(Items.Carrot) < needCarrotCount:
		polyHarvest(size)

	clear()
	while num_items(Items.Pumpkin) < unlockCost['Pumpkin']:
		openingPumpkinHarvest(size)
	unlock(Unlocks.Expand)
	clear()

def unlockMazeAction():
	unlockCost = {'Weird_Substance': 1000 + 50}

	size = get_world_size()
	while num_items(Items.Weird_Substance) < unlockCost['Weird_Substance']:
		polyHarvest(size)
	unlock(Unlocks.Mazes)

def unlockMegaFarmAction():
	unlockCost = {'Gold': 2000}
	size = get_world_size()
	needSubstanceCount = 2000
	while num_items(Items.Weird_Substance) < needSubstanceCount:
		polyHarvest(size)
	clear()
	while num_items(Items.Gold) < unlockCost['Gold']:
		initMaze(size)
		runnerMaze()
	unlock(Unlocks.Megafarm)

def unlockMegaFarm2Action():
	unlockCost = {'Gold': 8000}
	size = get_world_size()
	needSubstanceCount = 8000
	while num_items(Items.Weird_Substance) < needSubstanceCount:
		polyHarvest(size)
	clear()
	while num_items(Items.Gold) < unlockCost['Gold']:
		initMaze(size)
		runnerMaze()
	unlock(Unlocks.Megafarm)

def unlockPumpkin3Action():
	unlockCost = {'Carrot': 4000}

	size = get_world_size()
	while num_items(Items.Carrot) < unlockCost['Carrot']:
		polyHarvestV2(size)
	unlock(Unlocks.Pumpkins)

def unlockTree5Action():
	unlockCost = {'Hay': 19200}

	size = get_world_size()
	while num_items(Items.Hay) < unlockCost['Hay']:
		polyHarvestV2(size)
	unlock(Unlocks.Trees)

def unlockCarrot5Action():
	unlockCost = {'Wood': 31200}

	size = get_world_size()
	while num_items(Items.Wood) < unlockCost['Wood']:
		polyHarvestV2(size)
	unlock(Unlocks.Carrots)

def unlockGrass6Action():
	unlockCost = {'Wood': 62500}

	size = get_world_size()
	while num_items(Items.Wood) < unlockCost['Wood']:
		polyHarvestV2(size)
	unlock(Unlocks.Grass)

def unlockCactusAction():
	unlockCost = {'Pumpkin': 5000}
	size = get_world_size()

	needCarrotCount = unlockCost['Pumpkin']

	while num_items(Items.Carrot) < needCarrotCount:
		polyHarvestV2(size)

	clear()
	while num_items(Items.Pumpkin) < unlockCost['Pumpkin']:
		pumpkinHarvest(size)
	unlock(Unlocks.Cactus)

def unlockPumpkin4Action():
	unlockCost = {'Carrot': 16000}
	size = get_world_size()

	needCarrotCount = unlockCost['Carrot']

	while num_items(Items.Carrot) < needCarrotCount:
		polyHarvestV2(size)

	clear()
	while num_items(Items.Carrot) < unlockCost['Carrot']:
		pumpkinHarvest(size)
	unlock(Unlocks.Pumpkins)

def unlockCactus2Action():
	unlockCost = {'Pumpkin': 20000}
	size = get_world_size()

	needCarrotCount = unlockCost['Pumpkin']

	while num_items(Items.Carrot) < needCarrotCount:
		polyHarvestV2(size)

	clear()
	while num_items(Items.Pumpkin) < unlockCost['Pumpkin']:
		pumpkinHarvest(size)
	unlock(Unlocks.Cactus)

def unlockExpand7Action():
	unlockCost = {'Pumpkin': 64000}
	size = get_world_size()

	needCarrotCount = unlockCost['Pumpkin']

	while num_items(Items.Carrot) < needCarrotCount:
		polyHarvestV2(size)

	clear()
	while num_items(Items.Pumpkin) < unlockCost['Pumpkin']:
		pumpkinHarvest(size)
	unlock(Unlocks.Expand)

def unlockDinoAction():
	unlockCost = {'Cactus': 2000}
	size = get_world_size()

	needCarrotCount = unlockCost['Cactus']
	needPumpkinCount = unlockCost['Cactus']

	clear()
	while num_items(Items.Carrot) < needCarrotCount:
		polyHarvestV2(size)
	clear()
	while num_items(Items.Pumpkin) < needPumpkinCount:
		pumpkinHarvest(size)

	while num_items(Items.Cactus) < unlockCost['Cactus']:
		cactusHarvest(size)
	unlock(Unlocks.Dinosaurs)

def unlockDino2Action():
	if (unlock(Unlocks.Dinosaurs)):
		return

	unlockCost = {'Cactus': 12000}
	size = get_world_size()

	needCarrotCount = unlockCost['Cactus']
	needPumpkinCount = unlockCost['Cactus']

	clear()
	while num_items(Items.Carrot) < needCarrotCount:
		polyHarvestV2(size)
	clear()
	while num_items(Items.Pumpkin) < needPumpkinCount:
		pumpkinHarvest(size)

	while num_items(Items.Cactus) < unlockCost['Cactus']:
		cactusHarvest(size)
	unlock(Unlocks.Dinosaurs)

def unlockMaze2Action():
	if (unlock(Unlocks.Mazes)):
		return

	unlockCost = {'Cactus': 12000}
	size = get_world_size()

	needCarrotCount = unlockCost['Cactus']
	needPumpkinCount = unlockCost['Cactus']

	clear()
	while num_items(Items.Carrot) < needCarrotCount:
		polyHarvestV2(size)
	clear()
	while num_items(Items.Pumpkin) < needPumpkinCount:
		pumpkinHarvest(size)

	while num_items(Items.Cactus) < unlockCost['Cactus']:
		cactusHarvest(size)
	unlock(Unlocks.Mazes)

def unlockDino3Action():
	unlockCost = {'Cactus': 72000}
	size = get_world_size()
	count = size * size
	needCarrotCount = unlockCost['Cactus'] // count
	needPumpkinCount = unlockCost['Cactus'] // count

	clear()
	while num_items(Items.Carrot) < needCarrotCount:
		polyHarvestV2(size)
	clear()
	while num_items(Items.Pumpkin) < needPumpkinCount:
		pumpkinHarvest(size)

	while num_items(Items.Cactus) < unlockCost['Cactus']:
		cactusHarvest(size)
	unlock(Unlocks.Dinosaurs)


def unlockPolyculture2Action():
	unlockCost = {'Bone': 10000 }

	size = get_world_size()
	needCarrotCount = unlockCost['Bone']
	needPumpkinCount = unlockCost['Bone']
	needCactusCount = unlockCost['Bone']

	while num_items(Items.Carrot) < needCarrotCount:
		polyHarvestV2(size)
	clear()
	while num_items(Items.Pumpkin) < needPumpkinCount:
		pumpkinHarvest(size)
	while num_items(Items.Cactus) < needCactusCount:
		cactusHarvest(size)
	clear()
	while num_items(Items.Bone) < unlockCost['Bone']:
		dinoBasicRunner(size)
	unlock(Unlocks.Polyculture)

def unlockPolyculture3Action():
	unlockCost = {'Bone': 50000 }

	size = get_world_size()
	needCarrotCount = size * size
	needPumpkinCount = size * size
	needCactusCount = size * size

	while num_items(Items.Carrot) < needCarrotCount:
		polyHarvestV2(size)
	clear()
	while num_items(Items.Pumpkin) < needPumpkinCount:
		pumpkinHarvest(size)
	while num_items(Items.Cactus) < needCactusCount:
		cactusHarvest(size)
	clear()
	while num_items(Items.Bone) < unlockCost['Bone']:
		dinoBasicRunner(size)
	unlock(Unlocks.Polyculture)

def unlockMaze3Action():
	unlockCost = {'Cactus': 72000}
	size = get_world_size()
	count = size * size
	needCarrotCount = unlockCost['Cactus'] // count
	needPumpkinCount = unlockCost['Cactus'] // count

	clear()
	while num_items(Items.Carrot) < needCarrotCount:
		polyHarvestV2(size)
	clear()
	while num_items(Items.Pumpkin) < needPumpkinCount:
		pumpkinHarvest(size)

	while num_items(Items.Cactus) < unlockCost['Cactus']:
		cactusHarvest(size)
	unlock(Unlocks.Mazes)


def unlockPolyculture4Action():
	unlockCost = {'Bone': 250000 }

	size = get_world_size()
	needCarrotCount = size * size
	needPumpkinCount = size * size
	needCactusCount = size * size

	while num_items(Items.Carrot) < needCarrotCount:
		polyHarvestV2(size)
	clear()
	while num_items(Items.Pumpkin) < needPumpkinCount:
		pumpkinHarvest(size)
	while num_items(Items.Cactus) < needCactusCount:
		cactusHarvest(size)
	clear()
	while num_items(Items.Bone) < unlockCost['Bone']:
		dinoBasicRunner(size)
	unlock(Unlocks.Polyculture)

def unlockMegaFarm3Action():
	unlockCost = {'Gold': 32000}
	size = get_world_size()
	needSubstanceCount = 32000
	while num_items(Items.Weird_Substance) < needSubstanceCount:
		polyHarvest(size)
	clear()
	while num_items(Items.Gold) < unlockCost['Gold']:
		initMaze(size)
		runnerMaze()
	unlock(Unlocks.Megafarm)

def unlockMegaFarm4Action():
	unlockCost = {'Gold': 128000}
	size = get_world_size()
	needSubstanceCount = 50000
	while num_items(Items.Weird_Substance) < needSubstanceCount:
		polyHarvest(size)
	clear()
	while num_items(Items.Gold) < unlockCost['Gold']:
		initMaze(size)
		runnerMaze()
	unlock(Unlocks.Megafarm)

def unlockLeaderboardAction():
	unlockCost = {'Gold': 1000000, 'Bone': 2000000 }
	size = get_world_size()
	needSubstanceCount = 500000
	while num_items(Items.Weird_Substance) < needSubstanceCount:
		cactusHarvest(size)
	clear()
	while num_items(Items.Gold) < unlockCost['Gold']:
		bulkMazeRunner()
	clear()
	while num_items(Items.Bone) < unlockCost['Bone']:
		dinoBasicRunner(size)
	unlock(Unlocks.Leaderboard)


def unlockMegaFarm5Action():
	unlockCost = {'Gold': 512000}
	size = get_world_size()
	needSubstanceCount = 50000
	while num_items(Items.Weird_Substance) < needSubstanceCount:
		polyHarvest(size)
	clear()
	while num_items(Items.Gold) < unlockCost['Gold']:
		bulkMazeRunner()
	unlock(Unlocks.Megafarm)

