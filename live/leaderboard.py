isDev = True
isDev = False
simSpeed = 10000000
prodSpeed = 10000
bkFlg = False

targets = {
	'sh': 'Hay_Single',
	'sc': 'Carrots_Single',
	'sw': 'Wood_Single',
	'sp': 'Pumpkins_Single',
	'sf': 'Sunflowers_Single',
	'scu': 'Cactus_Single',
	'sm': 'Maze_Single',

	'rh': 'Hay',
	'rc': 'Carrots',
	'rw': 'Wood',
	'rp': 'Pumpkins',
	'rf': 'Sunflowers',
	'rcu': 'Cactus',
	'rm': 'Maze',
}
target = targets['rp']

def Hay_Single_finish():
	return num_items(Items.Hay) >= 100000000,
def Carrots_Single_finish():
	return num_items(Items.Carrot) >= 100000000
def Wood_Single_finish():
	return num_items(Items.Wood) >= 500000000
def Pumpkins_Single_finish():
	return num_items(Items.Pumpkin) >= 10000000
def Sunflowers_Single_finish():
	return num_items(Items.Power) >= 10000
def Cactus_Single_finish():
	return num_items(Items.Cactus) >= 131072
def Maze_Single_finish():
	return num_items(Items.Gold) >= 616448

def Hay_Resouce_finish():
	return num_items(Items.Hay) >= 2000000000
def Carrots_Resouce_finish():
	return num_items(Items.Carrot) >= 2000000000
def Wood_Resouce_finish():
	return num_items(Items.Wood) >= 10000000000
def Pumpkin_Resouce_finish():
	return num_items(Items.Pumpkin) >= 200000000
def Sunflower_Resouce_finish():
	return num_items(Items.Power) >= 100000
def Cactus_Resouce_finish():
	return num_items(Items.Cactus) >= 33554432
def Dino_Resouce_finish():
	return num_items(Items.Bone) >= 33488928
def Maze_Resouce_finish():
	return num_items(Items.Gold) >= 9863168

settings = {
	'Hay_Single': {
		'filename': 'lb_single_hay',
		'type': Leaderboards.Hay_Single,
		'unlocks': Unlocks,
		'items': {},
		'globals': {},
		'finish': Hay_Single_finish,
		'seed': -1,
	},
	'Carrots_Single': {
		'filename': 'lb_single_carrots',
		'type': Leaderboards.Carrots_Single,
		'unlocks': Unlocks,
		'items': {
			Items.Hay: 1000000000,
			Items.Wood: 1000000000,
		},
		'globals': {},
		'finish': Carrots_Single_finish,
		'seed': -1,
	},
	'Wood_Single': {
		'filename': 'lb_single_wood',
		'type': Leaderboards.Wood_Single,
		'unlocks': Unlocks,
		'items': {},
		'globals': {},
		'finish': Wood_Single_finish,
		'seed': -1,
	},
	'Pumpkins_Single': {
		'filename': 'lb_single_pumpkin',
		'type': Leaderboards.Pumpkins_Single,
		'unlocks': Unlocks,
		'items': {
			Items.Carrot: 1000000000,
			Items.Power: 1000000000,
		},
		'globals': {},
		'finish': Pumpkins_Single_finish,
		'seed': -1,
	},
	'Sunflowers_Single': {
		'filename': 'lb_single_sunflower',
		'type': Leaderboards.Sunflowers_Single,
		'unlocks': Unlocks,
		'items': {
			Items.Carrot: 1000000000,
		},
		'globals': {},
		'finish': Sunflowers_Single_finish,
		'seed': -1,
	},
	'Cactus_Single': {
		'filename': 'lb_single_cactus',
		'type': Leaderboards.Cactus_Single,
		'unlocks': Unlocks,
		'items': {
			Items.Pumpkin: 1000000000,
		},
		'globals': {},
		'finish': Cactus_Single_finish,
		'seed': -1,
	},
	'Maze_Single': {
		'filename': 'lb_single_maze',
		'type': Leaderboards.Maze_Single,
		'unlocks': Unlocks,
		'items': {
			Items.Weird_Substance: 1000000000,
			Items.Power: 1000000000,
		},
		'globals': {},
		'finish': Maze_Single_finish,
		'seed': -1,
	},
	'Hay': {
		'filename': 'lb_resouce_hay',
		'type': Leaderboards.Hay,
		'unlocks': Unlocks,
		'items': {},
		'globals': {},
		'finish': Hay_Resouce_finish,
		'seed': -1,
	},
	'Carrots': {
		'filename': 'lb_resouce_carrot',
		'type': Leaderboards.Carrots,
		'unlocks': Unlocks,
		'items': {
			Items.Hay: 10000000000,
			Items.Wood: 100000000000,
		},
		'globals': {},
		'finish': Carrots_Resouce_finish,
		'seed': -1,
	},
	'Wood': {
		'filename': 'lb_resouce_wood',
		'type': Leaderboards.Wood,
		'unlocks': Unlocks,
		'items': {},
		'globals': {},
		'finish': Wood_Resouce_finish,
		'seed': -1,
	},
	'Pumpkins': {
		'filename': 'lb_resouce_pump',
		'type': Leaderboards.Pumpkins,
		'unlocks': Unlocks,
		'items': {
			Items.Carrot: 1000000000,
			Items.Power: 1000000000,
		},
		'globals': {},
		'finish': Pumpkin_Resouce_finish,
		'seed': -1,
	},
	'Sunflowers': {
		'filename': 'lb_resouce_sn',
		'type': Leaderboards.Sunflowers,
		'unlocks': Unlocks,
		'items': {},
		'globals': {},
		'finish': Sunflower_Resouce_finish,
		'seed': -1,
	},
	'Cactus': {
		'filename': 'lb_resouce_cactus',
		'type': Leaderboards.Cactus,
		'unlocks': Unlocks,
		'items': {
			Items.Pumpkin: 1000000000,
			Items.Power: 1000000000,
		},
		'globals': {},
		'finish': Cactus_Resouce_finish,
		'seed': -1,
	},
	'Dinosaur': {
		'filename': 'lb_resouce_dino',
		'type': Leaderboards.Dinosaur,
		'unlocks': Unlocks,
		'items': {
			Items.Cactus : 1000000000,
			Items.Power: 1000000000
		},
		'globals': {},
		'finish': Dino_Resouce_finish,
		'seed': -1,
	},
	'Maze': {
		'filename': 'lb_resouce_maze',
		'type': Leaderboards.Maze,
		'unlocks': Unlocks,
		'items': {
			Items.Weird_Substance : 1000000000,
			Items.Power: 1000000000,
		},
		'globals': {},
		'finish': Maze_Resouce_finish,
		'seed': -1,
	},
	'Speedrun': {
		'filename': 'lb_speedrun',
		'type': Leaderboards.Fastest_Reset,
		'unlocks': {},
		'items': {},
		'globals': {},
		'finish': None,
		'seed': -1,
	},

}

def run_dev(key):
	op = settings[key]
	op['globals']['finish'] = op['finish']
	filename = op['filename']
	if bkFlg:
		filename += '_bk'
	time = simulate(
		filename,
		op['unlocks'],
		op['items'],
		op['globals'],
		op['seed'],
		simSpeed
	)
	print(key, time)

def run(key):
	op = settings[key]
	filename = op['filename']
	if bkFlg:
		filename += '_bk'

	leaderboard_run(op['type'], filename, prodSpeed)

if (isDev):
	run_dev(target)
else:
	run(target)
