"""
ALPHABETICAL SUBSTRINGS (15/15 points)
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters
occur in alphabetical order. For example, if s = 'azcbobobegghakl',
then your program should print:

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring. For example, if s = 'abcbcd',
then your program should print:

Longest substring in alphabetical order is: abc
"""

base_string = 'Longest substring in alphabetical order is: '

def alphasubs(s):
    i = 0
    buf = ''
    stack = []
    while i < len(s):
        if ((i + 1) < len(s)) and (s[i] <= s[i + 1]):
            buf += s[i]
            i += 1
        else:
            buf += s[i]
            if len(stack) == 0:
                stack.append(buf)
                buf = ''
            elif len(buf) > 1:
                temp = stack.pop()
                if len(temp) < len(buf):
                    stack.append(buf)
                else:
                    stack.append(temp)
                buf = ''
            else:
                buf = ''
            i += 1
    return stack.pop()

# To run in the EDX platform
#print(base_string + alphasubs(s))


## some test cases from EDX
import unittest
class StringTests(unittest.TestCase):
    def test_alphabetical(self):
        self.assertEqual(alphasubs('jxwsrserrwjysvjktrcfesjf'), 'errw')
        self.assertEqual(alphasubs('heokjetjroyzmjgmgo'), 'oyz')
        self.assertEqual(alphasubs('vlczsarcosuyppi'), 'cosuy')
        self.assertEqual(alphasubs('hbvcqxmcpmjcfbj'), 'cqx')
        self.assertEqual(alphasubs('dacvlkdppeywzlf'), 'acv')
        self.assertEqual(alphasubs('jojhmjjn'), 'jjn')
        self.assertEqual(alphasubs('mnqtbsqgumwmxwlktk'), 'mnqt')
        self.assertEqual(alphasubs('abcdefghijklmnopqrstuvwxyz'), 'abcdefghijklmnopqrstuvwxyz')

if __name__ == '__main__':
    unittest.main()
