# WORLD	6
objects_6 = set()

forces_6 = set()
world_6 = world(objects_6, forces_6)


Blue	mass:	Medium
Yellow	mass:	Heavy
Red	mass:	Light
Green	patch:	Smooth
Purple	patch:	Weak
Brown	patch:	Strong
Pairwise forces:	Blue	attracts	Blue,	Blue	attracts	Yellow
Global	forces:	None

World	7
Blue	mass:	Medium
Yellow	mass:	Heavy
Red	mass:	Light
Green	patch:	Smooth
Purple	patch:	Weak
Brown	patch:	Strong
Pairwise forces:	Blue	attracts	Blue,	Yellow	attracts	Yellow
Global	forces:	West
World	8
Blue	mass:	Heavy
Yellow	mass:	Light
Red	mass:	Medium
Green	patch:	Weak
Purple	patch:	Strong
Brown patch:	Smooth
Pairwise forces:	Yellow	attracts	Yellow,	Red	attracts	Red,	Red	and	Yellow	repel
Global	forces:	East
World	9
Blue	mass:	Light
Yellow	mass:	Medium
Red	mass:	Heavy
Green	patch:	Weak
Purple	patch:	Strong
Brown	patch:	Smooth
Pairwise forces:	Blue	repels	Blue,	Red	repels	Red,	Red	and	Blue	attract
Global	forces:	South
World	10
Blue	mass:	Heavy
Yellow	mass:	Light
Red	mass:	Medium
Green	patch:	Strong
Purple	patch:	Smooth
Brown	patch:	Weak
Pairwise forces:	Yellow	attracts	Yellow,	Yellow	attracts	Red
Global	forces:	North