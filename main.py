from controller import Controller
from sim_objs import Person
from model import Model


def main():

    # Initialize for now with a few people. This should not be the final place for this
    # sort of thing, I am just putting this code here for now
    Model.get().sim_objs += [Person(), Person(), Person()]

    Controller().run()

if __name__=='__main__':
    main()
