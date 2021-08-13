from offset import OFFSET
# cool down
address = [0xe0d60, 0x2abbcc, 0x612218]

for a in address:
    print("sum: {}, diff: {}".format(hex(a + OFFSET), hex(a - OFFSET)))
