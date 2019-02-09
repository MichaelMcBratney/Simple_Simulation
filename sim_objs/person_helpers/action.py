from model import Model
import random
from .genes import Genes
from .state import State
import sim_objs.person_helpers.state
from definitions import *
import sim_objs.person


class Action:

	def affinity(self, person):
		""" To be defined in concrete action classes. Returns a
		float [0, 1] which defines the affinity the given person
		has towards the action """

		raise NotImplementedError

	def apply(self, person):
		""" To be defined in the concrete action classes. Applies
		the action to the person. Can affect person's:

		- traits
		- state

		Returns: a list of actions to be immediately taken
		"""

		raise NotImplementedError


class Breed(Action):

	def affinity(self, person):

		# For now I will just return one. This means that every person has a 100% affinity towards
		# breeding. In other words, there is a high likelihood that a person will try to breed.
		# everyday. This does not mean the breeding will be successful, this happens in
		# Breed.apply()

		return random.uniform(0, 1)

	def apply(self, person):
		"""
		One parent is the person. Gets random other parent.
		"""

		# print (f"Trying to breed, {person.name}")

		parent1 = person
		parent2 = random.choice(Model.get().sim_objs)
		for i in range(random.randint(0, 10)):  # else sometimes the loop keeps running indefinitely
			if parent1 == parent2 or (not parent1.state[sim_objs.person_helpers.state.State.ALIVE]) or (not parent1.state[
				sim_objs.person_helpers.state.State.ALIVE]):
				parent2 = random.choice(Model.get().sim_objs)
			else:
				break

		if parent1.genes[Genes.GENDER] != parent2.genes[Genes.GENDER]:
			if (Model.get().time - parent1.state[State.DOB]) / 365 >= parent1.genes[Genes.REPRODUCTIVE_AGE] and \
					(Model.get().time - parent2.state[State.DOB]) / 365 >= parent2.genes[Genes.REPRODUCTIVE_AGE]:
				if random.randint(0, 100) <= 2:
					Model.get().sim_objs.append(Breed.breed(parent1, parent2))
					print(f"{parent1.name} and {parent2.name} gave birth to a baby {Model.get().sim_objs[-1].gender} "
					      f"named {Model.get().sim_objs[-1].name}.")

	@staticmethod
	def breed(person1, person2):
		parents = dict()
		if person1.genes[Genes.GENDER] is MALE:
			father = parents['father'] = person1
			mother = parents['mother'] = person2
		else:
			father = parents['father'] = person2
			mother = parents['mother'] = person1
		genes = dict()
		genes[Genes.PARENTS] = parents
		genes[Genes.GENDER] = random.choice([MALE, FEMALE])
		genes[Genes.ETHNICITY] = random.choice(ETHNICITIES)
		if genes[Genes.GENDER] == MALE:
			genes[Genes.REPRODUCTIVE_AGE] = round((father.genes[Genes.REPRODUCTIVE_AGE] +
			                                       mother.genes[Genes.REPRODUCTIVE_AGE] + random.uniform(-1, 1)) / 2, 1)
			genes[Genes.ADULT_HEIGHT] = round((father.genes[Genes.ADULT_HEIGHT] + mother.genes[Genes.ADULT_HEIGHT] +
			                                   random.uniform(-0.15, 0.15)) / 2, 1)
			genes[Genes.ADULT_WEIGHT] = round((father.genes[Genes.ADULT_WEIGHT] + mother.genes[Genes.ADULT_WEIGHT] +
			                                   random.uniform(-5, 5)), 1)
		else:
			genes[Genes.REPRODUCTIVE_AGE] = round((father.genes[Genes.REPRODUCTIVE_AGE] +
			                                       mother.genes[Genes.REPRODUCTIVE_AGE] +
			                                       random.uniform(-0.7, 0.7)) / 2, 1)
			genes[Genes.ADULT_HEIGHT] = round((father.genes[Genes.ADULT_HEIGHT] + mother.genes[Genes.ADULT_HEIGHT] +
			                                   random.uniform(-0.12, 0.12)) / 2, 1)
			genes[Genes.ADULT_WEIGHT] = round((father.genes[Genes.ADULT_WEIGHT] + mother.genes[Genes.ADULT_WEIGHT] +
			                                   random.uniform(-2.8, 2.8)), 1)
		return sim_objs.person.Person(genes=genes)


class HitByACar(Action):

	def affinity(self, person):
		# TODO: Analyze the persons traits and determine how likely they are to be hit by a car
		return random.uniform(0, 1)

	def apply(self, person):
		""" Low chance to kill the person """

		if random.randint(0, 100) <= 2:
			print(f"{person.name} is hit by a car and killed.")
			person.state[sim_objs.person_helpers.state.State.ALIVE] = False
