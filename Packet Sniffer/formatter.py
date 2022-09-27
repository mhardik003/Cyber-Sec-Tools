import re
file = open("sample_data.txt")
data = file.read()
data= re.sub(r'\\x[0-9a-z][0-9a-z]','',data)
print(data)