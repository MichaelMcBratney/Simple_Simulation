from model import Model
from sim_objs.person_helpers.state import State
from sim_objs.person_helpers.genes import Genes


class Controller:
	@staticmethod
	def run():

		print("Commands:")
		print("\trun DAYS           --> runs simulation for DAYS days")
		print("\tinfo 1) PERSON_NUM --> provides current info about the PERSON_NUM\n"
		      "\t     2) all        --> provides current info about all people")
		print("\tage                --> gives the current age of the simulation")
		print("\tpopulation         --> gives the current population of the city")
		print("\tparent PERSON_NUM  --> gives info about parent of PERSON_NUM")
		print("\tquit or exit")

		# Continuously ask for commands then execute
		while True:

			command = input("Enter a command: ")
			command = command.lower().strip().split()

			if command[0] in ['quit', 'exit']:
				return

			elif command[0] == 'run':
				Model.get().run(int(command[1]))

			elif command[0] == 'info':
				try:
					Model.get().sim_objs[int(command[1]) - 1].get_info()
				except (IndexError, ValueError):
					print(f'There are records of {len(Model.get().sim_objs)} people')

			elif command[0] == 'age':
				time = str(Model.get().time) + ' days'
				if int(time.split()[0]) > 365:
					time = str(int(time.split()[0]) / 365) + ' years'
				print(f'The city is {time} old')

			elif command[0] == 'population':
				count = 0
				for person in Model.get().sim_objs:
					if person.state[State.ALIVE]:
						count += 1
				print(f'Population of the city is {count}')

			elif command[0] == 'parent':
				try:
					parents = Model.get().sim_objs[int(command[1]) - 1].genes[Genes.PARENTS]
					if parents is not None:
						print(f"{parents['father'].state[State.NAME]} is {Model.get().sim_objs[int(command[1]) - 1].state[State.NAME]}'s father. {parents['mother'].state[State.NAME]} is {Model.get().sim_objs[int(command[1]) - 1].state[State.NAME]}'s mother.")  # can be used to get info about parents
					else:
						print('This person is a child of God')
				except (IndexError, ValueError):
					print(f'There are records of {len(Model.get().sim_objs)} people')

			else:
				print("Commands:")
				print("\trun DAYS           --> runs simulation for DAYS days")
				print("\tinfo 1) PERSON_NUM --> provides current info about the PERSON_NUM\n"
				      "\t     2) all        --> provides current info about all people")
				print("\tage                --> gives the current age of the simulation")
				print("\tpopulation         --> gives the current population of the city")
				print("\tparent PERSON_NUM  --> gives info about parent of PERSON_NUM")
				print("\tquit or exit")
