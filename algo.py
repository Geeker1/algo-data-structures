"""The birthday paradox says that the probability that two people in a room
will have the same birthday is more than half, provided n, the number of
people in the room, is more than 23. This property is not really a paradox,
but many people find it surprising. Design a Python program that can test
this paradox by a series of experiments on randomly generated birthdays,
which test this paradox for n = 5,10,15,20, . . . ,100."""

import random
import itertools


def fetch_birthdays(num):
    return [random.randint(1900,2000) for index in range(num)]

def check_similarity(num):
    group = fetch_birthdays(num)
    combinations = itertools.combinations(group, 2)
    return

def main():
    probability = 0
    for i in range(0, 100, 5):
        check_similarity(i)
    pass
