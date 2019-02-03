# Simple Simulation Plan - dwdineen

I have worked with some simulations before, albiet in C++ not Python. So some of the things I will be saying might sound more C++ than Pythonic so bear with me. 

# Simulated Objects

All simulated objects (Persons, MotherNature, Cars, etc.) will be in charge of updating themselves when told to. Think of this as when told to update, a person has a chance to reproduce, or when told to MotherNature has a chance of creating a tornado. These objects can interact with each other as well.

# MVC

I suggest that we use Model-View-Controller paradigm in order to keep the code extensible and organized.

## Model

The Model will be the unit that keeps track of all simulated objects (people, houses, cars, natural disasters, etc.) and tell each object to update themselves every timestep (1 hr, 6 hr, 1 day). Therefore model also keeps track of the time.

## Controller

Controller is the unit that interacts with the user. We will want to be able to input commands in order to interact for our simulation. For example, "Run 10yr" which will run the simulation for 10 years. Something like that. All commands will live in Controller unit, commands generally will interact with Model.

## View

If we ever have more complex ways to look at our city. Such as graphics or simply complex text, that code will live in View.



