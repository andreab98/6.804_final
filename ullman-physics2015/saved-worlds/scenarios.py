import data_structures as struct
import glob
import re
from paths import path_parser

def create_scenarios(folderpath):
	'''
	Parameters:
	folderpath (str): path of folder containing specifications

	Returns:
	scenarios (lst)
	'''
	scenarios = []

	full_paths = glob.glob(folderpath + '/*.txt')
	# print(full_paths)
	# Hannah:
	# paths = [x[73:] for x in full_paths]

	# Andrea:
	paths = [x[79:] for x in full_paths]

	# print(paths)
	for file in paths:
		print(file)

		all_lines = open(file, 'r').readlines()

		for i in range(6):
			lines = all_lines[16*i : 16*(i+1)]

			name = lines[0].split('.')[0].split('\\')[1]

			global_forces = lines[2]

			pairwise_forces = lines[4].split('(')[1:]
			pairwise_forces = [re.sub("[()'\n]", '', f).split(' ')[:3] for f in pairwise_forces]
			pairwise_forces_list = []
			for f in pairwise_forces:
				new_force = (float(re.sub('["]', '', f[0])), float(re.sub('["]', '', f[1])), re.sub('["]', '', f[2]))
				pairwise_forces_list.append(new_force)

			pucks = lines[6][1:-3].split(')) ((')
			pucks = [p.split(')') for p in pucks]
			new_pucks = []
			for p in pucks:
				new_pucks.append([re.sub('["()]', '', prop).split(' ') for prop in p])
			puck_list = []
			for p in new_pucks:
				puck_list.append({})
				for prop in p:
					curr_dict = puck_list[-1]
					try:
						curr_dict[prop[-2]] = float(prop[-1])
					except:
						curr_dict[prop[-2]] = prop[-1]

			surfaces = lines[8].split('((')[1:]
			surfaces = [s.split(' ') for s in surfaces]
			new_surfaces = []
			for s in surfaces:
				new_surfaces.append([re.sub('["()\n]', '', prop).split(' ') for prop in s][:6])
			surfaces_list = []
			for s in new_surfaces:
				curr_dict = {}
				curr_dict['upperleft'] = (float(s[0][0]), float(s[1][0]))
				curr_dict['lowerright'] = (float(s[2][0]), float(s[3][0]))
				curr_dict['friction'] = float(s[4][0])
				curr_dict['color'] = s[5][0]
				surfaces_list.append(curr_dict)

			positions = lines[10].split('(')[1:]
			positions = [p.split(' ')[:2] for p in positions]
			positions_list = []
			for p in positions:
				positions_list.append(tuple(float(re.sub('[()\n]', '', prop)) for prop in p))

			velocities = lines[12].split('(')[1:]
			velocities = [v.split(' ')[:2] for v in velocities]
			velocities_list = []
			for v in velocities:
				velocities_list.append(tuple(float(re.sub('[()\n]', '', prop)) for prop in v))


			path = lines[14]
			observed_path = path_parser(path)[0]

			# print(name)
			# print(global_forces)
			# print(pairwise_forces_list)
			# print(puck_list)
			# print(surfaces_list)
			# print(positions_list)
			# print(velocities_list)
			# print(path)
			# print('\n')

			scen_pucks = []
			for i in range(len(puck_list)):
				mass = puck_list[i]['mass']
				elastic = puck_list[i]['elastic']
				size = puck_list[i]['size']
				color = puck_list[i]['color']
				field_color = puck_list[i]['field-color']
				field_strength = puck_list[i]['field-strength']
				x, y = positions_list[i]
				v_x, v_y = velocities_list[i]
				scen_pucks.append(struct.Puck(mass, elastic, size, color, field_color, field_strength, x, y, v_x, v_y))

			scen_surfaces = []
			for s in surfaces_list:
				upperleft = s['upperleft']
				lowerright = s['lowerright']
				friction = s['friction']
				color = s['color']
				scen_surfaces.append(struct.Surface(upperleft, lowerright, friction, color))

			scen_global_forces = struct.Global_Force(global_forces)

			scen_pairwise_forces = []
			for pf in pairwise_forces_list:
				scen_pairwise_forces.append(struct.Pairwise_Force(pf[0], pf[1], pf[2]))

			scenario = struct.Scenario(name, scen_pucks, scen_surfaces, scen_global_forces, scen_pairwise_forces, observed_path)
			scenarios.append(scenario)
			# for p in scenario.pucks:
			# 	print("mass",p.mass)
			# 	print("color",p.color)
			# 	print("postition",p.position)
			# 	print("elastic",p.elastic)
			# 	print("size",p.size)
			# 	print("velocity",p.velocity)
			break
		break
	return(scenarios)

# Hannah:
# create_scenarios('C:/Users/hanna/Dropbox (MIT)/6.804_final/ullman-physics2015/saved-worlds/')

# Andrea:
# create_scenarios('/Users/andreabolivar/Desktop/6.804/6.804_final/ullman-physics2015/saved-worlds')
