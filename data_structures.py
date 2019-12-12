
class Puck:
	def __init__(self, mass, friction, color, diameter, x, y, v_x, v_y):
		self.mass = mass
		self.friction = friction
		self.color = None
		self.diameter = diameter
		self.position = (x, y)
		self.velocity = (v_x, v_y)


class Surface:
	def __init__(self, mass, friction, color, length, x, y):
		self.mass = mass
		self.friction = friction
		self.color = None
		self.length = length
		self.position = (x, y)


class Pairwise_force:
	def __init__(self, object_a, object_b, f_strength):
		self.f_strength = f_strength


class Global_force:
	def __init__(self, f_strength, f_direction):
		self.f_strength = f_strength
		self.f_direction = f_direction


class World:
	def __init__(objects, forces):
		self.objects = objects
		self.forces = forces


class Scenario(World):
	def init_conditions(objects, conditions):
		for o in objects:
			o.x, o.y, o.v_x, o.v_y = conditions[o]
		return objects
