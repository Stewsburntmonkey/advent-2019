""" Day 1 """
from advent.fuel import launch_fuel_required, module_fuel_required

def main():
    with open('data/day-01.txt') as infile:
        fuel_needed = 0
        total_fuel_needed = 0

        for line in infile.readlines():
            line = line.strip()
            fuel_needed += launch_fuel_required(int(line))
            total_fuel_needed += module_fuel_required(int(line))

    print(f'Question 1: {fuel_needed}')
    print(f'Question 2: {total_fuel_needed}')


if __name__ == '__main__':
    main()
