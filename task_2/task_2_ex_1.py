"""
Task 2_3

You are given n bars of gold with weights: w1, w2, ..., wn and bag with capacity W.
There is only one instance of each bar and for each bar you can either take it or not
(hence you cannot take a fraction of a bar). Write a function that returns the maximum weight of gold that fits
into a knapsack's capacity.

The first parameter contains 'capacity' - integer describing the capacity of a knapsack
The next parameter contains 'weights' - list of weights of each gold bar
The last parameter contains 'bars_number' - integer describing the number of gold bars
Output : Maximum weight of gold that fits into a knapsack with capacity of W.

Note:
Use the argparse module to parse command line arguments. You don't need to enter names of parameters (i. e. -capacity)
Raise ValueError in case of false parameter inputs
Example of how the task should be called:
python3 task3_1.py -W 56 -w 3 4 5 6 -n 4
"""
import argparse as arg
from itertools import combinations


def bounded_knapsack(capacity, weights):
    all_combinations = []
    for size in range(len(weights) + 1):
        for subset in combinations(weights, size):
            all_combinations.append(sum(subset))
    for weight in sorted(all_combinations, reverse=True):
        if weight <= capacity:
            return weight


def main():
    parser = arg.ArgumentParser()
    parser.add_argument('-W', '--capacity', type=int, help='Capacity of the bag.')
    parser.add_argument('-w', '--weights', nargs='*', type=float, help='All weights of gold bars.')
    parser.add_argument('-n', '--bars_number', type=int, help='Count of gold bars.')
    arguments = parser.parse_args()
    if len(arguments.weights) != arguments.bars_number or arguments.bars_number < 0 or arguments.capacity < 0:
        raise ValueError
    for weight in arguments.weights:
        if weight < 0:
            raise ValueError
    print(bounded_knapsack(arguments.capacity, arguments.weights))


if __name__ == '__main__':
    main()
