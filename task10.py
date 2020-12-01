#1.
print("1.check a string that contains only a set of characters")
import re
def check(string):
    pattern = r'[^\.a-z0-9A-Z]'
    if re.search(pattern, string):
        print('Invalid : %r' % (string))
    else:
        print('Valid   :%r' % (string))
check(string='AFERef34')
check(string='&dre123$')
check(string='oir34.@1')
check(string='85eDE3u')
print()

#2.
print("2.match a word containing ab")
import re
def text_match(text):
        patterns = '\w*ab.\w*'
        if re.search(patterns,  text):
                return("Found a match....")
        else:
                return("Not matched....")
print(text_match("abacus was the first calculating device"))
print(text_match("which was invented by Tim cranmer"))
print()

#3.
print("3.check for a word at the end of a word")
import re
def end(str):
    string = re.compile(r".*[0-9]$")
    if string.match(str):
        return("Found")
    else:
        return("Not found")

print(end("Charishma"))
print(end("CharishmaJalla9"))
print()
#4.
print("4.Search the numbers(0-9) of length between 1 to 3 in a given string")
import re
result = re.finditer(r"([0-9]{1,3})", "9,18,27,450,5400 are multiples of nine")
print("Number of length 1 to 3")
for n in result:
    print(n.group(0))
print()

#5.
print("5.Match a string that contains only uppercase letters")
import re
def match(text):
        uppercase = '^[A-Z]+$'
        if re.search(uppercase,text):
                return("Found a match....")
        else:
                return("No match found....")
print(match("STUDENT"))
print(match("python"))




