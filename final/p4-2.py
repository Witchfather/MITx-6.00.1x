def longestRun(L):
    """
        L -> list
        Returns the length of the longest run of monotonically
        increasing numbers occurring in L.

        This function returns the length of the longest run of monotonically
        increasing numbers occurring in L. A run of monotonically increasing
        numbers means that a number at position k+1 in the sequence is either
        greater than or equal to the number at position k in the sequence.
    """
    i = 0
    longest = 0
    while i < len(L):
        j = i + 1
        temp = 1
        while j < len(L):
            if L[j] >= L[j-1]:
                j += 1
                temp += 1
            else:
                break
        if temp > longest:
            longest = temp
        i = j
    return longest

# test case 1
L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2]
n = longestRun(L)
expected_n = 5
print "Running test case 1...",
if not n == expected_n:
    raise Exception("Got " + str(n) + "; expected " + str(expected_n))
print("Ok")

# test case 2
L = [1, 0, 0, 0, 4, 5, 1, 2, 9, 4, -1, 0]
n = longestRun(L)
expected_n = 5
print "Running test case 1...",
if not n == expected_n:
    raise Exception("Got " + str(n) + "; expected " + str(expected_n))
print("Ok")
