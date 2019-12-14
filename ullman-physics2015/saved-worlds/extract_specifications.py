import glob

def extract_specifications(folderpath):
	'''
	Takes in a folder and outputs a .txt file containing the scenario specifications.

	Parameters:
	folderpath (str): path of folder containing 6 scenario specifications for one world

	Returns:
	None
	'''
	world_num = folderpath.split('/')[-1]
	
	with open(world_num + '_specs' + '.txt', 'w+') as file_new:
		full_paths = glob.glob(folderpath + '/*.ss')
		paths = [x[73:] for x in full_paths]

		for file in paths:
			specs, positions, velocities, path = open(file, 'r').readlines()
			
			global_forces, pairwise_forces, pucks, surfaces = specs[26:-2].split("'")
			pairwise_forces = pairwise_forces[1:-2]
			pucks = pucks[1:-2]
			surfaces = surfaces[1:-2]

			positions = positions[13:-4]
			velocities = velocities[13:-4]
			path = path[23:]

			file_new.write(file + '\n')
			file_new.write('GLOBAL FORCES:\n' + global_forces + '\n')
			file_new.write('PAIRWISE FORCES:\n' + pairwise_forces + '\n')
			file_new.write('PUCKS:\n' + pucks + '\n')
			file_new.write('SURFACES:\n' + surfaces + '\n')
			file_new.write('POSITIONS:\n' + positions + '\n')
			file_new.write('VELOCITIES:\n' + velocities + '\n')
			file_new.write('PATH:\n' + path + '\n\n')

for i in range(1, 11):
	extract_specifications('C:/Users/hanna/Dropbox (MIT)/6.804_final/ullman-physics2015/saved-worlds/world' + str(i))
