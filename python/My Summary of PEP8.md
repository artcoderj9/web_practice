## PEP8 Summary
<https://www.python.org/dev/peps/pep-0008/>
<br/><br/>

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
    * It's ok
        ~~~
        from subprocess import Popen, PIPE
        ~~~
* Imports are always put at the top of the file, just after any module comments and docstrings, and before module globals and constants.

* Imports should be grouped in the following order
    * Standard library imports
    * Related third party imports
    * Local application/library specific imports

* Absolute imports are recommended
    ~~~
    import mypkg.sibling
    from mypkg import sibling
    from mypkg.sibling import example
    ~~~
    * Explicit relative imports are acceptable when complex package layouts (for unnecessary verbose)
        ~~~
        from . import sibling
        from .sibling import example
        ~~~
    * Standard library always use absolute imports
* Importing a class from a class-containing module, it's usually okay to spell this:
    ~~~
    from myclass import MyClass
    from foo.bar.yourclass import YourClass
    ~~~
* Whildcard imports (from `<module`> import *) should be avoided

#### Module Level Dunder Names
* Module level "dunders" should be placed after the module docstring, but before any import statements except "from `_`_future`_`_"
    * dunders : names with two leading and two trailling underscores
    <br/>(ex) `_`_all`_`_, `_`_author`_`_, `_`_version`_`_
    ~~~
    """This is the example module.

    This module does stuff.
    """

    from __future__ import barry_as_FLUFL

    ___all__ = ['a', 'b', 'c']
    __version__ = '0.1'
    __author__ = 'Cardinal Biggles'

    import os
    import sys
    ~~~

### String Quotes
* Single-quoted strings and double-quoted strings. Anything is ok.
* For triple-quoted strings, always use double quoted characters to consistent with the docstring convention

### Whitespace in Expressions and Statements
