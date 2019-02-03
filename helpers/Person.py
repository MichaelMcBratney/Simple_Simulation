# TODO: need to add more to the person class
#  what things should they be able to do?
#  what are all of their characteristics?
#  add a way to procedurally generate names
import random, datetime


class Person:
    def __init__(self, age=0):
        possible_genders = ['Male',"Female"]
        possible_ethnicities = ["White", "African-American", "African", "Asian", "Latino", "Jewish", "Arab", "Indigenous"]
        random.seed(datetime.datetime.now())
        self.gender = random.choice(possible_genders)
        self.name = self.pickName(self.gender)
        self.age = age
        self.ethnicity = random.choice(possible_ethnicities)
        self.height = round(random.uniform(0.4, 0.6), 1)    # Height is in Meters.
        self.weight = round(random.uniform(2.5, 4.5), 1)    # Weight is in Kilograms.

    def pickName(self, gender):
    # Replace generic names with random.procedurally generated names.
        if self.gender == 'Male':
            return "John Doe"

        elif self.gender == "Female":
            return "Jane Doe"

