import pyperclip
import os

text_file = "br.txt"
if not os.path.exists(text_file):
    with open(text_file, "w") as f:
        f.close()
    exit("{} is not found, it has been created".format(text_file))

offset = 0x90000
with open(text_file, "r") as f:
    ida_search = f.read()

    output = ""
    for line in ida_search.splitlines():
        if line and not "stop reason = breakpoint" in line:  # the first line
            temp = line.replace("*", " ").split(" ")
            address = temp[6]
            number = temp[5]
            temp = int(address, 16) - offset
            br = "{} {}".format(number, hex(temp))
            print(br)
            output += br + "\n"

    # only copy if output is not empty
    if output:
        pyperclip.copy(output)
        print("\nCopied to clipboard")
