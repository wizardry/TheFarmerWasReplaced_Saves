from lb_single_utils import *

# singlePumpkinRun is default has items carrot 1B and power 1B

set_world_size(8)
# set_execution_speed(1)

notRankingFlg = False

size = 8 #get_world_size()
rSize =  range(size)

state = {
	'finishCount': 0,
	'iterator': 0,
	'items': {
		'Carrot': 100000000,
	},
}

# use Leaderboards.Pumpkin_Single
# finish is num_items(Items.Pumpkin) >= 10000000

# pupkin 1 = 512, 2x2 = 4096
# 単一収穫量 x 面積 x 一片の長さ
# 3*3 *3 = 55,296
# 6*6 = 110,592
# 8*8 = 196,608
# 設計方針：
# 8x8を最大効率で収穫を繰り返すのがよさそう

def run():
	# 初回のみtill が発生するためwhileの外で行う。
	# それによりループ毎のtillをするかどうかのifを外すことができ、tick省略が狙えるはず

	# plant and till
	for x in rSize:
		for y in rSize:
			till()
			plant(Entities.Pumpkin)
			# 1マス移動と決まっている場合過剰なifを通るmvToより直接moveを呼んだ方が良い
			move(North)
		move(East)

	# while True:
	while not state['finishCount'] > 10000000:
		# mappingをx, yで行うため 0,0 に戻らないといけない。
		# get_pos_N はtickを消費する
		mvTo()
		# 成長途中のものもEntity.Pumpkinとして扱ってしまうためentityで判定するとcanHarvestも必要になりチェック数が増える。
		# Pumpkinを全域に埋めることが確定しているためcanHarvestのみを見る
		# {(x, y), (x, y)...}
		cantHarvSet = set()
		# check and plant
		# tillは外で行っているため行わない。palntは成功時にのみ200t, 何も行わないときは1tなので妥協する
		# tillついでに植えられている1周目と2周目では役割が若干異なり
		# 2周目以降はMap生成をするついでに植えるイメージとなり、成長前に判定してしまう。
		for x in rSize:
			for y in rSize:
				plant(Entities.Pumpkin)
				if not can_harvest():
					cantHarvSet.add((x, y))
				move(North)
			move(East)

		while not len(cantHarvSet) == 0:
			_set = set(cantHarvSet)
			for pos in _set:
				mvTo(pos)
				if not (can_harvest()):
					use_item(Items.Water)
					plant(Entities.Pumpkin)
				else:
					cantHarvSet.remove(pos)
		harvest()
		state['finishCount'] += 196608
		state['iterator'] += 1


run()
quick_print(num_items(Items.Pumpkin), state)
quick_print('Pumpkin_single tick counts', get_tick_count())

