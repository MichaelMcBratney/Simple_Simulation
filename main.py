from controller import Controller
from sim_objs import Person
from model import Model
from definitions import NUM_PEOPLE  # , TOTAL_PEOPLE


def main():
    for i in range(NUM_PEOPLE):
        Model.get().sim_objs.append(Person())

    Controller().run()


if __name__ == '__main__':
    main()
