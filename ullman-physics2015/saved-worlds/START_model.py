import scenarios as scen
# import SSS_model as sss
import random

def start_model(obs_path, scenario_id):
	initial = scen.scenarios[16]
	# initial = sss.sss_model(obs_path, scenario_id)
	# for i in range(50):
	initial_diff

	poss_worlds = {}
	# diff = {}

	for s in scen.scenarios:
		if s.name.split('_')[-1] == str(scenario_id):
			name = s.name.split('_')[0]
			path = [p[0] for p in s.path]
			poss_worlds[name] = path
	
	name, path = list(poss_worlds.items())[random.randint(0, len(poss_worlds))]
	world_id = int(name.split('d')[1])
	world_diff = 0

	for i in range(len(path)):
		for j in range(4):
			simulated_x, simulated_y = path[i][j]
			observed_x, observed_y = obs_path[i][j]
			world_diff += ((simulated_x-observed_x)**2 + (simulated_y-observed_y)**2)**0.5

	diff[world_id] = world_diff

	print(diff)
	return min(diff, key=diff.get)

w10s1 = [p[0] for p in scen.scenarios[0].path]
w10s2 = [p[0] for p in scen.scenarios[1].path]
w1s1 = [p[0] for p in scen.scenarios[6].path]

print(start_model(w10s2, 2))