from lb_speedrun_util import *
from lb_speedrun_mains import *

# 単一の農地からリーダーボードを再びアンロックするまで、ゲームを完全に自動化します。

# Simulator より
# > 開始時のアンロック
# > ループ、if文、リスト、辞書などのすべてのプログラミング機能は、常にアンロックされたままです。

timer = get_time()

def run():
	# ~Unlocks.Speed > cost Grass20
	unlockSpeedAction()
	# ~Unlocks.Expand 拡大 Grass30
	unlockExpandAction()
	# ~Unlocks.Plant Grass 50
	# 待機状態で収穫した方が早いのか移動した方が早いのか要検証
	unlockPlantAction()
	# ~Unlock.Expand_2 Wood20
	unlockExpand2Action()
	# ~Unlock.Expand_2 Wood20
	# Hay ...50~
	unlockSpeed2Action()
	# ~Unlock.Carrot Wood50
	# Hay ...80~
	unlockCarrotAction()

	# ~Unlock.Expand_3 Wood30, Carrot20
	# Hay ...100~
	unlockExpand3Action()

	# ~Unlock.Speed_3 Wood50, Carrot50
	unlockSpeed3Action()

	# ~Unlock.Tree Wood50, Carrot70
	unlockTreeAction()

	# ~Unlock.Grass_2 Hay300
	unlockGrass2Action()

	# ~Unlock.Grass_2 Wood100, Carrot50
	unlockExpand4Action()

	# ~Unlock.Carrot_2 Wood250, already have it
	unlockCarrot2Action()

	# ~Unlock.Water Wood50
	unlockWaterAction()

	# ~Unlock.Grass_3 Wood500
	unlockGrass3Action()

	# ~Unlock.Tree_2 Hay300
	unlockTree2Action()

	# ~Unlock.Fertilizer Wood500
	unlockFertilizerAction()

	# ~Unlock.Carrot_3 Tree 1250
	unlockCarrot3Action()

	# ~Unlock.Speed_4 Carrot500
	unlockSpeed4Action()

	# ~Unlock.Watering_2 Carrot200
	unlockWater2Action()

	# ~Unlock.Pumpkins Wood500, Carrot200
	unlockPumpkinAction()

	# ~Unlock.Grass_4 Wood2500
	unlockGrass4Action()

	# ~Unlock.Sunflowers Carrot500
	unlockSunflowerAction()

	# ~Unlock.Fertilizer_2 Wood 1500
	unlockFertilizer2Action()

	# ~Unlock.Tree_3 Hay1200
	unlockTree3Action()

	# ~Unlock.Pumpkins_2 Carrot1000
	unlockPumpkin2Action()

	# ~Unlock.Watering_3 Tree 800
	unlockWater3Action()

	# ~Unlock.Carrot_4 Tree 6250
	unlockCarrot4Action()

	# ~Unlock.Expand_5 Pumpkin 1000
	unlockExpand5Action()

	# ~Unlock.Tree_4 Hay 4800
	unlockTree4Action()

	# ~Unlock.Speed_5 Carrot 1000
	unlockSpeed5Action()

	# ~Unlock.PolycultureAction Pumpkin 3000
	unlockPolycultureAction()

	# ~Unlock.Grass_5 Wood12500
	unlockGrass5Action()

	# ~Unlock.Fertilizer_3 Wood 9000
	unlockFertilizer3Action()

	# ~Unlock.Expand_6 Pumpkin 8000
	unlockExpand6Action()

	# ~Unlock.Mazes Weird_Substance 1000
	unlockMazeAction()

	# Unlocks.Megafarm Gold 2000
	unlockMegaFarmAction()

	# Unlocks.Megafarm_2 Gold 8000
	unlockMegaFarm2Action()

	# Unlocks.Pumpkins_3 Carrot 4000
	unlockPumpkin3Action()

	# Unlocks.Trees_5 Hay 19200
	unlockTree5Action()

	# Unlocks.Carrots_5 Wood 31200
	unlockCarrot5Action()

	# Unlocks.Grass_6 Wood 62500
	unlockGrass6Action()

	# Unlocks.Cactus Pumpkin 5000
	unlockCactusAction()

	# Unlocks.Pumpkin Carrot 16000
	unlockPumpkin4Action()

	# Unlocks.Cactus_2 Pumpkin 20000
	unlockCactus2Action()

	# Unlocks.Expand_7 Pumpkin 64000
	unlockExpand7Action()

	# Unlocks.Dinosaurs Cactus 2000
	unlockDinoAction()

	# Unlocks.Dinosaurs_2 Cactus 12000 (has 18,7k ~ )
	unlockDino2Action()

	# Unlocks.Maze_2 Cactus 12000
	unlockMaze2Action()

	# Unlocks.Maze_2 Cactus 12000
	unlockDino3Action()

	# Unlocks.Polyculture_2 Bone 72000
	unlockPolyculture2Action()

	# Unlocks.Polyculture_3 Bone 50000
	unlockPolyculture3Action()

	# Unlocks.Mazes_3 Cactus 72000
	unlockMaze3Action()

	# Unlocks.MagaFarm_3 Gold 32000
	unlockMegaFarm3Action()

	# Unlocks.MagaFarm_4 Gold 128000
	unlockMegaFarm4Action()

	# Unlocks.Leaderboard { Gold 1000000, Bone 2000000 }
	unlockLeaderboardAction()

	# Unlocks.MagaFarm_5 Gold 512000
	# unlockMegaFarm5Action()

	# # Unlocks.Polyculture_4 Bone 50000
	# unlockPolyculture4Action()

	# Unlocks.Carrots
	# Unlocks.Watering
	# Unlocks.Fertilizer
	# Unlocks.Pumpkins
	# Unlocks.Mazes
	# Unlocks.Megafarm
	# Unlocks.Polyculture
	# Unlocks.Cactus
	# Unlocks.Dinosaurs
	# Unlocks.Leaderboard
	clear()
run()
quick_print('Completed tick: '+ str(get_tick_count()) + ', time: ' + str(get_time() - timer))

# History
#
# V1: とりあえず終わらせた
# Completed tick: 33866280, time: 11455.7
