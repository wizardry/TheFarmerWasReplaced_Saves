from lb_single_utils import *

set_world_size(8)
# set_execution_speed(1)

notRankingFlg = False

size = 8 #get_world_size()
rSize =  range(size)
iCarrot = 512
iiCarrot = 81900
targets = [(0, 0), (0, 4), (2, 6), (2, 2), (4, 0), (4, 4), (6, 6), (6, 2)]
# targets = [(0, 0), (4, 3)]

CARRORT_COST = 512


state = {
	'finishCount': 0,
	'iterator': 0,
}
map = {}

# use Leaderboards.Carrots_Single
# finish is num_items(Items.Carrot) >= 100000000
# 設計方針：
# 混作利用。
# 極力キャッシュ参照を行って判定する
# 特に get_~ はStateやmapを参照して記録から引っ張れるなら記録から引っ張ること。
# なぜならtickが増えるからである。


def run():
	# carrotを植えるための素材を集める。
	# つもりが初期Itemsで用意されていた
#	for i in [0, 1]:
#		for x in [0, 1, 2, 3]:
#			for y in rSize:
#				harvest()
#				if (x+y) % 2:
#					plant(Entities.Bush)
#				move(North)
#			move(East)
#		mvTo()

	while not state['finishCount'] > 100000000:
#	while True:
		targetLen = 8 # len(targets)
		targetPos = targets[state['iterator'] % targetLen]
		mvTo(targetPos)

		# mapにposがないすなわち初アクセスなのでtillを行う
		if not (targetPos in map):
			till()
		else:
			if (can_harvest()):
				harvest()
				_c = map[targetPos]['companion']
				if (map[_c[1]]['entity'] == _c[0]):
					state['finishCount'] += iiCarrot
				else:
					state['finishCount'] += iCarrot

		plant(Entities.Carrot)
		c = get_companion()
		map[targetPos] = {
			'ground': Grounds.Soil,
			'companion': c,
		}
		if (num_items(Items.water) > 5):
			use_item(Items.water)

		if not (c[1] in map):
			map[c[1]] = {
				'entity': c[0],
				'ground': Grounds.Grassland
			}
		else:
			if (map[c[1]]['entity'] == c[0]):
				if (can_harvest()):
					harvest()
					state['finishCount'] += iiCarrot
					continue
				# harvest task and return
			else:
				map[c[1]]['entity'] = c[0]
		mvTo(c[1])
		# Groundsが切り替わるならその処理が必要そうだが
		# Carrots以外Grasslantで実行できるので切り替わらなさそう
#		if (c[0] == Entities.Grass):
#			if (map[c[1]]['ground'] == Grounds.Soil)
#				till()
#		if (c[0]  [])
#		if (map[c[1]]['ground'] ==)
		harvest()
		plant(c[0])
		state['iterator'] += 1

run()
# quick_print(num_items(Items.Carrot))
# quick_print('Carrots_single tick counts', get_tick_count())

