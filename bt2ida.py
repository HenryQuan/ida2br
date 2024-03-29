import os
from offset import OFFSET

text_file = "bt.txt"
if not os.path.exists(text_file):
    with open(text_file, "w") as f:
        f.close()
    exit("{} is not found, it has been created".format(text_file))

with open(text_file, "r") as f:
    ida_search = f.read()

    output = ""
    for line in ida_search.splitlines():
        if line and not "stop reason = breakpoint" in line:  # the first line
            temp = line.replace("*", " ").split(" ")
            address = temp[6]
            number = temp[5]
            temp = int(address, 16) - OFFSET
            br = "{} {}".format(number, hex(temp))
            print(br)
            output += br + "\n"
