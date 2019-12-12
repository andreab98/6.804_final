
class puck:
	def __init__(self, mass, friction):
		self.mass = mass
		self.friction = friction


class surface:
	def __init__(self, mass, friction):
		self.mass = mass
		self.friction = friction


class pairwise:
	def __init__(self, f_strength):
		self.f_strength = f_strength


class global_force:
	def __init__(self,f_strength,f_direction):
		self.f_strength = f_strength
		self.f_direction = f_direction

# class path --> nothing 
# 

