
class puck:
	def __init__(self, mass, friction, diameter, x, y, v_x, v_y):
		self.mass = mass
		self.friction = friction
		self.diameter = diameter
		self.position = (x, y)
		self.velocity = (v_x, v_y)


class surface:
	def __init__(self, mass, friction, length, x, y):
		self.mass = mass
		self.friction = friction
		self.length = length
		self.position = (x, y)


class pairwise_force:
	def __init__(self, f_strength):
		self.f_strength = f_strength


class global_force:
	def __init__(self, f_strength, f_direction):
		self.f_strength = f_strength
		self.f_direction = f_direction


class scenario:
	def __init__():
