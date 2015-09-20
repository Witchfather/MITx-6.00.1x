def countword(s, word):
    total = 0
    for i in range(0, (len(s) - len(word) + 1)):
        if s[i:i + len(word)] == word:
            total += 1
    return total

# To run in the EDX platform
#word = 'bob'
#print('Number of times ' + word + ' occurs is: ' + str(countword(s, word)))
