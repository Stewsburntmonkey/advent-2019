""" Day 3 """
from advent.wire import earliest_intersection, nearest_intersection

def main():
    with open('data/day-03.txt') as infile:
        paths = infile.read().strip()
    
    output = nearest_intersection(paths)
    print(f'Question 1: {output}')

    output = earliest_intersection(paths)
    print(f'Question 2: {output}')


if __name__ == '__main__':
    main()
