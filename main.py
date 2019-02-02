import random
from helpers.timer import CustomTimer
import datetime

population = 0


def birth_count():
    global population
    random.seed(datetime.datetime.now())
    if population < 1000:  # since we can't use percentages if the amount of people is low, there are hard values to the births
        births = random.randint(5, 10)
    else:
        births = random.randint(round(population/200), round(population/50))
    population += births
    print(f'Current population is {population} after {births} births')


def death_count():
    global population
    random.seed(datetime.datetime.now())
    if population < 1000:
        deaths = random.randint(1, 5)  # generates a random number of deaths every time, same way as births
    else:
        deaths = random.randint(round(population/250), round(population/100))
    population -= deaths
    print(f'Current population is {population} after {deaths} deaths')


def main_loop():
	birth = CustomTimer(interval=3, function=birth_count)  # runs every 3 seconds
	death = CustomTimer(5, death_count)  # runs every 5 seconds, since death rate is slower than birth rate
	birth.start()  # starts the birth timer
	death.start()  # starts the death timer


if __name__ == '__main__':
	main_loop()
