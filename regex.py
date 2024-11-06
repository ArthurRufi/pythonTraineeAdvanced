import re


string = "this is a teste regular expression teste teste teste"
name = 'aba'
print (re.search(r'teste2', string))
print(re.findall(r'teste', string))
print(re.sub(r'teste', name, string, count= 1))