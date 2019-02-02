import random
from helpers.timer import CustomTimer
import datetime

population = 0

def natural_disaster():  # Natural disaster that kills a percentage of people once a population minimum has been met
    global population
    population_minimum = 100000  # minimum population for a disaster to occur
    random.seed(datetime.datetime.now())
    disaster_chance = 0.0000969863  # taken from wikipedia and divided for every day (in the UK)
    if population >= population_minimum:
        rand_result = random.randint(1, round(1 / disaster_chance))
        if rand_result == 3:  # arbitrary number
            deaths = random.randint(round(population / 1000), round(population / 100))  # should probably be changed for optimization
            population -= deaths
            print(f'NATURAL DISASTER -- caused {deaths} deaths. Current population is now {population}')


def birth_count():
	global population
	random.seed(datetime.datetime.now())
	births = random.randint(5, 10)  # generates a random number of births every time
	population += births
	print(f'Current population is {population} after {births} births')


def death_count():
	global population
	random.seed(datetime.datetime.now())
	deaths = random.randint(1, 5)  # generates a random number of deaths every time
	population -= deaths
	print(f'Current population is {population} after {deaths} deaths')


def main_loop():
	birth = CustomTimer(interval=3, function=birth_count)  # runs every 3 seconds
	death = CustomTimer(5, death_count)  # runs every 5 seconds, since death rate is slower than birth rate
	natural_disaster_time = CustomTimer(interval=3, function=natural_disaster)  # not sure about the interval
	birth.start()  # starts the birth timer
	death.start()  # starts the death timer
	natural_disaster_time.start()  # starts the natural disaster timer

if __name__ == '__main__':
	main_loop()
