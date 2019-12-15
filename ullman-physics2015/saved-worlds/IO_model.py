import scenarios as scen

def io_model(obs_path, scenario_id):
	poss_worlds = {}
	diff = {}

	for s in scen.scenarios:
		if s.name.split('_')[-1] == str(scenario_id):
			name = s.name.split('_')[0]
			path = [p[0] for p in s.path]
			poss_worlds[name] = path
	
	for name, path in poss_worlds.items():
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


# TESTING

w10s1 = [p[0] for p in scen.scenarios[0].path]
w10s2 = [p[0] for p in scen.scenarios[1].path]
w1s1 = [p[0] for p in scen.scenarios[6].path]

print(io_model(w10s2, 2))