"""
Starter code for Advent of Code 2019 Day #10

You must implement functions part1 and part2
"""

import sys
import os


def part1(jolts):
    """
    Solves Part 1 (see problem statement for more details)

    Parameter:
    - jolts (list of integers)

    Returns an integer
    """

    ### Replace with your code
    # new_jolts = [0] + jolts 
    # sorted_jolts = sorted(new_jolts)
    # one_diffs = 0
    # three_diffs = 1
    # for i in range(len(jolts)):
    #     if sorted_jolts[i+1] - sorted_jolts[i] == 1:
    #         one_diffs += 1
    #     if sorted_jolts[i+1] - sorted_jolts[i] == 3:
    #         three_diffs += 1
    # return one_diffs * three_diffs

    new_jolts = [0] + sorted(jolts)
    def rec_part1(lst, one_diffs = 0, three_diffs = 1):
        if len(lst) == 2:
            if lst[1] - lst[0] == 1:
                return (one_diffs + 1) * three_diffs
            return one_diffs * (three_diffs + 1)
        if lst[1] - lst[0] == 1:
            return rec_part1(lst[1:], one_diffs + 1, three_diffs)
        return rec_part1(lst[1:], one_diffs, three_diffs + 1)
    
    return rec_part1(new_jolts)


def part2(numbers):
    """
    Solves Part 2 (see problem statement for more details)

    Parameter:
    - jolts (list of integers)

    Returns an integer
    """

    ### Replace with your code
    new_jolts = [0] + sorted(numbers)
    def gen_arrangements(jolts):
        if not jolts:
            return [[]]
        start = jolts[0]
        arrangements = []
        rem_jolts = jolts[1:]
        for i, next_jolt in enumerate(rem_jolts):
            if next_jolt - start <= 3:
                for subarr in gen_arrangements(jolts[i + 1:]):
                    arrangements.append([next_jolt] + subarr)
            else:
                break
        return arrangements
    print(gen_arrangements(new_jolts))
    return len(gen_arrangements(new_jolts))


############################################
###                                      ###
###      Do not modify the code below    ###
###                EXCEPT                ###
###    to comment/uncomment the calls    ###
###        to the functions above        ###
###                                      ###
############################################

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"USAGE: python3 {os.path.basename(sys.argv[0])} <INPUT FILE>")
        sys.exit(1)

    input_file = sys.argv[1]

    if not os.path.exists(input_file):
        print(f"ERROR: No such file: {input_file}")
        sys.exit(1)

    with open(input_file) as f:
        jolts = [int(x) for x in f.read().split()]

    print(f"Part 1:", part1(jolts))
    
    # Uncomment the following line when you're ready to work on Part 2
    print(f"Part 2:", part2(jolts))
