from controller import Controller
from sim_objs import Person
from model import Model


def main():
    num_people = 3 # Change this variable to however many people you wish to run the simulation with.
    initial_people = []
    for i in range(num_people):
        initial_people.append(Person())

    Model.get().sim_objs += initial_people

    Controller().run()

if __name__=='__main__':
    main()
