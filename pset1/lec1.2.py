"""
COUNTING BOBS  (15/15 points)
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s.
For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2
"""

def countword(s, word):
    w = 0
    i = 0
    total = 0
    while i < len(s):
        c = s[i]
        if c == word[w]:
            w += 1
            if w == len(word):
                total += 1
                w = 0
            else:
                i += 1
        else:
            if (c != word[0]):
                w = 0
                i += 1
            else:
                w = 1
                i += 1
    return total

# To run in the EDX platform
#word = 'bob'
#print('Number of times ' + word + ' occurs is: ' + str(countword(word)))


## some test cases from EDX
import unittest
class StringTests(unittest.TestCase):
    def test_countword(self):
        word = 'bob'
        self.assertEqual(countword('obobbobbbobobjo', word), 4)
        self.assertEqual(countword('bobobbobobuboobbobdobobobbobtbobbdvxbooboe', word), 9)
        self.assertEqual(countword('mboobobobbobobooboohoobobotzbobbobbobobbobbbobobobobo', word), 14)
        self.assertEqual(countword('mobobovoboboc', word), 2)
        self.assertEqual(countword('ubkbockob', word), 0)
        self.assertEqual(countword('bobobgbobobboobcobioboo', word), 4)
        self.assertEqual(countword('boobbobbzobooqiwoboobooywcv', word), 1)
        self.assertEqual(countword('yhtqpgnzdfi', word), 0)
        self.assertEqual(countword('bobobobobobobobobob', word), 9)
        self.assertEqual(countword('obooboobtboofdjbobobeeboboboobboobbobobbb', word), 6)
        self.assertEqual(countword('bebobbbokbobv', word), 2)

if __name__ == '__main__':
    unittest.main()
