import random
from helpers.timer import CustomTimer
import datetime
population = 0


def birth_count():
    global population
    random.seed(datetime.datetime.now())
    if population < 500:  # since we can't use percentages if the amount of people is low, there are hard values to the births
        births = random.randint(5, 10)

    elif population < 1000:
    	births = random.randint(5, 15)

    else:
        births = random.randint(round(population/200), round(population/50))
    
    population += births
    print(f'Current population is {population} after {births} births')


def death_count():
    global population
    random.seed(datetime.datetime.now())
    if population < 500:
        deaths = random.randint(1, 5)  # generates a random number of deaths every time, same way as births

    elif population < 1000:
    	deaths = random.randint(1, 8)
    
    else:
        deaths = random.randint(round(population/250), round(population/100))
    
    population -= deaths
    print(f'Current population is {population} after {deaths} deaths')

def natural_disaster():
	global population 
        # 5% chance for a wildfire to wipeout 5-10% of the population
	if population >= 1000:
		if random.randint(1,100) <= 5:
			deaths = random.randint(int(population * 0.05), int(population * 0.1)) 
			population -= deaths
			print(f'A wildfire has killed {deaths}! {population} remain alive')
		# 10% chance for drought to kill 10-15% of the population
		if population >= 10000: 
			if random.randint(1,100) <= 10:
				deaths = random.randint(int(population * 0.1), int(population * 0.15))
				population -= deaths
				print(f'A drought has starved {deaths}! {population} remain alive')
                	# 3% chance for the plague to kill 60-80% of the population
			if population >= 100000:
				if random.randint(1,100) <= 3:
					deaths = random.randint(int(population * 0.6), int(population * 0.8))
					population -= deaths
					print(f'A plague has killed {deaths}! only {population} remain alive')

def main_loop():
	birth = CustomTimer(interval=3, function=birth_count)  # runs every 3 seconds
	death = CustomTimer(5, death_count)  # runs every 5 seconds, since death rate is slower than birth rate
	disaster = CustomTimer(10, natural_disaster) 
	birth.start()  # starts the birth timer
	death.start()  # starts the death timer
	disaster.start() # starts the disaster timer


if __name__ == '__main__':
	main_loop()
