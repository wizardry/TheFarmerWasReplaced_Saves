isDev = True
isDev = False
simSpeed = 1000
prodSpeed = 128
target = None
bkFlg = False

# speed > palnt > expand > speed2 > carrot > grass2 > expand2
# > Tree > carrot2 > speed3 >  expand3 > water > grass3 > Tree2 > Fertilizer
# > Carrot3 > speed4 > Pumpkin > water2 > Grass4 > Pumpkin2 > Speed5(max)
# > sunflower > carrot4 > expand4 > water3 > expand5

SCENES = [
	"Grass", "Speed", "Plant", "Expand", "Speed_2",
	"Carrot", "Grass_2", "Expand_2", "Tree", "Carrot_2",
	"Speed_3" , "Expand_3", "Water", "Grass_3", "Tree_2",
	"Fertilizer", "Carrot_3", "Speed_4", "Pumpkin", "water2",
	"Grass_4", "Pumpkin_2", "Speed_5", "Sunflower", "Carrot_4",
	"Expand_4", "Water_3", "Expand_5"
]


setting = {
	'filename': 'lb_speedrun',
	'type': Leaderboards.Fastest_Reset,
	'unlocks': {},
	'items': {},
	'globals': {},
	'finish': None,
	'seed': -1,
}
def run_dev(scene = None):
	op = settings
	# TODO: scene制御
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
	print(scene, time)

def run(scene = None):
	filename = setting['filename']
	if bkFlg:
		filename += '_bk'

	leaderboard_run(setting['type'], filename, prodSpeed)

if (isDev):
	run_dev(target)
else:
	run(target)
