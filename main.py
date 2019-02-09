from controller import Controller
import sim_objs.person
from model import Model
from definitions import NUM_PEOPLE
import os
with open('app.txt', 'a') as file:
	file.write('Entered ' + os.path.basename(__file__))


def main():
	for i in range(NUM_PEOPLE):
		Model.get().sim_objs.append(sim_objs.person.Person())

	Controller().run()


if __name__ == '__main__':
	main()
