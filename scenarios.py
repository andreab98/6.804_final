import data_structures as struct
import worlds as worlds

# WORLD	1 SCENARIO 1
w1s1 = struct.scenario(worlds.world_1)
conditions_1 = {'b_mass' : [((486.5287228238303 309.47667316137813), (-2382.7911182306707 2875.210356898606))],
			    'y_mass' : [((341.61388013279065 368.2284079347737), (3593.2519887574017 2101.3808876741678))],
			    'r_mass' : [((313.3033750941977 205.75192537577823), (-479.8910531681031 -3459.197635995224)), ((366.9199564852752 101.3832494742237), (693.0247542914003 93.63981429487467))],
			    'g_patch' : g_patch_1,
			 	'p_patch' : p_patch_1,
			 	'b_patch' : b_patch_1}
w1s1.init_conditions(conditions_1)