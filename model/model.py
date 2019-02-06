class Model:
	""" Using singleton. See https://gist.github.com/pazdera/1098129

	Singleton is used when we only want a single instance of this class across all of our code,
	and importantly we do not want to accidently make a second instance. Therefore, whenever we
	want to use Model we do:

	Model.get().WHATEVER

	This ensures that we only have a single instance
	"""

	# This variable holds the true instance. Notice it is a class variable and
	# not an instance variable
	__instance = None

	@staticmethod
	def get():
		""" Static access method. """
		if Model.__instance is None:
			Model()
		return Model.__instance

	def __init__(self):
		""" Virtually private constructor. """
		if Model.__instance is not None:
			raise Exception("This class is a singleton!")

		# If exception was not raised, this is the only instance of Model
		Model.__instance = self

		# Initialize vars
		self.time = 0
		self.sim_objs = []

	def run(self, hours):
		"""update each simulated object by #hours worth of time"""

		for _ in range(hours):
			for obj in self.sim_objs:
				obj.update()
			self.time += 1
