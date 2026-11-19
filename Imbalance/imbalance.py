"""
Array Imbalance Minimization Practice

This program calculates the total imbalance of a list by adding the absolute
differences between consecutive elements. It then evaluates the imbalance
after removing each element individually and returns the smallest possible
imbalance.

Purpose: Practice working with lists, loops, functions, slicing, and the
absolute value function (abs).
"""

def imbalance(nums):
    imb = 0
    for n in range(len(nums)-1):
      imb += abs(nums[n] - nums[n+1])   
    return imb


def imbalance_without(nums, i):
    n_nums = []
    indxs = len(nums) - 1
    if indxs < 0 or indxs < i:
        n_nums = 0
    elif indxs == i:
        n_nums = nums[:i]
    else:
        n_nums = nums[:i] + nums[i+1:]
    return imbalance(n_nums)


def min_imbalance_after_removal(nums):
    smallest = imbalance(nums)
    for i in range(len(nums)):
        imb = imbalance_without(nums, i)
        if imb < smallest:
            smallest = imb
    return smallest