import re
txt=str(input('Unesite regex: '))
txt.lower()
result = re.match('^m[0-5] k$', txt)
if result:
    print('Točan unos.')

