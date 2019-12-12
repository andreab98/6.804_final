import data_structures as struct

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