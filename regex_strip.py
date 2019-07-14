# Write a function that takes a string and does the same thing as the strip()
# string method. If no other arguments are passed other than the string to
# strip, then whitespace characters will be removed from the beginning and
# end of the string. Otherwise, the characters specified in the second argu-
# ment to the function will be removed from the string.

import re

def strippo(a, regex):
    if(regex == ''):
        strip = re.compile(r'^\s+|\s+$')
        a = strip.sub('', a)
    else:
        for i in list(regex):
            for i in list(regex):
                l_strip = re.compile("^{}+".format(i))
                a = l_strip.sub('', a)
                print('after l_strip',i)
                print('`' + a + '`\n')
                r_strip = re.compile("{}+$".format(i))
                a = r_strip.sub('', a)
                print('after r_strip',i)
                print('`' + a + '`\n')


print('Write text to be stripped: ')
text = input()
print('Write regex: ')
regex = input()
strippo(text, regex)
