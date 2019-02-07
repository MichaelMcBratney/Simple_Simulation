"""
	This is for all things that remain unchanged during a person's life
"""
import random
from definitions import *


class Genes(dict):

	GENDER             = 'gender'
	ETHNICITY          = 'ethnicity'
	REPRODUCTIVE_AGE   = 'reproductive_age'  # years
	ADULT_HEIGHT       = 'adult_height'  # meters
	ADULT_WEIGHT       = 'adult_weight'  # kilograms
	PARENTS            = 'parents'
	CUSTOM_DEATH_PROBS = 'death_probs'
	PRONOUNS           = 'pronouns'

	def __init__(self, genes):
		super().__init__(self)

		self[Genes.GENDER] = genes.get(Genes.GENDER) or random.choice([MALE, FEMALE])
		self[Genes.ETHNICITY] = genes.get(Genes.ETHNICITY) or random.choice(ETHNICITIES)
		self[Genes.REPRODUCTIVE_AGE] = genes.get(Genes.REPRODUCTIVE_AGE)
		self[Genes.ADULT_HEIGHT] = genes.get(Genes.ADULT_HEIGHT)
		self[Genes.ADULT_WEIGHT] = genes.get(Genes.ADULT_WEIGHT)
		self[Genes.PARENTS] = genes.get(Genes.PARENTS)
		self[Genes.PRONOUNS] = ['He', 'his'] if self[Genes.GENDER] is MALE else ['She', 'her']

		# Calculate Reproductive Age
		if not self.get(Genes.REPRODUCTIVE_AGE):
			if self[Genes.GENDER] == MALE:
				self[Genes.REPRODUCTIVE_AGE] = round(random.uniform(13, 17), 1)
			elif self[Genes.GENDER] == FEMALE:
				self[Genes.REPRODUCTIVE_AGE] = round(random.uniform(11, 16), 1)

		# Calculate Adult Height
		if not self.get(Genes.ADULT_HEIGHT):
			if self[Genes.GENDER] == MALE:
				self[Genes.ADULT_HEIGHT] = round(random.uniform(1.6, 2.1), 1)  # Height is in Meters.
			elif self[Genes.GENDER] == FEMALE:
				self[Genes.ADULT_HEIGHT] = round(random.uniform(1.5, 1.9), 1)  # Height is in Meters.

		# Calculate Adult Weight
		if not self.get(Genes.ADULT_WEIGHT):
			if self[Genes.GENDER] == MALE:
				self[Genes.ADULT_WEIGHT] = round(random.uniform(50, 110), 1)  # Weight is in Kilograms
			elif self[Genes.GENDER] == FEMALE:
				self[Genes.ADULT_WEIGHT] = round(random.uniform(50, 100), 1)  # Weight is in Kilograms

		# Calculate the death probs for the individual
		new_death_probs = DEATH_PROBS[self[Genes.GENDER].lower()]
		for probs in new_death_probs.keys():
			if random.uniform(0, 1) < 0.1:
				new_death_probs[probs]['chance'] += random.uniform(-0.0005, 0.0005)
				new_death_probs[probs]['chance'] = round(new_death_probs[probs]['chance'], 4)
			elif random.uniform(0, 1) < 0.2:
				new_death_probs[probs]['age_factor'] += random.uniform(-0.009, 0.009)
				new_death_probs[probs]['age_factor'] = round(new_death_probs[probs]['age_factor'], 2)
		self[Genes.CUSTOM_DEATH_PROBS] = new_death_probs
