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

def natural_disaster():
	global population 
        # 10% chance for a wildfire to wipeout 10% of the population
	if population >= 1000:
		if (random.randint(1,100) <= 10):
			deaths = int(population * 0.1) 
			population = population - deaths
			print(f'A wildfire has killed {deaths}! {population} remain alive')
		# 15% chance for drought to kill 10% of the population
		if population >= 10000: 
			if random.randint(1,100) <= 15:
				deaths = int(population * 0.1)
				population = population - deaths
				print(f'A drought has starved {deaths}! {population} remain alive')
                	# 5% chance for the plague to kill 80% of the population
			if population >= 100000:
				if random.randint(1,100) <= 5:
					deaths = int(population * 0.8)
					population = population - deaths
					print(f'A plague has killed {deaths}! only {population} remain alive')

def main_loop():
	birth = CustomTimer(interval=3, function=birth_count)  # runs every 3 seconds
	death = CustomTimer(5, death_count)  # runs every 5 seconds, since death rate is slower than birth rate
	disaster = CustomTimer(5, natural_disaster) 
	birth.start()  # starts the birth timer
	death.start()  # starts the death timer
	disaster.start() # starts the disaster timer


if __name__ == '__main__':
	main_loop()
