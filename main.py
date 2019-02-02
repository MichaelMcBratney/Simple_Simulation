import random
from helpers.timer import CustomTimer
import datetime

population = 0


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
	birth.start()  # starts the birth timer
	death.start()  # starts the death timer


if __name__ == '__main__':
	main_loop()
