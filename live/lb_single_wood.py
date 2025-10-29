from lb_single_utils import *

set_world_size(8)
# set_execution_speed(1)

notRankingFlg = False

size = 8 #get_world_size()
rSize =  range(size)
iWood = 512
iiWood = 81900
targets = [(0, 0), (0, 4), (2, 6), (2, 2), (4, 0), (4, 4), (6, 6), (6, 2)]
# targets = [(0, 0), (4, 3)]

CARRORT_COST = 512


state = {
	'finishCount': 0,
	'iterator': 0,
	'items': {
		'Hay': 0,
		'Wood': 0,
	},
}
map = {}

# use Leaderboards.Wood_Single
# finish is num_items(Items.Carrot) >= 500000000
# 設計方針：
# 混作利用。
# 極力キャッシュ参照を行って判定する
# 特に get_~ はStateやmapを参照して記録から引っ張れるなら記録から引っ張ること。
# なぜならtickが増えるからである。


def run():
	# while True:
	while not state['finishCount'] > 100000000:
		targetLen = 8 # len(targets)
		targetPos = targets[state['iterator'] % targetLen]
		mvTo(targetPos)
		if not (targetPos in map):
			map[targetPos] = {
				'ground': Grounds.Grassland,
				'companion': None,
			}

		_c = map[targetPos]['companion']
		if (_c != None):
			if (can_harvest()):
				harvest()
				if (map[_c[1]]['entity'] == _c[0]):
					state['finishCount'] += iiWood
				else:
					state['finishCount'] += iWood

		plant(Entities.Tree)
		c = get_companion()
		map[targetPos] = {
			'ground': Grounds.Grassland,
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
			# すでに対象の作物が植えられている場合
			if (map[c[1]]['entity'] == c[0]):
				if (can_harvest()):
					harvest()
					state['finishCount'] += iiWood
					continue
			else:
				map[c[1]]['entity'] = c[0]
		mvTo(c[1])

		# 前回植えて、また指定されたうえで戻ってきているため成長しきっている前提でharvestする
		harvest()

		if (c[0] == Entities.Grass):
			if (map[c[1]]['ground'] == Grounds.Soil):
				till()
				map[c[1]]['ground'] = Grounds.Grassland
			harvest()
			state['items']['Hay'] += 512
		elif (c[0] == Entities.Bush):
			plant(Entities.Bush)
			state['items']['Wood'] += 512
			state['finishCount'] += 512
		elif (c[0] == Entities.Carrot):
			# iteratorは苦肉の策なのでstate.itemsの挙動を見直せば省ける
			if (state['iterator'] > 1 and  state['items']['Wood'] > CARRORT_COST and state['items']['Hay'] > CARRORT_COST):
				if (map[c[1]]['ground'] == Grounds.Grassland):
					till()
					map[c[1]]['ground'] = Grounds.Soil
				plant(Entities.Carrot)
		state['iterator'] += 1

run()
# quick_print(num_items(Items.Wood))
# quick_print('Tree_single tick counts', get_tick_count())

