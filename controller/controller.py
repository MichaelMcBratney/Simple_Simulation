from model import Model


class Controller:
	@staticmethod
	def run():

		print("Commands:")
		print("\trun DAYS")
		print("\tinfo PERSON NUM")
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
					if command[1] == 'all':
						for person in Model.get().sim_objs:
							person.get_info()
					else:
						Model.get().sim_objs[int(command[1]) - 1].get_info()
				except IndexError:
					print(f'There are only {len(Model.get().sim_objs)} people in the city')

			elif command[0] == 'parent':
				Model.get().sim_objs[int(command[1]) - 1].get_parent_info()  # can be used to extract info about parents

			else:
				print("Commands:")
				print("\trun DAYS")
				print("\tinfo PERSON NUM")
				print("\tquit or exit")