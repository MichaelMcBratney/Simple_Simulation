"""
	This is for all things that may change during a person's life
"""
from .genes import Genes
from model import Model
import sim_objs.person
import random


class State(dict):

    NAME        = 'name'
    ALIVE       = 'alive'
    DOB         = 'dob'
    DEATH       = 'death'
    DEATH_CAUSE = 'death_cause'
    HEIGHT      = 'height'
    WEIGHT      = 'weight'
    
    def __init__(self, state, genes, traits):
        super().__init__(self)

        self[State.NAME] = state.get(State.NAME) or sim_objs.person.Person.pick_name(genes[Genes.GENDER])
        self[State.ALIVE] = True
        self[State.DOB] = Model.get().time
        self[State.HEIGHT] = round(random.uniform(0.4, 0.6), 1)
        self[State.WEIGHT] = round(random.uniform(2.5, 4.5), 1)
        self[State.DEATH] = None
