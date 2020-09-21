offset = 0xc60000
address = [0xf5559c, 0xf55e64, 0xf2cb00, 0xf35430]

for a in address:
    print(hex(a - offset))
