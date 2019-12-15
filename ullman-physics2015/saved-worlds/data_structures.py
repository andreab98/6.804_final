class Puck:
	def __init__(self, mass, elastic, size, color, field_color, field_strength, x, y, v_x, v_y):
		self.mass = mass
		self.elastic = elastic
		self.size = size
		self.color = color
		self.field_color = field_color
		self.field_strength	= field_strength
		self.position = (x, y)
		self.velocity = (v_x, v_y)
		self.positions  = [(x, y)]
		self.velocities = []

	def update_pos(self,new_x,new_y):
		self.position = (new_x, new_y)
		self.positions.append((new_x, new_y))

	def get_averg_pos(self):
		sum_x, sum_y = 0, 0
		l = len(self.positions)

		for x, y in self.positions:
			sum_x += x
			sum_y += y

		return (sum_x/l, sum_y/l)

	def total_change(self):
		x_delta = self.positions[-1][0]-self.positions[0][0]
		y_delta = self.positions[-1][1]-self.positions[0][1]
		return (x_delta, y_delta)


class Surface:
	def __init__(self, upperleft, lowerright, friction, color):
		self.upperleft = upperleft
		self.lowerright = lowerright
		self.friction = friction
		self.color = color


class Global_Force:
	def __init__(self, f_direction):
		self.f_direction = f_direction
		self.f_strength = 5


class Pairwise_Force:
	def __init__(self, object_a, object_b, f_direction):
		self.object_a = object_a
		self.object_b = object_b
		self.f_strength = 5 if (f_direction == 'attract') else -5


class Scenario:
	def __init__(self, name, pucks, surfaces, global_forces, pairwise_forces, path):
		self.name = name
		self.pucks = pucks
		self.surfaces = surfaces
		self.global_forces = global_forces
		self.pairwise_forces = pairwise_forces
		self.path = path
