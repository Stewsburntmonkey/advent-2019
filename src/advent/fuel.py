""" Fuel functions """
from math import floor


def launch_fuel_required(mass: int) -> int:
    """ Calculate fuel required to launch given mass """
    return floor(mass / 3) - 2


def fuel_for_fuel(fuel: int) -> int:
    """ Calculate fuel needed to launch fuel amount """
    fuel_needed = 0
    additional_fuel = fuel

    while True:
        additional_fuel = launch_fuel_required(additional_fuel)
        if additional_fuel <= 0:
            break
        
        fuel_needed += additional_fuel
    
    return fuel_needed


def module_fuel_required(mass: int) -> int:
    """ Calculate fuel required to launch module with given mass """
    module_fuel = launch_fuel_required(mass)
    fuel_fuel = fuel_for_fuel(module_fuel)

    return module_fuel + fuel_fuel
