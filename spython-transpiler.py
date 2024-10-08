from keywords import s_to_py_keywords
import re
import tokenize

print("Welcome to the Spython language transpiler!")
file_path = input("Enter the path to your .spy file: ")
if (file_path.endswith(".spy")):
    file = open(file_path, "r").read()
    outfile = ""

    # import ply yacc and parse with lex & yacc

    # # Token version
    # tokens = file.split(" ")
    # for token in tokens:
    #     new_token = ""
    #     for linebroken_token in token.split("\n"):
    #         new_token += (s_to_py_keywords[linebroken_token] if linebroken_token in s_to_py_keywords else linebroken_token) + "\n"
    #     outfile += " " + new_token[:-1]
    # print(outfile.strip())

    # Attempted regex version
    outfile = file
    for key in s_to_py_keywords.keys():
        # re.sub(key, s_to_py_keywords[key], outfile)
        outfile = re.sub(r'(\W)' + key + r'(\W)', r'\g<1>' + s_to_py_keywords[key] + r'\g<2>', outfile)
    re.sub(r'es', r'bes', outfile)
    # f = open("file_path"[:-3] + "py", "w")
    # f.write(outfile.strip())
    # f.close()
    print("\nTRANSPILED PROGRAM:")
    print(outfile.strip())
    print("\nPROGRAM OUTPUT:")
    # hi alec!
    # Need to handle:
    # keyword replacement
    # built in function replacement
    # ignoring anything in quotations
    # ignoring anything after a # not in quotations
    # ignoring anything between """
    # later: error handling
    exec(outfile.strip())
else:
    raise Exception("Wrong file extension for input file: " + file_path)
# print(s_to_py_keywords)