## PEP8 Summary
<https://www.python.org/dev/peps/pep-0008/>
<https://yoonpunk.tistory.com/1> (한국어 정리)
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

* Whildcard imports (from &lt;module&gt; import *) should be avoided

#### Module Level Dunder Names
* Module level "dunders" should be placed after the module docstring, but before any import statements except "from \_\_future\_\_"
    * dunders : names with two leading and two trailling underscores
    <br/>(ex) \_\_all\_\_, \_\_author\_\_, \_\_version\_\_
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
#### Avoid extraneous whitespaces in the following situations
* Immediately inside parentheses, brackets or braces
    ~~~
    Yes: spam(ham[1], {eggs: 2})
    No:  spam( ham[ 1 ], { eggs: 2 } )
    ~~~

* Between a trailing comma and a following close parenthesis
    ~~~
    Yes: foo = (0,)
    No:  foo = (0, )
    ~~~

* Immediately before a comma, semicolon, or colon
    ~~~
    Yes: if x == 4: print(x, y); x, y = y, x
    No:  if x == 4 : print(x , y) ; x , y = y , x
    ~~~

* A slice the colon acts like a binary operator. 
    * In an exended slice, both colons must have the same amount of spacing applied.
    * Exception: when a slice parameter is omitted, the space is omitted
    <br/>Yes:
    ~~~
    ham[1:9]
    ham[1:9:3]
    ham[:9:3]
    ham[1::3]
    ham[1:9:]
    ham[lower:upper]
    ham[lower:upper:]
    ham[lower::step]
    ham[lower+offset : upper+offset]
    ham[lower + offset : upper + offset]
    ham[: upperfn(x) : step_fn(x)]
    ham[:: step_fn(x)]
    ~~~
    No:
    ~~~
    ham[lower + offset:upper + offset]
    ham[1:9]
    ham[1 :9]]
    ham[1:9 :3]
    ham[lower : : upper]
    ham[ : upper]
    ~~~

* Immediately before the open parenthesis that starts the argument list of **a functions call**
    ~~~
    Yes: spam(1)
    No:  spam (1)
    ~~~

* Immediately before the open parenthesis that starts an indexing or slicing
    ~~~
    Yes: dct['key'] = lst[index]
    No:  dct ['key'] = lst [index]
    ~~~

* More than one space around an assignment operator to aligh it with another
    <br/>Yes:
    ~~~
    x = 1
    y = 1
    logn_variable = 3
    ~~~
    No:
    ~~~
    x             = 1
    y             = 2
    long_variable = 3
    ~~~

#### Other Recommendations
* Avoid trailing whitespace anywhere

* Always surround these binary operators with a single space on either side
    ~~~
    = 
    +=, -= etc
    ==, <, >, !=, <>, <=, >=, in, not in, is, is not
    and, or, not
    ~~~

* If operators with different prioritie are used, consider adding whitespace around the operators with the lowest priority. Use your own judgment
    <br/>Yes:
    ~~~
    i = i + 1
    submitted += 1
    x = x*2 - 1
    hypot2 =  x*x + y*y
    c = (a+b) * (a-b)
    ~~~
    No:
    ~~~
    i=i+1
    submitted +=1
    x = x * 2 - 1
    hypot2 = x * x + y * y
    c = (a + b) * (a - b)
    ~~~

* Function annotations ahould use the normal rules for colons and always have spaces around the -> arrow if present
    <br/>Yes:
    ~~~
    def munge(input: AnyStr): ...
    def munge() -> AnyStr: ...
    ~~~
    No:
    ~~~
    def munge(input:AnyStr): ...
    def munge()->AnyStr: ...
    ~~~

* Dont's use space around the = sign when used to indicate a keyword argument, or when used to indicate a default value for an unannotated function parameter.
    <br/>Yes:
    ~~~
    def complex(real, imag=0.0):
        return magic(r=real, i=imag)
    ~~~
    No:
    ~~~
    def complex(real, imag = 0.0):
        return magic(r = real, i = imag)
    ~~~

* When combining an argument annotation with a default value, however, do use spaces around the = sign.
    <br/>Yes:
    ~~~
    def munge(sep: AnyStr = None): ...
    def munge(input: AnyStr, sep: AnyStr = None, limit=1000): ...
    ~~~
    No:
    ~~~
    def munge(input: AnyStr=None): ...
    def munge(input: AnyStr, limit = 1000): ...
    ~~~

* Compound statements(=multiple statements on the same line) are generally discouraged.
    <br/>Yes:
    ~~~
    if foo == 'blah':
        do_blah_thing()
    do_one()
    do_two()
    do_three()
    ~~~
    Rather not:
    ~~~
    if foo == 'blah': do_blah_thing()
    do_one(); do_two(); do_three()
    ~~~

* While sometimes it's okay to put an if/for/while with a small body on the same line, never do this for multi-clause statements.
    <br/>Rather not:
    ~~~
    if foo == 'blah': do_blah_thing()
    for x in lst: total += x
    while t < 10: t = delay()
    ~~~
    Definitely not:
    ~~~
    if foo == 'blah': do_blah_thing()
    else: do_non_blah_thing()

    try: something()
    finally: cleanup()

    do_one(); do_two(); do_three(long, argument, 
                                 list, like, this)
    if foo == 'blah': one(); two(); three()
    ~~~

### When to Use Trailing Commas
* They are mandatory when making a tuple of one element.
    * For clarity, it is recommended to surround the latter in parentheses
    <br/>Yes:
    ~~~
    FILES = ('setup.cfg',)
    ~~~
    OK, bug confusing:
    ~~~
    FILES ='setup.cfg',
    ~~~

* To put each value on a line by itself, always a trailing comma, and add the close parenthesis/bracket/brace on the enxt line.
    <br/>Yes:
    ~~~
    FILES = [
        'setup.cfg',
        'tox.ini',
        ]
    initialize(FILES,
               error=True,
               )
    ~~~
    No:
    ~~~
    FILES = ['setup.cfg', 'tox.ini',]
    initialize(FILES, error=True,)
    ~~~

### Comments
* Always make a priority of keeping the comments up-to-date when the code changes

* Comments should be complete sentences
    * The first word should be capitalized
    
* Block comments generally consisit fo one or more paragraphs build out of complete sentences, whth each sentence ending in a period

* You should use two space after a sentence-ending period in multi-sentence comments, except after the final sentence.

* Follow Strunk and White. (The book: The Elements of Style, 번역도서: 영어글쓰기의 기본)

* Write your comments in English

#### Block Comments
* Block comments generally apply to some code that follows them.

* Block comments are indented to the same level as that code.

* Each line of a block comment starts with a # and a single space

#### Inline Comments
* Use inline comments sparingly


#### Documentation Strings
* Write docstrings for all public modules, functions, classes, and methods.

* Docstrings are not mecessary for non-public methods.

* https://www.python.org/dev/peps/pep-0257/

### Naming Conventions
#### Overriding Principle
* Names that are visible to the user as public parts of the API should follow conventions

#### Descriptive: Naming Styles
* Naming Styles
    * b (single lowercase letter)
    * B (single uppercase letter)
    * lowercase
    * lower_case_with_underscores
    * UPPERCASE
    * UPPER_CASE_WITH_UNDERSCORES
    * CapitalizedWords
    * mixedCase
    * Capitalized_Words_With_Underscores (ugly!)

* Special Format
    * _single_leading_underscore: weak "internal use" indicator
        * **from M import \*** does not import objects whose names start with an underscore.
    * single_trailing_underscore_: used by convention to avoid conflicts with Python keyword
        ~~~
        Tkinter.Toplevel(master, class_='ClassName')
        ~~~
    * __double_leading_underscore: when naming a class attribute, invokes name mangling
        ~~~
        class FooBar, __boo => _FooBar__boo
    * \_\_double_leading_and_trailing_underscore\_\_ : magic objects, or attributes that live in user-controlled namespaces

 #### Prescriptive: Naming Conventions
 * Name to avoid
    ~~~
    l,  O, I
    ~~~

* ASCII compatibility

* Package and Module Names
    * Modules should have short, all-lowercase anmes
        * Underscores can be used
    * Packages should have short, all-lowercase names
        * The use of underscores is discouraged

* Class Names
    * CapWords

* Type Variable Names
    * CapWords
    * Short names. eg)T, AnyStr, Num
    * covariant: suffix _co
    * contravriant: suffix _contra
    ~~~
    from typing import TypeVar

    VT_co = TypeVar('VT_co', covariant=True)
    KT_contra = TypeVar('KT_contra', contravariant=True)
    ~~~

* Exception Names
    * CapWords
    * suffix "Error" 

* Global Variable Names
    * Same as those for functions (Lowercase, with words separated by underscores)
    * Prevent exporting globals (module non-public)
        * Use the \_\_all\_\_ mechanism
        * Prefix with an underscore

* Function and Variable Names
    * Lowercase, with words separated by underscores

* Function and Method Arguments
    * Always use *self* for the first argument to instance methods.
    * Always use *cls* for the first argument to class methods.
    * Function arguments's name - append a single trailing underscore, if name clashes with a reserved keyword.

* Method Names and Instance Variables
    * Same as those for functions (Lowercase, with words separated by underscores)
    * One leading underscore only for non-public methods and instance variables.
    * To avoid name clashes with subclasses, use two leading undescores. (to invoke Python's name mangling rules.)

~~~
Python's name mangling rules.

If class Foo has an attribute named __a, it cannot be accessed by Foo.__a
An insistent user could still gain access by calling Foo._Foo__a
~~~

* Constants
    * All capital letters with underscores separating words.
    * Constatns are usually defined on a module level
    ~~~
    MAX_OVERFLOW
    TOTAL
    ~~~

* Designing for inheritance
    * Alway decide whether a class's methods and instance variables(collectively:"attributes") should be public or non-public.
    * If in doubt, choose non-public
    * When designing such a class, take care to make explicit decisions about which atributes are public, which are part of the subclassAPI, and which are truly only to be used your base class.

    * Pythonic guidelines
        * Public attributes should have no leading underscores.
        * If public attribute name collides with a reserved keyword, append a single trailing underscore to your attribute name.
        * For simple public data attributes, it is best to expole just the attribute name.
        * If your class is intended to be subclassed, and you have attributes that you do not want subclasses to use, consider naming them with double elading underscores and no trailing underscores.

* Public and internal interfaces
    * Any backwards compatibility guarantees apply only to public interfaces.
    * Documented interfaces are considered public
    * To better support introspection, modules should explicitly declare the names in their public API using the \_\_all\_\_ attribute.
    * Even with __all__ set appropriately, internal interfaces (packages, modules, classes, functions, attributes or other names) should still be prefixed with a single leading underscore.
    * Imported names should always be considered an implementation detail.

### Programming Recommendations
* TODO

#### Function Annotations
* [PEP 484 - Type Hints](https://www.python.org/dev/peps/pep-0484/)
* In Python 3 code should preferably use *PEP 484* systax
* The experimentation with annotation styles is no longer encouraged
* Experiments within the rules of *PEP 484* are now encouraged.
* To make a different use of function annotations
    ~~~
    # type: ignore
    ~~~
* Type checkers are optional
* *PEP 484* recommends the use of stub files: .pyi files
* For code that needs to be backwards compatible, type annotations can be added in the form of comments.


#### Variable Annotations
* [PEP526 - Syntax for Variable Annotations](https://www.python.org/dev/peps/pep-0526/)
* Single space after the colon
* No space before the colon
* The equality sign should have exactly one space on both side
    <br/>Yes:
    ~~~
    code: int

    class Point:
        coords: Tuple[int, int]
        label: str = '<unknown>'
    ~~~
    No:
    ~~~
    code:int
    code : int

    class Test:
        result: int=0
    ~~~