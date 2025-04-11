Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #number of rows
>>> row=6
>>> #outer loop to handle the number of rows for i in range(rows,0,-1):
>>> #inner loop to print the repeated number in each row
>>> for j in range(rows,-i,+1):
...     print(i,end="")
...     # move to the next line after each row
