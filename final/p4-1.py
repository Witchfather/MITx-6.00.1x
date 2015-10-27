def getSublists(L, n):
    """
    L -> list
    n -> int
    Returns a list of all possible sublists in L of length n

    This function returns a list of all possible sublists in L of length n
    without skipping elements in L. The sublists in the returned list should be
    ordered in the way they appear in L, with those sublists starting from a
    smaller index being at the front of the list.
    """
    idx = 0
    sublists = []
    while (idx + n) <= len(L):
        sublists.append(L[idx : idx + n])
        idx += 1
    return sublists

# test case 1
L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2]
n = 4
expected_sublists = [[10, 4, 6, 8], [4, 6, 8, 3], [6, 8, 3, 4], [8, 3, 4, 5], [3, 4, 5, 7], [4, 5, 7, 7], [5, 7, 7, 2]]
sublists = getSublists(L, n)
print "Running test case 1...",
if not sublists == expected_sublists:
    raise Exception("Got " + str(sublists) + "; expected " + str(expected_sublists))
print("Ok")

# test case 2
L = [1, 1, 1, 1, 4]
n = 2
expected_sublists = [[1, 1], [1, 1], [1, 1], [1, 4]]
sublists = getSublists(L, n)
print "Running test case 2...",
if not sublists == expected_sublists:
    raise Exception("Got " + str(sublists) + "; expected " + str(expected_sublists))
print("Ok")
