import re

# search for string that starts with csc and ends with 001
text = 'my roll is csc-lkj-001 csc001 cscjhh001'
result = re.findall(r'csc.*001$', text)
print(result)


# Write a regexp that will match name and extension of any Python (.py) file
files = 'test.py a.py py python'
result1 = re.findall(r'\w+\.py', files)
print(result1)

# Check using a regexp the following string contain a legal Python filename?
String = 'This contains two files, assignment1.py and ids.py'
result2 = re.findall(r'\w+\.py', String)
print(result2)


# Write a regexp which detects legal Microsoft Word file names in a string and make a list of them
file_list = 'abc.docx xyz.doc .docx .doc abc2022.docx test.pdf'
result3 = re.findall(r'\w+\.doc{1}x{0,1}', file_list)
print(result3)

# Print out the start location of the first such filename you encounter in the following string
test_string = 'Please edit the following two MS Word documents (bscs.doc) and (bsse.docx), and share with us'
result4 = re.search(r'\w+\.doc{1}x{0,1}', test_string)
print(result4.span())
