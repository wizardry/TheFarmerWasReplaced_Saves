
def checkOverSizeFromWorld(x = 0, y = 0):
	now = [get_pos_x(), get_pos_y()]
	if (now[0] + x > get_world_size()):
		print('Error: over size to x')
	if (now[1] + y > get_world_size()):
		print('Error: over size to y')
		