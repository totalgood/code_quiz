def is_mirrored(x=[]):
    """Check to see if second half of list is duplicate, reversed of first half

    >>> is_mirrored([1,2,3,3,2,1])
    True
    >>> is_mirrored([1,2,3,4,3,2,1])
    True
    >>> is_mirrored(list('abcdedcba'))
    True
    >>> is_mirrored(list('a'))
    True
    >>> is_mirrored(range(3))
    False
    """
    N2 = int(len(x) / 2)
    first = x[:N2]
    last = x[-N2:]
    return first == list(reversed(last))


from itertools import product

def all_pairs(ints=(), target=1):
    """Find all pairs of ints in the provided list and return those that sum to target as tuples
    >>> all_pairs(ints=[1,2,3,4], target=3)
    [(1, 2), (2, 1)]
    >>> all_pairs(ints=[1,2,2,3,4], target=4)
    [(1, 3), (2, 2), (2, 2), (2, 2), (2, 2), (3, 1)]
    """
    ints = sorted([i for i in ints if i <= target])
    ans = []
    for i in reversed(ints):
        for j in ints:
            pair = (i, j)
            if sum(pair) > target:
                break
            elif sum(pair) == target:
                ans += [pair]
            else:
                break
    return ans



def find_indices(ints=(), =()):
    """Find the values
    >>> find_indices(ints=[5,6,7,8], indices=(1,3))
    [5, 7]
    """
    return [j for i, j in enumerate(ints) if i not in set(indices)]

    set_of_indices = set(indices)
    ans = []
    for i, j in enumerate(product(ints)):

        if i not in set_of_indices




