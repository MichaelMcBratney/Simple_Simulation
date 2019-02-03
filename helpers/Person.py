# TODO: need to add more to the person class
#  what things should they be able to do?
#  what are all of their characteristics?
import random, datetime


class Person:
    def __init__(self, gender=None,adult_height=None, adult_weight=None, ethnicity=None, reproductive_age=None, age=0):
        random.seed(datetime.datetime.now())
        possible_genders = ['Male',"Female"]
        possible_ethnicities = ["European", "African-American", "African", "Asian", "Latino", "Jewish", "Arab", "Indigenous"] #TODO: make ethnicities more abstract
        self.age = age
        if gender:
            self.gender = gender
        else:
            self.gender = random.choice(possible_genders)
        if reproductive_age:
            self.reproductive_age = reproductive_age
        else:
            if self.gender == "Male":
                self.reproductive_age = round(random.uniform(13,17), 1)
            elif self.gender == "Female":
                self.reproductive_age = round(random.uniform(11,16), 1)
        if name:
            self.name = name
        else:
            self.name = self.pickName(self.gender)
        if ethnicity:
            self.ethnicity = ethnicity
        else:
            self.ethnicity = random.choice(possible_ethnicities)
        if adult_height:
            self.adult_height = adult_height
        else:
            if self.gender == "Male":
                self.adult_height = round(random.uniform(1.6,2.1), 1) # Height is in Meters.
            elif self.gender == "Female":
                self.adult_height = round(random.uniform(1.5,1.9), 1) # Height is in Meters.
        if adult_weight:
            self.adult_weight = adult_weight
        else:
            if self.gender == "Male":
                self.adult_weight = round(random.uniform(50,110), 1) # Weight is in Kilograms
            elif self.gender == "Female":
                self.adult_weight = round(random.uniform(50,100), 1) # Weight is in Kilograms
        self.height = round(random.uniform(0.4, 0.6), 1) # Height is in Meters.    
        self.weight = round(random.uniform(2.5, 4.5), 1) # Weight is in Kilograms

    def pickName(self, gender):
    # TODO: Replace generic names with random/procedurally generated names.
        if self.gender == 'Male':
            return "John Doe"

        elif self.gender == "Female":
            return "Jane Doe"

def breed(person1, person2):
    if person1.age >= person1.reproductive_age and person2.age >= person2.reproductive_age:
        if person1.gender != person2.gender:
            if person1.gender != "Male":
                person1, person2 = person2, person1
            ethnicity = random.choice((person1.ethnicity,person2.ethnicity)) #TODO: make ethnicities more abstract
            gender = random.choice(['Male',"Female"])
            if gender == "Male":
                adult_height = round((person1.adult_height + person2.adult_height+13)/2,1)
                adult_weight = round((person1.adult_weight+person2.adult_weight+13)/2,1)
                reproductive_age = round((person1.reproductive_age+person2.reproductive_age+3))
            elif gender == "Female":
                adult_height = round((person1.adult_height + person2.adult_height-13)/2,1)
                adult_weight = round((person1.adult_weight+person2.adult_weight-13)/2,1)
                reproductive_age = round((person1.reproductive_age+person2.reproductive_age-3))
            

            return Person(gender=gender, adult_height=adult_height,adult_weight=adult_weight, ethnicity=ethnicity, reproductive_age=reproductive_age)