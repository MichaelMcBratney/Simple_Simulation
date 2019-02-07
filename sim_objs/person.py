# TODO: need to add more to the person class
#  what things should they be able to do?
#  what are all of their characteristics?
import random
from model import Model
from .sim_obj import SimObj
from definitions import *
import sim_objs.person_helpers.action as action
from .person_helpers import Traits, Genes, State


class Person(SimObj):

	# Some class variables. These might be moved to a better home later. Where they are does
	# not really matter

	# List of all actions that must be evaluated every day, for every person
	required_actions = [
		action.Breed(),
	]

	# List of all optional actions that can be done and picked based on an optional_picking function
	optional_actions = [
		action.HitByACar()
	]

	def __init__(self, name=None, genes=None, traits=None):  # , state=None, age=0):

		self.genes = Genes(genes or {})
		self.traits = Traits(traits or {}, self.genes)
		self.state = State({State.NAME: name}, self.genes, self.traits)

	# I am making properties to easily access some of the more popular Person
	# genes/traits/state
	@property
	def name(self):
		return self.state[State.NAME]

	@property
	def age(self):
		cur_age = Model.get().time - self.state[State.DOB]
		if cur_age < 365:
			return f'{cur_age} days'
		return f'{cur_age / 365} years old'

	@property
	def gender(self):
		return self.genes[Genes.GENDER]

	def update(self):
		"""
		1. Go through list of all required actions. Any action that is a non-zero affinity is performed
		2. Use self.pick_optional_actions() to get a list of optional actions to perform. Keep executing the
		   actions until done.
		TODO: Implement scheduled actions
		"""

		# 1. Filter the required actions by affinity > 0
		reqs = [act for act in Person.required_actions if act.affinity(self) > 0.95]

		# apply each required action to Person
		for act in reqs:
			act.apply(self)

		if self.state[State.ALIVE]:
			cause_of_death = self.decide_fate()
			if cause_of_death:
				self.kill(cause_of_death)
				print(f'{self.name} has died due to {cause_of_death} at {self.get_age_string()} old.')
			else:
				age = Model.get().time - self.state[State.DOB]
				if age > 365:
					age = round(age / 365, 3)
				if self.state[State.HEIGHT] < self.genes[Genes.ADULT_HEIGHT]:
					if age < self.genes[Genes.REPRODUCTIVE_AGE]:
						self.state[State.HEIGHT] += (random.uniform(0.06, 0.08) / 365)
					else:
						self.state[State.HEIGHT] += (random.uniform(0.03, 0.05) / 365)
				if self.state[State.WEIGHT] < self.genes[Genes.ADULT_HEIGHT]:
					if age < self.genes[Genes.REPRODUCTIVE_AGE]:
						self.state[State.WEIGHT] += (random.uniform(2, 3) / 365)
					else:
						self.state[State.WEIGHT] += (random.uniform(1.2, 1.8) / 365)

	@staticmethod
	def pick_name(gender):
		"""
		Input: gender, one of : 'male' , 'female'
		Output: A random full name  (string)
		Example use:
		pickName('female') will return a female name as string.
		"""

		def load_names(filename):
			"""
			Input: Name of file that contains a single name per line (string)
			Output: List of all the names in file with \n removed from the end (string list)
			"""
			namelist = []
			file_location = os.path.join(RESOURCES_DIR, filename)
			with open(file_location, 'r') as f:
				for line in f:
					namelist.append(line.strip('\n'))
			return namelist

		if gender == MALE:
			firstnames = load_names('male_firstnames.txt')
		elif gender == FEMALE:
			firstnames = load_names('female_firstnames.txt')
		else:
			return "NO GENDER"
		lastnames = load_names('lastnames.txt')
		# Sizes of the firstnames and lastnames lists:
		first = random.choice(firstnames)
		last = random.choice(lastnames)
		fullname = ''.join((first, ' ', last))
		return fullname

	def get_info(self):
		if self.state[State.ALIVE]:
			age = (Model.get().time - self.state[State.DOB]) / 365
			print(f'{self.name} is {round(age, 3)} years old, is a {self.gender}, and is {self.genes[Genes.ETHNICITY]}. '
			      f'{self.genes[Genes.PRONOUNS][0]} is {round(self.state[State.HEIGHT], 1)} meters tall, and '
			      f'{round(self.state[State.WEIGHT], 1)} kilograms. {self.genes[Genes.PRONOUNS][0]} will reach '
			      f'{self.genes[Genes.PRONOUNS][1]} reproductive age at {self.genes[Genes.REPRODUCTIVE_AGE]} years old.')
		else:
			age = self.state[State.DEATH]
			print(f'{self.name} died at age {age}, was a {self.gender}, and was {self.genes[Genes.ETHNICITY]}. '
			      f'{self.genes[Genes.PRONOUNS][0]} was {round(self.state[State.HEIGHT], 1)} meters tall, and weighed '
			      f'{round(self.state[State.WEIGHT], 1)} kilograms. {self.genes[Genes.PRONOUNS][0]} cause of death was '
			      f'{self.state[State.DEATH_CAUSE]}')

	def kill(self, cause):
		"""
		Kills this person
		Input: Cause of death (string)
		"""
		if self.state[State.ALIVE]:
			self.state[State.ALIVE] = False
			self.state[State.DEATH] = self.get_age_string()
			self.state[State.DEATH_CAUSE] = cause

	def decide_fate(self):
		"""
		Decides if person dies of some cause. CHANCE_OF_DEATH chance of coming close to death at a given day
		"""
		if random.randint(1, 1000) >= CHANCE_OF_DEATH:
			return None
		deathprobs = self.genes[Genes.CUSTOM_DEATH_PROBS]
		for cause, prob in deathprobs.items():
			if random.randint(1, 100) <= round(prob['chance']*80.0 + prob['age_factor']*((Model.get().time -
			                                                                              self.state[State.DOB]) / 365)):
				return cause
		return None

	def get_age_string(self):
		if self.state[State.DEATH] is None:
			age = Model.get().time - self.state[State.DOB]
			if age < 365:
				return str(age) + ' days'
			else:
				return str(round(age / 365, 3)) + ' years'
		return self.state[State.DEATH]
