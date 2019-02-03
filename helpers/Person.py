# TODO: need to add more to the person class
#  what things should they be able to do?
#  what are all of their characteristics?
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
            with open(filename, 'r') as f:
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

