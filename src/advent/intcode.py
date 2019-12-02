""" Implement Intcode computer """
from typing import List


def op_add(current_pos, intcode_array) -> str:
    int_a = intcode_array[intcode_array[current_pos+1]]
    int_b = intcode_array[intcode_array[current_pos+2]]
    intcode_array[intcode_array[current_pos+3]] = int_a + int_b

    return 'next'


def op_multiply(current_pos, intcode_array) -> str:
    int_a = intcode_array[intcode_array[current_pos+1]]
    int_b = intcode_array[intcode_array[current_pos+2]]
    intcode_array[intcode_array[current_pos+3]] = int_a * int_b

    return 'next'


def op_halt(current_pos, intcode_array) -> str:
    return 'halt'


OPCODES = {
    1: op_add,
    2: op_multiply,
    99: op_halt,
}


def run(intcode_array: List[int]) -> str:
    current_pos = 0

    while True:
        opcode = intcode_array[current_pos]

        if opcode not in OPCODES:
            raise NotImplementedError(f'Unsupported opcode: {opcode}')
        
        state_change = OPCODES[opcode](current_pos, intcode_array)

        if state_change == 'halt':
            break

        current_pos += 4
    
    return intcode_array


def to_array(intcode_str: str) -> List[int]:
    return [int(x) for x in intcode_str.split(',')]


def to_string(intcode_array: List[int]) -> str:
    return ','.join([str(x) for x in intcode_array])


def run_noun_verb(noun: int, verb: int, intcode_array: List[int]) -> int:
    intcode_array[1] = noun
    intcode_array[2] = verb
    intcode_array = run(intcode_array)

    return intcode_array[0]

