offset = 0xea0000
address = [0x2F3E00]

for a in address:
    print("sum: {}, diff: {}".format(hex(a + offset), hex(a - offset)))
