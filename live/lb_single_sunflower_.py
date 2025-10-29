from lb_single_utils import *

# singleSunflowerRun is default has items Carrot 1B

set_world_size(8)
# set_execution_speed(1)

notRankingFlg = False

size = 8 #get_world_size()
rSize =  range(size)

state = {
	'finishCount': 0,
	'iterator': 0,
	'items': {},
}

# use Leaderboards.Sunflower_Single
# finish is num_items(Items.Power) >= 10000

# 収穫: 1, 消費: 30Action につき 1消費
# Action = 移動、植え付け、収穫
# コード実行でもパワーを消費するが詳細値は不明
# 仕様: measureでpetalのcountを取得。7~15
# 10本以上植えられてるときにヒマワリ全体でもっとも大きいpetalを収穫すればボーナスとして収穫*5
# しかし、ボーナスのみを狙ってもたいして効率が良くなるわけではないことに注意
#
# 設計方針：
# 花びら関係なく収穫 -> tick counts 6393261 15~6分
# 15の花びらだけ -> 20分
# 全体を埋めて大きい順から収穫していく -> 10分　3713662

def run():
	# { petalCount: [(x,y)]}
	map = {
		15: [],
		14: [],
		13: [],
		12: [],
		11: [],
		10: [],
		9: [],
		8: [],
		7: [],
	}

	# plant and till
	for x in rSize:
		for y in rSize:
			till()
			plant(Entities.Sunflower)
			m = measure()
			map[m].append((x,y))
			# 1マス移動と決まっている場合過剰なifを通るmvToより直接moveを呼んだ方が良い
			move(North)
		move(East)
	# while True:
	while not state['finishCount'] > 10000:

		_t = []
		for i in map:
			# 7は最小値なので10枚のこす
			if (i == 7):
				# スライス構文 10以降の数値をスライスして取得
				for pos in map[i][10:]:
					mvTo(pos)
					if not (can_harvest()):
						use_item(Items.Fertilizer)
					a = num_items(Items.Power)
					c = measure()
					harvest()
					b = num_items(Items.Power)
			else:
				for pos in map[i]:
					mvTo(pos)
					if not (can_harvest()):
						use_item(Items.Fertilizer)
					a = num_items(Items.Power)
					c = measure()
					harvest()
					b = num_items(Items.Power)

		map = {
			15: [],
			14: [],
			13: [],
			12: [],
			11: [],
			10: [],
			9: [],
			8: [],
			7: [],
		}
		mvTo()
		for x in rSize:
			for y in rSize:
				plant(Entities.Sunflower)
				use_item(Items.Water)
				map[measure()].append((x, y))
				move(North)
			move(East)
		state['finishCount'] = num_items(Items.Power)
run()
quick_print(num_items(Items.Power), state)
quick_print('Sunflower_single tick counts', get_tick_count())

