# TODO: need to add more to the person class
#  what things should they be able to do?
#  what are all of their characteristics?
import random, datetime
import os
from model import Model
from .sim_obj import SimObj
from definitions import RESOURCES_DIR, DEATH_PROBS, CHANCE_OF_DEATH
from pathlib import Path
from collections import Iterable


class Person(SimObj):
    def __init__(self, name=None, genes=None, age=0):
        possible_genders = ['Male',"Female"]
        possible_ethnicities = ["European", "African-American", "African", "Asian", "Latino", "Jewish", "Arab", "Indigenous"] #TODO: make ethnicities more abstract
        
        # Set state of person to one of : 'alive' or 'deceased'.
        self.state = "alive"
        self.death_cause = None

        #Initialize age
        self.age = age

        # If the parameter, "genes" is specified, the information in
        # the parameter will be translated and assigned to the person class's instances.
        # Else both the genes and the translated assigned instances will be randomly generated.
        if genes:
            self.genes = genes
            #print(self.genes) Debugging
            self.gender = genes[0]
            self.ethnicity = genes[1]
            self.reproductive_age = genes[2]
            self.adult_height = genes[3]
            self.adult_weight = genes[4]
        else:
            #Calculate Gender
            gender = random.randint(0,1)
            self.gender = possible_genders[gender]

            # Calculate Reproductive Age
            if self.gender == "Male":
                self.reproductive_age = round(random.uniform(13,17), 1)
            elif self.gender == "Female":
                self.reproductive_age = round(random.uniform(11,16), 1)
            
            # Calculate Ethnicity
            ethnicity = random.randint(0,len(possible_ethnicities)-1)
            self.ethnicity = possible_ethnicities[ethnicity]

            # Calculate Adult Height
            if self.gender == "Male":
                self.adult_height = round(random.uniform(1.6,2.1), 1) # Height is in Meters.
            elif self.gender == "Female":
                self.adult_height = round(random.uniform(1.5,1.9), 1) # Height is in Meters.

            # Calculate Adult Weight
            if self.gender == "Male":
                self.adult_weight = round(random.uniform(50,110), 1) # Weight is in Kilograms
            elif self.gender == "Female":
                self.adult_weight = round(random.uniform(50,100), 1) # Weight is in Kilograms

            self.genes = [self.gender, self.ethnicity, self.reproductive_age, self.adult_height, self.adult_weight]


        #Calculate name
        if name:
            self.name = name
        else:
            self.name = self.pickName(self.gender)


        self.height = round(random.uniform(0.4, 0.6), 1) # Height is in Meters.    
        self.weight = round(random.uniform(2.5, 4.5), 1) # Weight is in Kilograms

    def pickName(self, gender):
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
        fullname = ''.join((first,' ', last))
        return fullname

    def getInfo(self):
        if self.gender.lower() == "male":
            self.pronoun1 = "He"
            self.pronoun2 = "his"
        elif self.gender.lower() == "female":
            self.pronoun1 = "She"
            self.pronoun2 = "her"
        if self.state == "alive":
            print(f'{self.name} is {round(self.age, 3)} years old, is a {self.gender}, and is {self.ethnicity}. {self.pronoun1} is {self.height} meters tall, and {self.weight} kilograms. {self.pronoun1} will reach {self.pronoun2} reproductive age at {self.reproductive_age} years old.')
        elif self.state == "deceased":
            print(f'{self.name} died at age {round(self.age, 3)}, was a {self.gender}, and was {self.ethnicity}. {self.pronoun1} was {self.height} meters tall, and weighed {self.weight} kilograms. {self.pronoun2} cause of death was {self.death_cause}')
    
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
        if random.randint(1,1000) >= CHANCE_OF_DEATH:
            return None
        deathprobs = DEATH_PROBS[self.gender.lower()]
        for cause, prob in deathprobs.items():
            if random.randint(1, 100) <= round(prob['chance']*100 + prob['age_factor']*self.age):
                return cause
        return None    

    def get_age_string(self):
        if self.age < 1:
            return ' '.join((str(round(self.age * 365)),'days'))
        else:
            return ' '.join((str(round(self.age, 1)),'years')) 
        
    def update(self):
        if self.state == "alive":
            self.age = float(self.age)
            self.age += (1/365)
            cause_of_death = self.decide_fate()
            if cause_of_death:
                self.kill(cause_of_death)
                print(f'{self.name} has died due to {cause_of_death} at {self.get_age_string()} old.')

        parent1 = random.choice(Model.get().sim_objs)
        parent2 = random.choice(Model.get().sim_objs)
        while parent1 == parent2:
            parent2 = random.choice(Model.get().sim_objs)

        if parent1.gender != parent2.gender:
            if parent1.age >= parent1.reproductive_age and parent2.age >= parent2.reproductive_age:
                if random.randint(0, 100) <= 2:
                    Model.get().sim_objs.append(breed(parent1, parent2))
                    print(f"{parent1.name} and {parent2.name} gave birth to a baby {Model.get().sim_objs[-1].gender} named {Model.get().sim_objs[-1].name}.")

            # Should only print age when getInfo is called
            #if self.age < 1:
            #    print(f'{self.name} is {round(self.age * 365)} days old.')
            #else:
            #    print(f'{self.name} is {round(self.age, 1)} years old.')

def breed(person1, person2):
    #print(person1) Debugging
    #print(person2)
    new_genes = []
    testament = list(map(random.choice((lambda x: x, lambda x: x * -1)), [[] if isinstance(i, Iterable) else 1 if i % 2 == 0 else -1 for i in range(len(person1.genes))]))
    for aj, bj in zip(person1.genes, person2.genes):
        #if isinstance(aj, Iterable):               Dafuq is this?
            #new_genes.append(breed(aj, bj))
            #continue                               Someone please explain this to me...
        translator = {-1: aj, 1: bj}
        chosen_succesor = random.choice(testament)
        testament.pop(testament.index(chosen_succesor))
        new_genes.append(translator[chosen_succesor])
    return Person(genes=new_genes)

'''     
Test1 = Person()
Test2 = Person()
Test3 = Person()

Test1.getInfo()
Test2.getInfo()
Test3.getInfo()

#Uncomment these lines to test Person Function.
'''
