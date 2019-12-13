import data_structures as struct

# WORLD	1
b_mass_1 = struct.puck('blue', 'heavy', 0, 0, 0, 0)
y_mass_1 = struct.puck('yellow', 'light', 0, 0, 0, 0)
r_mass_1 = struct.puck('red', 'medium', 0, 0, 0, 0)
g_patch_1 = struct.surface('green', 'strong', width, height, 0, 0)
p_patch_1 = struct.surface('purple', 'smooth', width, height, 0, 0)
b_patch_1 = struct.surface('brown', 'weak', width, height, 0, 0)

objects_1 = {'b_mass' : b_mass_1,
			 'y_mass' : y_mass_1,
			 'r_mass' : r_mass_1,
			 'g_patch' : g_patch_1,
			 'p_patch' : p_patch_1,
			 'b_patch' : b_patch_1}

forces_1 = set()

world_1 = struct.world(objects_1, forces_1)

# Blue mass: Heavy
# Yellow mass: Light
# Red mass: Medium
# Green	patch: Strong
# Purple patch: Smooth
# Brown	patch: Weak
# Pairwise forces: None
# Global forces: None

# WORLD	2
b_mass_2 = struct.puck('blue', 'light', 0, 0, 0, 0)
y_mass_2 = struct.puck('yellow', 'medium', 0, 0, 0, 0)
r_mass_2 = struct.puck('red', 'heavy', 0, 0, 0, 0)
g_patch_2 = struct.surface('green', 'smooth', width, height, 0, 0)
p_patch_2 = struct.surface('purple', 'weak', width, height, 0, 0)
b_patch_2 = struct.surface('brown', 'strong', width, height, 0, 0)

objects_2 = {'b_mass' : b_mass_2,
			 'y_mass' : y_mass_2,
			 'r_mass' : r_mass_2,
			 'g_patch' : g_patch_2,
			 'p_patch' : p_patch_2,
			 'b_patch' : b_patch_2}

forces_2 = set(struct.pairwise_force(b_mass_2, b_mass_2, 'attract'),
			   struct.pairwise_force(r_mass_2, r_mass_2, 'attract'))

world_2 = struct.world(objects_2, forces_2)

# Blue	mass: Light
# Yellow mass: Medium
# Red mass:	Heavy
# Green	patch:	Smooth
# Purple patch:	Weak
# Brown	patch: Strong
# Pairwise forces:	Blue attracts Blue, Red attracts Red
# Global forces: None

# WORLD	3
b_mass_3 = struct.puck('blue', 'medium', 0, 0, 0, 0)
y_mass_3 = struct.puck('yellow', 'heavy', 0, 0, 0, 0)
r_mass_3 = struct.puck('red', 'light', 0, 0, 0, 0)
g_patch_3 = struct.surface('green', 'weak', width, height, 0, 0)
p_patch_3 = struct.surface('purple', 'strong', width, height, 0, 0)
b_patch_3 = struct.surface('brown', 'smooth', width, height, 0, 0)

objects_3 = {'b_mass' : b_mass_3,
			 'y_mass' : y_mass_3,
			 'r_mass' : r_mass_3,
			 'g_patch' : g_patch_3,
			 'p_patch' : p_patch_3,
			 'b_patch' : b_patch_3}

forces_3 = set(struct.pairwise_force(b_mass_3, b_mass_3, 'attract'),
			   struct.pairwise_force(y_mass_3, y_mass_3, 'attract'),
			   struct.pairwise_force(b_mass_3, y_mass_3, 'repel'))

world_3 = struct.world(objects_3, forces_3)

# Blue	mass: Medium
# Yellow mass: Heavy
# Red mass:	Light
# Green	patch: Weak
# Purple patch:	Strong
# Brown	patch: Smooth
# Pairwise forces: Blue	attracts Blue, Yellow attracts Yellow, Blue and	Yellow repel
# Global forces: None

# WORLD	4
b_mass_4 = struct.puck('blue', 'heavy', 0, 0, 0, 0)
y_mass_4 = struct.puck('yellow', 'light', 0, 0, 0, 0)
r_mass_4 = struct.puck('red', 'medium', 0, 0, 0, 0)
g_patch_4 = struct.surface('green', 'strong', width, height, 0, 0)
p_patch_4 = struct.surface('purple', 'smooth', width, height, 0, 0)
b_patch_4 = struct.surface('brown', 'weak', width, height, 0, 0)

objects_4 = {'b_mass' : b_mass_4,
			 'y_mass' : y_mass_4,
			 'r_mass' : r_mass_4,
			 'g_patch' : g_patch_4,
			 'p_patch' : p_patch_4,
			 'b_patch' : b_patch_4}

forces_4 = set(struct.pairwise_force(y_mass_4, y_mass_4, 'repel'),
			   struct.pairwise_force(r_mass_4, r_mass_4, 'repel'))

world_4 = struct.world(objects_4, forces_4)

# Blue mass: Heavy
# Yellow mass: Light
# Red mass: Medium
# Green	patch: Strong
# Purple patch: Smooth
# Brown	patch:	Weak
# Pairwise forces: Yellow repels Yellow, Red repels	Red
# Global forces: None

# WORLD	5
b_mass_5 = struct.puck('blue', 'light', 0, 0, 0, 0)
y_mass_5 = struct.puck('yellow', 'medium', 0, 0, 0, 0)
r_mass_5 = struct.puck('red', 'heavy', 0, 0, 0, 0)
g_patch_5 = struct.surface('green', 'strong', width, height, 0, 0)
p_patch_5 = struct.surface('purple', 'smooth', width, height, 0, 0)
b_patch_5 = struct.surface('brown', 'weak', width, height, 0, 0)

objects_5 = {'b_mass' : b_mass_5,
			 'y_mass' : y_mass_5,
			 'r_mass' : r_mass_5,
			 'g_patch' : g_patch_5,
			 'p_patch' : p_patch_5,
			 'b_patch' : b_patch_5}

forces_5 = set(struct.pairwise_force(b_mass_5, b_mass_5, 'repel'),
			   struct.pairwise_force(r_mass_5, r_mass_5, 'repel'),
			   struct.pairwise_force(r_mass_5, b_mass_5, 'attract'))

world_5 = struct.world(objects_5, forces_5)

# Blue mass: Light
# Yellow mass: Medium
# Red mass: Heavy
# Green patch: Strong
# Purple patch: Smooth
# Brown	patch: Weak
# Pairwise forces: Blue	repels Blue, Red repels Red, Red and Blue attract
# Global forces: None

# WORLD	6
b_mass_6 = struct.puck('blue', 'medium', 0, 0, 0, 0)
y_mass_6 = struct.puck('yellow', 'heavy', 0, 0, 0, 0)
r_mass_6 = struct.puck('red', 'light', 0, 0, 0, 0)
g_patch_6 = struct.surface('green', 'smooth', width, height, 0, 0)
p_patch_6 = struct.surface('purple', 'weak', width, height, 0, 0)
b_patch_6 = struct.surface('brown', 'strong', width, height, 0, 0)

objects_6 = {'b_mass' : b_mass_6,
			 'y_mass' : y_mass_6,
			 'r_mass' : r_mass_6,
			 'g_patch' : g_patch_6,
			 'p_patch' : p_patch_6,
			 'b_patch' : b_patch_6}

forces_6 = set(struct.pairwise_force(b_mass_6, b_mass_6, 'attract'),
			   struct.pairwise_force(b_mass_6, y_mass_6, 'attract'))

world_6 = struct.world(objects_6, forces_6)

# Blue mass: Medium
# Yellow mass: Heavy
# Red mass: Light

# Green	patch: Smooth
# Purple patch: Weak
# Brown	patch: Strong

# Pairwise forces: Blue	attracts Blue, Blue attracts Yellow
# Global forces: None

# WORLD 7
b_mass_7 = struct.puck('blue', 'medium', 0, 0, 0, 0)
y_mass_7 = struct.puck('yellow', 'heavy', 0, 0, 0, 0)
r_mass_7 = struct.puck('red', 'light', 0, 0, 0, 0)
g_patch_7 = struct.surface('green', 'smooth', width, height, 0, 0)
p_patch_7 = struct.surface('purple', 'weak', width, height, 0, 0)
b_patch_7 = struct.surface('brown', 'strong', width, height, 0, 0)

objects_7 = {'b_mass' : b_mass_7,
			 'y_mass' : y_mass_7,
			 'r_mass' : r_mass_7,
			 'g_patch' : g_patch_7,
			 'p_patch' : p_patch_7,
			 'b_patch' : b_patch_7}

forces_7 = set(struct.pairwise_force(b_mass_7, b_mass_7, 'attract'),
			   struct.pairwise_force(y_mass_7, y_mass_7, 'attract'),
			   struct.global_force(f_strength, 'west'))

world_7 = struct.world(objects_7, forces_7)

# Blue mass: Medium
# Yellow mass:	Heavy
# Red mass:	Light

# Green	patch: Smooth
# Purple patch:	Weak
# Brown	patch: Strong

# Pairwise forces: Blue	attracts Blue, Yellow attracts Yellow
# Global forces: West

# WORLD 8
b_mass_8 = struct.puck('blue', 'heavy', 0, 0, 0, 0)
y_mass_8 = struct.puck('yellow', 'light', 0, 0, 0, 0)
r_mass_8 = struct.puck('red', 'medium', 0, 0, 0, 0)
g_patch_8 = struct.surface('green', 'weak', width, height, 0, 0)
p_patch_8 = struct.surface('purple', 'strong', width, height, 0, 0)
b_patch_8 = struct.surface('brown', 'smooth', width, height, 0, 0)

objects_8 = {'b_mass' : b_mass_8,
			 'y_mass' : y_mass_8,
			 'r_mass' : r_mass_8,
			 'g_patch' : g_patch_8,
			 'p_patch' : p_patch_8,
			 'b_patch' : b_patch_8}

forces_8 = set(struct.pairwise_force(y_mass_8, y_mass_8, 'attract'),
			   struct.pairwise_force(r_mass_8, r_mass_8, 'attract'),
			   struct.pairwise_force(r_mass_8, y_mass_8, 'repel'),
			   struct.global_force(f_strength, 'east'))

world_8 = struct.world(objects_8, forces_8)

# Blue	mass: Heavy
# Yellow mass: Light
# Red mass:	Medium

# Green	patch: Weak
# Purple patch:	Strong
# Brown patch: Smooth

# Pairwise forces: Yellow attracts Yellow, Red attracts Red, Red and Yellow	repel
# Global forces: East

# WORLD 9
b_mass_9 = struct.puck('blue', 'light', 0, 0, 0, 0)
y_mass_9 = struct.puck('yellow', 'medium', 0, 0, 0, 0)
r_mass_9 = struct.puck('red', 'heavy', 0, 0, 0, 0)
g_patch_9 = struct.surface('green', 'weak', width, height, 0, 0)
p_patch_9 = struct.surface('purple', 'strong', width, height, 0, 0)
b_patch_9 = struct.surface('brown', 'smooth', width, height, 0, 0)

objects_9 = {'b_mass' : b_mass_9,
			 'y_mass' : y_mass_9,
			 'r_mass' : r_mass_9,
			 'g_patch' : g_patch_9,
			 'p_patch' : p_patch_9,
			 'b_patch' : b_patch_9}

forces_9 = set(struct.pairwise_force(b_mass_9, b_mass_9, 'repel'),
			   struct.pairwise_force(r_mass_9, r_mass_9, 'repel'),
			   struct.pairwise_force(r_mass_9, b_mass_9, 'attract'),
			   struct.global_force(f_strength, 'south'))

world_9 = struct.world(objects_9, forces_9)

# Blue	mass: Light
# Yellow mass: Medium
# Red mass:	Heavy

# Green	patch:	Weak
# Purple patch:	Strong
# Brown	patch:	Smooth

# Pairwise forces: Blue repels Blue, Red repels Red, Red and Blue attract
# Global forces: South

# WORLD 10
b_mass_10 = struct.puck('blue', 'heavy', 0, 0, 0, 0)
y_mass_10 = struct.puck('yellow', 'light', 0, 0, 0, 0)
r_mass_10 = struct.puck('red', 'medium', 0, 0, 0, 0)
g_patch_10 = struct.surface('green', 'strong', width, height, 0, 0)
p_patch_10 = struct.surface('purple', 'smooth', width, height, 0, 0)
b_patch_10 = struct.surface('brown', 'weak', width, height, 0, 0)

objects_10 = {'b_mass' : b_mass_10,
			  'y_mass' : y_mass_10,
			  'r_mass' : r_mass_10,
			  'g_patch' : g_patch_10,
			  'p_patch' : p_patch_10,
			  'b_patch' : b_patch_10}

forces_10 = set(struct.pairwise_force(y_mass_10, y_mass_10, 'attract'),
				struct.pairwise_force(y_mass_10, r_mass_10, 'attract'),
				struct.global_force(f_strength, 'north'))

world_10 = struct.world(objects_10, forces_10)

# Blue mass: Heavy
# Yellow mass: Light
# Red mass: Medium

# Green	patch: Strong
# Purple patch: Smooth
# Brown	patch: Weak

# Pairwise forces: Yellow attracts Yellow, Yellow attracts Red
# Global forces: North
