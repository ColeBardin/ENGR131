'''ENGR 131 Notes:'''
1/11/21
Statements: 1 instruction
is$>>>
x=input()
print()
 identifiers:
    names that point to objects
    reserved words cannot be used for identifiers
    case sensitive
    can not begin with digits
Floats
    whole number plus decimal = float
        answer = 7/3
        answer 2.333333333333333333
    Min 2.3x10^-308
    Max 1.8x10^308
Arithmetic operations in Python
    +-/*^
    Modulo % gives you remainder
        36%5 = 1, 5 and 1 remainder
    // Largest value that fits into number, rounds down, gets rid of rem
        43//5 = 8, 5*8<43, 5*9>43
    compount operator +=
        x = x + 10
        x += 10 changes x value as it increases
            Incriment: y+=1
Precedent Rules:(), Negation, *, /, %, (+/-), **or^
Print()
    wage = 20
    print('Wage:', wage)
        return would be Wage: 20
    Newline character \n
    end=' ' keeps next print command on same line as this one
Errors
    Syntax:The program contains invalid code that cannot be understood.
    Indentation: The lines of the program are not properly indented.
    Value: An invalid value is used – can occur if giving letters to int().
    Name: The program tries to use a variable that does not exist.
    Type: An operation uses incorrect types – can occur if adding an integer to a string.
    Logical: Bugs
Sample Processor Instructions
    Add X,   num, Y	Adds data in memory location X to the number num, storing result in location Y
    Sub X,   num, Y	Subtracts num from random import choice, random
from types import DynamicClassAttribute, WrapperDescriptorType
from typing import ValuesView, no_type_check

from numpy.lib.histograms import _ravel_and_check_weights
from data in location X, storing result in location Y
    Mul X,   num, Y	Multiplies data in location X by num, storing result in location Y
    Div X,   num, Y	Divides data in location X by num, storing result in location Y
    Jmp Z	Tells the processor that the next instruction to execute is in memory location Z
str(): yields a string of the object
id(): yields the objects identity from memory address
type(): yields the type of an object, integer or string
value(): lists value of identifier
float vs int
    float: rational or irrational number with decimals
    integers: ditto bitch
print selected digits of irrational or repeating decimals:
    print('{:.Xf}'.format(selected_num))
        x = number of digits
        selected_num = number, for example, 'math.pi'

Math Functions, must use math.'function'
Function	    Description		                Function	Description
ceil	        Round up value	                fabs	Absolute value
factorial	    factorial(3 != 3 * 2 * 1)	    floor	Round down value
fmod	        Remainder of division           fsum	Floating-point sum
exp	        Exponential function ex         log	    Natural logarithm
pow	        Raise to power		            sqrt	Square root
acos	        Arc cosine		                asin	Arc sine
atan	        Arc tangent		                atan2	Arc tangent with two parameters
cos	        Cosine		                    sin	    Sine
hypot	        Length of vector from origin    degrees	Convert from radians to degrees
radians	    Convert degrees to radians		tan	    Tangent
cosh	        Hyperbolic cosine		        sinh	Hyperbolic sine
gamma	        Gamma function		            erf	    Error function
pi(constant)	Mathematical constant 3.141592..e(constant)	Mathematical constant 2.718281..

how to edit automatic spacing:
print('poopoo',end='')
print('poopoo', sep='')

ASCII and Encoded text values:
Bit code	Dec 	Char
010 0000	32  	(space)
010 0001	33      !
010 0010	34  	"
010 0011	35      #
010 0100	36	    $
010 0101	37      %
010 0110	38      &
010 0111	39	    '
010 1000	40	    (
010 1001	41	    )
010 1010	42      *
010 1011	43      +
010 1100	44	    ,
010 1101	45      -
010 1110	46  	.
010 1111	47      /
011 0000	48	    0
011 0001	49	    1
011 0010	50	    2
011 0011	51	    3
011 0100	52	    4
011 0101	53	    5
011 0110	54	    6
011 0111	55	    7
011 1000	56	    8
011 1001	57	    9
011 1010	58	    :
011 1011	59	    ;
011 1100	60      <
011 1101	61      =
011 1110	62      >
011 1111	63	    ?
100 0000	64	    @
100 0001	65	    A
100 0010	66	    B
100 0011	67	    C
100 0100	68	    D
100 0101	69	    E
100 0110	70	    F
100 0111	71	    G
100 1000	72	    H
100 1001	73	    I
100 1010	74	    J
100 1011	75	    K
100 1100	76	    L
100 1101	77	    M
100 1110	78	    N
100 1111	79	    O
101 0000	80	    P
101 0001	81	    Q
101 0010	82	    R
101 0011	83	    S
101 0100	84	    T
101 0101	85	    U
101 0110	86	    V
101 0111	87	    W
101 1000	88	    X
101 1001	89	    Y
101 1010	90	    Z
101 1011	91	    [
101 1100	92      \
101 1101	93  	]
101 1110	94      ^
101 1111	95	    _
110 0000	96	    `
110 0001	97	    a
110 0010	98	    b
110 0011	99	    c
110 0100	100 	d
110 0101	101 	e
110 0110	102 	f
110 0111	103 	g
110 1000	104 	h
110 1001	105 	i
110 1010	106 	j
110 1011	107 	k
110 1100	108 	l
110 1101	109 	m
110 1110	110 	n
110 1111	111     o
111 0000	112 	p
111 0001	113 	q
111 0010	114     r
111 0011	115 	s
111 0100	116 	t
111 0101	117 	u
111 0110	118 	v
111 0111	119 	w
111 1000	120 	x
111 1001	121 	y
111 1010	122 	z
111 1011	123 	{
111 1100	124     |
111 1101	125 	}
111 1110	126 	~

Common Escape Sequences
First 3 allow for those special characters to be printed
\\	Backslash(\)
    print('\\home\\users\\')
    \home\users\

\'	Single quote (')
   print('Name: John O\'Donald')
    Name: John O'Donald

\"	Double quote (")
    print("He said, \"Hello friend!\".")
    He said, "Hello friend!".

\n	Newline
    print('My name...\nIs John...')
    My name...
    Is John...

\t	Tab(indent)
    print('1. Bake cookies\n\t1.1. Preheat oven')
    1. Bake cookies
    1.1. Preheat oven

r'' Raw string (Prints string in its entirety)
    print(r'raw string \n \'raw')
    raw string \n \'raw

    num=int(input('Enter 2 digit number:\n'))

    result=num * (3 * 7 * 13 * 37)

    print(result)ord() function
    returns encoded number for a character of length 1

chr() function
    returns encoded value's character equivelant

String Literal: string value specified in the source code of a program
    characters are indexed in code
    may contain spaces, periods, and other non-letetr characters
    must be surrounded by single or double quotes
    first_name = 'Cole'
    print(first_name)
    first_name = input('Type your name:')
    Empty String: first_name = ' '
len(): find the length of a string of a variable
String indexing
    starts counting from 0 L-R
    -1 = last character
Accessing selected characters of a string:
    String[index]
    alphabet[0] = A
changing strings
can't change individual characters in a string at one time, must change entire string at once
containers: groups related values
my_list = [10, 'abc'] created a list with elements, order is indexed, starting at 0

lamborghini_veneno = 3900000   #$3.9 million!
bugatti_veyron = 2400000       #$2.4 million!
aston_martin_one77 = 1850000   #$1.85 million!

prices = [lamborghini_veneno, bugatti_veyron, aston_martin_one77]

print('Lamborghini Veneno:', prices[0], 'dollars')
print('Bugatti Veyron Super Sport:', prices[1], 'dollars')
print('Aston Martin One-77:', prices[2], 'dollars')

Updating list items:
    mynums = [1, 4 ,6]
     mynums[1] = -28
    4->-28
append() a list method used to add a new element to a list
pop()removes an itme according to its index
 remove() removes an item from a list according to its value
my_list.append('abc')
Operation	        Description
len(list)	        Find the length of the list.
list1 + list2	    Produce a new list by concatenating list2 to the end of list1.
min(list)      	    Find the element in list with the smallest value.
max(list)	        Find the element in list with the largest value.
sum(list)	        Find the sum of all elements of a list(numbers only).
list.index(val)	Find the index of the first element in list whose value matches val.
list.count(val)	Count the number of occurrences of the value val in list.

Tuples: like lists but use () instead of []
namedtuple() creates new data type, not objects
House = namedtuple('House', ['street', 'postal_code', 'country'])
    adding objects to named tuples:
    Address = namedtuple('Address', ['street', 'city', 'country']).
    house = Address('221B Baker Street', 'London', 'England')
adding aspects of namedtuples
    car1.price + car2.price
    where car1 and car 2 are namedtuples and price is an aspect
Set basics
A set is an unordered collection of unique elements
    unordered, no position or index
    unique, no elements in the same set share the same value
Set() creates set
print(set) will print the items in no specific order
set(['A', 'Z'])
    no quotes for ints
set() function removes duplicates within set
    set([100, 200, 100, 200, 300])
    this set contains 100, 200, and 300
Operation	        Description
len(set)	        Find the length(number of elements) of the set.
set1.update(set2)	Adds the elements in set2 to set1.
set.add(value)	    Adds value into the set.
set.remove(value)	Removes value from the set. Raises KeyError if value is not found.
set.pop()      	Removes a random element from the set.
set.clear()	    Clears all elements from the set.

2 ways to make sets
    nums1 = set([1, 2, 3]) with set function
    nums2 = {7, 8, 9} make literal set
Adding to set
    names.add('Cole')

Operation	                                Description
set.intersection(set_a, set_b, set_c...)	Returns a new set containing only the elements in common between set and all provided sets.
set.union(set_a, set_b, set_c...)	        Returns a new set containing all of the unique elements in all sets.
set.difference(set_a, set_b, set_c...)	    Returns a set containing only the elements of set that are not found in any of the provided sets.
set_a.symmetric_difference(set_b)	        Returns a set containing only elements that appear in exactly one of set_a or set_b
Dictionary: dict
    object and associates keys with values
players = {
    'Lionel Messi': 10,
    'Cristiano Ronaldo': 7
    }
    print(players)

dictionay = { }
 How to call upon keys: curly brackets build dicts, use hard brackets to access specific trait
   prices = {'apples': 1.99, 'oranges': 1.49}
    print('The price of apples is', prices['apples'])
    print('\nThe price of lemons is', prices['lemons'])
Dict tools (strings need '')
    prices = {}   Create empty dictionary
    prices['banana'] = 1.49   Add new entry
    print(prices)

    prices['banana'] = 1.69   Modify entry
    print(prices)

    del prices['banana']   Remove entry
    print(prices)
Type	    Notes
string	    Sequence type: Used for text.
list	    Sequence type: A mutable container with ordered elements.
tuple	    Sequence type: An immutable container with ordered elements.
set	    Set type: A mutable container with unordered and unique elements.
dict   	Mapping type: A container with key-values associated elements.

Function	    Notes	            Can convert:
int()	        Creates integers    int, float, strings w / integers only
float()	    Creates floats      int, float, strings w / integers or fractions
str()	        Creates strings	    Any

format() function:
uses placeholders surrounded with {} –replacement fields

number = 6
amount = 32

print('{}burritos cost ${}'.format(numberr, amount))
    6 burritons cost $32 
        replaces {} with selected variables

Cannot combine following replacements in a single statement:
Positional replacement
'The {1} in the {0} is {2}.'.format('hat', 'cat', 'fat')
The cat in the hat is fat.

Inferred positional replacement
'The {} in the {} is {}.'.format('cat', 'hat', 'fat')
The cat in the hat is fat.

Named replacement
'The {animal} in the {headwear} is {shape}.'.format(
    animal='cat', headwear='hat', shape='fat')
The cat in the hat is fat.

named replacements allow keyword arugments
print('April {}, {}'.format(22, 2020))

date = 'April {}, {}'
print(date.format(22, 2020))

month = 'April'
day = 22
print('Today is {month} {0}'.format(day, month=month))

format          specifications
Type	        Description	                                                        Example	                Output
s	            String(default presentation type - can be omitted)                  '{:s}'.format('Aiden')  Aiden
d	            Decimal(integer values only)                                        '{:d}'.format(4)        4
b	            Binary(integer values only)                                         '{:b}'.format(4)        100
x, X	        Hexadecimal in lowercase(x) and uppercase(X)(integer values only)   '{:x}'.format(15)       f
e	            Exponent notation                                                   '{:e}'.format(44)       4.400000e+01
f	            Fixed-point notation(6 places of precision)                         '{:f}'.format(4)        4.000000
.[precision]f	Fixed-point notation(programmer-defined precision)                  '{:.2f}'.format(4)      4.00

Referencing the correct format() values in replacement fields
Replacement                         type	                                                                                    Example	Output
Inferred positional replacement     '{:s} ${:.2f} tacos is ${:.2f} total'.format('Three', 1.50, 4.50)                           Three $1.50 tacos is $4.50 total
Positional replacement              '{0:s} ${2:.2f} tacos is ${1:.2f} total'.format('Three', 4.50, 1.50)                        Three $1.50 tacos is $4.50 total
Named replacement                   '{cnt:s} ${cost:.2f} tacos is ${sum:.2f} total'.format(cnt='Three', cost=1.50, sum=4.50)    Three $1.50 tacos is $4.50 total

example of ordered replacement:
user_word = str(input())
user_number = int(input())
print('{0},{1}'.format(user_word, user_number))

Unicode code points for control characters and basic Latin (stored by 32 bits)
    Code point	Char
    0020	space
    0021    !
    0022	"
    0023    #
    0024	$
    0025    %
    0026    &
    0027	'
    0028	(
    0029	)
    002A    *
    002B    +
    002C	,
    002D    -
    002E	.
    002F    /
    0030	0
    0031	1
    0032	2
    0033	3
    0034	4
    0035	5
    0036	6
    0037	7
    0038	8
    0039	9
    003A	:
    003B	;
    003C    <
    003D    =
    003E    >
    003F	?
    0040	@
    0041	A
    0042	B
    0043	C
    0044	D
    0045	E
    0046	F
    0047	G
    0048	H
    0049	I
    004A	J
    004B	K
    004C	L
    004D	M
    004E	N
    004F	O
    0050	P
    0051	Q
    0052	R
    0053	S
    0054	T
    0055	U
    0056	V
    0057	W
    0058	X
    0059	Y
    005A	Z
    005B    [
    005C	\
    005D	]
    005E    ^
    005F	_
    0060	`
    0061	a
    0062	b
    0063	c
    0064	d
    0065	e
    0066	f
    0067	g
    0068	h
    0069	i
    006A	j
    006B	k
    006C	l
    006D	m
    006E	n
    006F	o
    0070	p
    0071	q
    0072	r
    0073	s
    0074	t
    0075	u
    0076	v
    0077	w
    0078	x
    0079	y
    007A	z
    007B	{
    007C    |
    007D	}
    007E	~

If-else branches General
Branch is a program path taken only if an expression's value is true

if-elseif-else branches
year = Gen next input
If year equals 1984         Put "Orwell!" to output
Else If year equals 2001    Put "Space Odyssey!" to output
else                        Put "Nothing special" to output

    If x equals - 1
    Put "Disagrees" to output

    Else If x equals 0
    Put "Neutral" to output

    Else If x equals 1
    Put "Agrees" to output

    Else
    Put "Invalid entry" to output

If statements
    hotel_rate=155

    user_age=int(input('Enter age: '))

    if user_age > 65:
   hotel_rate=hotel_rate - 20

    print('Your hotel rate:', hotel_rate)

    # Statements that execute before the branches

    if expression:
    # Statements that execute when expression is true (first branch)
    else:
    # Statements that execute when expression is false (second branch)

        # Statements that execute after the branches

Constructing multi-branch if-else Statements
if expression1:
   # Statements that execute when expression1 is true
   # (first branch)
elif expression2:
   # Statements that execute when expression1 is false and expression2 is true
   # (second branch)
else:
   # Statements that execute when expression1 is false and expression2 is false
   # (third branch)


num_years = int(input('Enter number years married: '))

if num_years == 1:
    print('Your first year -- great!')
elif num_years == 10:
    print('A whole decade -- impressive.')
elif num_years == 25:
    print('Your silver anniversary -- enjoy.')
elif num_years == 50:
    print('Your golden anniversary -- amazing.')
else:
    print('Nothing special.')

Nested if-else Statements
if sales_type == 2:
    if sales_bonus < 5:
        sales_bonus = 10
    else:
        sales_bonus = sales_bonus + 2
else:
    sales_bonus = sales_bonus + 1

Equality operators	    Description	                                    Example (assume x is 3)
==	                    a == b means a is equal to b	                x == 3 is True
                                                                        x == 4 is False
!=	                    a != b means a is not equal to b	            x != 3 is False
                                                                        x != 4 is True
<	                    a < b means a is less than b	                x < 4 is True
                                                                        x < 3 is False
>	                    a > b means a is greater than b	                x > 2 is True
                                                                        x > 3 is False
<=	                    a <= b means a is less than or equal to b	    x <= 4 is True
                                                                        x <= 3 is True
                                                                        x <= 2 is False
>=	                    a >= b means a is greater than or equal to b	x >= 2 is True
                                                                        x >= 3 is True
                                                                        x >= 4 is False  
Dont compare floats with '==' ? more to come later -ZyBooks

Common errors:
using = instead of ==
=> !< <>

Boolean Operators and Expressions:
    A Boolean refers to a value that is either True or False. Note that True and False are keywords in Python and must be capitalized. 
    A programmer can assign a Boolean value by specifying True or False, or by evaluating an expression that yields a Boolean.

    Let x=7,   y=9
    (x > 0) and (y < 10)
    True        True    True

    (x > 0) and (y < 5)
    True    False       False

    (x < 0) or (y > 10)
    False   False       False

    (x < 0) or (y > 5)
    False   True        True

    not (x < 0)
    False   True

    not (x > 0)
    True    False

    young=(input() == 'True')
    famous=(input() == 'True')

    if young and famous:
    print('You must be rich!')
    else:
    print('There is always the lottery...')

This if statements checks if the variables have a True of False boolean value

Membership operators: in/not in
Can detect if a certain numeric value, string, or variable is in a string or list (etc type)

Checking for an items in a List:
# Use the "in" operator
barcelona_fc_roster = ['Alves', 'Messi', 'Fabregas']

name = input('Enter name to check: ')

if name in barcelona_fc_roster:
    print('Found', name, 'on the roster.')
else:
    print('Could not find', name, 'on the roster.')

# Use the "not in" operator
barcelona_fc_roster = ['Alves', 'Messi', 'Fabregas']

name = input('Enter name to check: ')

if name not in barcelona_fc_roster:
    print('Could not find', name, 'on the roster.')
else:
    print('Found', name, 'on the roster.')

Substrings:
request_str = 'GET index.html HTTP/1.1'

if '/1.1' in request_str:
    print('HTTP protocol 1.1')

if 'HTTPS' not in request_str:
    print('Unsecured connection')

Dictionary Keys:
my_dict = {'A': 1, 'B': 2, 'C': 3}

if 'B' in my_dict:
   print("Found 'B'")
else:
   print("'B' not found")

# Membership operator does not check values
if 3 in my_dict:
    print('Found 3')
else:
    print('3 not found')

Identity operators
x = 500 + 500  # Create a new object with value 1000
y = 500 + 500  # Create a second object with value 1000
z = x  # Bind z to the same object as x

if z is x:
    print('z and x are bound to the same object')
if z is not y:
    print('but z and y are not.')

Order of evaluation:
Operator/Convention	            Description	                                                                    Explanation
( )	                            Items within parentheses are evaluated first	                                In (a * (b + c)) - d, the + is evaluated first, then *, then -.
* / % + -	                    Arithmetic operators (using their precedence rules; see earlier section)	    z - 45 * y < 53 evaluates * first, then -, then <.
<   <=   >   >=   ==   !=	    Relational, (in)equality, and membership operators	                            x < 2 or x >= 10 is evaluated as (x < 2) or (x >= 10) because < and >= have precedence over or.
not	                            not (logical NOT)	                                                            not x or y is evaluated as (not x) or y
and	                            Logical AND	                                                                    x == 5 or y == 10 and z != 10 is evaluated as (x == 5) or ((y == 10) and (z != 10)) because and has precedence over or.
or	                            Logical OR	                                                                    x == 7 or x < 2 is evaluated as (x == 7) or (x < 2) because < and == have precedence over or

Code Blocks:
Code blocks can only be parted after statements that end with :'s 
such as if, else:
    
# First code block has no indentation

model = input('Enter car model: ')
year = int(input('Enter year of car manufacture: '))

antique = False
domestic = False

if year < 1970:
    # New code block has indentation of 4 columns
    antique = True

# Back to code block 0

if model in ['Ford', 'Chevrolet', 'Dodge']:
  # New code block has indentation of 2 columns
  # Any amount of indentation > 0 is OK.
  domestic = True

# Back to code block 0

if antique:
    # New code block has indentation of 4 columns
    if domestic:
        # New block has 4 additional columns (8 total)
        print('My own model-T still runs like a charm...')

Some indentations are continuations of the previous line:
Multiple lines enclosed within parentheses are implicitly joined into a single string (without newlines between each line); use implicit line joining for very long strings or functions with numerous arguments. Ex: All extra lines are indented to the same column as the opening quotation mark on the first line.

When declaring list or dict literals, entries can be placed on separate lines for clarity.
declaration = ("When in the Course of human events, it becomes necessary for "
               "one people to dissolve the political bands which have connected "
               "them with another, and to assume among the powers of the earth...")
 
result_of_power = math.pow(long_variable_name_left_operand,
                           long_variable_name_right_operand)

List, dict multi-line constructs
my_list = [
    1, 2, 3,
    4, 5, 6
    ]

my_dict = {
    'entryA': 1,
    'entryB': 2
}

Conditional expressions: or Ternary operation
    expr_when_true if condition else expr_when_false
Not preffered within the python community due to its difficulty to read/unintuitiveness
if condition:
   my_var = expr1
else:
   my_var = expr2

#is the same as 

my_var = expr1 if (condition) else expr2

Conditional expressions can only be used with the same variables in both branches
ex of violation:
if x < 1:
    y = x
else:
    z = x

#cannot be the same as

y = x if x<1 else z = x

Loops
while variable is not 0

while expression:  # Loop expression
    # Loop body: Sub-statements to execute
    # if the loop expression evaluates to True

# Statements to execute after the expression evaluates to False



curr_power = 2
user_char = 'y'

while user_char == 'y':
    print(curr_power)
    curr_power = curr_power * 2
    user_char = input()

print('Done')

Loop expression logic:
Interate while:                         
x is less than 100                      X<100
x is greater than or equal to 100       x>=100
x equals 'g'                            x=='g'

until c equals 'g'                      x!='g'

Takes 2 inputs and calculates GCD
num_a = int(input('Enter first positive integer: '))
print()

num_b = int(input('Enter second positive integer: '))
print()

while num_a != num_b:
    if num_a > num_b:
        num_a = num_a - num_b
    else:
        num_b = num_b - num_a

print('GCD is {}'.format(num_a))

Random numbers
use function:
random.randint(a,b)
    choses a random number from a to b, inclusive

Counting
Specific number of iterations, N iterations
i = 1
while i<=N:
    #loop body
    i = i+1

Factorial calculator
N = int(input())  # Read user-entered number
total = N

while N >1:
    N-=1
    total = total*(N)

print(total)

For loops
a statement that loops over each element in a container one at a time
for name in ['Bill', 'Nicole', 'John']:
  print('Hi {}!'.format(name))

useful applications:
channels = {
    'MTV': 35,
    'CNN': 28,
    'FOX': 11,
    'NBC': 4,
    'CBS': 12
}

for c in channels:
    print('{} is on channel {}'.format(c, channels[c]))

Can also iterate over strings
my_str = ''
for character in "Take me to the moon.":
    my_str += character + '_'
print(my_str)

List:
for my_pet in ['Scooter', 'Kobe', 'Bella']:
    # Loop body statements
for price in my_prices

strings:
for number in '911'

Reversed function
reversed()
Will reverse the order of list itmes
names = [
    'Biffle',
    'Bowyer', 
    'Busch',
    'Gordon',
    'Patrick'
]

for name in names:
    print(name, '|', end=' ')

print('\nPrinting in reverse:')
for name in reversed(names):
    print(name, '|', end=' ')

Using a for loop to print contacts in a list of contacts
contact_emails = {
    'Sue Reyn' : 's.reyn@email.com',
    'Mike Filt': 'mike.filt@bmail.com',
    'Nate Arty': 'narty042@nmail.com'
}

new_contact = input()
new_email = input()
contact_emails[new_contact] = new_email

for contacts in contact_emails:
    print(contact_emails[contacts], 'is', contacts)

Range function
range()
allows for counting in for loops

Uses:
The range() function can take up to three integer arguments.

range(Y) generates a sequence of all non-negative integers less than Y.
Ex: range(3) creates the sequence 0, 1, 2.

range(X, Y) generates a sequence of all integers >= X and < Y.
Ex: range(-7, -3) creates the sequence -7, -6, -5, -4.

range(X, Y, Z), where Z is positive, generates a sequence of all integers >= X and < Y, incrementing by Z.
Ex: range(0, 50, 10) creates the sequence 0, 10, 20, 30, 40.

range(X, Y, Z), where Z is negative, generates a sequence of all integers <= X and > Y, incrementing by Z.
Ex: range(3, -1, -1) creates the sequence 3, 2, 1, 0.

Range	            Generated sequence	    Explanation
range(5)	        0 1 2 3 4               Every integer from 0 to 4.
range(0, 5)	        0 1 2 3 4               Every integer from 0 to 4.
range(3, 7)	        3 4 5 6                 Every integer from 3 to 6.
range(10, 13)	    10 11 12                Every integer from 10 to 12.
range(0, 5, 1)	    0 1 2 3 4               Every 1 integer from 0 to 4.
range(0, 5, 2)	    0 2 4                   Every 2nd integer from 0 to 4.
range(5, 0, -1)	    5 4 3 2 1               Every 1 integer from 5 down to 1
range(5, 0, -2)     5 3 1                   Every 2nd integer from 5 down to 1

'''Program that calculates savings and interest'''
'''Uses an inputs for ranged for loops to control how many years are printed'''
initial_savings = 10000
interest_rate = 0.05

years = int(input('Enter years: '))
print()

savings = initial_savings
for i in range(years):
    print(' Savings in year {}: ${:.2f}'.format(i, savings))
    savings = savings + (savings*interest_rate)

print('\n')

While vs for loops

i = 0
while i < 100 : 
   # Loop body statements
   i += 1

is the same as 
for i in range(0,100,1):
        # Loop body statements
General rules:
Use a for loop when the number of iterations is computable before entering the loop, as when counting down from X to 0, printing a string N times, etc.
Use a for loop when accessing the elements of a container, as when adding 1 to every element in a list, or printing the key of every entry in a dict, etc.
Use a while loop when the number of iterations is not computable before entering the loop, as when iterating until a user enters a particular character.

Nested loops
outer loop and inner loop
Program to print all 2-letter domain names.

Note that ord() and chr() convert between text and the ASCII or Unicode encoding:
-  ord('a') yields the encoded value of 'a', the number 97.
-  ord('a')+1 adds 1 to the encoded value of 'a', giving 98.
-  chr(ord('a')+1) converts 98 back into a letter, producing 'b'
-  chr(98) converts 98 into the letter 'b'
print('Two-letter domain names:')

letter1 = 'a'
letter2 = '?'
while letter1 <= 'z':  # Outer loop
    letter2 = 'a'
    while letter2 <= 'z':  # Inner loop
        print('{}{}.com'.format(letter1, letter2))
        letter2 = chr(ord(letter2) + 1)
    letter1 = chr(ord(letter1) + 1)

num_rows = int(input())
num_cols = int(input())
i1=0

while i1< num_rows: 
    col_char = 64
    i1+=1
    while col_char < (64+num_cols):
        col_char +=1
        print(i1,chr(col_char), sep = '', end =' ')
print()

user_input = input('Enter phone number: ')

index = 0
for character in user_input:
    print('Element {} is: {}'.format(index, character))
    index += 1

FIXME comments
add #FIXME: add 'element' to do this
in unfinished spaces

Break statements
    a break statement inside a loop causes the loop to exit immediately
empanada_cost = 3
taco_cost = 4

user_money = int(input('Enter money for meal: '))

max_empanadas = user_money // empanada_cost
max_tacos = user_money // taco_cost

meal_cost = 0
for num_tacos in range(max_tacos + 1):
    for num_empanadas in range(max_empanadas + 1):
        meal_cost = (num_empanadas * empanada_cost) + (num_tacos * taco_cost)

        # Find first meal option that exactly matches user money
        if meal_cost == user_money:
            break

    # Find first meal option that exactly matches user money
    if meal_cost == user_money:
        break

if meal_cost == user_money:
    print('${} buys {} empanadas and {} tacos without change.'
        .format(meal_cost, num_empanadas, num_tacos))
else:
    print('You cannot buy a meal without having change left over.')

Continue statements:
    a continue statement in a loop causes an immediate jump to the while or for loop header statement
empanada_cost = 3
taco_cost = 4

user_money = int(input('Enter money for meal: '))

num_diners = int(input('How many people are eating: '))

max_empanadas = user_money // empanada_cost
max_tacos = user_money // taco_cost

meal_cost = 0
num_options = 0
for num_tacos in range(max_tacos + 1):
    for num_empanadas in range(max_empanadas + 1):

        # Total items purchased must be equally divisible by number of diners
        if (num_tacos + num_empanadas) % num_diners != 0:
            continue

        meal_cost = (num_empanadas * empanada_cost) + (num_tacos * taco_cost)

        if meal_cost == user_money:
            print('${} buys {} empanadas and {} tacos without change.'
                  .format(meal_cost, num_empanadas, num_tacos))
            num_options += 1

if num_options == 0:
    print('You cannot buy a meal without having change left over.')

Loop else construct
    loops can contain else statements that will execute if the loop terminates normally (without a break statement)

#While loop else:
while expression:  # Loop expression
    # Loop body: Sub-statements to execute if 
    # the expression evaluated to True
else:
    # Else body: Sub-statements to execute once 
    # if the expression evaluated to False

# Statements to execute after the loop

#For loop else:
for name in iterable:
    # Loop body: Sub-statements to execute 
    # for each item in iterable
else:
    # Else body: Sub-statements to execute 
    # once when loop completes

# Statements to execute after the loop

names = ['Janice', 'Clarice', 'Martin', 'Veronica', 'Jason']

num = int(input('Enter number of names to print: '))
for i in range(len(names)):
    if i == num:
        break
    print(names[i], end= ' ')
else:
    print('All names printed.')

Enumerate function
    enumerate()

origins = [4, 8, 10]
for index in range(len(origins)):
    value = origins[index]  # Retrieve value of element in list.
    print('Element {}: {}'.format(index, value)

origins = [4, 8, 10]
for value in origins:
    index = origins.index(value)  # Retrieve index of value in list
    print('Element {}: {}'.format(index, value))

origins = [4, 8, 10]
for (index, value) in enumerate(origins):
    print('Element {}: {}'.format(index, value))

numbers = [-7, -3, -2, -6, 10, 4]
for position, number in enumerate(numbers):
    if number < 0:
        print(position, number)
    else:
        print(position, 'x')

Functions (general)
reduce redundancy and allow for more efficient code
c1 = (f1-32.0)*(5.0/9.0)
c2 = (f2-32.0)*(5.0/9.0)
c3 = (f3-32.0)*(5.0/9.0)
cluttered and repeated

instead:
F2C(f)
    c = (f-32.0)*(5.0/9.0)
    return c

c1 = F2C(f1)
c2 = F2C(f2)
c3 = F2C(f3)

Function definition:
consists of a name and a block of statements
    def print_pizza_area():

Function call:
invocation of the functions name, causing the functions statements to execute
    print_pizza_area(21)

def keyword is used to define new functions
def print_pattern():
   print('*****')

print_pattern()
print_pattern()

prints ***** twice, over 2 lines

parameters cannot be expressions mixing variables and numbers

Multiple parameter function:
def print_pizza_volume(pizza_diameter, pizza_height):
    pi_val = 3.14159265

    pizza_radius = pizza_diameter / 2.0
    pizza_area = pi_val * pizza_radius * pizza_radius
    pizza_volume = pizza_area * pizza_height
    print('{:.1f} x {:.1f} inch pizza is {:.3f} cubic inches.'
        .format(pizza_diameter, pizza_height, pizza_volume))


print_pizza_volume(12.0, 0.3)
print_pizza_volume(12.0, 0.8)
print_pizza_volume(16.0, 0.8)

parameters are seperated by comma in function definition, and call

return statements in functions
    replaces the function call with the value returned

Hierarchical function calls
    nested function calls
print_pizza_area(inches_to_centimeters(pizza_diameter))

Dynamic and static typing
dynamic typing in python allows the function to determine variable class
static typing in c,c++ makes the user identify it every time

Functions with branching loops
def print_popcorn_time(bag_ounces):
    if bag_ounces < 3:
        print("Too small")
    elif bag_ounces >10:
        print("Too large")
    else:
        print(6*bag_ounces,'seconds')
    

user_ounces = int(input())
print_popcorn_time(user_ounces)

Shampoo routine:
def shampoo_instructions(num_cycles):
    if num_cycles < 1:
        print('Too few.')
    elif num_cycles > 4:
        print('Too many.')
    else:
        n = 0
        while n < num_cycles:
            print(n+1, ': Lather and rinse.')
            n += 1
        print('Done.')

Function stubs: like FIXME statements
allow programers to capture correct high-level behavior
    without being distracted by low level details
    use pass keyword
def steps_to_calories(num_steps):
    pass 

raise NotImplementedError
used at the end of unfinished functions so theyre not computed during testing

Functions are objects
they can be set to variables and make new functions
def print_face():
   # print face statements...


print_face()

func = print_face
func()

allows for functions to be inside other functions
def human_head():
    print('   ||||| ')
    print('   o   o')
    print('     >' )
    print('   ooooo')
    return

def monkey_head():
    print('   .-"-.')
    print(' _/.-.-.\\_')
    print('( ( o o ) )')
    print(' |/  "  \\|')
    print('  \\ .-. /')
    print('  /`"""`\\')
    return

def print_figure(face):
    face()  # Print the face
    print('     |')
    print('   --|--')
    print('  /  |  \\')
    print('@    |    @')
    print('     |')
    print('    /|\\')
    print('   @   @')
    return

choice = int(input('Enter "1" to draw monkey, "2" for human: '))

if choice == 1:
    print_figure(monkey_head)
elif choice == 2:
    print_figure(human_head)

variables:
global vs local
global: variables visible to the entire code
local: variables only visible within function and loops

scope:
area of the code where a name is visible

namespace:
maps names to objects

locals() function
returns a dictionary of the names found in the local namespace

scope resolution:
process of searching namespaces for a name

if the programmer defines a built-in function, that function gets priority over the built in one

Keyword arguments
for functions with a lot of parameters
keyword arguments allows parameters to map to parameters by name instead of order

def print_book_description(title, author, publisher, year, version, num_chapters, num_pages):
    # Format and print description of a book...
print_book_description('The Lord of the Rings', 'J. R. R. Tolkien', 'George Allen & Unwin', 
                       1954, 1.0, 22, 456)
Order matters in this example^^^

def print_book_description(title, author, publisher, year, version, num_chapters, num_pages):
    # Format and print description of a book...

print_book_description(title='The Lord of the Rings', publisher='George Allen & Unwin',
                       year=1954, author='J. R. R. Tolkien', version=1.0,
                       num_pages=456, num_chapters=22)
These paramerers can be input in any order^^^

use keyword arguments for functions with more than 4 arguments
position arguments can be mixed with keyword but it is easy to mix up
common error is to place keyword arguments before all position arguments, which does not work
do position before keyword!

def split_check(amount, num_people, tax_percentage, tip_percentage):
    # ...

split_check(125.00, tip_percentage=0.15, num_people=2, tax_percentage=0.095


default parameter values:
def print_date(day, month, year, style=0):
    if style == 0:  # American
        print(month, '/', day, '/', year)
    elif style == 1:  # European
        print(day, '/', month, '/', year)
    else:
        print('Invalid Style')


print_date(30, 7, 2012, 0)
print_date(30, 7, 2012, 1) #style argument given as 1, therefore style=1
print_date(30, 7, 2012) #style argument not provdided! default value of 0 used


def print_date(day=1, month=1, year=2000, style=0):
print_date(30, 7, 2012, 0)   # Defaults: none
print_date(30, 7, 2012)      # Defaults:                            style=0
print_date(30, 7)            # Defaults:                 year=2000, style=0
print_date(30)               # Defaults:        month=1, year=2000, style=0
print_date()                 # Defaults: day=1, month=1, year=2000, style=0

with no default value or provided argument, the function generates an error

common error is to use a mutable object like a list as a default value
default value is only set when the function is defined (script is loaded)

mixing keyword arguments and default parameter values
def print_date(day=1, month=1, year=2000, style=0):
    # ...


print_date(day=30, year=2012)   # Defaults:        month=1,            style=0
print_date(style=1)             # Defaults: day=1, month=1, year=2000
print_date(year=2012, month=4)  # Defaults: day=1,                     style=0

allows for only keyword arguments to be typed into the call

arbitrary arguments
for when you dont know how many arguments a function requires
include '*args' paramter that collections optional positional parameters into an arbitrary argument list tuple

**kwargs
allows for arbitrary keyword arguments
creares a dictionary of extra arguments not defined in the function

using **kwargs effectively
def stats(name, **info):
    print(name, 'is:')
    for key, value in info.items():
        print('{}: {}'.format(key, value))
stats('John', age=10, gender='m')

John is collected as name
other arguments are put into dictionary 'info'
for loop calls upon the dictionary for all its elements to display them

'''this example is a useful!!'''
**kwargs are put into containers:
they have a key and a value
    key is the name of the argument
    value is the value of what the variable is set to
to access the containers for **info: 'info'.itmes()
can be used in for loops

'''Example of using **kwargs'''
'''courtesy of my own code :), no zybooks code'''
def pizzaProcess(name, phone, ID = 'new customer',**options):
    order_total = 0
    order_string = 'order for {} :: {} :: {}'.format(name, phone, ID)
    for key, value in options.items():
        order_string += ' :: {}'.format(key)
        order_total += value
    order_string += ", total due=${:.2f}".format(order_total)
    return order_string
if __name__ == "__main__":
    my_result = pizzaProcess('andy', '215-867-5309', Onions=4.8, Extra_cheese=3.2)
    print(my_result)


multiple function outputs:
functions can only output 1 thing, but that can be a tuple with other elements as outputs
student_scores = [75, 84, 66, 99, 51, 65]

def get_grade_stats(scores):
    # Calculate the arithmetic mean
    mean = sum(scores)/len(scores)

    # Calculate the standard deviation
    tmp = 0
    for score in scores:
        tmp += (score - mean)**2
    std_dev = (tmp/len(scores))**0.5

    # Package and return average, standard deviation in a tuple
    return mean, std_dev

# Unpack tuple
average, standard_deviation = get_grade_stats(student_scores)

print('Average score:', average)
print('Standard deviation:', standard_deviation)

docstrings:
a string literal placed in the first line of the function body to say with words what the function does

'''Multiple inputs
Unknown inputs
unknown number of inputs
Taking a number of inputs, specified in the first input:'''
numbers = []
results = []
count = int(input())
i = 0
n = 0
while i < count:
    inp = int(input())
    numbers.append(inp)
    i += 1
cap = int(input())
#print(numbers, cap)

while n < len(numbers):
    num = numbers[n]
    if num <= cap:
        results.append(numbers[n])
    n += 1
#print(results)
for k in range(len(results)):
    print(results[k], ',', end='', sep='')


'''as long as the input is not negative, last input is negative:'''
numbers = []
a = int(input())
while a > -1:
    numbers.append(a)
    a = int(input())
print(min(numbers), 'and', max(numbers))


'''Fibonacci Sequence code:'''
x0 = int(input())
x1 = int(input())
n = int(input())

last = x1
entire = x0
numbers = []
m = n-2

numbers.append(x0)
numbers.append(x1)

for i in range(m):
    entire = numbers[0+i] + numbers[1+i]
    numbers.append(entire)
print(numbers)

Reading files
myjournal = open('file.txt')
contents = myjournal.read()

open() is a built in function
    automatically assumes that the argument is in same directory
    but you can always specify open('C:\\Users\\BWayne\\tax_return.txt')
my_file = open('readme.txt')
my_file.close() closes a file after no more reads or writes to the file are allowed

my_file.read() returns first line
my_ile.readlines() returns a list of strings where the first element is contents of the first line and etc
my_file.readline() reurns a single line at a time
EOF is end of file

'''counting average of a file of numbers'''
# Read file contents
print('Reading in data...')
f = open('mydata.txt')
lines = f.readlines()
f.close()

# Iterate over each line
print('\nCalculating average...')
total = 0
for ln in lines:
    total += int(ln)

# Compute result
avg = total/len(lines)
print('Average value:', avg)

'''Iterating over the lines of a file'''
"""Echo the contents of a file."""
f = open('myfile.txt')

for line in f:
    print(line, end="")

f.close()

Writing files
file.write()
    writes a string argument into afile
f = open('myfile.txt', 'w')  # Open file
f.write('Example string:\n  test...')  # Write string
f.close()  # Close the file

write() only allows str 
so convert float and int to str 
f.write(str(5.75))

Modes for opening files:
Mode	Description	                                                                            Allow read?	    Allow write?	Create missing file?	Overwrite file?
'r'	    Open the file for reading.	                                                            Yes	            No	            No	                    No

'w'	    Open the file for writing. If file does not exist then the file is created. 
        Contents of an existing file are overwritten.	                                        No	            Yes	            Yes	                    Yes

'a'	    Open the file for appending. If file does not 
        exist then the file is created. Writes are added to end of existing file contents.	    No	            Yes	            Yes	                    No

update mode:
add r+ w+ a+ to allow for both reading and writing of a file at the same time

f = open('myfile.txt', 'a')
f = open('myfile.txt', 'w')
f = open('myfile.txt', 'r')
f = open('myfile.txt', 'a+')

write files put all arguments on same line with no spaces

myfile = open('myfile.xtx','w')
myfile.write('Num')
myfile.write('5')
myfile.write('\n')

adds: 'Num5\n'

optional argument in open statement
adjusting buffer size
0 = no buffering
1 = default buffering
>1 = a specific buffer size in bytes
f = open('myfile.txt', 'w', buffering=100)

flush() method
forces output buffer to write to disk
os.fsync() function may have to be called in some operating systems. closing an open file flushes the output buffer

import OS 

# Open a file with default line-buffering.
f = open('myfile.txt', 'w')

# No newline character, so not written to disk immediately
f.write('Write me to a file, please!')

# Force output buffer to be written to disk
f.flush()
os.fsync(f.fileno())

# ...

Interacting with file systems
python programmers toolbox
using import OS

import OS
# ...

my_file = open('myfile.txt', 'r')
# ...
file_info = os.stat('myfile.txt')
# ...
os.remove('myfile.txt')

common error is to type a file path as a string literal
instead using the OS functions to make sure the code is portable
path = os.path.join('subdir', 'bath_mobile.jpg')
instead of path = subdir/bat_mobile.jpg

os.path.join() concatenates the arguments using the correct path separator for the current operating system. 

the os and os.path modules contain other helpful functions

#os.path.split(path) – Splits a path into a 2-tuple(head, tail), where tail is the last token in the path string and head is everything else
    import optparse
    p = os.path.join('C:\\', 'Users', 'BWayne', 'batsuit.jpg')
    print(os.path.split(p))
returns 
('C:\\Users\\BWayne', 'batsuit.jpg')

#os.path.exists(path) – Returns True if path exists, else returns False
    import os
    p = os.path.join('C:\\', 'Users', 'BWayne', 'batsuit.jpg')
    if os.path.exists(p):
        print('Suit up...')
    else:
        print('The Lamborghini then?')
returns 
If file exists:
Suit up...

If file does not exist:
The Lamborghini then?

#os.path.isfile(path) – Returns True if path is an existing file, and false otherwise (e.g., path is a directory). must be a file
    import os
    p = os.path.join('C:\\', 'Users', 'BWayne', 'bat_chopper')
    if os.path.isfile(p):
        print('Found a file...')
    else:
        print('Not a file...')
returns
If path is a file:
Found a file...

If path is not a file:
Not a file...

#os.path.getsize(path) – Returns the size in bytes of path.
    import os
    p = os.path.join('C:\\', 'Users', 'BWayne', 'batsuit.jpg')
    print('Size of file:', os.path.getsize(p), 'bytes')
returns
Size of file: 65544 bytes

os.walk()
walks a directory tree like the one below, shows all subdirectories in the specified path

os.walk(logs)
logs/
    2009/
       April/
               1/
                log.txt
                 words.doc
        January/
              15/
                log.txt
               21/
                log.txt
                 temp23.pdf
               24/
                presentation.ppt
    2010/
       March/
            3/
             log.txt
             7/
             music.mp3

but actually looks like:

Binary data
bytes() function is built in
byte values are immutable

bytes('A text string', 'ascii') – creates a sequence of bytes by encoding the string using ASCII.
bytes(100) – creates a sequence of 100 bytes whose values are all 0.
bytes([12, 15, 20]) – creates a sequence of 3 bytes with values from the list.

creating a bytes object using a bytes literal
assigning byte literals
my_bytes = b'This is a bytes literal'

print(my_bytes)
print(type(my_bytes))

would be
b'This is a bytes literal'
<class 'bytes'>

byte string literals
print(b'123456789 is the same as \x31\x32\x33\x34\x35\x36\x37\x38\x39')

would print: '123456789 is the same as 123456789'


'''reading a bitmap'''
f = open('ball.bmp', 'rb')  # Open in binary mode using 'b'

# Read image binary data
contents = f.read()

print('Contents of ball.bmp\n')
print(contents)

f.close()

The print(contents) statement displays the value of contents, converting each byte to human-readable character if 
that bytes value is a readable ASCII character (less than 128). The first portion of the file's contents is shown 
in the output, though the file portion is abbreviated because the image contains about 27,000 bytes. Note how the 
first 14 bytes of the bitmap file is "BMb\xe6\x00\x00\x00\x00\x00\x006\x04\x00\x00". This sequence constitutes the 
header of the binary file, which describes the bitmaps contents. The first 2 bytes "BM" indicates the type of bitmap. 
The following 4 bytes "b\xe6\x00\x00" indicates the size of the bitmap. The sequence "6\x04\x00\x00" indicates where 
in the file the RGB (red-green-blue) values for each pixel in the image are stored.

Altering a BMP image file
overwrites a portion of the image with new pixel colors

import struct

ball_file = open('ball.bmp', 'rb')
ball_data = ball_file.read()
ball_file.close()

# BMP image file format stores location
# of pixel RGB values in bytes 10-14
pixel_data_loc = ball_data[10:14]

# Converts byte sequence into integer object
pixel_data_loc = struct.unpack('<L', pixel_data_loc)[0]

# Create sequence of 3000 red, green, and yellow pixels each
new_pixels = b'\x01'*3000 + b'\x02'*3000 + b'\x03'*3000

# Overwrite pixels in image with new pixels
new_ball_data = ball_data[:pixel_data_loc] + \
              new_pixels + \
              ball_data[pixel_data_loc + len(new_pixels):]

# Write new image
new_ball_file = open('new_ball.bmp', 'wb')
new_ball_file.write(new_ball_data)
new_ball_file.close()

struct module commonly used python standard library module for packing values into sequences of bytes and unpacking sequences of bytes into values
struct.pack()
struct.unpack()

import struct

print('Result of packing 5:', end=' ')
print(struct.pack('>h', 5))

print('Result of packing 256:', end=' ')
print(struct.pack('>h', 256))

print('Result of packing 5 and 256:', end=' ')
print(struct.pack('>hh', 5, 256))

prints:
Result of packing 5: b'\x00\x05'
Result of packing 256: b'\x01\x00'
Result of packing 5 and 256: b'\x00\x05\x01\x00'

formatting string
first argument in pack statements: says how following arguments hsould be covered into bytes
    < or > indicates the byte order or endainness
    > places most significan byte first
    < places least significant byte first

    h character says how many bytes are used when packing the value
    b = 1 byte integer
    h = 2 byte integer
    i = 4 byte integer
    s = String

struct.unpack() module performs in reverse operation struct.pack(), unpacking a sequence of bytes into a new opject
import struct

print('Result of unpacking {}:'.format(repr('\x00\x05')), end=' ')
print(struct.unpack('>h', b'\x00\x05'))


print('Result of unpacking {}:'.format(repr('\x01\x00')), end=' ')
print(struct.unpack('>h', b'\x01\x00'))

print('Result of unpacking {}:'.format(repr('\x00\x05\x01\x00')), end=' ')
print(struct.unpack('>hh', b'\x00\x05\x01\x00'))

prints:
Result of unpacking '\x00\x05': (5,)
Result of unpacking '\x01\x00': (256,)
Result of unpacking '\x00\x05\x01\x00': (5, 256

Command-line arguments and files
location of file may not be known during time writing program
unknown file location
use command line arguments to allow user to specify location of an input file as shown:
import sys
import os

if len(sys.argv) != 2:
    print('Usage: {} input_file'.format(sys.argv[0]))
    sys.exit(1)  # 1 indicates error

print('Opening file {}.'.format(sys.argv[1]))

if not os.path.exists(sys.argv[1]):  # Make sure file exists
    print('File does not exist.')
    sys.exit(1)  # 1 indicates error

f = open(sys.argv[1], 'r')

# Input files should contain two integers on separate lines

print('Reading two integers.')
num1 = int(f.readline())
num2 = int(f.readline())

print('Closing file {}'.format(sys.argv[1]))
f.close()  # Done with the file, so close it

print('\nnum1: {}'.format(num1))
print('num2: {}'.format(num2))
print('num1 + num2: {}'.format(num1 + num2))


sys.argv[0] is always the script name
sys.argv[1] = second inputed value


The 'with' statements
with statement

can be used to open a file, execute a block of statements, and automatically close a file when complete
with open('myfile.txt', 'r') as myfile:
    # Statement-1
    # Statement-2
    # ...
    # Statement-N
returned object is bound to myfile
when the Nth statement is executed, the file is closed

with statements create context managers, which manage the usage of a resource

print('Opening myfile.txt')

# Open a file for reading and appending
with open('myfile.txt', 'r+') as f:
    # Read in two integers
    num1 = int(f.readline())
    num2 = int(f.readline())

    product = num1 * num2

    # Write back result on own line
    f.write('\n')
    f.write(str(product))

# No need to call f.close() - f closed automatically 
print('Closed myfile.txt')

CSV
comma seperated values
data items called fields

python standard library csv module can be used to help read and write files in the csv format
csv.reader(file) reads file 'file'

'''reading each row of a cvs file'''
import csv

with open('grades.csv', 'r') as csvfile:
    grades_reader = csv.reader(csvfile, delimiter=',')

    row_num = 1
    for row in grades_reader:
        print('Row #{}:'.format(row_num), row)
        row_num += 1

returns:
Row #1: ['name', 'hw1', 'hw2', 'midterm', 'final']
Row #2: ['Petr Little', '9', '8', '85', '78']
Row #3: ['Sam Tarley', '10', '10', '99', '100']
Row #4: ['Joff King', '4', '2', '55', '61']

delimiyer argument in the csv.reader() function specifies the character used in the csv file to separate fields
by default is a comma, but can be changed
import csv

# Dictionary that maps student names to a list of scores
grades = {}

# Use with statement to guarantee file closure
with open('grades.csv', 'r') as csvfile:
    grades_reader = csv.reader(csvfile, delimiter=',')

    first_row = True
    for row in grades_reader:
        # Skip the first row with column names
        if first_row:
            first_row = False
            continue

        ## Calculate final student grade ##

        name = row[0]

        # Convert score strings into floats
        scores = [float(cell) for cell in row[1:]]

        hw1_weighted = scores[0]/10 * 0.05
        hw2_weighted = scores[1]/10 * 0.05
        mid_weighted = scores[2]/100 * 0.40
        fin_weighted = scores[3]/100 * 0.50

        grades[name] = (hw1_weighted + hw2_weighted + 
                        mid_weighted + fin_weighted) * 100

for student, score in grades.items():
    print('{} earned {:.1f}%'.format(student, score))

returns:
Petr Little earned 81.5%
Sam Tarley earned 99.6%
Joff King earned 55.5%

can also write text into a csv file using writer object
writerow() and writerows()
import csv

row1 = ['100', '50', '29']
row2 = ['76', '32', '330']

with open('gradeswr.csv', 'w') as csvfile:
    grades_writer = csv.writer(csvfile)

    grades_writer.writerow(row1)
    grades_writer.writerow(row2)

    grades_writer.writerows([row1, row2])

returns:
100,50,29
76,32,330
100,50,29
76,32,330

'''prints every row in the csv file'''
import csv
with open('myfile.csv', 'r') as myfile:
    csv_reader = csv.reader(myfile)
    for row in csv_reader:
        print(row[1])

Plotting and visualizing data
matplotlib package can be used for plotting data in python
recreates the capability of MATLAB
using matplotlib commands

import matplotlib.pyplot as plt

with open('ocean_temps.csv') as temp_file:
    temps = []
    for t in temp_file:
        temps.append(float(t))

years = range(1850, 2012)

plt.plot(years, temps)
plt.show()


plt.show() function shows the graph
plt.plot()
    accepts various arguments about what to graph and how much of it to graph
        plot(x,y)
        plt.plot([5, 10, 15], [0.25, 0.34, 0.44])

'''plotting multiple limnes on the same graph:'''
import matplotlib.pyplot as plt

with open('ocean_temp.csv') as temp_file:
    temps = []
    for t in temp_file:
        temps.append(float(t))

temp_years = range(1850, 2012)
plt.plot(temp_years, temps)

pirate_years = range(1850, 2025, 25)
num_pirates_thousands = [20, 17, 15, 5, 0.4, 0.05, 0.025]
plt.plot(pirate_years, num_pirates_thousands)
plt.show()


plt.plot() command is called twice before the plot is showed

styling plots:
plot() takes an optional format string that helps style it
'''plot(x,y,'r--') plots it with red hyphens'''
import matplotlib.pyplot as plt

with open('ocean_temps.csv') as temp_file:
    temps = []
    for t in temp_file:
        temps.append(float(t))

years = range(1850, 2012)

plt.plot(years, temps, 'r--')
plt.show()

Format Strings
Formatting strings
Character(s)    Line color/Marker style    
b               Blue
g               Green
r               Red
w               White
k               Black
y               Yellow
m               Magenta
c               Cyan
-               Solid Line
--              Dashed line
-.              Dashed-dot line
:               Dotted line
.               Point marker   
,               Pixel marker
o               circle marker
+               Plus marker
X               X marker
v               Triangle down marker
^               Triangle up marker
<               Triagnle left marker
>               Triagnle right marker
*               Star marker
p               Pentagon marker
1               Tri-down marker
2               Tri-up marker   
3               Tri-left marker
4               Tri-right marker
H               Hexagon1 marker
D               Hexagon2 marker
d               Thin diamond marker
|               Vertical line marker
_               Horizonal line marker
S               Square marker

Line properties
format strings are a shortcut setting line property
line properties are attributes of the line objects created by matplotlib when plot() is called
line properties determine how the line will be displayed when show() is called

Property	        Possible property values	                Description
alpha	            float	                                    Alpha compositing enables transparency
antialiased	        Boolean	                                    Enabled anti-aliasing of the line
color	            A matplotlib color	                        Color of the markers, line
solid_capstyle	    'butt', 'round', or 'projecting'	        How the cap of a line appears
solid_joinstyle	    'miter', 'round', or 'bevel'	            How the join of a line appears
data	            [x_data, y_data]	                        The arrays of x and y coordinates
label	            string	                                    The label to use for the line
linestyle	        '-', '--', '-.', ':', ... (see above)       The style of the line
linewidth	        float	                                    The width of the line when drawn.
marker	            '+', ',', '.', '1', '2', ... (see above)	The style of the marker to use
markersize	        float	                                    The size of the marker
visible	            Boolean	                                    Show/hide the line

format strings provide useful shortcuts to the color, linestyle and marker properties
keyword arguments are used to change other properties values
import matplotlib.pyplot as plt

pirate_years = range(1850, 2025, 25)
number_of_pirates_thousands = [20, 17, 15, 5, 0.4, 0.05, 0.025]
plt.plot(pirate_years, number_of_pirates_thousands, 'ro-',
         linewidth=5, markersize=5, alpha=0.35)
plt.show()

Adding a legend
plt.legend() displays a legend of the lines
import matplotlib.pyplot as plt

with open('ocean_temp.csv') as temp_file:
    temps = []
    for t in temp_file:
        temps.append(float(t))

temp_years = range(1850, 2012)
plt.plot(temp_years, temps, label="Ocean temperature change")

p_years = range(1850, 2025, 25)
pirates_thousands = [20, 17, 15, 5, 0.4, 0.05, 0.025]
plt.plot(p_years, pirates_thousands, label="Number of pirates")
plt.legend(shadow=True, loc="upper right")
plt.show()

many othe keyword arguments can be used to format the legends
for example: 
shadow = True/False
loc = 'lower right'/'upper right'/'lower left'/'upper left'

Adding text to a plot
plt.title() function allows you to add text to a plot
this alone adds it above the graph

# Add plot title
plt.title("Alcohol related fatalities on highways")

# Add text giving specific x,y coordinates of the plot
#placing text in graph
plt.text(1970.5, 11000, 'Fatalities spike\n in 1970s', color='grey', fontsize=12)

# Add a vertical line at x-coordinate 1980
plt.axvline(1980, color='grey')

# Add annotation
arrow_properties = {
    'facecolor': 'black',
    'shrink': 0.1,
    'headlength': 10,
    'width': 2
}
#Actual annotation command \/
plt.annotate('Drinking age changed to 21',
             xy=(1984, 24762),
             xytext=(1986, 30000),
             arrowprops=arrow_properties)

Formatting Graph Axis:
plt.axis() function
plt.axis(xmin, xmax, ymin, ymax)

Numpy
package that includes tools for scientifi and mathematical computations in python
can do linear algebra, fast fourier transformations and stats

numpy uses an array data type that is conceptually similar to a list
ordered set of elements of the same type
array() constructor from numpy package

multidimensional arrays are created by specifying a list with a tuple for each dimensions elements
import numpy as np

# 1-dimension array
my_array1 = np.array([15.5, 25.11, 19.0])
print('my_array_1:')
print(my_array1)
print()

# 2-dimension array
my_array2 = np.array([(34, 25), (16, 12)])
print('my_array_2:')
print(my_array2)

'''returns:'''
my_array_1:
[ 15.5   25.11  19.  ]

my_array_2:
[[34 25]
 [16 12]]

its hard to change the size of an array
so create the array that is the right size first but with filler entries
import numpy as np

zero_array = np.zeros((1, 5))   # 1-dimension array with 5 elements
print('zero_array:')
print(zero_array)
print()

one_array = np.ones((5, 2))  # 2-dimension array with 5 rows and 2 elements per row (2 columns)
print('one_array:')
print(one_array)

'''returns'''
zero_array:
[[ 0.  0.  0.  0.  0.]]

one_array:
[[ 1.  1.]
 [ 1.  1.]
 [ 1.  1.]
 [ 1.  1.]
 [ 1.  1.]]

using np.ones() or np.zeroes(), order of the elements are (num rows, num numcolums)

linspace() function '''NOT LINESPACE()'''
similar to range() function but can create fractional values as well
linspace(0,1,11) creates a sequence with 11 evenly spaced elements between 0 and 1

import numpy as np

print(np.linspace(0, 1, 11))
print()
print(np.linspace(0, np.sin(np.pi/4), 20))

'''returns'''
[ 0.   0.1  0.2  0.3  0.4  0.5  0.6  0.7  0.8  0.9  1. ]

[ 0.          0.03721615  0.07443229  0.11164844  0.14886459  0.18608073
  0.22329688  0.26051302  0.29772917  0.33494532  0.37216146  0.40937761
  0.44659376  0.4838099   0.52102605  0.5582422   0.59545834  0.63267449
  0.66989063  0.70710678]

Array operations program
[5 5 5] + [1 2 3] would compute [5+1 5+2 5+3], or [6 7 8]

import numpy as np

array1 = np.array([10, 20, 30, 40])
array2 = np.array([1, 2, 3, 4])

# Some common array operations

#Adding addition
print('Adding arrays (array1 + array2)')
print(array1 + array2)

#Subtracting subtraction
print('\nSubtracting arrays (array1 - array2)')
print(array1 - array2)

#Multiplication
print('\nMultiplying arrays (array1 * array2)')
print(array1 * array2)

#Matrix multplication
print('\nMatrix multiply (dot(array1 * array2))')
print(np.dot(array1, array2))

#Square root
print('\nFinding square root of each element in array1')
print(np.sqrt(array1))

#Minimum element
print('\nFinding minimum element in array1')
print(array1.min())

#Maximum element
print('\nFinding maximum element in array1')
print(array1.max())

'''returns'''
Adding arrays (array1 + array2)
[11 22 33 44]

Subtracting arrays (array1 - array2)
[ 9 18 27 36]

Multiplying arrays (array1 * array2)
[ 10  40  90 160]

Matrix multiply (dot(array1 * array2))
300

Finding square root of each element in array1
[ 3.16227766  4.47213595  5.47722558  6.32455532]

Finding minimum element in array1
10

Finding maximum element in array1
40

Multiple plots on the same chart
making new figures
figure() function

will allow two graphs to be printed

'''Making multiple figures
more than 1 figure'''
import numpy as np
import matplotlib.pyplot as plt

# Unique identifiers for each figure
FIGURE1 = 1
FIGURE2 = 2

# Wave parameters
FREQUENCY = 3
SAMPLING_RATE = 100
TIME_STEP = 1.0 / SAMPLING_RATE

# Like range() for floating point
t1 = np.arange(0.0, 5.0, TIME_STEP)

# Compute a sine wave
wave = np.sin(FREQUENCY*2*np.pi*t1)

# Compute Fast Fourier Transform (FFT)
fft_result = np.fft.fft(wave)

# Compute x-axis values for frequency domain
t2 = np.fft.fftfreq(len(t1), TIME_STEP)

plt.figure(FIGURE1)
plt.plot(t1, wave)
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.axis([-1, 6, -1.2, 1.2])  # Empty space buffer

plt.figure(FIGURE2)
plt.plot(t2, np.abs(fft_result))
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")

# Set plot axis ranges [min_x, max_x, min_y, max_y]
plt.axis([-5, 5, 0, 260])

plt.show()


xlabel()
axis()

using subplots
subplot() function
'''allows multiple plots in a single figure'''
plt.subplot(2, 1, 1)  # 2 rows, 1 column. Use loc 1
plt.plot(t1, wave)
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.axis([-1, 6, -1.2, 1.2])  # Empty space buffer

plt.subplot(2, 1, 2)  # 2 rows, 1 column. Use loc 2
plt.plot(t2, np.abs(fft_result))
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")

the arguments in subplot function determine how many columns and rows of graphs there are in the figure
and what position this plot will be in


twinx() function allows for multiple things to be graphed on the same x axis with different y axis
figure = plt.figure()
left_axis = figure.add_subplot(1, 1, 1)
right_axis = left_axis.twinx()

left_axis.plot(years, total_fatalities, label="Total")
left_axis.plot(years, alcohol_fatalities, label="Alcohol-related")
right_axis.plot(years, percentages, 'r--', label="% alcohol-related")
right_axis.axis([1970, 2012, 0, 100])

left_axis.set_xlabel('Year')
left_axis.set_ylabel('Number of highway fatalities')
left_axis.legend(loc="upper left")
right_axis.set_ylabel('% fatalities involving alcohol')
right_axis.legend(loc="upper right")

set_right_ylabel() creates the right-side axis

'''figure.addsubplot() is called, which returns the subplot axis (the actual creation of the default 
subplot is not important or necessary). twinx() is called to create the right-side axis. left_axis 
and right_axis can then be used to set axis labels, plot data series, and enable legends.
'''


"""ADDING MULTIPLE LEGENDS IN MATPLOTLIB"""
recalling plt.legend will replace last legend
call plt.legend(my_list_of_legends)


String Slicing
showing multple characters from a string
slice notation:
my_str[start:end]
    does not include end character
print(url[7:23])

negative indicies can also be used:
my_str[0:-2]
if you dont know how many characters there will be but you do not need the last 2

Slices create new objects
my_str = "The cat jumped the brown cow"
animal = my_str[4:7]
print('The animal is a {}'.format(animal))

my_str = 'The fox jumped the brown llama'
print('The animal is still a', animal)  # animal variable remains unchanged.

Common Slicing Operations:
Assume the value of my_str is 'http://en.wikipedia.org/wiki/Nasa/'
Syntax	        Result	                            Description
my_str[10:19]	wikipedia	                        Gets the characters in indices 10-18.
my_str[10:-5]	wikipedia.org/wiki/	                Gets the characters in indices 10-28.
my_str[8:]  	n.wikipedia.org/wiki/Nasa/	        All characters from index 8 until the end of the string.
my_str[:23]	    http://en.wikipedia.org	            Every character up to index 23, but not including my_str[23].
my_str[:-1]	    http://en.wikipedia.org/wiki/Nasa	All but the last character.

String slices also permit variables as arguments

Slice Stride
optional third argument that allows to determine how big of an incriment to take, default is 1
numbers = '0123456789'

print('All numbers: {}'.format(numbers[::]))
print('Every even number: {}'.format(numbers[::2]))
print('Every third number between 1 and 8: {}'.format(numbers[1:9:3]))

Outputs
All numbers: 0123456789
Every even number: 02468
Every third number between 1 and 8: 147


Advanced string formatting
field width options:
    A field width is defined in a format specification by including an integer after the colon, as in {name:16} 
    to specify a width of 16 characters. Numbers will be right-aligned within the width by default, whereas 
    most other types like strings will be left-aligned.
format_string = '{name:16}{goals:8}' #Assigns name and goals with 16 and 8 spaces respectively
print(format_string.format(name='Player Name', goals='Goals')) #Assigns areas label names
print('-' * 24) #Prints bar of hypens, 24 = 16+8
print(format_string.format(name='Sadio Mane', goals=22)) #Gives each category with data inputs
print(format_string.format(name='Gabriel Jesus', goals=7))

Aligning text
format specification can include an alighment character
Alignment type	<format_string>	Output

#Left-aligned	
'{name:<16}{goals:<8}'	
Player Name     Goals   
------------------------
Sadio Mane      22      
Gabriel Jesus   7

#Right-aligned	
'{name:>16}{goals:>8}'	
     Player Name   Goals
------------------------
      Sadio Mane      22
   Gabriel Jesus       7

#Centered	
'{name:^16}{goals:^8}'	
  Player Name    Goals  
------------------------
   Sadio Mane      22   
 Gabriel Jesus     7


Fill characters
pad a replacement field when the string being inserted is smaller than the field width
Format specification	Value of score	    Output
{score:}	            9	                9
{score:4}	            9	                   9
{score:0>4}	            9	                0009
{score:0>4}	            18                  0018
{score:0^4}	            18	                0180

1	name = 'Wayne Rooney'
2	goals = 36
3	
4	# Use default empty space fill character
5	print('{name:<16}{goals:>6}'.format(name=name, goals=goals))
6	
7	# Use '0' as a fill character for score
8	print('{name:<16}{goals:0>6}'.format(name=name, goals=goals))
9	
10	# Use '_' as fill character for name
11	print('{name:_<16}{goals:0>6}'.format(name=name, goals=goals))

Outputs:
Wayne Rooney        36
Wayne Rooney    000036
Wayne Rooney____000036


Floating point precision:
import math
real_pi = math.pi  # math library provides close approximation of pi
approximate_pi = 22.0 / 7.0  # Approximately correct pi to within 2 decimal places

print('pi is {pi}'.format(pi=real_pi))
print('22/7 is {pi}'.format(pi=approximate_pi))
print('22/7 looks better like {pi:.2f}'.format(pi=approximate_pi))

'''Cool example''':
'{x:4.1f}'.format(x=5)
x - variable being printed
:4 - 4 character spaces
.1f - 1 floating point decimal

String methods
finding and replacing:
my_string.replace(old,new,count)
    old is text to find
    new is what to replace old with
    count is optional, replaces firs n(count) occurances of old 
replace() returns a copy of the string with all occurrences of the substring old replaced by the string new
    old/new may be variables or literals

Other useful functions
my_string.find(x) 
    returns the index of the first occurence of item x in the string, else returns -1
    x may be a string literal or variable

my_string.find(x,start,end)
    same as find x but starts from start and ends at end, both are optional and can be used exclusively

my_string.rfind(x)
    same as find(x) but in reverse, returning the last occurance

my_string.count(x)
    returns the number of times x occurs in the string

using find commands are for when you need to know the exact location, the in membership operator should be used to check for if x is in the string

Comparing strings
strings may be compared using: 
relational operators(<, <=, >=, >) 
equality operators(==, !=)
membership operators(in, not in)
identity operators(is, is not)

Example	                            Expression result	Why?
'Hello' == 'Hello'	                True	            The strings are exactly identical values
'Hello' == 'Hello!'	                False	            The left hand string does not end with '!'
'Yankee Sierra' > 'Amy Wise'	    True	            The first character of the left side 'Y' is "greater than" (in ASCII value) the first character of the right side 'A'
'Yankee Sierra' > 'Yankee Zulu'	    False	            The characters of both sides match until the second word. The first character of the second word on the left 'S' is not "greater than" (in ASCII value) the first character on the right side 'Z'
'seph' in 'Joseph'	                True	            The substring 'seph' can be found starting at the 3rd position of 'Joseph'
'jo' in 'Joseph'	                False	            'jo' (with a lowercase 'j') is not in 'Joseph' (with an uppercase 'J')

if str1 is longer than str2 with all corresponding characters equal,
str1>str2

Identity vs Equality operators:
student_name = input('Enter student name:\n')

if student_name is 'Amy Adams':
    print('Identity operator: True')
else:
    print('Identity operator: False')

if student_name == 'Amy Adams':
    print('Equality operator: True')
else:
    print('Equality operator: False')

#'''Outputs'''
Enter student name: Amy Adams
Identity operator: False
Equality operator: True

Methods to check a string value that returns a True or False Boolean value:
    isalnum() -- Returns True if all characters in the string are lowercase or uppercase letters, or the numbers 0-9.
    isdigit() -- Returns True if all characters are the numbers 0-9.
    islower() -- Returns True if all cased characters are lowercase letters.
    isupper() -- Return True if all cased characters are uppercase letters.
    isspace() -- Return True if all characters are whitespace.
    startswith(x) -- Return True if the string starts with x.
    endswith(x) -- Return True if the string ends with x.

Note that the methods islower() and isupper() ignore non-cased characters. Ex: 'abc?'.islower() returns True, ignoring the question mark.

Methods to create new strings:
Methods to create new strings:
    capitalize() -- Returns a copy of the string with the first character capitalized and the rest lowercased.
    lower() -- Returns a copy of the string with all characters lowercased.
    upper() -- Returns a copy of the string with all characters uppercased.
    strip() -- Returns a copy of the string with leading and trailing whitespace removed.
    title() -- Returns a copy of the string as a title, with first letters of words capitalized.


Splitting and joining strings:
split() method
themy_string.split(x)
    returns a list with the elements that were in the string divided by the seperator(x)
        x can be string literal or variable
        seperator character is NOT included in the list
.split() removes whitespace

url = input('Enter URL:\n')

tokens = url.split('/')  # Uses '/' separator
print(tokens)

'''returns'''
Enter URL: http://en.wikipedia.org/wiki/Lucille_ball
['http:', '', 'en.wikipedia.org', 'wiki', 'Lucille_ball']
...
Enter URL: en.wikipedia.org/wiki/ethernet/
['en.wikipedia.org', 'wiki', 'ethernet', '']

if the string starts or ends with the separator or if two consecutive separators exist, the list will contain an empty string

The join() method
my_string = 'x'.join(['pee'],['poo']) joins 'pee' and 'poo' with separator 'x'
    peexpoo

Much easier to use join() method instead of for loops:
phrases = ['To be, ', 'or not to be.\n', 'That is the question.']

#For loop
sentence = ''
for phrase in phrases:
    sentence += phrase 
print(sentence)

'''OR'''

#Join() Method
sentence = ''.join(phrases)
print(sentence)

'''both return'''
To be, or not to be.
That is the question.

Using split() and join() methods together
#
path = input('Enter file name: ')

new_separator = input('Enter new separator: ')
tokens = path.split('/')
print(new_separator.join(tokens))

'''Returns'''
Enter file name: C:/Users/Wolfman/Documents/report.pdf
Enter new separator: \\
C:\\Users\\Wolfman\\Documents\\report.pdf

Splitting and joining: Edition tokens:
#
url = input('Enter Wikipedia URL: ')

tokens = url.split('/')

if 'wiki' != tokens[3]:
    tokens.insert(3, 'wiki')
    new_url = '/'.join(tokens)

    print('{} is not a valid address.'.format(url))
    print('Redirecting to {}'.format(new_url))
else:
    print('Loading {}'.format(url))

'''returns'''
Enter Wikipedia URL: http://en.wikipedia.org/wiki/Rome
Loading http://en.wikipedia.org/wiki/Rome
...
Enter Wikipedia URL: http://en.wikipedia.org/Rome
http://en.wikipedia.org/Rome is not a valid address.
Redirecting to http://en.wikipedia.org/wiki/Rome

Lists and dictionaries
In depth
Dictionary

Operation	                    Description	                                        Example code            Example output
my_list[i] = x	                Change the value of the ith element in-place.	    my_list = [1, 2, 3]     [1, 2, 9]
                                                                                    my_list[2] = 9 
                                                                                    print(my_list)

my_list[len(my_list):] = [x]	Add the elements in [x] to the end of my_list.      my_list = [1,2,3]       [1,2,3,9]
                                The append(x) method (explained in another          my_list[len(my_list)] = 9
                                section) may be preferred for clarity.	            print(my_list)    

del my_list[i]	                Delete an element from a list.	                    my_list = [1, 2, 3]     [1,3]
                                                                                    del my_list[1]
                                                                                    print(my_list)

List Methods
'''Adding elements:'''
List method	        Description	                                Code example	                Final my_list value
list.append(x)	    Add an item to the end of list.	            my_list = [5, 8]
                                                                my_list.append(16)	
                                                                                                [5, 8, 16]
list.extend([x])    Add all items in [x] to list.	            my_list = [5, 8]
                                                                my_list.extend([4, 12])	
                                                                                                [5, 8, 4, 12]
list.insert(i, x)	Insert x into list before position i.	    my_list = [5, 8]
                                                                my_list.insert(1, 1.7)	
                                                                                                [5, 1.7, 8]
'''Removing elements:'''
list.remove(x)	    Remove first item from list with value x.	my_list = [5, 8, 14]
                                                                my_list.remove(8)	
                                                                                                [5, 14]
list.pop()	        Remove and return last item in list.	    my_list = [5, 8, 14]
                                                                val = my_list.pop()	
                                                                                                [5, 8] val is 14
list.pop(i)	        Remove and return item at position i in list.	my_list = [5, 8, 14]
                                                                    val = my_list.pop(0)	
                                                                                                [8, 14] val is 5
'''Modifying Elements:'''
list.sort()	        Sort the items of list in-place.	        my_list = [14, 5, 8]
                                                                my_list.sort()	
                                                                                                [5, 8, 14]
list.reverse()	    Reverse the elements of list in-place.	    my_list = [14, 5, 8]
                                                                my_list.reverse()	
                                                                                                [8, 5, 14]
'''Miscellaneous:'''
list.index(x)	    Return index of first item in list with value x.	my_list = [5, 8, 14]
                                                                        print(my_list.index(14))	Prints "2"
list.count(x)	    Count the number of times value x is in list.	    my_list = [5, 8, 5, 5, 14]
                                                                        print(my_list.count(5))	Prints "3"                                                                                                

Enumerate function:
for for loops
for position, item in enumerate(my_list):
    print('{} {}'.format(position, item))

'''Built in functions that iterate over lists:'''
Function	    Description	                                        Example code	            Example output
all(list)	    True if every element in list is True (!= 0),
                or if the list is empty.	                        print(all([1, 2, 3]))       True
                                                                    print(all([0, 1, 2]))	    False

any(list)	    True if any element in the list is True.	        print(any([0, 2]))          True
                                                                    print(any([0, 0]))	        False

max(list)	    Get the maximum element in the list.	            print(max([-3, 5, 25]))     25	

min(list)	    Get the minimum element in the list.	            print(min([-3, 5, 25]))	    -3

sum(list)	    Get the sum of all elements in the list.	        print(sum([-3, 5, 25]))	    27

List nesting:
List items can be lists themselves
The code my_list = [[5, 13], [50, 75, 100]]

my_list = [ ['a', 'b'], ['c', 'd'], ['e', 'f'] ]
my_list[0][0] = a
my_list[0][1] = b
my_list[1][0] = c
my_list[1][1] = d
my_list[2][0] = e
my_list[2][1] = f

Multidimensional data structure:
Lists with elements of lists all the same legnth

Level of nested lists is arbitrary:
nested_table = [
    [
        [10, 0, 55],
        [0, 4, 16]
    ],
    [
        [0, 0, 1],
        [1, 20, 2]
    ]
]
2x2x2 list

currency = [

        [1.00, 5.00, 10.0], # US Dollars
        [0.75, 3.77, 7.53], # Euros
        [0.65, 3.25, 6.50]  # British pounds
]
for row in currency:
    for cell in row:
        print(cell, end=' ')
    print()

'''Returns'''
1.00 5.00 10.0
0.75 3.77 7.53
0.65 3.25 6.50

'''Iterating through multi-dimensional lists using enumerate()'''
currency = [
   [1, 5, 10 ],  # US Dollars
   [0.75, 3.77, 7.53],  #Euros
   [0.65, 3.25, 6.50]  # British pounds
]
for row_index, row in enumerate(currency):
   for column_index, item in enumerate(row):
       print('currency[{}][{}] is {:.2f}'.format(row_index, column_index, item))
'''Returns'''
currency[0][0] is 1.00
currency[0][1] is 5.00
currency[0][2] is 10.00
currency[1][0] is 0.75
currency[1][1] is 3.77
currency[1][2] is 7.53
currency[2][0] is 0.65
currency[2][1] is 3.25
currency[2][2] is 6.50

'''Printing multi dimensional list with separators'''
user_input= input()
lines = user_input.split(',')

# This line uses a construct called a list comprehension, introduced elsewhere,
# to convert the input string into a two-dimensional list.
# Ex: 1 2, 2 4 is converted to [ [1, 2], [2, 4] ]

mult_table = [[int(num) for num in line.split()] for line in lines]

for row in mult_table:
    print(row[0], end='')
    for col in row[1:]:
        print(' | {}'.format(col), end ='')
    print()

'''returns'''
for input '1 2 3, 2 4 6, 3 6 9'
1 | 2 | 3
2 | 4 | 6
3 | 6 | 9

List Slicing
Slice notation
    used to read multiple elements from a list

my_list = ['practicing', 'with', 'list', 'slicing']

print(my_list[0:3])
print(my_list[1:2])

optional stride argument
nums[0:5:2]

Common list slicing operations:
my_list[start:end]
my_list[start:end:stride]
my_list[start:]
my_list[:end]
my_list[:]

Loops modifying lists:
my_list = [3.2, 5.0, 16.5, 12.25]

for i in range(len(my_list)):
    my_list[ i ] += 5

'''Also'''
# Change negative values to 0
for pos in range(len(nums)):
    if nums[pos] < 0:
        nums[pos] = 0

Removing items from a list while not removing it from the for loop registry
nums1 = [5, 10, 15]
nums2 = [10, 15]

for val in nums1[:]:
    if val in nums2:
        nums1.remove(val)
#creates a copy list of nums1 bc of the [:]
#Iterating over a list and deleting elements from the original list might cause a logic program error

'''incorrect way to do it'''
nums1 = [5, 10, 15]
nums2 = [10, 15]

for val in nums1:
    if val in nums2:
        nums1.remove(val)

List comprehensions:
apply same change to every element in list
new_list = [expression for name in iterable]
    expression to evaluate for each element  in iterable object
    loop variable component to bind the current iteration element
    iterable object container/component to iterate over (list, string, tuple, enumerate, etc)
#Example
my_list = [10, 20, 30]
list_plus_5 = [(i + 5) for i in my_list]

print('New list contains:', list_plus_5)
'''returns'''
New list contains: [15, 25, 35]

#Add 10 to every element:
my_list = [5, 20, 50]
my_list = [(i+10) for i in my_list]
print(my_list)

#Convert every element to a string:
my_list = [5, 20, 50]
my_list = [str(i) for i in my_list]
print(my_list)

#Convert user input into a list of integers:
inp = input('Enter numbers:')
my_list = [int(i) for i in inp.split()]
print(my_list)

#Find the sum of each row in a 2D list:
my_list = [[5, 10, 15], [2, 3, 16], [100]]
sum_list = [sum(row) for row in my_list]
print(sum_list)

#Find the sum of the row with the smallest sum in a 2D table:
my_list = [[5, 10, 15], [2, 3, 16], [100]]
min_row = min([sum(row) for row in my_list])
print(min_row)

List comprehensions create new list objects, while for loops can modidify an existing loop
So theyre not a direct replacement

List Comprehension can be extended with an optional conditional clause that returns a list with only certain elements
new_list = [expression for name in iterable if condition]

'''Example of conditional list comprehension'''
# Get a list of integers from the user
numbers = [int(i) for i in input('Enter numbers:').split()]

# Return a list of only even numbers
even_numbers = [i for i in numbers if (i % 2) == 0]
print('Even numbers only:', even_numbers)
'''returns'''
Enter numbers: 5 52 16 7 25
Even numbers only: [52, 16]
...
Enter numbers: 8 12 -14 9 0
Even numbers only: [8, 12, -14, 0]

Sorting lists:
sort() method
my_list.sort() arranges items from smallest to largest
    will sort strings alphabetically

sorted() method does same thing as sort() but will create a new list instead of modifying existing
#Sorted() example
numbers = [int(i) for i in input('Enter numbers: ').split()]

sorted_numbers = sorted(numbers)

print('\nOriginal numbers:', numbers)
print('Sorted numbers:', sorted_numbers)
'''Returns'''
Enter numbers: -5 5 -100 23 4 5
Original numbers: [-5, 5, -100, 23, 4, 5]
Sorted numbers: [-100, -5, 4, 5, 5, 23]

my_list.sort() and sorted() function shave optional key argument
    key arguments are functions to be applied to each elements before being compared
    str.lower, str.upper, str.capitalize
#Example:
key_sort = sorted(names, key=str.lower)

key= max would allow for the rows to be sorted by the max of the rows
#Example:
my_list = [[25], [15, 25, 35], [10, 15]]

sorted_list = sorted(my_list, key=max)

'''returns'''
Sorted list: [[10, 15], [25], [15, 25, 35]]

possible key arguments:
key = 
    max
    str.lower
    str.upper
    str.capitalize
    max

additional argument: reverse
reverse = True or False

Command line arguments:
imput command line arguments are stored in a list called sys.argv

#Checking for proper number of command line arguments
import sys

if len(sys.argv) != 3:
    print('Usage: python myprog.py name age\n')
    sys.exit(1)  # Exit the program, indicating an error with 1.

name = sys.argv[1]
age = int(sys.argv[2])

print('Hello {}. '.format(name))
print('{} is a great age.\n'.format(age)

Dictionaries:
methods
my_dict.clear()
my_dict.get(key,default)
my_dict1.update(my_dict2)
my_dict.pop(key,default)

Iterating over a dictionary
dict.items() returns a view object that yields key,value tuples
dict.keys() returns a view object that yields dictionary keys
dict.values() returns a view object that yields dictionary values

view objects are not lists so they are not indexed
    my_dict.keys()[0] returns an error
    instead convert it to a list with list()
        list(my_dict.keys())

Dictionary Nesting:
dictionary values can be dictionaries themselves
#Nested dictionary:
students = {}
students ['Jose'] = {'Grade': 'A+', 'StudentID': 22321}

print('Jose:')
print(' Grade: {}'.format(students ['Jose']['Grade']))
print(' ID: {}'.format(students['Jose']['StudentID']))
'''Returns'''
Jose:
 Grade: A+
 ID: 22321


students['Jose']['Grade'] accesses 'jose' in the first dict, then within that dictionary, finds the value of the key 'grade'


Classes:
Grouping related items into objects
object is a grouping of data (variables) and operations that can be performed on that data (functions and methods)
Objects contain variables, functions, and methods all related and relevant to the object

Abstraction/Information hiding
or encapsulation
when a user interacts with an object at high level, allowing fo rlower level interal details to remain hidden

Entire groups of functions can be hidden from the user and only used internally

Abstract Data Type ADT
    data type whose creating and uodate are constrained to specific well defined operations
    a class cant be used to implement an ADT
Abstractions of a car are the gas pedal, steering wheel, brake, gear shifter, infotainment

abstracting = thing/input being used/accessible to user

Python built-in objects
mystr = 'Hello!' the value of the string 'Hello!' is one part of the object
    along with functions to operate on the string str.isdigit() and str.lower()



CLASSES
Grouping Data:
multiple variablesa re freuqently closely related and should thus be treated as one variable with multiple parts
    ex. two variables, hours and minutes can be grouped together in a single variable, time
    class keyword can be used to create a user-defined type of ob ject containing groups of related variables and functions

class ClassName:
    # Statement-1
    # Statement-2
    # ...
    # Statement-N

the object maintains a set of attributes that determines the data and behavior of the class
    ex. this contains two attributes, hours and minutes, whos values are initially 0
    class Time:
    """ A class that represents a time of day """
    def __init__(self):
        self.hours = 0
        self.minutes = 0

Instantiation:
    can be used to define new Time class variable and access that variables attributes
    can be performed by 'calling' the class 
        my_time = Time()
        creates an 'instance' which is an individual object of the given class
__init__ method commonly know as constructor
    responsible for setting up the initial state of the new instance
    has single parameter 'self' that autmatically references the instance being created
    self.hours = 0 within __init__ method to create new attribute 'hours'

Attribute reference operator '.' sometimes called member operator or dot notation
class Time():
    def __init__(self):      
        self.hours = 0                  
        self.minutes = 0                   

time1 = Time()             
time1.hours = 7              
time1.minutes = 15


Can create multiple instanes for a class:
class Time:
    """ A class that represents a time of day """
    def __init__(self):
        self.hours = 0
        self.minutes = 0


time1 = Time()  # Create an instance of the Time class called time1
time1.hours = 7
time1.minutes = 30

time2 = Time()  # Create a second instance called time2
time2.hours = 12
time2.minutes = 45

N before the '.' allows for creation of N class
Attribute is the name following the '.'


#Example of defining a class and using it:
class PatientData:
    def __init__(self):
        self.height_inches = 0
        self.weight_pounds = 0

patient = PatientData()
print('Patient data (before):', end=' ')
print(patient.height_inches, 'in,', end=' ')
print(patient.weight_pounds, 'lbs')


patient.height_inches = int(input())
patient.weight_pounds = int(input())

print('Patient data (after):', end=' ')
print(patient.height_inches, 'in,', end=' ')
print(patient.weight_pounds, 'lbs')


Creating an instance:
instance_name = YourClassName()
cat = Animal()

Referencing an instance
Class Frogs:
    def __init__(self):
        self.frog_type = 0
        self.pop = 0
treefrog = Frogs()
treefrog.frog_type = 5
treefrog.pop = 50000

Creates instance:
treefrog          Then:          treefrog
frog_type = 0                    frog_type = 5
pop = 0                          pop = 50000

Instance methods
    function defined within a class
class Time:
    def __init__(self):
        self.hours = 0
        self.minutes = 0

    def print_time(self): # DEFINING FUNCTION / INSTANCE METHOD
        print('Hours:', self.hours, end=' ')
        print('Minutes:', self.minutes)


time1 = Time()
time1.hours = 7
time1.minutes = 15
time1.print_time() # USING FUNCTION


Calling instance methods:
my_instance.MyMethod(optional_arguments)


__init__ is also a method of the class
__init__ is a 'special method name' indicating that the method implements some special behavior of the class
    special behaviour for __init__ is that it initializes the new instances
    special methods are always identified with __ (double underscore)
    avoid using __ in identifiers to prevent collisions with special method names

for all methods in a class, the first parameter must ALWAYS be self
    for all possible aditional parameters, include them after self

Example of class method:
class PersonInfo:
    def __init__(self):
        self.num_kids=0
# FIXME: Write inc_num_kids(self)
    def inc_num_kids(self):
        self.num_kids +=1
        return self.num_kids

Class and instance object types:
    user defined classes contain additional types of objects: class objects and instance objects
        class object acts as a factory that creates instance objects
        when created by the class object, an _instance object_ is initialized via the __init__ method
    __init__ prefills the instance object

Class and instance objects are namespaces used to group data and functions together

'Class Attribute' is shared amongst all of the instance of that class.
class attributes are defined within the scope of a class

'Instance Attribute' can be unique to each instance
variable value for a specific instance, can differ from init and instance

Typical clas attributes are variables only required by instances for the class
    placing them in the class scope helps reduce possible collisions with other variables or functions in the global scope

#Example
class Time:
    gmt_offset = 0  # Class attribute. Changing alters print_time output
    
    def __init__(self):  # Methods are a class attribute too
        self.hours = 0  # Instance attribute
        self.minutes = 0  # Instance attribute

    def print_time(self):  # Methods are a class attribute too
        offset_hours = self.hours + self.gmt_offset  # Local variable
        print('Time -- %d:%d' % (offset_hours, self.minutes))

'''Referencing default class attributes''':
class Shape:
    default_color = 'yellow'

    def __init__(self):
        self.color = None

a_shape = Shape()
a_shape.color = 'gray'

print(Shape.default_color)
print(a_shape.default_color)
print(a_shape.color)
'''Returns'''
yellow
yellow
gray


Class constructors:
__init__ method is a constructor that can be customized with additional parameters
#EX
    def __init__ (self, star_time, end_time, distance):

When constructing, the additional arguments MUST be passed through to the constructor

Constructor default parameters:
def __init__(self, name, wage=8.25, hours=20):
    self.name = name
    self.wage = wage
    self.hours = hours

Similar to functions, these can be mixed with positional and name-mapped arguments in an instantiation operatuon


Class interfaces:
classes usually contain a set of methods that a programmer interacts with
A 'Class Interface' consists of the methods that a programmer calls to create, modify, or access a class instance
#EX:
class RaceTime:
    def __init__(self, start_time, end_time, distance):
        # ...

    def print_time(self):
        # ...

    def print_pace(self):
        # ...
'''Interfaces: print_time, print_pace'''


Class interfaces may also contain other methods within the class
 def print_time(self):
        total_time = self._diff_time() # Referencing the other method)
        print('Time to complete race: {}:{}'.format(total_time[0], total_time[1]))

    def print_pace(self):
        total_time = self._diff_time() # Referencing the other method
        total_minutes = total_time[0]*60 + total_time[1]
        print('Avg pace (mins/mile): {:.2f}'.format(total_minutes / self.distance))

    def _diff_time(self): # Referenced method definition
        """Calculate total race time. Returns a 2-tuple (hours, minutes)"""

'IMPORTANT'
Internal methods used by the class should start with an underscore in their name
    makes it easier to read. standard practice
Well designed class separates its interface from its implementation


Class customization:
process of defining how a class should behave for some common operations
    such as: printing, accessing attributes, or how instances of that class are compared to each other
to customize, implement intance methods with special method names that the python interpreter recognizes
#EX
    to change how a class instance object is printed, the special __str__() method can be defined
    class Toy:
    def __init__(self, name, price, min_age):
        self.name = name
        self.price = price
        self.min_age = min_age

    def __str__(self):
        return ('{} costs only ${:.2f}. Not for children under {}!'
                .format(self.name, self.price, self.min_age))

truck = Toy('Monster Truck XX', 14.99, 5)
print(truck)
'''returns'''
Monster Truck XX costs only $14.99. Not for children under 5!

using the __str__() special method allows for the customizing of how it is printed, eliminating the need to specify format in each print function
    this makes it so the instance is stored as a custom string defined above. 
    all the class atributes and instance atributes are still accessible, but if printed it will be formatted
use 'return' instead of print because it needs to be a str object to be printed later
    not necessarily a function to be printed from at that moment



#COOL PRITNING SHIT
#change print string but not how the name
#str method
#printing instance
Customize how an instance name is printed:
__str__ method:
def __str__(self):
    return ('{} is supposed to be printed like this'.format(self.my_variable))
'''Makes it so that if you print(my_instance.my_variable),
instead prints in this format^
but will allow you to still treat it as a class instance
'''
'''if you return instance = MyClass(x,y), you can print(instance) and it will be formatted as such
not formatted as python object name
but you can also run operands on the instance without it being a string
'''



Operator Overloading
    with built-in operators like < > = + - * **

#EX
    Overloading the less than operator of the time class by defining a method with __lt__ special method name
class Time:
    def __innit__(self):
        #Body statements
    def __lt__(self, other):
        if self.hours < other.hours:
            return True
        elif self.hours == other.hours:
            if self.minutes < other.minutes:
                return True
        return False

"""In the above program, the Time class contains a definition for the __lt__ method, which overloads the < operator. 
When the comparison t < min_time is evaluated, the __lt__ method is automatically called. 
The self parameter of __lt__ is bound to the left operand, t, and the other parameter is bound to the right operand, min_time. 
Returning True indicates that t is indeed less-than min_time, and returning False indicates that t equal-to or greater-than min_time."""

Rich comparison methods examples:
'Rich comparison method'	#Overloaded operator
__lt__(self, other)	        less-than (<)
__le__(self, other)	        less-than or equal-to (<=)
__gt__(self, other)	        greater-than (>)
__ge__(self, other)	        greater-than or equal-to (>=)
__eq__(self, other)	        equal to (==)
__ne__(self, other)	        not-equal to (!=)


More operator overloading: Classes as Numeric Types
Numeric operators such as +, -, *, and / can also be overloaded using class customization techniques
can allow for subtracting arbitrarily around different bases and other stuff!

overloaded operators will only be applied when the operator is used between two instances


To hanlde subtraction of arbitrary object types:
built in function isinstance() function can be used
    returns True of False depending on whether a given variable matches a given type


The __sub__ function is modified below to first check the type of the right operand, 
and subtract an hour if the right operand is an integer, or find the time difference 
if the right operand is another Time24 instance:
#EX 
def __sub__(self, other):
    if isinstance(other, int): # right op is integer
        return Time24(self.hours - other, self.minutes)

    if isinstance(other, Time24):  # right op is Time24
        if self > other:
            larger = self
            smaller = other
        else:
            larger = other
            smaller = self

        hrs = larger.hours - smaller.hours
        mins = larger.minutes - smaller.minutes
        if mins < 0:
            mins += 60
            hrs -=1

        # Check if times wrap to new day
        if hrs > 12:
            hrs = 24 - (hrs + 1)
            mins = 60 - mins

        # Return new Time24 instance
        return Time24(hrs, mins)

    print('{} unsupported'.format(type(other)))
    raise NotImplementedError

Testing this code^
'Operation'	            #Result
t1 - t2	                Difference between t1, t2
t1 - 5	                t1 minus 5 hours.
t1 - 5.75	            "float unsupported"
t1 - <other_type>	    "<other_type> unsupported"

Numeric operator overloading:
'Method'	                #Description
__add__(self, other)	    Add (+)
__sub__(self, other)	    Subtract (-)
__mul__(self, other)	    Multiply (*)
__truediv__(self, other)	Divide (/)
__floordiv__(self, other)	Floored division (//)
__mod__(self, other)	    Modulus (%)
__pow__(self, other)	    Exponentiation (**)
__and__(self, other)	    "and" logical operator
__or__(self, other)	        "or" logical operator
__abs__(self)	            Absolute value (abs())
__int__(self)	            Convert to integer (int())
__float__(self)	            Convert to floating point (float())



Memory allocation and Garbage collection
Python automatically allocates memory for the programmer
not all languages will

objects are also delocated automatically by the Python runtime
    when an object is no longer referenced by any variables, the object becomes  a candidate for deallocation
reference count is an integer counter that represents how many variables reference an object
    when RC == 0, the object is no longer referenced



Scientific Computing with Numpy and SciPy

import numpy.polynomial as npoly
roots = npoly.Polynomial([-2,0,1]).roots()
    x^2 - 2
    counting up in degree in x starting at x^0

roots = npoly.Polynomial([36,-72,47,-12,1])
    x^4-12x^3+47x^2-72x+36

returns imaginary roots as well!

import scipy.optimize as so
import numpy as np
def f(x):
    return x*np.exp(-x*x) + x**(-0.67) - 1

def f(x):
    return x**0.5 + x + -3
root = so.fsolve(f,x0=2)
print(root[0], f(root[0]))


for 
3x+5y-7z=3
-x-y+10z=-4
-4x+8y+2z=3
import numpy.linalg as nl
import numpy as np
A = np.array([[3,5,-7],[-1,-1,10],[-4,8,2]])
b = np.array([3.-4,3])
x = nl.solve(A,b)

print(x)
print(np.matmul(A,x),b)
print(np.allclose(np.matmul(A,x),b))

[-0.41781364 0.26988636  -0.41477273]
[ 3. -4. 3.] [ 3 -4 3]
True



for an unknown list of data in 2 columns. presumably x,y oriented

import numpy as np
import matplotlib.pyplot as plt
x,y = np.loadtxt('some_data.dat',unpack=True)
plt.xlabel('x (column1)')
plt.ylabel('y (column2)')
plt.plot(x,y,'ko',label='some_data.dat')
plt.legend()
plt.show()

scipy has optimization for curve fitting
from scipy.optimize import curve_fit

def expdec(x,a,tau):
    return a*np.exp(-x/tau)

def biexpdec(x, a1, tau1, a2, tau2):
    return expdec(x,a1,tau1)+expdec(x,a2,tau2)

def getR2(filename, functionname, *pguess):
    x,y = np.loadtxt(filename,unpack=True)
    params,cov = curve_fit(functionname,x,y,p0=pguess,maxfev=2500)
    yfit = functionname(x,*params)
    r2 = 1-np.sum((y-yfit)**2)/np.sum((y-np.mean(y))**2)
    return r2, params

r2_exp, params_exp = getR2('some_data.dat',expdec,[1.0,1.0])
print('Single-exponential R^2 is {:.6f}'.format(r2_exp))





''''
ECE 105 Notes:
3/30/21

Two lowest lab scores dropped
Lowest HW score dropped
No final exam'''

import numpy as np
my_array = np.array(my_list)

accessing 2D/3D numpy array items
Normal list: A[1][2]

'''Indexing Numpy array'''
For Numpy:
A[1,2]
'''Note the comma instead of using seperate brackets'''


'''Slice notation'''
Slice notation in numpy:
all collumns with specified row
A[1,:]

All rows with specified column
A[:,1]

without numpy, for loop is needed
[row[1] for row in A]


'''Diagonal'''
Diagonal elements in numpy:
A.diagonal()

Without Numpy:
[A[i][i] for in in range len(A)]


'''Accessing in reverse'''
np.fliplr(A)
np.flipud(A)
#lr stands for left-right
#prints items of each row in reverse, but rows are printed in standard order
A = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(np.flip(A))
[[3,2,1]
 [6,5,4]
 [9,8,7]]

print(np.flipud(A))
[[7,8,9]
 [4,5,6]
 [1,2,3]]


'''Anti diagonal'''
'''reverse diagonal'''
np.fliplr(A).diagonal()
#Composing operations in numpy without introducting intermediate variables or arrays as placeholders


'''Counting num rows and collumns'''
A = np.array([[1,2,3],[4,5,6],[7,8,9],[0,0,0]])
A.shape # returns a tuple
(4, 3)

Index the tuple to get the num of rows(0) or columns(1)


'''Dividing arrays into sections'''
'''Splitting arrays, chopping, cutting'''
A = np.array([[1,2,3],[4,5,6],[7,8,9],[0,0,0]])
top, bottom = np.split(A,2)
                        #Splits array "A" into "2" part
#First section is stored in 'top', second is stored in 'bottom'
#SPLITS TOP TO BOTTOM


'''Split by left and right'''
A = np.array([[1,2,3,0],[4,5,6,0],[7,8,9,0]])
left, right = np.hsplit(A,s)
        #Note the 'h' in hsplit() function
#SPLITS LEFT TO RIGHT!
'''For both split functions:'''
'''MUST BE EQUAL DIVISION FOR PROPER EXECUTION'''
'''Will throw error if division isnt a whole number'''
#creates new arrays into specified variables to the right
    '''must have equal division'''
#For unknown number of rows or columns, use logic below.
    #Each array is made into a subarray of the 1 specified variable

'''Split array into however many rows it has'''
A = np.array([[1,2,3],[4,5,6],[7,8,9],[0,0,0]])
rows = np.split(A,A.shape[0])
for row in rows:
    print(row[0])
    #NEEDS the '[0]' because 'rows' is a 2D list with each item being an array

'''Split array into however many columns it has'''
A = np.array([[1,2,3,0],[4,5,6,0],[7,8,9,0]])
columns = np.hsplit(A,A.shape[1])
for column in columns:
    print(column[:,0])
    #NEEDS the '[:,0]' because 'columns' is a 2D list of 1D arrays


'''Transpose'''
#Changes rows into columns and columns into rows
np.transpose(A)
'''much easier than nested list comprehension'''


'''Convert array into Python list'''
#array to list
#array back to list
newlist = A.tolist()



'''Constructor arrays'''
A = np.zeros(5) #argument is length of 1D array
#[0. 0. 0. 0. 0.]

r,c = 3,4
B = np.zeros((r,c) dtype=int)
#[[0 0 0 0]
# [0 0 0 0]
# [0 0 0 0]]

length, val = 5, 6
C = np.full(length,val)
#[6 6 6 6 6]


'''Filtering via list comprehension'''
import sympy.ntheory.prumetest as pt
length = 9
numbers = arange(1,length+1)
print [e for e in numbers if pt.isprime(e)]

#nums = [1,2,3,4,5,6,7,8,9]
#primes: 2,3,5,7

'''Filtering via boolean indexing'''
import numpy as np
import sympy.ntheory.primetest as pt
a = np.arange(1,10)
b = [pt.isprime(e) for e in a]
print a[b] #boolean indexing

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = [False, True, True, False, True, False, True, False, False]
#returns values of 'a' correspond to True values in 'b'
a[b] = 2, 3, 5, 7

#since 'b' values are dependant on boolean logic described above, it determines that values of 'a' are printed


'''Convert numpy array to string via np.array2string(a)'''
a = np.arange(1,10)
s = np.array2string(a)
#WILL LEAVE BRACKETS FROM ARRAY FORMATTING IN STRING
print(s) returns '[1,2,3,4,5,6,7,8,9]' however it is in the str class

'''Type command'''
will return the data object type:
l = []
s = ''
a = np.zeroes((3,3), dtype=int)
type(l) returns 'list'
type(s) returns 'str'
type(a) returns 'np.ndarray'


'''Ternary Operator: value1 if condition else value2'''
def c1(b):
    return 1 if b else 0
              ^Ternary operator
'Old way'
def c2(b):
    if b: return 1
    else: return 0

'''String membership: use keywod 'in' to check membership via target in test'''
target = ’i’
test1 = ’team’
test2 = ’individual’
result1 = target in test1 # string test keyword: in
result2 = target in test2 # gives True if present else False
answer1 = ’is an’ if result1 else ’is no’
answer2 = ’is an’ if result2 else ’is no’
print("there {} {} in {}".format(answer1 , target , test1))
print("there {} {} in {}".format(answer2 , target , test2))


'''Selecting random choice from a lisy via random.choice(list)'''
#Must import random
import random
flavors = [’vanilla’, ’chocolate’, ’strawberry’]
for _ in range(10): # underscore is a throwaway variable
    print(random.choice(flavors))
#underscore just for repeating the code block in the for list 10 times. simple counting method
#underscore is typical for python coders to say that the iterable variable is not being used


'''Use of any() and all() on boolean lists'''
# "any": exists one or more true , "all": all true
blists = [
[False , False , False], # any: false , all: false
[True , False , True], # any: true , all: false
[True , True , True]] # any: true , all: true

def bl2s(bl): # convert binary list to T/F string
    return ’’.join(["T" if b else "F" for b in bl])
print("list\tany?\tall?")
for bl in blists:
    print("{}\t{}\t{}".format(bl2s(bl),any(bl),all(bl)))

'''Matricies: put all rows, columns, diagonals into array'''
import numpy as np
A = np.array([[2,7,6],[9,5,1],[4,3,8]])
Ar = A.tolist()
Ac = np. transpose (A).tolist ()
Ad = [A.diagonal ().tolist (),np.fliplr(A).diagonal ().tolist ()]
Arcd = np.array(Ar + Ac + Ad) #Concantenation of lists into a single list. the create an array of that list
print("{}".format(Arcd))
[[2 7 6]
[9 5 1]
[4 3 8]
[2 9 4]
[7 5 3]
[6 1 8]
[2 5 8]
[6 5 4]]

for rcd in Arcd:
print("sum of {} is {}".format(rcd ,np.sum(rcd)))
sum of [2 7 6] is 15
sum of [9 5 1] is 15
sum of [4 3 8] is 15
sum of [2 9 4] is 15
sum of [7 5 3] is 15
sum of [6 1 8] is 15
sum of [2 5 8] is 15
sum of [6 5 4] is 15

'''range vs np.arange vs np.linspace'''
functions to enumerate values
enumeration
'''range()'''
range(start,stop,step) #of dtype 'range'. can be cast as list
#dtype default is int

'''np.arange()'''
np.arange(start,stop,step) #not 'range' object, is numpy.ndarray object
#dtype default is int

'''np.linspace()'''
np.linspace(start,start,num) #'numpy.ndarray' object type
#INCLUDE STOPPING VALUE NOT -1 OF STOP, inclusive of stop value
#num is number of values
#returns floats as default dtype

'''List comprehension'''
will make a list for a bunch of values
[line for line in readerDJIA]
^each list val
    usually have some operation but this just allows to make a list of each element


'''
MATPLOTLIB
'''
import matplotlib.pyplot as plt
#standard form

graphing for (x/(1+x)) <= log(1+x) <= x over x >= 0
# illustrate matplotlib plot function
import matplotlib .pyplot as plt
import numpy as np
# create a figure
fig = plt.figure ()
# add axes (111: subplot 1 of 1 x 1 grid of subplots)
ax = fig. add_subplot (111)
# create 100 points between 0 and 2
x = np.linspace(0, 2, 100)
# add 3 functions: x, log(1+x), x/(1+x)
ax.plot(x, x)
ax.plot(x, np.log(1+x))
ax.plot(x, x/(1+x))
# save the plot as a pdf
plt.savefig("Example4aOutput.pdf")
# show the plot to the screen
plt.show ()


'''Alternate way of plotting matplotlib but without subplot command'''
# illustrate matplotlib plot function
import matplotlib .pyplot as plt
import numpy as np
# create a figure
fig = plt.figure ()
# create 100 points between 0 and 2
x = np.arange(0, 2.001 , 0.02)
# add 3 functions: x, log(1+x), x/(1+x)
#Uses plt.plot bc theres only 1 plot for now
plt.plot(x, x)
plt.plot(x, np.log(1+x))
plt.plot(x, x/(1+x))
# save the plot as a pdf
plt.savefig("Example4bOutput.pdf")
# show the p


'''Example2 DJIA and NASDAW data'''
# import csv library to read csv files
import csv
# create a file pointer fp to read the DJIA csv file
with open(’Example5 -DJIA.csv’, ’r’) as fpDJIA:
    # create a csv reader for file pointer fpDJIA
    readerDJIA = csv.reader(fpDJIA , delimiter=’,’)
    # use the csv reader to read lines from file
    dataDJIA = [line for line in readerDJIA]
print("DJIA data ({} entries)".format(len(dataDJIA)))
print(dataDJIA[0])
print(dataDJIA[1])
print(dataDJIA[-1])
# repeat for NASDAQ csv file
with open(’Example5 -NASDAQ.csv’, ’r’) as fpNASDAQ:
    readerNASDAQ = csv.reader(fpNASDAQ , delimiter=’,’)
    dataNASDAQ = [line for line in readerNASDAQ]
print("NASDAQ data ({} entries)".format(len( dataNASDAQ )))
print( dataNASDAQ[0])
print( dataNASDAQ[1])
print( dataNASDAQ[-1])

DJIA data (68 entries)
[’Date’, ’Open’]
[’1/2/20’, ’28638.9707’]
[’4/7/20’, ’23537.4395’]
NASDAQ data (68 entries)
[’Date’, ’Open’]
[’1/2/20’, ’9039.4600’]
[’4/7/20’, ’8129.9863’]


'''Matplotlib DJIA and NASDAW data'''
'''DATE CONVERSION''' dates, time, day month year
import csv
# import datetime package to manipulate date strings
import datetime as dt
# read in the data (same as Example5a.py)
with open(’Example5 -DJIA.csv’, ’r’) as fpD:
    dataD = [line for line in csv.reader(fpD , delimiter=’,’)]
with open(’Example5 -NASDAQ.csv’, ’r’) as fpN:
    dataN = [line for line in csv.reader(fpN , delimiter=’,’)]
# remove first element of both lists , holding column headers
dataD.pop(0)
dataN.pop(0)
# use library datetime function striptime for date strings
x = [dt.datetime.strptime(e[0], ’%m/%d/%y’) for e in dataD]
# convert opening trading volume strings into floats
yD = [float(entry[1]) for entry in dataD]
yN = [float(entry[1]) for entry in dataN]
# print first , last entries of both DJIA and NASDAQ
print("Date\t\t\tDJIA\t\tNASDAQ")
print("{}:\t{}\t{}".format(x[0],yD[0],yN[0]))
print("{}:\t{}\t{}".format(x[-1],yD[-1],yN[-1]))

Date DJIA NASDAQ
2020-01-02 00:00:00: 28638.9707 9039.46
2020-04-07 00:00:00: 23537.4395 8129.9863

Actually plot data
import csv
import datetime as dt
import matplotlib .pyplot as plt
# read in the data (same as Example5b.py)
with open(’Example5 -DJIA.csv’, ’r’) as fpD:
    dataD = [line for line in csv.reader(fpD , delimiter=’,’)]
with open(’Example5 -NASDAQ.csv’, ’r’) as fpN:
    dataN = [line for line in csv.reader(fpN , delimiter=’,’)]
# process data (same as Example5b.py)
dataD.pop(0), dataN.pop(0) # remove column headings
x = [dt.datetime.strptime(e[0], ’%m/%d/%y’) for e in dataD]
yD = [float(entry[1]) for entry in dataD] # DJIA volume
yN = [float(entry[1]) for entry in dataN] # NASDAQ data
# plot the data using the matplotlib plot_date command
plt.figure ()
plt.plot_date (x, yD) # plot the DJIA data
plt.plot_date (x, yN) # plot the NASDAQ data
plt.xticks( rotation=45) # rotate x-axis labels for visibility
plt. tight_layout () # tight layout to avoid cutoff of x-labels
plt.savefig("Example5cOutput.pdf")

#plot_date is built in that allows you to plot data with the axis as date


'''Martingale betting'''
import numpy as np
def play (): #play red-black on American roulette wheel
    return np.random.choice([’w’,’l’], p=[18/38 ,20/38])
# martingale: double bet (up to current wealth) on last loss
def martingale (last_out , last_bet , cur_w):
    return min([cur_w , 2 * last_bet]) if last_out == ’l’ else 1
w_init ,w_stop ,w_goal = 100 ,0,200 # start $100 , stop $0 or $200
w,b,o = [w_init],[],[] # wealth , bet, outcome for each play
# play the Martingale , stopping at w_stop or w_goal
while not w or (w[-1] > w_stop and w[-1] < w_goal):
    bet = martingale (o[-1], b[-1], w[-1]) if o else 1
    b.append(bet)
    o.append(play ())
    w_new = w[-1] + bet if o[-1] == ’w’ else w[-1] - bet
    w.append(w_new)
b.append(0), o.append(’-’) # no bet or play after finish
# print the outputs
print("t\tw\tb\to")
for t in range(len(w)):
    print("{}\t{}\t{}\t{}".format(t,w[t],b[t],o[t]))

'''map() method'''
map(int, my_list)
casts the 'int' method to each value of my_list
usually is converted to a last after using map function:
    second_list = list(map(int,my_list))
converts each value in my_list to an int


"""Linear Regression"""
best linear predictor
plot values with plt.scatter(x.y)

#Label 50 states at appropriate datat points
[plt.annotate(l,(wv,yv)) for l,xv,yv in zip(pt_lbls, x, y)]

#data truncation
less than xmax and ymax
dt = [r for r in data if int(r[1])<xmax and int(r[2])<ymax]

finding regression lines:
array: z
np.mean(z)
np.std(z) standard deviation
np.cov(x,y) returns 2x2 array:
    [ [sx^2,  sx,y]
      [sx,y,  sy^2] ]
np.corrcoeff(x,y) returns 2x2 array:
    [ [1,    rx,y]
      [rx,y,    1]]]

def reg_coeff(x,y):
    m = np.corrcoef(x,y)[0][1] * np.std(y) / np.std(x)
    b = np.mean(y) - m * np.mean(x)
    return m, b

def plot_regression:
    m, b = reg_coeff(x,y)
    regressionline = np.poly1d((m,b))
    plt.plot(x, regressionline(x), '-r')
'thats how its done'
'regressionline is a function that we created'

def mean_error(x, y, m, b):
    return np.mean([(yi-(m*xi*+b))** for xi,yi in zip(x,y)])

def coef_det(x, y, m, b): #or R^2 value
    return 1 - mean_error(x, y, m, b) / np.var(y)



'''POLYFIT'''
numpy.polyfit in SciPy:
np.polyfit(x, y, deg, rcond=None, full=False, w=None, cov=False)

'regression lines with polyfit'
c = np.polyfit(x, y, 1)
regressionline = np.poly1d(c) 
etc



'''Power Laws'''
y = bx^m
appears linear on log scales
x>=1 typically
m < 0 typically
b > 0 typically
logy = mlogx+ logb
similar to y = mx + b
power functions are a linear relationship within logorithmic variables

plt.loglog(x,y) # takes log of both x and y values to plot


'''Rank plots'''
Pop of states and pop of cities

def plot_data (y, xlbl , ylbl , title , filename):
    x = range(1,len(y)+1)
    plt.figure() # create figure (canvas)
    plt.scatter(x, y) # add scatter plot
    plt.xlim(1,len(y)+1)
    plt.ylim(y[-1],y[0])
    plt.grid(True , which=’both’)
    plt.xscale(’log’)
    plt.yscale(’log’)
    plt.xlabel(xlbl) # add x label
    plt.ylabel(ylbl) # add y label
    plt.title(title) # add title
    plt.savefig(filename) # save figure
    plt.show() # show figure


"Pareto's Law"
'80% of land owned by 20% of pop'
import matplotlib .pyplot as plt
n = 10 # number of data points
x = range(1,n+1) # x values are 1,... ,n
b = 100 # y-intercept
m = -2 # slope
y = [b * pow(xv ,m) for xv in x]

plt.figure()
plt.bar(x,y,0.15)
plt.title("linear scale: m = {}, b = {}".format(m,b))
plt.xlabel(’x’)
plt.ylabel(’y’)
plt.savefig("Example5a.pdf")
plt.show()

'''On a loglog scale:'''
import matplotlib .pyplot as plt
n = 10 # number of data points
x = range(1,n+1) # x values are 1,... ,n
b = 100 # y-intercept
m = -2 # slope
y = [b * pow(xv ,m) for xv in x]

plt.figure()
plt.loglog(x,y,marker=’o’)
plt.title("log-log scale: m = {}, b = {}".format(m,b))
plt.xlabel(’x’)
plt.ylabel(’y’)
plt.savefig("example5b.pdf")
plt.show()




'''Regression Power Laws'''
X = (logx1,...,logxn)
    X = list(map(np.log, x))
Y = (logy1,...,logyn)
    Y = list(map(np.log, y))

m, bl = reg_coef(X,Y)
b = e^bl
import csv
import numpy as np
import matplotlib .pyplot as plt
def reg_coef(x, y):
    m = np.corrcoef(x,y)[0][1] * np.std(y) / np.std(x)
    b = np.mean(y) - m * np.mean(x)
    return m, b

def mean_error (x, y, m, b):
    return np.mean([(yi-(m*xi+b))**2 for xi ,yi in zip(x,y)])

def coef_det(x, y, m, b):
    return 1 - mean_error (x, y, m, b) / np.var(y)

def get_data( data_filename ):
    with open(data_filename , ’r’) as fp:
        data = [line for line in csv.reader(fp , delimiter=’,’)]
    return np.array(data)[:,0]

def process_data (data):
    return list(map(int, data))

def power_law (x, m, b):
    return b * x**m

"""plotting with power regression laws"""
def plot_data (y, xlbl , ylbl , title , filename):
    x = range(1,len(y)+1)
    plt.figure() # create figure (canvas)
    plt.scatter(x, y) # add scatter plot
    plt.xlim(1,len(y)+1)
    plt.ylim(y[-1],y[0])
    X = list(map(np.log , x))
    Y = list(map(np.log , y))
    m, b = reg_coef (X, Y)
    plt.plot(x, power_law (x, m, np.exp(b)), ’-r’)
    plt.grid(True , which=’both’)
    plt.xscale(’log’)
    plt.yscale(’log’)
    plt.xlabel(xlbl) # add x label
    plt.ylabel(ylbl) # add y label
    rsq = coef_det(X,Y, m, b)
    rq = 'y=b x^m, m={:.3f}, b={:.0f}, R2={:.3f}'.format(m,np.exp(b),rsq)
    plt.title(title+rq) # add title
    plt.savefig(filename) # save figure


'''Using numpy whenever possible will help make code faster and cleaner'''

'''np.where''' where method
np.where(cond(x), x1, x2) returns an array with value x1[i] if cond(x) is true, ense x2[i]

import numpy as np
n = np.arange(-4,5) # (-4,-3,... ,3,4)
print(n)
print(np.where(n > 0, -2, 2))
print(np.where(n > 0, -n, n))
print(np.where(n > 0, -2*n, 2*n))

#returns
[-4 -3 -2 -1 0 1 2 3 4]
[ 2 2 2 2 2 -2 -2 -2 -2]
[-4 -3 -2 -1 0 -1 -2 -3 -4]
[-8 -6 -4 -2 0 -2 -4 -6 -8]

'''Timeit'''
timeit.timeit("f(x)", setup=str, numer=number_of_times_to_call)

import timeit # needed for timing function
def fac(n): # standard recursion for factorial
    return n * fac(n-1) if n > 0 else 1

arg = 5 # argument to function to be tested
N = 1000000 # number of times to call wrapper for sum time
M = 10 # number of measurements of sum time
def t(): return fac(arg) # wrapper test function
str = "from __main__ import t"
# call wrapper function
T = [timeit.timeit("t()",setup=str,number=N) for _ in range(M)]
print(’time(s): arg={}, N={}, M={}:’.format(arg ,N,M))
[print(’{:.3f}’.format(e)) for e in T]

#returns
time(s): arg=5, N=1000000 , M=10:
1.324
1.313
1.358
1.324
1.318
1.354
1.289
1.251
1.301
1.253



"""Vectorization"""
essential for efficient plotting

min(x,y) doesnt vectorize correctly for python lists but fine for nd.arrays

x = [1,4,9]
y = [3,5,7]
z = [0,5,10]
# min of two scalars is the smaller of the scalars
print("min({},{}) = {}".format(2,4,min(2,4)))
# min of one list is the smallest value in the list
print("min({}) = {}".format(x,min(x)))
# default min of two lists is list with smallest first element
print("min({},{}) = {}".format(x,y,min(x,y)))
print("min({},{}) = {}".format(x,z,min(x,z)))

'''returns'''
min(2,4) = 2
min([1, 4, 9]) = 1
min([1, 4, 9],[3, 5, 7]) = [1, 4, 9] #python does not take min of each element but returns list with lowest i0
min([1, 4, 9],[0, 5, 10]) = [0, 5, 10]

'''Solution?''':
np.minimum()

x,y,z are numpy arrays!
print("min({},{}) = {}".format(x,y,np.minimum(x,y)))
print("min({},{}) = {}".format(x,z,np.minimum(x,z)))

'''returns'''
min([1 4 9],[3 5 7]) = [1 4 7]
min([1 4 9],[ 0 5 10]) = [0 4 9]



'''np.meshgrid(x,y)'''
x = (1, 2, 3, 4) and y = (7, 8, 9)
np.meshgrd(x,y) will return mx and my
mx only holds x values and my holds only y values
mx:
[[1 2 3 4]
[1 2 3 4]
[1 2 3 4]]
my:
[[7 7 7 7]
[8 8 8 8]
[9 9 9 9]]


'''Matplotlib in 3D!'''
import numpy as np
import matplotlib .pyplot as plt
x = [1,2,3,4] # four x-values
y = [7,8,9] # three y-values
mx ,my = np.meshgrid(x,y) # meshgrid(x,y)
print(mx) # three rows of x
print(my) # four columns of y
# use mx, my to plot all pairs (x,y)
plt.figure ()
# plt.plot for 2d-arrays mx, my plots the element -wise pairs
# i.e., all possible combinations (x,y)
# for x in [1,2,3,4] and y in [7,8,9]
# marker=’o’, linestyle=’none’ just plots the points
plt.plot(mx ,my ,marker=’o’,color=’b’,linestyle=’none’)
plt.xlabel(’x’)
plt.ylabel(’y’)
plt.xticks(x) # set x-axis ticks to be [1,2,3,4]
plt.yticks(y) # set y-axis ticks to be [7,8,9]
plt.savefig("Example2jOutput.pdf")
plt.show ()

vmin ,vmax ,vnum = -2.0, +2.0, 9
v = np.linspace(vmin ,vmax ,vnum) # create vnum = 9 points
mx ,my = np.meshgrid(v,v)
plt.figure ()
ax = plt.gca () # get current axes from plot , needed below
ax. set_aspect (’equal’) # set plot aspect ratio to be one
plt.plot(mx ,my ,marker=’o’,color=’b’,linestyle=’none’)
plt.xlabel(’x’)
plt.ylabel(’y’)
plt.savefig("Example2kOutput.pdf")
plt.show ()

def f(x,y): # standard Gaussian (normal) PDF
return np.exp(-(np.power(x,2) + np.power(y,2))/2)/(2*np.pi)
vmin ,vmax ,vnum = -2.0, +2.0, 9 # use vnum = 9 for 9 points
v = np.linspace(vmin ,vmax ,vnum) # use linspace with vnum
mx ,my = np.meshgrid(v,v)
mz = f(mx ,my) # vectorization
np. set_printoptions ( precision=3,suppress=True) # format print
print(v) # print the values used for both x and y
print(mz) # print the 2d-array of values f(x,y)
plt.figure()
ax = plt.gca() # get current axes from plot , needed below
ax. set_aspect (’equal’) # set plot aspect ratio to be one
plt.imshow(mz) # simply plots a 2d-array of numbers using color
plt.xlabel(’x’)
plt.ylabel(’y’)
plt.savefig("Example2lOutput.pdf") #HEATMAP
plt.show()

def f(x,y): # standard Gaussian (normal) PDF
return np.exp(-(np.power(x,2) + np.power(y,2))/2)/(2*np.pi)
vmin ,vmax ,vnum = -2.0, +2.0, 101 # note we now use 101 values
v = np.linspace(vmin ,vmax ,vnum) # use linspace with vnum
mx ,my = np.meshgrid(v,v)
mz = f(mx ,my) # vectorization
plt.figure ()
ax = plt.gca () # get current axes from plot , needed below
ax. set_aspect (’equal’) # set plot aspect ratio to be one
cp = plt.contour(mx , my , mz) # create contour plot
plt.clabel(cp , inline=True , fontsize=10) # label contours
plt.xlabel(’x’)
plt.ylabel(’y’)
plt.savefig("Example2mOutput.pdf") #CONTOUR
plt.show ()

from mpl_toolkits .mplot3d import Axes3D # for 3d surface plot
def f(x,y): # standard Gaussian (normal) PDF
return np.exp(-(np.power(x,2) + np.power(y,2))/2)/(2*np.pi)
vmin ,vmax ,vnum = -2.0, +2.0, 101
v = np.linspace(vmin ,vmax ,vnum)
mx ,my = np.meshgrid(v,v)
mz = f(mx ,my) # vectorization
plt.figure()
ax = plt.axes( projection=’3d’) # specify plot axes to be 3d
ax.plot_surface(mx , my , mz , cmap=’viridis’)
ax.set_xlabel(’x’) # above cmap=’viridis’ is a color map
ax.set_ylabel(’y’)
ax.set_zlabel(’f(x,y)’)
ax.set_title(’standard normal (Gaussian) bivariate PDF’)
plt.savefig("Example2nOutput.pdf") #3D GRAPH BABY
plt.show()



'''Signals, waveforms, approximations'''
signals: functions of time, sin(t)
periodic signals: from specified times. in ECE105: -pi, pi

step functions
H(t) = 0, t<1
       1, t>=1



import numpy as np
import matplotlib .pyplot as plt
# define the unit step function
def u(t): return np.where(t >= 0, 1, 0)
# create the t-values
# [-1.0,-0.9,... ,9.9,10.0]
tmin , tmax , tnum = -1, 10 , 111
t = np.linspace(tmin , tmax , tnum)
# compute the three functions
u1 = u(t) # vectorization of unit step
u2 = u(t-5) # unit step with shift
u3 = u(t-3) - u(t-7) # unit step combination
plt.figure ()
# use subplots to create multiple plots
# ax1, ax2, ax 3 are the axes for the three subplots
f, (ax1 , ax2 , ax3) = plt.subplots(nrows=3, sharex=True)
plt. tight_layout () # improves spacing betweens subplots
ax1.plot(t,u1) # add the first subplot
ax1. set_title (’u(t)’) # set the first title
ax2.plot(t,u2) # add the second subplot
ax2. set_title (’u(t-5)’) # set the second title
ax3.plot(t,u3) # add the third subplot
ax3. set_title (’u(t-3) - u(t-7)’) # set the third title
plt.savefig("Example3bOutput.pdf")
plt.show()




'''Squarewave'''
original period = 2pi
scale it to 2 by *pi

import numpy as np
import matplotlib .pyplot as plt
import scipy.signal as ss # scipy.signal library
tmin , tmax , tnum = -5, 5, 101
t = np.linspace(tmin , tmax , tnum)
w1 = ss.square(t) # period 2 pi, values {-1,+1} #square for squarewave
w2 = ss.square(np.pi * t) # period 2, values {-1,+1}
w3 = (1 + ss.square(np.pi * t))/2 # period 2, values {0,1}
f, (ax1 , ax2 , ax3) = plt.subplots(nrows=3, sharex=True)
ax1.plot(t,w1)
ax2.plot(t,w2)
ax3.plot(t,w3)
ax1. set_title (’scipy.signal.square period 2pi, values {-1,+1}’)
ax2. set_title (’scipy.signal.square period 2, values {-1,+1}’)
ax3. set_title (’scipy.signal.square period 2, values {0,1}’)
plt.savefig("Example3gOutput.pdf")
plt.show ()


'''Fourier series signal approximations'''
comparing step function to Fourier series signal approximations:
import numpy as np
import matplotlib .pyplot as plt
import scipy.signal as ss # scipy.signal library
tmin , tmax , tnum = -5, 5, 101
t = np.linspace(tmin , tmax , tnum)
w0 = (1 + ss.square(np.pi * t))/2 # period 2, values {0,1}
s1 = 4/(1 * np.pi) * np.sin(1 * np.pi * t) # term #1
s2 = 4/(3 * np.pi) * np.sin(3 * np.pi * t) # term #2
s3 = 4/(5 * np.pi) * np.sin(5 * np.pi * t) # term #3
S1 = s1 # approximation 1: first term
S2 = s1 + s2 # approximation 2: sum of first two terms
S3 = s1 + s2 + s3 # approximation 3: sum of first three terms
w1 = (1+S1)/2 # adjust values from {-1,+1} to {0,1}
w2 = (1+S2)/2
w3 = (1+S3)/2



Fibonacci Via recursion:
def f(n):
    if n<=2: return 1
    else: return f(n-1) + f(n-2)

# compute the first nmax Fibonacci numbers
nmax = 25
n = range(1,nmax+1)
f = [f(nv) for nv in n]
phi = (1 + np.sqrt(5))/2 # Golden ratio

plt.figure ()
plt.subplot(121) # 1 x 2 grid of plots , first plot
# plot f vs n, AND plot Binet’s approximation
# ’bs’ means blue squares , while ’r--’ means red line
plt.plot(n,f,’bs’,n,phi**n/np.sqrt(5),’r--’)
plt.xlabel("n")
plt.ylabel("f(n)")
plt.title("Fibonacci (linear y-axis)")
plt.subplot(122) # 1 x 2 grid of plots , second plot
plt.plot(n,f,’bs’,n,phi**n/np.sqrt(5),’r--’)
plt.yscale(’log’) # set y-axis to be on log-scale
plt.xlabel("n")
plt.ylabel("f(n)")
plt.title("Fibonacci (log y-axis)")
plt.savefig("Example1bOutput.pdf")
plt.show()



fibonacci without recursion
def f(n):
    x,y = 1,1
    for _ in range(n-2): x,y = y, x+y
    return y



fibonacci using binets formula
import numpy as np # need np.sqrt

phiP = (1 + np.sqrt(5))/2 # Golden ratio
phiM = (1 - np.sqrt(5))/2

# Fibonacci using Binet
def f(n): # note the cast to integer
    return int(( phiP **n - phiM **n)/np.sqrt(5))

nmax = 6
print("n\tf(n)")

for n in range(1,nmax+1):
    print("{:>2}\t{:>2}".format(n,f(n)))


timing fibonacci sequences
import time # need time.clock
# Fibonacci via recursion , defining recurrence
def f(n):
    if n <= 2: return 1
    else: return f(n-1) + f(n-2)

nmin , nmax = 10 , 40
print("n\tf(n)\tt(n)")
for n in range(nmin ,nmax+1):
    ts = time.clock () # start clock
    fv = f(n) # get result
    tf = time.clock () # stop clock
    print("{:>2}\t{:>9}\t{:.5f}".format(n,fv ,tf-ts))
            #the :>2 determines amount of printed digits for integers


Other ways to process fiboncci sequence without recursion:
non recusion implementation or binets formula or the fast doubling formulas

implementing fast doubling formulas
# Fibonacci , recursive using fast doubling
def f(n):
    if n <= 2: return 1
    elif n % 2: # n is odd
        n = (n-1) / 2
        fl , fr = f(n+1), f(n)
        return fl*fl + fr*fr
    else: # n is even
        n = n / 2
        fl , fr = f(n+1), f(n)
        return fr * (2 * fl - fr)




''''''
MEMOIZATION:
''''''
Using a cache:
# recursive Fibonacci WITH cache
cache = {} # values previously computed, empty dictionary
def fc(n): # check cache , call _f, store so it doesn't have to be computed again
    if n not in cache: cache[n] = _f(n)
    return cache[n]

# called by fc for values not in cache
def _f(n):
    if n <= 2: return 1
    else: return fc(n-1) + fc(n-2)

# recursive Fibonacci WITHOUT cache
def f(n):
    if n <= 2: return 1
    else: return f(n-1) + f(n-2)

Using caches to store previous computed n values
checking that cache for existing values before computing them


'built in' support for memoization
Decorators: @ symbol



tming? research: pref_count




'''Object Oriented Programming'''
Classes


'''
Weighted Random choice
Choice with weights
'''
import random
random.choices([1, 2, 3, 4], weights = np.array([0.01, 0.85, 0.07, 0.07]))

will choose from first list with respective weights
note: choices not choice


'''
Graph Theory and Animations
'''

'''GRAPHVIZ'''
dot language

graph {
v1 -- v2;
v2 -- v3;
v3 -- v4;
v4 -- v5;
v5 -- v1;
v1 -- v6;
v2 -- v7;
v3 -- v8;
v4 -- v9;
v5 -- v10;
v6 -- v8;
v6 -- v9;
v7 -- v9;
v7 -- v10;
v8 -- v10;
}

'''NETWORKX'''
import matplotlib .pyplot as plt
import networkx as nx

G = nx.petersen_graph ()
    #Library includes several known graphs
nx.draw(G)
plt.draw ()
plt.savefig("Example1aOutput.pdf")
plt.show ()


#NetworkX and GraphViz can export graphs files in dot language
import networkx as nx
from networkx.drawing. nx_agraph import
write_dot
G = nx.petersen_graph ()
write_dot(G, "Petersen.gv")

strict graph "
Petersen
Graph" {
0 -- 1;
0 -- 4;
0 -- 5;
1 -- 2;
1 -- 6;
2 -- 3;
2 -- 7;
3 -- 4;
3 -- 8;
4 -- 9;
5 -- 7;
5 -- 8;
6 -- 8;
6 -- 9;
7 -- 9;
}


'''SNAP''' - collection of real world graphs
NOT WRITTEN IN DOT NOTATION!
# Nodes: 5242 Edges: 28980
# FromNodeId ToNodeId
3466 937
3466 5233
3466 8579
3466 10310
3466 15931
3466 17038
3466 18720
3466 19607
10310 1854
10310 3466
10310 4583
10310 5233
10310 9572
10310 10841

'''or'''

import networkx as nx
from networkx.drawing. nx_agraph import write_dot
G = nx.read_edgelist ("CA-GrQc.txt")
write_dot (G, "CA-GrQc.gv")

#header of CA-GrQc.gv
graph "" {
3466 -- 937;
3466 -- 5233;
3466 -- 8579;
3466 -- 10310;
3466 -- 15931;


'''Seven bridges of Koenigseberg'''
import networkx as nx
from networkx.drawing.nx_pydot import write_dot
# a multigraph (MG) is a graph with possibly more than one edge
# connecting each pair of vertices
MG = nx.MultiGraph()
MG.add_nodes_from([1,2,3,4])
# add the edges , give each edge a label
# these vertices & edges form 7 bridges of Konigsburg graph
MG.add_edges_from([(1,2,’a’) ,(1,2,’b’) ,(1,3,’c’)])
MG.add_edges_from([(1,4,’d’) ,(1,4,’e’) ,(2,3,’f’) ,(3,4,’g’)])
# write the "dot file" for use by GraphViz
write_dot(MG , "Example3aOutput.gv")
# is_eulerian: True if graph has Euler circuit , else False
print(nx.is_eulerian (MG))

returns: false



'''Another example of dot langauge'''
graph {
1;
2;
3;
4;
1 -- 2 [key=a];
1 -- 2 [key=b];
1 -- 3 [key=c];
1 -- 4 [key=d];
1 -- 4 [key=e];
2 -- 3 [key=f];
3 -- 4 [key=g];
}

'''Graph coloring check of US Map'''
import networkx as nx
from networkx.drawing.nx_pydot import write_dot
G = nx.read_adjlist ("Example4aInput.txt")
write_dot (G, "Example4aOutput.gv")
# dot -Tpdf Example4aOutput.gv -o Example4aOutput -
dot.pdf
# fdp -Tpdf Example4aOutput.gv -o Example4aOutput -
fdp.pdf
# check_planarity() returns:
# boolean: True if planar , False if not
# certificate: Kuratowski subgraph if not
# (recall Kuratowski’s theorem on K_5 and K_{3,3})
print(nx.check_planarity(G)[0])

True

Ex4aOutput.gv
strict graph
{
AL;
FL;
GA;
TN;
MS;
AZ;
NM;
AL -- GA;
AL -- TN;
AL -- MS;
FL -- GA;
GA -- SC;
GA -- NC;
GA -- TN;
TN -- AR;

etc.



'''Machine Learning'''
SciKit
Label Data 

focus on classification problems
using new library SciKit-Learn

data: x
labe;: y 

Labeled datum = (x,y)

classification problems: where labels (y values) are of a finite amount
regression problems: where labels can be an uncountably infinite set

Unsupervised learning:
take unlabeled datu,: feature vector x
computer given large number of feature vectores
computer clusters points into groups, and partitions the feature StopAsyncIteration

Reinforcred learning:
computer is given environment, controls and objective
computer explores its environment, tests impact of controls an duses algorithm to maximize value of object
Example: multi-armed bandit from week 2 Lab

Terms:
'feature space': continuous n-dimensional space in which feasible instance features are numerically described
    feature vector is denoted x=(x1,x2,...,xn)

'label space': finite set of possible labels for any feasible instance input. label is denoted by y 

'instance': a feature vector and its associated label. denoted by (x,y)

'training data': list of Mtr training instances, Xtr is an MtrXn matrix 
    with row i of Xtr matching entry of i Ytr for i in [Mtr]

'classifier': a function that assigns a label to each feature vector x. function is trained using training data 

'testing data': a list of Mte testing instances, Xte is an MteXn matrix 
    with row i of Xte matching entry i of Yte

'testing predictions': the Mte values obtained by passing testing feature vectors as inputs to the trained classifier

'feature importance': from perspective of random forest, how important each measure is for making decision
    when used by the right algorithm in the right way


Algorithm classes:
'Naive Bayes classifier'
'Support vector machine(SVM)':
partitions feature space X into regions ( X(y), yEY ) and predict z(x)=y if xEX(y).
feature space partition uses training data to establish hyperplanes (boundaries) with maximum 'margin'
    from points to boundary (optimization)
support vectors are the points closest to the hyperplane that are used to calculate the margin

'Decision Tree/Random forest':
binary classification decision tree uses a series of yes/no questions to assign label z to each input
random forest creates a large number of decision trees, computes predicted labels for a given input x
    using each tree and then uses majority voting rule to decide final label

SkiKit-Learn:
from sklearn import datasets
from skylearn.ensemble import RandomForestClassifier

Dimension: number of measurements, num cols
Samples total: number of samples, num rows
Classes: number of labels

loading an example from SciKit-Learn
dataset=datasets.load_breast_cancer()
X=dataset.data 
y=dataset.target
#target in 0 or 1 since there are only 2 classes

# print feature names
print("Feature names: {}".format(dataset. feature_names ))
# print target names
print("Target names: {}".format(dataset. target_names ))
# print feature shape
print("Feature shape: {}".format(dataset.data.shape))
# print target shape
print("Target shape: {}".format(dataset.target.shape))
# print set and # of target values
print("Target vals: {}, size: {}".format(set(y),len(set(y))))

'''NIST digit recognition'''
classes:10
samples per class: ~180
samples total: 1797
Dimensionality: 64 because the drawsing were digitized to 8x8 image
Featues: integers 0-16

import numpy as np
from sklearn import datasets, svm

dataset = datasets.load_digits()
X_im=dataset.images
y=dataset.target

# tally y
#will print a list of the target integers and how many features there are for each one
print("t\tn")
for t in range(10):
    c = list(y).count(t)
    print("{}\t{}".format(t,c))

#Split dataset into training vs testing data. usually split 50/50 randomly is sufficient
def split_train_test (X, y, f_tr):
    # get number of instances
    n = X.shape[0]
    # set number of images for training , testing
    n_tr = int(f_tr * n)
    n_te = n - n_tr
    # pick indices for training
    i_tr = np.random.choice(n, n_tr , replace=False)
    # split X_lst into training and testing
    X_tr = [X[i] for i in range(n) if i in i_tr]
    X_te = [X[i] for i in range(n) if i not in i_tr]
    # split y_lst into training and testing
    y_tr = [y[i] for i in range(n) if i in i_tr]
    y_te = [y[i] for i in range(n) if i not in i_tr]
    # return training and testing
    return X_tr , X_te , y_tr , y_te

# create a support vector classifier (SVC)
cls = svm.SVC()
# train the classifier with training data
cls.fit(X_tr , y_tr)
# use classifier to predict on test X_te
z_te = cls.predict(X_te)

# print table of mis-classified test values
print("i\ty\tz")
for i in range(len(y_te)):
    if y_te[i] != z_te[i]:
        print("{}\t{}\t{}".format(i,y_te[i],z_te[i]))

Confusion matrix:
k = |y| classes is a kxk matric summary of how the classifier performs. 
rows = correspond to the input featues
cols = predicted outputs by function for the row number integer
values = number of row integers predicted there there
main diagonal = correct values 

# number of targets
m = len(set(y))
# print confusion array
print("Confusion array:")
c_arr = np.zeros((m,m), dtype=int)
for i in range(len(y_te)):
    c_arr[y_te[i],z_te[i]] += 1
print(c_arr)

[[86 0 0 0 1 0 0 0 0 0]
[ 0 94 0 0 0 0 0 0 0 0]
[ 0 0 89 0 0 0 0 0 0 0]
[ 0 0 0 90 0 2 0 1 0 0]
[ 0 0 0 0 97 0 0 0 0 0]
[ 0 0 0 0 0 90 1 0 0 1]
[ 0 0 0 0 0 0 88 0 1 0]
[ 0 0 0 0 0 0 0 80 0 0]
[ 0 3 0 0 0 0 0 0 81 0]
[ 0 1 0 0 0 2 0 6 4 81]]


'''Using random forest''':


import numpy as np
import matplotlib .pyplot as plt
from sklearn import datasets

def plot_decision_tree (cls , fen , fn):
    plt.figure()
    tree. plot_tree (cls , feature_names=fen)
    plt.savefig(fn , bbox_inches = "tight")

# load the dataset
dataset = datasets.load_wine()
# get feature data
X = dataset.data
# get feature names
fen = dataset. feature_names
# get target data
y = dataset.target

# set fraction of images for training
f_tr = 1.0
# split into training and testing:
X_tr , X_te , y_tr , y_te = split_train_test(X, y, f_tr)

# create a decision tree classsifier
cls = tree.DecisionTreeClassifier()
# train the classifier with training data
cls.fit(X_tr , y_tr)
# visualize the classifier
fn = "Example3bOutput.pdf"
plot_decision_tree(cls , fen , fn)

'''Use sklearn tree command cls = tree.DecisionTreeClassifier() to
create a decision tree.'''



'''PANDAS'''
#df - data frame
#ds - data series
• Pandas is a powerful data analysis / data science tool
• Very easy to use, and well-integrated with other tools such as numpy and matplotlib

import pandas as pd

#make df with csv data
df = pd.read_csv (’GPSA.csv’)

#shape attribute
df.shape

#info() method
df.info()

<class ’pandas.core.frame.DataFrame’>
RangeIndex: 9637 entries , 0 to 9636
Data columns (total 13 columns):
# Column Non-Null Count Dtype
--- ------ -------------- -----
0 App 9637 non-null object
1 Category 9637 non-null object
2 Rating 8179 non-null float64
3 Reviews 9637 non-null int64
4 Size 9637 non-null object
5 Installs 9637 non-null object
6 Type 9636 non-null object
dtypes: float64(1), int64(1), object(11)
memory usage: 978.9+ KB

#columns attribute
df.columns

df.columns type: <class ’pandas.core.indexes.base.Index’>
Index([’App’, ’Category’, ’Rating’, ’Reviews’, ’Size’, ’
Installs’, ’Type’, ’Price’, ’
Content Rating’, ’Genres’, ’
Last Updated’, ’Current Ver’, ’
Android Ver’], dtype=’object’)

#pd.read_csv() with index_col
df = pd.read_csv (’GPSA.csv’, index_col=’App’)
print(df.info())

<class ’pandas.core.frame.DataFrame’>
Index: 9637 entries , Photo Editor ... to iHoroscope ...
Data columns (total 12 columns):
# Column Non-Null Count Dtype
--- ------ -------------- -----
0 Category 9637 non-null object
1 Rating 8179 non-null float64
2 Reviews 9637 non-null int64
3 Size 9637 non-null object
4 Installs 9637 non-null object
dtypes: float64(1), int64(1), object(10)
memory usage: 978.8+ KB
None

#iloc column as SERIES
"""df.iloc[:,0] is Series object holding df values in column index 0"""
col = df.iloc[:,0]
print('col type: {}'.format(type(col)))
print(col)

col type: <class ’pandas.core.series.Series’>
0 Photo Editor & Candy Camera & Grid & ScrapBook
1 Coloring book moana
2 U Launcher Lite FREE Live Cool Themes , Hide Apps
3 Sketch - Draw & Paint
4 Pixel Draw - Number Art Coloring Book
...
9632 Sya9a Maroc - FR
9633 Fr. Mike Schmitz Audio Teachings
Name: App , Length: 9637 , dtype: object

#iloc column as DATAFRAME
"""note brackets around the 0"""
col = df.iloc[:,[0]]
print("col type: {}".format(type(col)))
print(col)

col type: <class ’pandas.core.frame.DataFrame’>
App
0 Photo Editor & Candy Camera & Grid & ScrapBook
1 Coloring book moana
2 U Launcher Lite FREE Live Cool Themes , Hide Apps
... ...
9635 The SCP Foundation DB fr nn5n
9636 iHoroscope - 2018 Daily Horoscope & Astrology
[9637 rows x 1 columns]

#iloc columns as DATAFRAME
"""to make dataframe, cols must be specified as a list"""
col = df.iloc[:,[1,3,5]]
print("col type: {}".format(type(col)))
print(col)

col type: <class ’pandas.core.frame.DataFrame’>
Category Reviews Installs
0 ART_AND_DESIGN 159 10 ,000+
1 ART_AND_DESIGN 967 500 ,000+
... ... ... ...
9636 LIFESTYLE 398307 10 ,000 ,000+
[9637 rows x 3 columns]

#iloc columns SLICE
col = df.iloc[:,1:3]
''df.iloc[:,1:3] is DataFrame of columns with indices 1, 2''

#iloc row as SERIES
row = df.iloc[1,:]
''df.iloc[1,:] is Series holding df values in row with index 1''
print("row type: {}".format(type(row)))
print(row)

row type: <class ’pandas.core.series.Series’>
App Coloring book moana
Category ART_AND_DESIGN
Rating 3.9
Reviews 967
Size 14M
Installs 500 ,000+
Type Free
Price 0
Content Rating Everyone
Genres Art & Design;Pretend Play
Last Updated 15-Jan-18
Current Ver 2.0.0
Android Ver 4.0.3 and up
Name: 1, dtype: object

#iloc row as DATAFRAME
row = df.iloc[[1],:]
''df.iloc[[1],:] is DataFrame holding df values in row with index 1''

#iloc rows as DATAFRAME
row = df.iloc[[1,3,5],:]
''df.iloc[[1,3,5],:] is DataFrame of rows with indices 1, 3, 5''

#iloc rows via SLICE
row = df.iloc[1:3,:]
''df.iloc[1:3,:] is DataFrame of rows with indices 1, 2''

#iloc rows AND columns via SLICE
rc = df.iloc[4:6,1:3]
''df.iloc[4:6,1:3] is DataFrame holding df values in rows with indices
4, 5 and columns with indices 1, 2''

#loc column as SERIES
col = df.loc[:,’Category’]
''df.loc[:,’Category’] is Series object holding df values in column
named ’Category’''

#loc column as DATAFRAME
col = df.loc[:,[’Category’]]
''df.loc[:,[’Category’]] is DataFrame object holding df values in
column named ’Category’''

#loc columns as DATAFRAME
col = df.loc[:,[’Category’, ’Reviews’]]
''df.loc[:,[’Category’,’Reviews’]] is DataFrame of columns named
’Category’ and ’Reviews’''

#loc columns SLICE
col = df.loc[:, ’Category’ : ’Reviews’]
''df.loc[:,’Category’:’Reviews’] is DataFrame of columns from
’Category’ through ’Reviews’ inclusive (c.f., iloc is exclusive of right
index)''

#loc row as SERIES
row = df.loc[’Coloring book moana’,:]
''df.loc[’Coloring book moana’,:] is Series holding df values in row
named ’Coloring book moana’''

#loc row as DATAFRAME
row = df.loc[[’Coloring book moana’],:]
''df.loc[[’Coloring book moana’],:] is DataFrame holding df values
in row named ’Coloring book moana’''

#loc rows as DATAFRAME
row = df.loc[[’Coloring book moana’,’Sketch - Draw & Paint’],:]
''df.loc[[’Coloring book moana’, ’Sketch - Draw & Paint’],:]
is DataFrame of rows with names ’Coloring book moana’ and ’Sketch
- Draw & Paint’''

#loc rows via SLICE
row = df.loc[’Coloring book moana’ : ’Sketch - Draw & Paint’,:]
''df.loc[’Coloring book moana’ : ’Sketch - Draw & Paint’,:]
is DataFrame of rows from ’Coloring book moana’ through ’Sketch -
Draw & Paint’ inclusive (c.f., iloc is exclusive of right index)''

#loc rows AND columns via SLICE
rc = df.loc[’Coloring book moana’:’Sketch - Draw & Paint’,’Category’:’Reviews’]
''df.loc[’Coloring book moana’:’Sketch - Draw &
Paint’,’Category’:’Reviews’] is DataFrame holding df values in rows
with names ’Coloring book moana’ through ’Sketch - Draw &
Paint’ (inclusive) and columns with names ’Category’ through
’Reviews’ (inclusive)''

#unique
df.unique()
gives a count of number of unique values in each column

App 9637
Category 33
Rating 39
Reviews 5323
Size 461
Installs 21
Type 2
Price 90
Content_Rating 6
Genres 118
Last_Updated 1377
Current_Ver 2766
Android_Ver 33
dtype: int64

#ds.unique() distinct values in column
ds = df.loc[:,’Content_Rating’]
dsu = ds.unique()
''ds.unique() returns numpy array of unique values in Series ds.''

ds type: <class ’numpy.ndarray’>
[’Everyone’ ’Teen’ ’Everyone 10+’ ’Mature 17+’ ’Adults only 18+’ ’Unrated’]

#ds.value_counts() column value tally
ds = df.loc[:,’Content_Rating’]
dsvc = ds.value_counts()
''ds.value_counts() returns Series tallying values in Series ds''

dsvc type: <class ’pandas.core.series.Series’>
Everyone 7883
Teen 1035
Mature 17+ 392
Everyone 10+ 322
Adults only 18+ 3
Unrated 2
Name: Content_Rating , dtype: int64

#df.loc() find rows with column value
ds = df.loc[:,’Content_Rating’]
dft = df.loc[ds == ’Unrated’, :]
''df.loc[ds == ’Unrated’, :] returns a DataFrame holding all rows in
which the Series ds takes value ’Unrated’. This is called Boolean indexing''

#df.loc() under multiple criteria
dsr = df.loc[:,’Rating’]
dst = df.loc[:,’Type’]
dscr = df.loc[:,’Content_Rating’]
cl = [’App’,’Rating’,’Type’,’Price’,’Content_Rating’]
dft = df.loc[(dsr>=4.8) & (dst==’Paid’) & (dscr==’Teen’), cl]

''i) Find rows with ’Rating’ >= 4.8 and ’Type’ == ’Paid’ and
Content_Rating’ == ’Teen’ then ii) display columns listed in cl for
those rows''

#apply and method chaining
• ds.apply(f) applies function f to every element in DataSeries ds
• Pandas method chaining, e.g., df.loc[:,’Price’].apply(f)
• Goal: remove the symbol $ from the strings in column ’Price
import pandas as pd
# function to remove first character from string s
# if that first character is not numeric
# e.g., s = ’$4.99’ -> ’4.99’
def f(s):
    return s[1:] if not s[0]. isnumeric() else s
# read in the file
df = pd.read_csv(’GPSA.csv’)
# apply function f to every element in column ’Price’
df.loc[:,’Price’] = df.loc[:,’Price’].apply(f)
# create filter to select ’Paid’ apps under ’Type’
fil = df.loc[:,’Type’] == ’Paid’
# apply the filter
df = df.loc[fil ,:]
# print ’App’ and ’Price’ columns from df
print(df.loc[:,[’App’,’Price’]])

'''returns'''
    App Price
233 TurboScan: scan documents and receipts in PDF 4.99
234 Tiny Scanner Pro: PDF Doc Scan 4.99
... ... ...
9594 Word Search Tab 1 FR 1.04
[753 rows x 2 columns]

• There are 753 rows with value ’Paid’ in column ’Type’
• The entries in column ’Price’ no longer have $ but are still strings

#astype conversion
• ds.astype(float) converts every element in DataSeries ds to a float
• Pandas method chaining, e.g., df.loc[:,’Price’].astype(float)
• Goal: convert entries in column ’Price’ to floats
import pandas as pd
# remove first character from string s if not numeric
def f(s):
    return s[1:] if not s[0].isnumeric() else s
# read in the file
df = pd.read_csv(’GPSA.csv’)
# apply function f to every element in column ’Price’
df.loc[:,’Price’] = df.loc[:,’Price’].apply(f)
# convert every element in column ’Price’ to a float
df.loc[:,’Price’] = df.loc[:,’Price’].astype(float)
# create filter to select ’Paid’ apps under ’Type’
fil = df.loc[:,’Type’] == ’Paid’
# apply the filter
df = df.loc[fil ,:]
# print ’App’ and ’Price’ columns from df
print(df.loc[:,[’App’,’Price’]])

'''returns'''
    App Price
233 TurboScan: scan documents and receipts in PDF 4.99
234 Tiny Scanner Pro: PDF Doc Scan 4.99
... ... ...
9594 Word Search Tab 1 FR 1.04
[753 rows x 2 columns]
• Same apparent output as 5a, but the entries in column ’Price’ are now
floats, and are ready for numerical sorting

#sort_values dataframe sorting
• Goal: sort rows by ’Price’ column. Problem: ’Price’ values are
strings
• Solution: convert ’Price’ values to floats using apply and astype,
then use sort_values
import pandas as pd
# function to remove first character from string s
# if that first character is not numeric
# e.g., s = ’$4.99’ -> ’4.99’
def f(s):
    return s[1:] if not s[0].isnumeric() else s
# read in the file
df = pd.read_csv(’GPSA.csv’)
# apply function f to every element in column ’Price’
df.loc[:,’Price’] = df.loc[:,’Price’].apply(f)
# convert every element in column ’Price’ to a float
df.loc[:,’Price’] = df.loc[:,’Price’].astype(float)
# sort df by values in column ’Price’ in descending order
df = df. sort_values (’Price’,ascending=False)
# print out ’App’ and ’Price’ columns
print(df.loc[:,[’App’,’Price’]])

'''returns'''
App Price
3467 I’m Rich - Trump Edition 400.00
3325 most expensive app (H) 399.99
4406 I AM RICH PRO PLUS 399.99
4389 I am rich 399.99
4390 I am Rich Plus 399.99
... ... ...
9636 iHoroscope - 2018 Daily Horoscope & Astrology 0.00
[9637 rows x 2 columns]
• Apparently, there are apps whose sole appeal is that they cost a lot (?!).
• Most (but not all) Pandas commands do not alter the dataframe values
“in place”, unless the flag inplace=True is given.
• Consequently, after each step of processing, processed dataframe must be
saved, e.g., df = df.sort_values(’Price’,asending=False)

#'Rating' histogram
import numpy as np
import matplotlib .pyplot as plt
import pandas as pd
# read in the file
df = pd.read_csv(’GPSA.csv’)
# convert ’Rating’ column values to floats
df.loc[:,’Rating’] = df.loc[:,’Rating’].astype(float)
# DataSeries from ’Rating’ column
data = df.loc[:,’Rating’]
# summary statistics of ’Ratings’ column values
print(data.describe())
# plot histogram
bins = np.arange(1.0, 5.15 , 0.1)-0.05
plt.hist(data , bins=bins , edgecolor=’white’, linewidth=1)
plt.xlabel(’Rating’)
plt.ylabel(’# apps with rating’)
plt.title(’Histogram of app ratings’)
plt.savefig(’Example6aOutput.pdf’)

• plt.hist(data,bins=bins) with bins = [1.0, 1.1, . . . , 4.9.5.0]

count 8179.000000
mean 4.173481
std 0.537204
min 1.000000
25% 4.000000
50% 4.300000
75% 4.500000
max 5.000000
Name: Rating , dtype: float64
• ds.describe() gives DataSeries summary statistics, here for column
’Rating’

#'Reviews histogram
import numpy as np
import matplotlib .pyplot as plt
import pandas as pd
# read in the file
df = pd.read_csv(’GPSA.csv’)
# convert ’Reviews’ column values to ints
df.loc[:,’Reviews’] = df.loc[:,’Reviews’].astype(int)
# DataSeries from ’Rating’ column
data = df.loc[:,’Reviews’]
# bin boundary values: 0, 1, 10, ..., 10M, 100M
b = [0,1,10 ,10**2,10**3,10**4,10**5,10**6,10**7,10**8]
# y: # apps in each bin: 0, [1,10), [10,100) ,...,[10M,100M)
y = []
for i in range(len(b)-1):
yv = df.loc[(data >= b[i]) & (data < b[i+1]), :]
y.append(yv.shape[0])
• Count number of apps with # reviews of each magnitude:
    [10^k, 10^k+1), e.g., 0, [1, 10), [10, 100), . . ., [106, 107).

# x holds bin labels where [k,k+1) means [10^k,10^(k+1))
x=[’0’,’[0,1)’,’[1,2)’,’[2,3)’,’[3,4)’,’[4,5)’,’[5,6)’,’[6,7)’,’[7,8)’]
# plot app review histogram
plt.bar(x, y)
plt.xlabel(’# reviews ([k,k+1) means [10^k,10^(k+1)))’)
plt.ylabel(’# apps with specified review #s’)
plt.title(’Histogram of app review #s’)
plt.savefig(’Example6bOutput.pdf’)
• Use plt.bar(x,y) where 푥 is an array of 푥-axis label strings

#'Reviews' largest values
import numpy as np
import pandas as pd
# read in the file
df = pd.read_csv(’GPSA.csv’)
# convert ’Reviews’ column values to ints
df.loc[:,’Reviews’] = df.loc[:,’Reviews’].astype(int)
# sort df by ’Reviews’ column
df = df. sort_values (’Reviews’,ascending=False)
# print columns ’App’ and ’Reviews’ for top 19 rows
print(df.loc[:,[’App’,’Reviews’]].head(19))
• Convert ’Reviews’ column values to int using astype()
• Sort values using df.sort_values()
• Print out ’App’ and ’Reviews’ columns for top 19 apps

'''returns'''
     App Reviews
2002 Facebook 78158306
300 WhatsApp Messenger 69119316
2003 Instagram 66577313
299 Messenger Text and Video Chat for 56642847
1372 Clash of Clans 44891723
3179 Clean Master- Space Cleaner & Antivi 42916526
1356 Subway Surfers 27722264
2907 YouTube 25655305

#'Reviews' vs 'Rating' scatter plot
import numpy as np
import matplotlib .pyplot as plt
import pandas as pd
# read in the file
df = pd.read_csv(’GPSA.csv’)
# convert ’Rating’ column values to floats
df.loc[:,’Rating’] = df.loc[:,’Rating’].astype(float)
# convert ’Reviews’ column values to ints
df.loc[:,’Reviews’] = df.loc[:,’Reviews’].astype(int)
# scatter plot of (Rating , Reviews)
x = df.loc[:,’Rating’].tolist()
y = df.loc[:,’Reviews’].tolist()
plt.figure()
plt.scatter(x,y,s=1) # s=1: small point size for 10k points
plt.yscale(’Log’)
plt.xlabel(’Rating’)
plt.ylabel(’# reviews’)
plt.title(’# app reviews vs.\ app rating’)
plt.savefig(’Example6dOutput.pdf’)
• astype converts ’Rating’ to float, ’Reviews’ to int

#'Last_Updated' by year bar plot
df = pd.read_csv (’GPSA.csv’)
# useful shorthand for string
slu = ’Last_Updated’
# convert ’Last_Updated’ column values to dates
df.loc[:,slu] = pd. to_datetime (df.loc[:,slu])
# helper function: keep only year in date string
def f(x): return x.strftime(’%Y’)
# keep only year; strip day and month
df.loc[:,slu] = df.loc[:,slu].apply(f)
# count number of apps last updated in each year
v = df.loc[:,slu]. value_counts ()
# sort v by the year
v = v. sort_index ()
• pd.to_datetime converts ’Last_Updated’ to datetime objects.
• ds.apply(f), with f calling strftime, strips day, month from dates.
• value_counts counts apps by year; sort by index (year)
# plot the number of apps last updated in each year
plt.bar(v.index , v.values)
plt.yscale(’Log’)
plt.xlabel(’Year of last update’)
plt.ylabel(’# apps’)
plt.title(’# apps by year last updated’)
plt.savefig(’Example6eOutput.pdf’)
• Use plt.bar plot to show v.values (# apps last updated by year) vs. v.index (year)

#info, nunuqie, and unique
import pandas as pd
df = pd.read_csv (’HOBR.csv’)
print(df.info ())
# column name , value_counts
for j in range(df.shape[1]):
    c = df.columns[j]
    n = df.iloc[:,j].nunique ()
    print("\nColumn {}: {} ({} unique values)".format(j,c,n))
    if n < 10: print(df.iloc[:,j].unique ())
• df.info prints out column names, column dtypes, count of values
• Iterate over columns, use df.columns command to get column name,
and ds.nunique command to get number of unique values by column
• If a column has fewer than 10 distinct values, print them

'''returns'''
<class ’pandas.core.frame.DataFrame’>
RangeIndex: 724 entries , 0 to 723
Data columns (total 8 columns):
# Column Non-Null Count Dtype
--- ------ -------------- -----
0 Name of Covered Entity 724 non-null object
1 State 723 non-null object
2 Covered Entity Type 724 non-null object
3 Individuals Affected 724 non-null int64
4 Breach Submission Date 724 non-null object
5 Type of Breach 724 non-null object
6 Location of Breached Information 724 non-null object
7 Business Associate Present 724 non-null object
dtypes: int64(1), object(7)
memory usage: 45.4+ KB
None

#value_counts, filtering, head
import pandas as pd
df = pd.read_csv(’HOBR.csv’)
# find which covered entities have multiple breaches
ds = df.loc[:,’Name of Covered Entity’]. value_counts()
ds = ds.loc[ds > 1]
print(’{} CE w/ multiple breaches’.format(ds.shape[0]))
print(ds.head(18))
• ds.value_counts produces a DataSeries indexed by the values in
DataSeries ds holding the number of times that value occurs ds
• ds = ds.loc[ds > 1] is Boolean indexing: keeping those entries in
DataSeries ds satisfying the filter constraint ds > 1
• ds.head(18) returns the first 18 elements in DataSeries ds

'''returns'''
24 CE w/ multiple breaches
University of Utah 4
University of Missouri Health Care 3
Walmart Inc. 3
UnitedHealth Group Health Plan Single Affi 3
Walgreen Co. 3
Iowa Total Care , Inc. 2
Harbor Health Services , Inc. 2
Beaumont Health 2
Advocate Aurora Health 2
Cancer Treatment Centers of America (CTCA) 2
Montefiore Medical Center 2
Brandywine Counseling & Community Services 2
Solara Medical Supplies , LLC 2
Miracle - Ear 2
Presbyterian Healthcare Services 2
Rose Dental 2
Lycoming-Clinton Joinder Board Programs 2
Practice Transformation Solutions , LLC 2
Name: Name of Covered Entity , dtype: int64

#incorporating external data
df = pd.read_csv(’HOBR.csv’)
# find which states have the most breaches
ds = df.loc[:,’State’].value_counts()
print(’\nStates with most breaches’)
print(ds.head(5))
print(’\nStates with fewest (but nonzero) breaches’)
print(ds.tail(5))
# https://www.census.gov/data/tables/time-series/demo/popest/2010s-state -total.html
# has column ’State’ and column ’Population’
dssp = pd.read_csv (’USCSP.csv’, index_col =’State’)
ixsp , ixds = set(dssp.index.values), set(ds.index.values)
print("\nStates with zero breaches: {}".format(ixsp - ixds))
• value_counts on ’State’ column yields DataSeries of counts by state
• ds.head(5), ds.tail(5) lists states with most, fewest breaches
• Read external DataFrame from USCSP.csv listing states, populations
• List index values from ds, dssp and use set difference ixsp - ixds

States with most breaches
CA 59
TX 59
NY 56
FL 42
PA 36
Name: State , dtype: int64
States with fewest (but nonzero) breaches
MT 2
NH 2
HI 1
VT 1
MS 1
Name: State , dtype: int64
States with zero breaches: {’RI’, ’SD’}
• Rhode Island (RI) and South Dakota (SD) only states without breaches

#creating new columns from old
import pandas as pd
# Dataframe df from HOBR
df = pd.read_csv(’HOBR.csv’)
# DataSeries ds holds value_counts of df ’State’ column
ds = df.loc[:,’State’].value_counts()
# DataFrame dfsp holds state populations
dfsp = pd.read_csv (’USCSP.csv’, index_col =’State’)
# Convert dssp populations from strings to integers
dfsp.loc[:,’Population’] = dfsp.loc[:,’Population’].astype(int)
# Create new dfsp col. ’BPM’ for breaches per million citizens
dfsp.loc[:,’BPM’] = ds / dfsp.loc[:,’Population’] * 10**6
# Sort dfsp in descending order on values in new column ’BPM’
dfsp = dfsp. sort_values (’BPM’, ascending=False)
# Print out states with 5 highest and 5 lowest values of ’BPM’
print("States with highest # breaches per million residents")
print(dfsp.head(5))
print("\nStates with lowest # breaches per million residents")
print(dfsp.tail(5))
• dfsp.loc[:,’BPM’]: new col. ’BPM’ from ds, dfsp’s ’Population’

States with highest # breaches per million residents
Population BPM
State
DE 973764 8.215543
CT 3565287 5.048682
AR 3017804 4.970502
DC 705749 4.250803
AK 731545 4.100910
States with lowest # breaches per million residents
Population BPM
State
AL 4903185 0.815796
HI 1415872 0.706279
MS 2976149 0.336005
RI 1059361 NaN
SD 884659 NaN
• Delaware (DE) highest BPM at 8.22; Mississippi (MS) lowest nonzero
BPM at 0.34. Highest/lowest breach count & BPM states very different.

#Plot of breaches by month
df = pd.read_csv(’HOBR.csv’)
sbsd = ’Breach Submission Date’
# convert ’Breach Submission Date’ strings to datetimes
df.loc[:,sbsd] = pd.to_datetime(df.loc[:,sbsd])
# helper function: keep year and month in date string
def f(x): return x.strftime(’%Y-%m’)
df.loc[:,sbsd] = df.loc[:,sbsd].apply(f)
# DataSeries ds counts breaches by month
# Sort by month (index) to plot chronologically
ds = df.loc[:,sbsd].value_counts(). sort_index()
# Plot breaches by month: bbox_inches to avoid label cutoff
plt.bar(ds.index , ds.values)
plt.xlabel(’Month’)
plt.xticks( rotation=90)
plt. tight_layout ()
plt.ylabel(’# breaches’)
plt.title(’# breaches by month’)
plt.savefig(’Example7eOutput.pdf’, bbox_inches = ’tight’)

#Log-log plot of breach size vs. rank
df = pd.read_csv(’HOBR.csv’)
sia = ’Individuals Affected’
# Convert # individuals affected to integers
df.loc[:,sia] = df.loc[:,sia].astype(int)
# Sort DataFrame df by descending sia column values
df = df.sort_values(sia , ascending=False)
# Print ’Name of Covered Entity’ and sia: largest breaches
print(df.loc[:,[’Name of Covered Entity’, sia]])
y = df.loc[:,sia].tolist()
# Log-log plot of breach size vs. breach size rank
plt.figure ()
plt.plot(range(len(y)),y)
plt.xscale(’Log’)
plt.yscale(’Log’)
plt.xlabel(’Breach size rank’)
plt.ylabel(’Breach size’)
plt.title(’Breach size vs. breach size rank’)
plt.savefig(’Example7fOutput.pdf’)

Name of Covered Entity Ind. Aff.
694 Optum360 , LLC 11500000
116 Florida Healthy Kids Corporation 3500000
696 Dominion Dental Services , Inc., Dominion Natio ... 2964778
711 Inmediata Health Group , Corp. 1565338
85 The Kroger Co. 1474284
.. ... ...
563 North Texas Institute of Neurology and Headache 500
524 Customized Computer Software 500
444 Jim Dinh , DC 500
90 Andor Lab 500
495 Michiana Hematology Oncology , PC 500
[724 rows x 2 columns]
• Largest breach: ’Optum360, LLC’ with 11.5M individuals affected
• Wash. Post on Quest Diag. — Optum 360 is Quest billing contractor
• https://www.washingtonpost.com/business/economy/quest-diagnostics-discloses-breach-of-patient-records/2019/06/03/aa37b556-860a-11e9-a870-b9c411dc4312_story.
