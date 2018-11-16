"""Find the subsequence with the largest sum.

Given a list of integers, like:

  [1, 0, 3, -8, 4, -2, 3]

Return the contiguous subsequence with the largest sum. For
that example, the answer would be [4, -2, 3], which sums to 5.


    >>> largest_sum([1, 0, 3, -8, 4, -2, 3])
    [4, -2, 3]

    >>> largest_sum([1, 0, 3, -8, 4, -2, 3, -2])
    [4, -2, 3]

    >>> largest_sum([1, 0, 3, -8, 19, -20, 4, -2, 3, -2])
    [19]

For ties, return the first one:

    >>> largest_sum([2, 2, -10, 1, 3, -20])
    [2, 2]

Return the shortest version:

    >>> largest_sum([2, -2, 3, -1])
    [3]

If the list is all negative numbers, the subsequence
with the highest sum will be empty (ie, we can do no better
than pick nothing!):

    >>> largest_sum([-1, -2])
    []
"""


def largest_sum(nums):
    """Find subsequence with largest sum."""

    max_sum_list = []
    sum_list = []
    current_list = []

    # loop through list
    # add to current list
    # if sum of items in current list >= 0, add to sum_list
    # if sum of items in current list < 0, save sum_list to max_sum list, 
    # and reset sum_list and current_list
    # return max_sum_list

    for number in nums:
        current_list.append(number)

        if sum(sum_list) == 0:
            sum_list = []

        if sum(current_list) >= 0:
            sum_list.append(number)

        if sum(sum_list) > sum(max_sum_list):
            max_sum_list = sum_list[:]
        
        if sum(current_list) < 0:
            current_list = []
            sum_list = []


    return max_sum_list




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU HANDLED THIS SUMMARILY!\n")
