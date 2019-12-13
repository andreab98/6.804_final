import data_structures as struct

# WORLD	1
p1 = struct.puck('blue', 'heavy', 0, 0, 0, 0)
p2 = struct.puck('yellow', 'light', 0, 0, 0, 0)
p3 = struct.puck('red', 'medium', 0, 0, 0, 0)
s1 = struct.surface('green', 'strong', width, height, 0, 0)
s2 = struct.surface('purple', 'smooth', width, height, 0, 0)
s3 = struct.surface('brown', 'weak', width, height, 0, 0)

objects_1 = set(p1, p2, p3, s1, s2, s3)
forces_1 = set()
world_1 = struct.world(objects_1, forces_1)

# World	1
# Blue	mass: Heavy
# Yellow mass: Light
# Red mass: Medium
# Green	patch: Strong
# Purple patch: Smooth
# Brown	patch: Weak
# Pairwise forces: None
# Global forces: None

# WORLD	2
p1 = struct.puck('blue', 'light', 0, 0, 0, 0)
p2 = struct.puck('yellow', 'medium', 0, 0, 0, 0)
p3 = struct.puck('red', 'heavy', 0, 0, 0, 0)
s1 = struct.surface('green', 'smooth', width, height, 0, 0)
s2 = struct.surface('purple', 'weak', width, height, 0, 0)
s3 = struct.surface('brown', 'strong', width, height, 0, 0)

f1 = struct.pairwise_force(p1, p1, f_strength) #attracts
f2 = struct.pairwise_force(p3, p3, f_strength) #attracts

objects_2 = set(p1, p2, p3, s1, s2, s3)
forces_2 = set(f1, f2)
world_2 = struct.world(objects_2, forces_2)

# World	2
# Blue	mass: Light
# Yellow mass: Medium
# Red mass:	Heavy
# Green	patch:	Smooth
# Purple patch:	Weak
# Brown	patch: Strong
# Pairwise forces:	Blue attracts Blue, Red attracts Red
# Global forces: None

# WORLD	3
p1 = struct.puck('blue', 'medium', 0, 0, 0, 0)
p2 = struct.puck('yellow', 'heavy', 0, 0, 0, 0)
p3 = struct.puck('red', 'light', 0, 0, 0, 0)
s1 = struct.surface('green', 'weak', width, height, 0, 0)
s2 = struct.surface('purple', 'strong', width, height, 0, 0)
s3 = struct.surface('brown', 'smooth', width, height, 0, 0)

f1 = struct.pairwise_force(p1, p1, f_strength) #attracts
f2 = struct.pairwise_force(p2, p2, f_strength) #attracts
f3 = struct.pairwise_force(p1, p2, f_strength) #repel

objects_3 = set(p1, p2, p3, s1, s2, s3)
forces_3 = set(f1, f2, f3)
world_3 = struct.world(objects_3, forces_3)

# World	3
# Blue	mass: Medium
# Yellow mass: Heavy
# Red mass:	Light
# Green	patch: Weak
# Purple	patch:	Strong
# Brown	patch:	Smooth
# Pairwise forces: Blue	attracts Blue, Yellow attracts Yellow, Blue and	Yellow repel
# Global forces:	None

# WORLD	4
p1 = struct.puck('blue', 'heavy', 0, 0, 0, 0)
p2 = struct.puck('yellow', 'light', 0, 0, 0, 0)
p3 = struct.puck('red', 'medium', 0, 0, 0, 0)
s1 = struct.surface('green', 'strong', width, height, 0, 0)
s2 = struct.surface('purple', 'smooth', width, height, 0, 0)
s3 = struct.surface('brown', 'weak', width, height, 0, 0)

f1 = struct.pairwise_force(p2, p2, f_strength) #repels
f2 = struct.pairwise_force(p3, p3, f_strength) #repels

objects_4 = set(p1, p2, p3, s1, s2, s3)
forces_4 = set(f1, f2)
world_4 = struct.world(objects_4, forces_4)

# World	4
# Blue mass: Heavy
# Yellow mass: Light
# Red mass: Medium
# Green	patch: Strong
# Purple patch: Smooth
# Brown	patch:	Weak
# Pairwise forces: Yellow repels Yellow, Red repels	Red
# Global forces: None

# WORLD	5
p1 = struct.puck('blue', 'heavy', 0, 0, 0, 0)
p2 = struct.puck('yellow', 'light', 0, 0, 0, 0)
p3 = struct.puck('red', 'medium', 0, 0, 0, 0)
s1 = struct.surface('green', 'strong', width, height, 0, 0)
s2 = struct.surface('purple', 'smooth', width, height, 0, 0)
s3 = struct.surface('brown', 'weak', width, height, 0, 0)

f1 = struct.pairwise_force(p1, p1, f_strength) #repels
f2 = struct.pairwise_force(p3, p3, f_strength) #repels
f3 = struct.pairwise_force(p1, p3, f_strength) #attract

objects_5 = set(p1, p2, p3, s1, s2, s3)
forces_5 = set(f1, f2, f3)
world_5 = struct.world(objects_5, forces_5)

# World	5
# Blue mass: Light
# Yellow mass: Medium
# Red mass: Heavy
# Green patch: Strong
# Purple patch: Smooth
# Brown	patch: Weak
# Pairwise forces: Blue	repels Blue, Red repels Red, Red and Blue attract
# Global forces: None

# WORLD	6

p1 = struct.puck('blue', 'medium', 0, 0, 0, 0)
p2 = struct.puck('yellow', 'heavy', 0, 0, 0, 0)
p3 = struct.puck('red', 'light', 0, 0, 0, 0)
s1 = struct.surface('green', 'smooth', width, height, 0, 0)
s2 = struct.surface('purple', 'weak', width, height, 0, 0)
s3 = struct.surface('brown', 'strong', width, height, 0, 0)

f1 = struct.pairwise_force(p1, p1, f_strength)
f2 = struct.pairwise_force(p1, p2, f_strength)

objects_6 = set(p1, p2, p3, s1, s2, s3)
forces_6 = set(f1, f2)
world_6 = struct.world(objects_6, forces_6)

# Blue mass: Medium
# Yellow mass: Heavy
# Red mass: Light

# Green	patch: Smooth
# Purple patch: Weak
# Brown	patch: Strong

# Pairwise forces: Blue	attracts Blue, Blue attracts Yellow
# Global forces:	None


# WORLD	7
# Blue	mass:	Medium
# Yellow	mass:	Heavy
# Red	mass:	Light
# Green	patch:	Smooth
# Purple	patch:	Weak
# Brown	patch:	Strong
# Pairwise forces:	Blue	attracts	Blue,	Yellow	attracts	Yellow
# Global	forces:	West

# World	8
# Blue	mass:	Heavy
# Yellow	mass:	Light
# Red	mass:	Medium
# Green	patch:	Weak
# Purple	patch:	Strong
# Brown patch:	Smooth
# Pairwise forces:	Yellow	attracts	Yellow,	Red	attracts	Red,	Red	and	Yellow	repel
# Global	forces:	East

# World	9
# Blue	mass:	Light
# Yellow	mass:	Medium
# Red	mass:	Heavy
# Green	patch:	Weak
# Purple	patch:	Strong
# Brown	patch:	Smooth
# Pairwise forces:	Blue	repels	Blue,	Red	repels	Red,	Red	and	Blue	attract
# Global	forces:	South

# World	10
# Blue	mass:	Heavy
# Yellow	mass:	Light
# Red	mass:	Medium
# Green	patch:	Strong
# Purple	patch:	Smooth
# Brown	patch:	Weak
# Pairwise forces:	Yellow	attracts	Yellow,	Yellow	attracts	Red
# Global	forces:	North
