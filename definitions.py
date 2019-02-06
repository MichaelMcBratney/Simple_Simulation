import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
RESOURCES_DIR = os.path.join(ROOT_DIR, "resources")
DEATH_PROBS = {'male': {'Cardiovascular disease': {'chance': 0.0128, 'age_factor': 0.06},
                        'Road Injury': {'chance': 0.0107, 'age_factor': 0.00},
                        'HIV/AIDS': {'chance': 0.0107, 'age_factor': 0.04},
                        'Neoplasms': {'chance': 0.0094, 'age_factor': 0.05},
                        'Self-harm': {'chance': 0.0057, 'age_factor': 0.03}
                        },
               'female': {'HIV/AIDS': {'chance': 0.0144, 'age_factor': 0.04},
                          'Maternal condition': {'chance': 0.0073, 'age_factor': 0.05},
                          'Cardiovascular disease': {'chance': 0.0107, 'age_factor': 0.04},
                          'Diarrhoea': {'chance': 0.0107, 'age_factor': 0.02}}}
CHANCE_OF_DEATH = 2

NUM_PEOPLE = 5  # Change this variable to however many people you wish to run the simulation with.

POSSIBLE_GENDERS = ['Male', "Female"]

POSSIBLE_ETHNICITIES = ["European", "African-American", "African", "Asian", "Latino", "Jewish", "Arab",
                        "Indigenous"]  # TODO: make ethnicities more abstract
