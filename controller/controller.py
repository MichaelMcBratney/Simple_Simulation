from model import Model

class Controller:

    def run(self):

        print("Commands:")
        print("\trun DAYS")
        print("\tinfo PERSON NUM")
        print("\tquit")

        # Continuously ask for commands then execute
        while True:

            command = input("Enter a command: ")
            command = command.lower().strip().split()

            if command[0] == 'quit': return

            elif command[0] == 'run':
                Model.get().run(int(command[1]))

            elif command[0] == 'info':
                Model.get().sim_objs[int(command[1]) - 1].getInfo()



