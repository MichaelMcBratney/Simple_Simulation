# TODO: need to add more to the person class
#  what things should they be able to do?
#  what are all of their characteristics?
import random, datetime
import os
import csv
from model import Model
from .sim_obj import SimObj
from definitions import RESOURCES_DIR, DEATH_PROBS, CHANCE_OF_ILLNESS, REPRODUCTIVE_MAX
from pathlib import Path
from collections import Iterable


class Person(SimObj):
    def __init__(self, name=None, genes=None, age=0.0):
        possible_genders = ['Male',"Female"]
        possible_ethnicities = ["European", "African-American", "African", "Asian", "Latino", "Jewish", "Arab", "Indigenous"] #TODO: make ethnicities more abstract
        
        
        # Initialize Health status:
        self.health = {}
        # Set state of person to one of : 'alive' or 'deceased'.
        self.health['state'] = 'alive'
        self.health['death_cause'] = None
        self.health['age'] = age
        # Height is in Meters.
        self.health['height'] = round(random.uniform(0.4, 0.6), 1)
        # Weight is in Kilograms     
        self.health['weight'] = round(random.uniform(2.5, 4.5), 1) 
        # Ability to reproduce
        self.health['fertile'] = False 
        # Illnesses
        self.health['afflictions'] = {}
        
        # Initialize Social status
        # Placeholder dictionary for relationships etc.
        self.social = {}
        self.social['spouse'] = None

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
        if self.health['state'] == "alive":
            print(f"{self.name} is {round(self.health['age'], 1)} years old, is a {self.gender}, and is {self.ethnicity}. {self.pronoun1} is {round(self.health['height'],2)} meters tall, and {round(self.health['weight'],2)} kilograms. {self.pronoun1} will reach {self.pronoun2} reproductive age at {self.reproductive_age} years old.")
        elif self.health['state'] == "deceased":
            print(f"{self.name} died at age {round(self.health['age'], 1)}, was a {self.gender}, and was {self.ethnicity}. {self.pronoun1} was {round(self.health['height'],2)} meters tall, and weighed {round(self.health['weight'],2)} kilograms. {self.pronoun2} cause of death was {self.health['death_cause']}")
    
    def kill(self, cause):
        """
        Kills this person
        Input: Cause of death (string)
        """
        if self.health['state'] == 'alive':
            self.health['state'] = 'deceased'
            self.health['death_cause'] = cause

    def get_sick(self):
        """
        Decides if person gets an illness with CHANCE_OF_ILLNESS chance of getting terminal illness.
        Output: returns a dict with illness and days till death. 
        Example: {'Cardiovascular Disease': 1000}
        """
        if random.randint(1,20000) >= CHANCE_OF_ILLNESS:
            return None
        fileloc = os.path.join(RESOURCES_DIR, self.gender.lower()+'_illnesses.csv')
        
        with open(fileloc,'r', newline='') as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                # illness file structure:
                # [0]name, [1]min, [2]max, [3]duration
                if self.health['age'] >= int(row[1]) and self.health['age'] <= int(row[2]):
                    self.health['afflictions'][row[0]] = int(row[3])
                    print(f"{self.name} has contracted {row[0]}.")
                    return None   

    def get_age_string(self):
        if self.health['age'] < 1:
            return ' '.join((str(round(self.health['age'] * 365)),'days'))
        else:
            return ' '.join((str(round(self.health['age'], 1)),'years')) 
    
    def get_health(self, parameter=None):
        '''
        Returns the person's health parameter
        Output: The parameter from self.health['parameter']
        If no parameter specified then returns dictionary of health status.
        '''
        if parameter:
            return self.health[parameter]
        else:
            return self.health
    
    def treat_illnesses(self):
        '''
        Removes person's illness
        
        Input: illness (string) The illness to remove           
        '''
        afflictions = list(self.health['afflictions'].keys())
        x = random.choice(afflictions)
        _ = self.health['afflictions'].pop(x)
        print(f"{self.name} has received medical treatment for {x}")


    def update_health(self):
        '''
        Updates person's health status.
        afflictions, pregnancies etc.
        '''
        if self.health['state'] == "alive":
            self.health['age'] += (1.0/365)
            if self.health['weight'] <= self.adult_weight:
                self.health['weight'] += round(random.uniform(-0.01, 0.05), 2)
            if self.health['height'] <= self.adult_height:
                self.health['height'] += round(random.uniform(0, 0.0002), 4)
            if self.health['fertile'] and self.health['age'] >= REPRODUCTIVE_MAX:
                # Lose ability to reproduce due to old age.
                self.health['fertile'] = False
                print(f"{self.name} can no longer reproduce")                
            elif not self.health['fertile']:
                if self.health['age'] >= self.reproductive_age and self.health['age'] < REPRODUCTIVE_MAX:
                    # Gain ability to reproduce if young and reached reproductive age.
                    self.health['fertile'] = True
                    print(f"{self.name} can now reproduce!")
            if not self.health['afflictions']:
                self.get_sick()
            else:
                if random.randint(1,1500) <= 2:
                    self.treat_illnesses()
                for illness in self.health['afflictions'].keys():
                    self.health['afflictions'][illness] -= 1
                    if not self.health['afflictions'][illness]:
                        self.kill(illness)
                        print(f'{self.name} has died due to {illness} at {self.get_age_string()} old.')
            # Check for and update pregnancy state.
            # Uncomment after social structure of spouses/relationships implemented.
            # if self.gender.lower() == 'female':
            #     try:
            #         if self.health['pregnant']:
            #             self.health['pregnant'] -= 1
            #             if self.health['pregnant'] == 0:
            #                 Model.get().sim_objs.append(breed(self, self.social['spouse']))
            #                 print(f"{self.name} gave birth to a baby {Model.get().sim_objs[-1].gender} named {Model.get().sim_objs[-1].name}.")
            #     except KeyError:
            #         self.health['pregnant'] = None


    def update_social(self):
        ''' 
        Placeholder for social updates of person
        Relationships etc
        '''
        pass

    def update(self):
        self.update_health()
        self.update_social()
            
        parent1 = random.choice(Model.get().sim_objs)
        parent2 = random.choice(Model.get().sim_objs)
        while parent1 == parent2:
            parent2 = random.choice(Model.get().sim_objs)

        if parent1.gender != parent2.gender:
            if parent1.health['age'] >= parent1.reproductive_age and parent2.health['age'] >= parent2.reproductive_age:
                if random.randint(0, 100) <= 2:
                    Model.get().sim_objs.append(breed(parent1, parent2))
                    print(f"{parent1.name} and {parent2.name} gave birth to a baby {Model.get().sim_objs[-1].gender} named {Model.get().sim_objs[-1].name}.")


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
