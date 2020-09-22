offset = 0x208000
address = [0x507fd4]

for a in address:
    print("sum: {}, diff: {}".format(hex(a + offset), hex(a - offset)))
