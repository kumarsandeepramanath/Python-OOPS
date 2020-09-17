import re

pattern = re.compile("this")
string = "Search inside of this text please"

print(pattern.search(string).group())

#At least 8 char long
#contains letter, numbers $%#@