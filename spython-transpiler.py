from keywords import s_to_py_keywords
import re

print("Welcome to the Spython language transpiler!")
file_path = input("Enter the path to your .spy file: ")
if (file_path.endswith(".spy")):
    file = open(file_path, "r").read()
    outfile = file
    for key in s_to_py_keywords.keys():
        re.sub(key, s_to_py_keywords[key], outfile)
        # re.sub(r'[\b$]' + key + r'[\b^]', s_to_py_keywords[key], outfile)
    print(outfile)
else:
    raise Exception("Wrong file extension for input file: " + file_path)
print(s_to_py_keywords)