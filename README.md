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
           
 