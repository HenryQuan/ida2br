# ida2br
Convert ida search lists to breakpoints + offset. Simply paste the search result to `ida.txt`, update the offset, run the script and ctrl + v to lldb console.

This script can be quite powerful. As long you are in the right direction, you should be able to find the right address because you set breakpoints to all possible addresses. However, if there are too many results, you need to remove many incorrect addresses even before the program continues to run. This should be solved with `lldb-helper` if I could make it.

For example, if you see the number is decrementing by 1 every time. You can then search `SUB.*#1$` in ida to find all sub commands. There might be a few hundreds and maybe even thousands but the address you want should be there as well. With enough time and patience, you should eventually find the one. 

# calc
A simple script for calculating the correct address plus or minus the offset

# lldb-helper
The goal for this is to remove all breakpoints that stop the program from running. This is currently only an idea.