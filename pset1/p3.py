base_string = 'Longest substring in alphabetical order is: '

def alphasubs(s):
    longest = ''
    idx = 0
    for i in range(1, len(s)):
        if s[i-1] <= s[i]:
            idx += 1
        else:
            idx = 0

        if idx > len(longest):
            print(s[i-idx:i+1])
            longest = s[i-idx:i+1]

    return longest

# To run in the EDX platform
#print(base_string + alphasubs(s))
# abcdefghij

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
