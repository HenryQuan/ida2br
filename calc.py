offset = 0x4844000
address = [0x104848b64]

for a in address:
    print("sum: {}, diff: {}".format(hex(a + offset), hex(a - offset)))
