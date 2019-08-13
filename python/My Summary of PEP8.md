## PEP8 Summary

### Code Lay-out

#### Indentation
* Use 4 spaces per indentation level

#### Tabs or Spaces
* Spaces are the preferred
* Python 3 disallows mixing the use of tabs and spaces for indentation

#### Maximum Line Length
* Limit all lines to maximum of 79 characters
* docstrings/comments to 72
* using parentheses, brackets and braces
* using backslash in some case

#### Should a Line Break Before or After a Binary Operator?
* Line break before a binary operator
~~~
income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)
~~~

#### Blank Lines
* Surround **top-level function** and **class definitions** with **two blank lines**.
* **Method definitions inside a class** are surrounded by **a single blank line**
* Extra blank lines may be used to separated groups of realted functions
* Use blank lines in functions to indicate logical sections

#### Source File Encoding
* Code in core Python disribution should always use UTF-8 (in Python3)
* Files using UTF-8 (in Python 3) should not have an encoding declaration

#### Imports
* Imports should usually be on separate lines
~~~
import os
import sys
~~~
* Imports are always put at the top of the file