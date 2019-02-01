# Hello all. Just so you know I am an inexperienced coder.
# I will probably implement everything in the worst possible way.
# But I would like to learn from you and see the way you do things and the way you implement things.
# So hopefully this ends up being a good project for all of us.

# Someone should find a library to record timing better than this method with the timer.
timer = 0
population = 0
total_births = 0
total_deaths = 0

while True:
	timer += 1
	if timer % 200000 == 0:
		total_births += 1
		population += 1
	if timer % 500000 == 0:
		total_deaths += 1
		population -= 1
	if timer > 1000000:
		print("%s people have been born. %s people have died. The population is %s." %(total_births,total_deaths,population))
		timer = 0