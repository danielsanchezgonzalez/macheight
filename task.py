#!/usr/bin/env python3
"""This module solves the opening task"""
import sys

def find_pairs(numbers: list[int], target_sum: int):
    """
    find_pairs gets the pair of numbers that sum the target integer

    :param number: list of integers
    :param target_sum: target integer
    """
    indices = {}
    pairs = []

    for i, num in enumerate(numbers):
        num = int(num)
        complement = target_sum - num
        if complement in indices:
            pairs.append((int(numbers[indices[complement]]), num))
        indices[num] = i
    return pairs

if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise Exception("Incorrect usage\nUsage: list_if_integers target_sum \ne.g.: 1,2,3,4 5")
    for pair in find_pairs(sys.argv[1].split(","), int(sys.argv[2])):
        print(pair)
