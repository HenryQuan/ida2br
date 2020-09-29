import pyperclip

offset = 0x90000
with open("ida.txt", "r") as f:
    ida_search = f.read()

    output = ""
    for line in ida_search.splitlines():
        if line and not "Address" in line: # ignore empty lines
            address = line.split("\t")[0].replace("__text:", "")
            temp = int(address, 16) + offset
            br = "b {}".format(hex(temp))
            print(br)
            output += br + "\n"

    # only copy if output is not empty
    if output:
        pyperclip.copy(output)
        print("\nCopied to clipboard")

    print("Done")
