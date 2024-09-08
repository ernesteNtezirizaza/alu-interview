#!/usr/bin/python3
"""Check readme for full description"""


def rain(walls):
    """Rain function"""
    water_retained = 0

    if not isinstance(walls, list) or len(walls) < 3:
        return 0

    # The left and right max at each index
    length = len(walls)
    left, right = [[0]*length, [0]*length]

    # Compute the values of the those maxes
    left[0] = walls[0]
    for i in range(1, length):
        left[i] = max(left[i-1], walls[i])

    right[length-1] = walls[length-1]
    for i in range(length-2, -1, -1):
        right[i] = max(right[i + 1], walls[i])

    # Compute the water retained at each index
    # using the min of the left and right max
    for i in range(len(walls)):
        water_retained += min(left[i], right[i]) - walls[i]

    return water_retained
