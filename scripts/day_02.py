""" Day 2 """
from advent.intcode import run, run_noun_verb, to_array, to_string

def main():
    initial_state = None
    with open('data/day-02.txt') as infile:
        line = infile.readline().strip()
        initial_state = to_array(line)
        intcode_array = list(initial_state)
        # intcode_array[1] = 12
        # intcode_array[2] = 2
        # output = run(to_string(intcode_array))
        # intcode_array = to_array(output)

        output = run_noun_verb(12, 2, intcode_array)

    print(f'Question 1: {output}')

    for noun in range(0, 100):
        for verb in range(0, 100):
            output = run_noun_verb(noun, verb, list(initial_state))
            if output == 19690720:
                print(f'Question 2: {noun * 100 + verb}')


if __name__ == '__main__':
    main()
