""" Day 4 """
from advent.password import is_valid, has_digit_pair

def main():
    possible_count = 0
    possible_count_2 = 0
    for x in range(264793, 803935+1):
        if is_valid(x):
            possible_count += 1

            if has_digit_pair(x):
                possible_count_2 += 1

    print(f'Question 1: {possible_count}')
    print(f'Question 2: {possible_count_2}')


if __name__ == '__main__':
    main()
