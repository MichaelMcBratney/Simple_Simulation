from model import Model

class Controller:

    def run(self):

        print("Commands:")
        print("\trun DAYS")
        print("\tinfo PERSON_ID")
        print("\tquit")

        # Continuously ask for commands then execute
        while True:

            command = input("Enter a command: ")
            command = command.lower().strip().split()
            
            if not command:
                continue

            if command[0] == 'quit': return

            elif command[0] == 'run':
                #try:
                Model.get().run(int(command[1]))
                #except:
                    #print("\nINVALID INPUT\nExpected usage: run DAYS \nWhere DAYS is a positive integer\n")

            elif command[0] == 'info':
                try:
                    Model.get().sim_objs[int(command[1]) - 1].getInfo()
                except ValueError:
                    print("\nINVALID INPUT\nExpected usage: run PERSON_ID \nWhere PERSON_ID is a positive integer\n")                   
                except IndexError:
                    print("\nNo person with this id exists.\n")            

