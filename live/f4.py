from lb_single_utils import *
clear()
size = 3
set_world_size(size)
mvTo((2,1), size, True)
plant(Entities.Bush)
print(0)
mvTo((0,0), size, True)
plant(Entities.Bush)
print(1)