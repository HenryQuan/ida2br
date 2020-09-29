
offset = 0x90000
with open("bt.txt", "r") as f:
    ida_search = f.read()

    output = ""
    for line in ida_search.splitlines():
        if line and not "stop reason = breakpoint" in line: # the first line
            temp = line.replace("*", " ").split(" ")
            address = temp[6]
            number = temp[5]
            temp = int(address, 16) - offset
            br = "{} {}".format(number, hex(temp))
            print(br)
            output += br + "\n"

    print("Done")
