base_string = 'Longest substring in alphabetical order is: '

def alphasubs(s):
    longest = ''
    temp = s[0]

    for i in range(1, len(s)):
        if s[i-1] <= s[i]:
            temp += s[i]
        else:
            if len(temp) > len(longest):
                longest = temp
            temp = s[i]

    if len(temp) > len(longest):
        longest = temp

    return longest

print(base_string + alphasubs(s))
