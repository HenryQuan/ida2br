# ida2br

Convert ida search lists to breakpoints + offset. Simply paste the search result to `ida.txt`, update the offset, run the script and ctrl + v to lldb console.

This script can be quite powerful as long as you are in the right direction. You should be able to find the right address because you set breakpoints to all possible ones. However, if there are too many results, you need to remove many incorrect addresses even before the program continues to run. This should be solved with `lldb-helper` if I could make it.

For example, if you see the number is substracting `1` every time. Then, you can search `SUB.*#1$` in ida to find all sub commands. There might be a few hundreds and maybe even thousands but the address you want should be there as well. With enough time and patience, you should eventually find the right one.

# calc

A simple script for calculating the correct address plus or minus the offset

# remove-continue

Type `command script import delc.py` to use `delc` in `lldb`.
