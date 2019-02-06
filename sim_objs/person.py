# TODO: need to add more to the person class
#  what things should they be able to do?
#  what are all of their genes?
import random
import os
from model import Model
from sim_objs import sim_obj
from definitions import RESOURCES_DIR, DEATH_PROBS, CHANCE_OF_DEATH, POSSIBLE_GENDERS, POSSIBLE_ETHNICITIES
# from collections import Iterable


class Person(sim_obj.SimObj):
	def __init__(self, name=None, genes=None, age=0, death_probs=DEATH_PROBS, parents=None):
		# Set state of person to one of : 'alive' or 'deceased'.
		self.state = "alive"
		self.death_cause = None

		# Initialize age
		self.age = age

		self.parents = parents

		# If the parameter, "genes" is specified, the information in
		# the parameter will be translated and assigned to the person class's instances.
		# Else both the genes and the translated assigned instances will be randomly generated.

		if genes:
			self.genes = genes
			if genes['gender'] == "Male":
				self.pronoun1 = "He"
				self.pronoun2 = "his"
			else:
				self.pronoun1 = "She"
				self.pronoun2 = "her"
		else:
			genes = dict()
			genes['gender'] = random.choice(POSSIBLE_GENDERS)
			genes['ethnicity'] = random.choice(POSSIBLE_ETHNICITIES)
			if genes['gender'] == "Male":
				genes['reproductive_age'] = round(random.uniform(13, 17), 1)
				genes['adult_height'] = round(random.uniform(1.6, 2.1), 1)
				genes['adult_weight'] = round(random.uniform(50, 110), 1)
				self.pronoun1 = "He"
				self.pronoun2 = "his"
			else:
				genes['reproductive_age'] = round(random.uniform(11, 16), 1)
				genes['adult_height'] = round(random.uniform(1.5, 1.9), 1)
				genes['adult_weight'] = round(random.uniform(50, 100), 1)
				self.pronoun1 = "She"
				self.pronoun2 = "her"

			self.genes = genes

		# Calculate name
		if name:
			self.name = name
		else:
			self.name = self.pick_name(self.genes['gender'])

		self.height = round(random.uniform(0.4, 0.6), 1)  # Height is in Meters.
		self.weight = round(random.uniform(2.5, 4.5), 1)  # Weight is in Kilograms

		# having the same death probability for every person doesn't make sense, so I created a new_prob for every
		# individual with some chances of the probabilities being increased or decreased
		if death_probs is DEATH_PROBS:
			new_death_probs = death_probs[self.genes['gender'].lower()]
			for probs in new_death_probs.keys():
				if random.uniform(0, 1) < 0.1:
					new_death_probs[probs]['chance'] += random.uniform(-0.0005, 0.0005)
					new_death_probs[probs]['chance'] = round(new_death_probs[probs]['chance'], 4)
				elif random.uniform(0, 1) < 0.2:
					new_death_probs[probs]['age_factor'] += random.uniform(-0.009, 0.009)
					new_death_probs[probs]['age_factor'] = round(new_death_probs[probs]['age_factor'], 2)
			self.death_probs = new_death_probs
		else:
			self.death_probs = death_probs

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

		if gender.lower() == 'male':
			firstnames = load_names('male_firstnames.txt')
		elif gender.lower() == 'female':
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
		self.height = round(self.height, 1)
		self.weight = round(self.weight, 1)
		if self.state == "alive":
			print(f'{self.name} is {round(self.age, 3)} years old, is a {self.genes["gender"]}, and is '
			      f'{self.genes["ethnicity"]}. {self.pronoun1} is {self.height} meters tall, and {self.weight} '
			      f'kilograms. {self.pronoun1} will reach {self.pronoun2} reproductive age at '
			      f'{self.genes["reproductive_age"]} years old.')
		elif self.state == "deceased":
			print(f'{self.name} died at age {round(self.age, 3)}, was a {self.genes["gender"]}, and was '
			      f'{self.genes["ethnicity"]}. {self.pronoun1} was {self.height} meters tall, and weighed '
			      f'{self.weight} kilograms. {self.pronoun2} cause of death was {self.death_cause}')

	def kill(self, cause):
		"""
		Kills this person
		Input: Cause of death (string)
		"""
		if self.state == 'alive':
			self.state = 'deceased'
			self.death_cause = cause

	def decide_fate(self):
		"""
		Decides if person dies of some cause. CHANCE_OF_DEATH chance of coming close to death at a given day
		"""
		if random.randint(1, 1000) >= CHANCE_OF_DEATH:
			return None
		deathprobs = self.death_probs
		for cause, prob in deathprobs.items():
			if random.randint(1, 100) <= round(prob['chance']*100 + prob['age_factor']*self.age):
				return cause
		return None

	def get_age_string(self):
		if self.age < 1:
			return ' '.join((str(round(self.age * 365)), 'days'))
		else:
			return ' '.join((str(round(self.age, 1)), 'years'))

	def update(self):
		if self.state == "alive":
			self.age = float(self.age)
			self.age += (1/365)
			cause_of_death = self.decide_fate()
			if cause_of_death:
				self.kill(cause_of_death)
				print(f'{self.name} has died due to {cause_of_death} at {self.get_age_string()} old.')
			if self.height < self.genes['adult_height']:
				if self.age < self.genes['reproductive_age']:
					self.height += (random.uniform(0.06, 0.08) / 365)
				else:
					self.height += (random.uniform(0.03, 0.05) / 365)
			if self.weight < self.genes['adult_weight']:
				if self.age < self.genes['reproductive_age']:
					self.weight += (random.uniform(2, 3) / 365)
				else:
					self.weight += (random.uniform(1.2, 1.8) / 365)
		if len(Model.get().sim_objs) > 2:
			parent1 = random.choice(Model.get().sim_objs)
			parent2 = random.choice(Model.get().sim_objs)
			while parent1 == parent2 or (parent1.state is 'deceased' or parent2.state is 'deceased'):
				parent1 = random.choice(Model.get().sim_objs)
				parent2 = random.choice(Model.get().sim_objs)
			if parent1.genes['gender'] != parent2.genes['gender']:
				if parent1.age >= parent1.genes['reproductive_age'] and parent2.age >= parent2.genes['reproductive_age']:
					if random.randint(0, 100) <= 2:
						Model.get().sim_objs.append(breed(parent1, parent2))
						print(f"{parent1.name} and {parent2.name} gave birth to a baby "
						      f"{Model.get().sim_objs[-1].genes['gender']} named {Model.get().sim_objs[-1].name}.")

	def get_parent_info(self):
		if self.parents is not None:
			pass  # return info about parent depending upon parameters
		else:
			print(f'{self.name} has no parents. He is a child of God')


def breed(person1, person2):
	parents = dict()
	if person1.genes['gender'] is "Male":
		father = parents['father'] = person1
		mother = parents['mother'] = person2
	else:
		father = parents['father'] = person2
		mother = parents['mother'] = person1
	genes = dict()
	genes['gender'] = random.choice(POSSIBLE_GENDERS)
	genes['ethnicity'] = random.choice(POSSIBLE_ETHNICITIES)
	if genes['gender'] == "Male":
		genes['reproductive_age'] = round((father.genes['reproductive_age'] + mother.genes['reproducive_age'] +
		                                  random.uniform(-1, 1)) / 2, 1)
		genes['adult_height'] = round((father.genes['adult_height'] + mother.genes['adult_height'] +
		                               random.uniform(-0.15, 0.15)) / 2, 1)
		genes['adult_weight'] = round((father.genes['adult_weight'] + mother.genes['adult_weight'] +
		                               random.uniform(-5, 5)), 1)
	else:
		genes['reproductive_age'] = round((father.genes['reproductive_age'] + mother.genes['reproducive_age'] +
		                                  random.uniform(-0.7, 0.7)) / 2, 1)
		genes['adult_height'] = round((father.genes['adult_height'] + mother.genes['adult_height'] +
		                               random.uniform(-0.12, 0.12)) / 2, 1)
		genes['adult_weight'] = round((father.genes['adult_weight'] + mother.genes['adult_weight'] +
		                               random.uniform(-2.8, 2.8)), 1)

	'''
	testament = list(map(random.choice((lambda x: x, lambda x: x * -1)), [[] if isinstance(i, Iterable) else 1 if
	i % 2 == 0 else -1 for i in range(len(person1.genes))]))
	
	for aj, bj in zip(person1.genes, person2.genes):
		# if isinstance(aj, Iterable):               Dafuq is this?
			# new_genes.append(breed(aj, bj))
			# continue                               Someone please explain this to me...
		translator = {-1: aj, 1: bj}
		chosen_succesor = random.choice(testament)
		testament.pop(testament.index(chosen_succesor))
		new_genes.append(translator[chosen_succesor])
	'''
	return Person(genes=genes, parents=parents)


'''
Test1 = Person()
Test2 = Person()
Test3 = Person()

Test1.get_info()
Test2.get_info()
Test3.get_info()

# Uncomment these lines to test Person Function.
'''