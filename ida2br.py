import pyperclip

offset = 0xc60000
# simply copy and paste it in between """ """
ida_search = """
100148294	sub_100147D0C	MOV             W9, #0x7FFFFFFF
100150934	sub_100150908	MOV             W0, #0x7FFFFFFF
100150954	sub_100150908	MOV             W0, #0x7FFFFFFF
100154A9C	sub_10015493C	AND             W1, W26, #0x7FFFFFFF
100154B9C	sub_10015493C	TST             W26, #0x7FFFFFFF
100154BEC	sub_10015493C	AND             W8, W26, #0x7FFFFFFF
100154C50	sub_10015493C	AND             W8, W26, #0x7FFFFFFF
100155420	sub_1001553F4	MOV             W9, #0x7FFFFFFF
10015545C	sub_1001553F4	MOV             W9, #0x7FFFFFFF
10019D458	sub_10019D188	MOV             W23, #0x7FFFFFFF
10021BB0C	sub_10021B4D0	AND             W14, W14, #0x7FFFFFFF
10021BB20	sub_10021B4D0	AND             W14, W14, #0x7FFFFFFF
10021BB38	sub_10021B4D0	AND             W14, W14, #0x7FFFFFFF
10021C874	sub_10021C84C	MOV             W23, #0x7FFFFFFF
10026D974	sub_10026D938	MOV             W8, #0x7FFFFFFF
100288150	sub_10028812C	MOV             W20, #0x7FFFFFFF
10028D618	sub_10028C84C	MOV             W9, #0x7FFFFFFF
1002A7E74	sub_1002A7DC4	MOV             W8, #0x7FFFFFFF
1002C8994	sub_1002C8834	AND             W0, W22, #0x7FFFFFFF
1002D0374	sub_1002D0300	MOV             W10, #0x7FFFFFFF
1002DDFE0	sub_1002DD84C	MOV             W8, #0x7FFFFFFF
1002E1290	sub_1002E1254	MOV             W8, #0x7FFFFFFF
1002EA734	sub_1002EA6FC	MOV             W12, #0x7FFFFFFF
1002F5598	sub_1002F5510	MOV             W25, #0x7FFFFFFF
1002FCE20	sub_1002FCD58	MOV             W22, #0x7FFFFFFF
100308064	sub_100307FEC	MOV             W12, #0x7FFFFFFF
1003080F0	sub_100307FEC	MOV             W11, #0x7FFFFFFF
1003081E0	sub_100307FEC	MOV             W12, #0x7FFFFFFF
100309F28	sub_100309DC0	MOV             W9, #0x7FFFFFFF
10030A0E0	sub_100309DC0	MOV             W10, #0x7FFFFFFF
10030A128	sub_100309DC0	MOV             W9, #0x7FFFFFFF
10030FB98	sub_10030F9E0	AND             X8, X10, #0x7FFFFFFF
100316058	sub_100316008	MOV             W8, #0x7FFFFFFF
10038AC38	sub_10038AADC	MOV             W21, #0x7FFFFFFF
1003C6BC0	sub_1003C6BBC	AND             W0, W8, #0x7FFFFFFF
1003E7D34	sub_1003E78A8	MOV             W9, #0x7FFFFFFF
1003E7D6C	sub_1003E78A8	MOV             W8, #0x7FFFFFFF
1001C60DC	LSL             W8, W9, #0x1F
"""

output = ""
for line in ida_search.splitlines():
    if line: # ignore empty lines
        address = line.split("\t")[0]
        temp = int(address, 16) + offset
        br = "b {}".format(hex(temp))
        print(br)
        output += br + "\n"

# only copy if output is not empty
if output:
    pyperclip.copy(output)
    print("\nCopied to clipboard")

print("Done")
