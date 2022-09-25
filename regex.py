import re

# re.match()
# re.search()
# re.findall()
# re.finditer()
# re.sub()
# re.subn()

text  = 'hello world this is a regular expression'

match = re.match(r'hello', text)
print (match.group())