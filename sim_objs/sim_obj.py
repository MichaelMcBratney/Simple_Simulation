class SimObj:
    """ This class acts as a base class of all simulated objects """

    def update(self):
        """ Update is intended to be defined in child classes """

        raise NotImplementedError
