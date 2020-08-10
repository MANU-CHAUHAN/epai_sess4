# EPAI_sess4

#### session4.py file contain a Qualean class that is inspired by Boolean + Quantum concepts. The input could only be 3 values (1, 0, -1).

#### Internally the class uses random.uniform(-1, 1) to genrate a new number by multiplying with the input value and then stores it.

#### Another condition imposed on the values is that the precision is 10 digits and rounding used is Banker's rounding.

#### For this Decimal module was used to set precision and rounding is ` ROUND_HALF_EVEN ` which is Banker's rounding.

##### The methods for class Qualean are:

#### The truth table to refer for `__and__` and `__or__`:
#####  `q1`&nbsp;&nbsp;   |&nbsp;&nbsp;&nbsp;&nbsp;    `q2`&nbsp;&nbsp;   |&nbsp;&nbsp;&nbsp;&nbsp;   `or`&nbsp;&nbsp;&nbsp;&nbsp;   |&nbsp;&nbsp;&nbsp;&nbsp;   `and`&nbsp;&nbsp;&nbsp;&nbsp;

-----------------------------------------------------
#####  0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;     0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0
#####  0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;     1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0
#####  1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;     0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0
#####  1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;     1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1

<br/><br/>

1)` __and__ `:
> This is used to check for logical `and`. The output of `__and__` must be always `False` is either of the input is `False`, `True` otherwise.
> The property of short-circuiting is quite useful as program checks and return if first operand is `False` otherwise both are checked for the result.

2)` __or__ `:
> This is used to check for logical `or`. The output is `True` if either of the input is `True`. It is `False` only when both inputs are `False`.
> This also has short-circuiting property but returns `True` if first operand is `True` and does not check for the second in this case.
 
3)` __repr__ `:
> Gives the string containing the representation of the value assigned to `object`.
> So it returns value inside the string "".
> The idea of repr is to give a string which contains a series of symbols which we can type in the interpreter and get the same value which was sent as an argument to repr.
> eg. 
>  
     >>> x = 'foo'
     >>> x
     'foo'
     
     >>> repr(x)
     "'foo'"
     >>> x.__repr__()
     "'foo'"
     
     >>> eval("'foo'")
     'foo'
> When we call eval("'foo'"), it's the same as we type 'foo' in the interpreter. It's as we directly type the contents of the outer string "" in the interpreter.


4)` __str__ `:
> This method returns the string representation of the object. This method is called when print() or str() function is invoked on an object.
>
> This method must return the String object. If we don’t implement __str__() function for a class, then built-in object implementation is used that actually calls __repr__() function.
>

5)` __add__ `:
> Overridden to add two objects' values, the calling( self ) and the passed object.
    
    >>>def __add__(self, other):
           return self.value + other.value 
            
6)` __eq__ `:
> Overloads `==` for equality testing of values of the two objects.
    
     >>>def __eq__(self, other):
            return self.value == other.value

7)` __float__ `:
> Returns `float` object for the calling object, in this case returns the Qualean object's value as `float`.

8)` __ge__ `:
> Overloads `>=` (greater than equal to) comparison operator for the class defined. 


9)` __gt__ `:
> Overloads `>` (greater than) comparison operator for the objects of class defined.

10)` __invertsign__ `:
> Reverses the sign of the object on which the method is called.

11)` __le__ `:
> Overloads `<=` (less than equal to) comparison operator for the objects of class defined.

12)` __lt__ `:
> Overloads `<` (less than) comparison operator for the objects of class defined.

13)` __mul__ `:
> Overloads `*` operator to multiply two objects of the class, the values of the self and other passed object.
 
14)` __sqrt__ `:
> Returns the square root of the object for the class after checking the sign. If negative returns a complex object. Uses `cmath . sqrt()` and `Decimal . sqrt()` .

15)` __bool__ `:
> Is used to check for `truthyness` of the object. Simple implementation involves checking for non-zero value.
    
    >>>def __bool__(self):
           return self.value != 0
           
### Test Cases (28 total)

 ------------------------
 1) test_readme_exists -> tests if README.md exists.
 
 2) test_requirement_file_exists -> tests if requirements.txt exists.
 
 3) test_readme_contents -> Opens README.md, reads entire file, splits on space and then count for words which should be at leas 500.
 
 4) test_readme_proper_description -> tests if the items in README_CONTENT_CHECK_FOR = [
    'Qualean',
    "Banker's",
    'rounding',
    'precision',
    '__and__',
    '__or__',
    '__repr__',
    '__str__',
    '__add__',
    '__eq__',
    '__float__',
    '__ge__',
    '__gt__',
    '__invertsign__',
    '__le__',
    '__lt__',
    '__mul__',
    '__sqrt__',
    '__bool__'
] are mentioned in README.md.

5) test_readme_file_for_formatting -> tests if at least 10 hashes (#) are used for decent formatting of README.md.

6) test_indentations -> Returns pass if used four spaces for each level of syntactically significant indenting.

7) test_function_name_had_cap_letter -> checks if every function defined has small letters.

8) test_things_implemented -> tests if important things in list CHECK_FOR_IMPLEMENTED_FUNCTIONS = [
    '__and__',
    '__or__',
    '__repr__',
    '__str__',
    '__add__',
    '__eq__',
    '__float__',
    '__ge__',
    '__gt__',
    '__invertsign__',
    '__le__',
    '__lt__',
    '__mul__',
    '__sqrt__',
    '__bool__'
] have been defined in main file (session4.py).

9) test_decimal_used_or_not -> tests if 'import' and 'decimal' exists in main file for importing decimal.

10) test_add -> tests `__add__()` for class Qualean.

11) test_for_bool -> tests truthyness of object for class Qualean.

12) test_invert_sign -> tests inversion of sign of the object's value.

13) test_sqrt -> tests if the `__sqrt__()` method of Qualean works correctly and matches as per sign of the object's value.

14) test_eq -> tests equality `__eq__()` ( == ) works fine by adding 1 million times a random number from possible numbers and checks if sum is close to zero. Additionally, makes all possible pairs from the given list of numbers and tests two objects at a time for equality.
 
15) test_function_for_gt -> Checks greater than functionality of `__gt__()` by using two Qualean objects' values and comparing with output of `__gt__()`.    

16) test_function_for_lt -> Checks less than functionality of `__lt__()` by using two Qualean objects' values and comparing with output of `__lt__()`.

17) test_function_for_le -> Checks less than equal to functionality of `__le__()` by using two Qualean objects' values and comparing with output of `__le__()`.

18) test_function_for_ge -> Checks greater than equal to functionality of `__ge__()` by using two Qualean objects' values and comparing with output of `__ge__()`.

19) test_mul -> tests multiplication result from `__mul__()` and 2 objects' * value.

20) test_or -> tests logical or from `__or__()`.

21) test_and -> test logical and from `__and__()`.

22) test_float -> tests if the value of the objects returned using `__float__()` is actually equal to float(value).

23) test_repr -> tests output of `__repr__()` to not include default (`'object at'`) output and if calling `repr()` and then `eval` actually results in string.

24) test_str -> tests if the output of `__str__()` does not include `'<__main__.Qualean object at'`, the default string for an object of class Qualean.

25) test_ne -> tests not equal to `!=` from `__ne__`

26) test_not_implemented -> tests if sesion4.py has returned `NotImplemented`, used in case of wrong object type.

27) test_random_uniform_usage -> tests if session4.py has indeed used `random.uniform(-1, 1)`

28) test_context_usage -> tests if `context` from decimal has been used in main file.
