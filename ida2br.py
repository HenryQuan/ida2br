import pyperclip
import os
from offset import OFFSET

text_file = "ida.txt"
if not os.path.exists(text_file):
    with open(text_file, "w") as f:
        f.close()
    exit("{} is not found, it has been created".format(text_file))

with open(text_file, "r") as f:
    ida_search = f.read()

    output = ""
    for line in ida_search.splitlines():
        if line and not "Address" in line:  # ignore empty lines
            address = line.split("\t")[0].replace("__text:", "")
            temp = int(address, 16) + OFFSET
            br = "b {}".format(hex(temp))
            print(br)
            output += br + "\n"

    # only copy if output is not empty
    if output:
        pyperclip.copy(output)
        print("\nCopied to clipboard")

    print("Done")
