1/19/2020
Listing Literals:
f = a + a'b + acd + c'
literals are: aa'acdc'
Count all variables and the order they're in. reapeated
Number of literals can tell how many wires coming in you would need.
This helps show where possible points of failure

How to add a variable to a SoP to make it a SoMin
acd 
acd(b+b')
abcd + ab'cd
Basic Properties of Boolean Algebra:
Property	                    Name	                    Description

a(b + c) = ab + ac              Distributive(AND)           (AND) Same as multiplication in regular algebra
a + (bc) = (a + b)(a + c)	    Distributive(OR)            (OR) Not at all like regular algebra

ab = ba
a + b = b + a	                Commutative	                Variable order does not matter. Good practice is to sort variables alphabetically.

(ab)c = a(bc)
(a + b) + c = a + (b + c)	    Associative	                Same as regular algebra

aa' = 0                         Complement(AND)             (AND) Clearly one of a, a' must be 0    1 · 0 = 0 · 1 = 0
a + a' = 1	                    Complement(OR)              (OR) Clearly one of a, a' must be 1   1 + 0 = 0 + 1 = 1

a · 1 = a                       Identity(AND)               (AND) Result of a · 1 is always a's value    0 · 1 = 0   1 · 1 = 1
a + 0 = a	                    Identity(OR)                (OR) Result of a + 0 is always a's value   0 + 0 = 0     1 + 0 = 1

a · 0 = 0
a + 1 = 1	                    Null elements	            Result doesn't depend on the value of a.

a · a = a
a + a = a	                    Idempotent	                Duplicate values can be removed.

(a')'=a	                        Involution                  (0')'=(1)'=0
                                                            (1')'=(0)'=1
(ab)' = a' + b'
(a + b)' = a'b'	                DeMorgan's Law	            Discussed in another section

ab' + a'b = a XOR b             Cole's Law                  Founded it myself bitch
ab + a'b' = a NOT-XOR b

Sum of minterms:
    A canonical form of a Boolean equation is a standard equation form for a function.
    Sum-of-minterms form is a canonical form of a Boolean equation where the right-side expression is a sum-of-products with each product a unique minterm.
    A minterm is a product term having exactly one literal for every function variable.
    A literal is a variable appearance, in true or complemented form, in an expression, such as b, or b'.

Transforming to sum of minterms
    y=ab + a'	sum-of-products, but not sum-of-minterms
    y=ab + a'(b + b')
    y=ab + a'b + a'b'	sum-of-minterms

Example:
y = a(b+bc')
=ab+abc'
=ab(1)+abc'
=ab(c+c')+abc'
=abc+abc'+abc'
=abc+abc'

another rule: y = a + a'b = a + b

Minterm truth tables
x = num of variables
num of rows = 2^x
a'b'=00

Number of AND gates is directly related to the number of 1 in the truth table

Terms with all 3 variables:
Minterms are AND inputs
    Where truth table output is 1
    1 = a, 0 = a'
Maxterms are OR inputs
    Where truth table output is 0
    0 = a, 1 = a'

Designing:
    Capture: The task of precisely describing a circuit's desired behavior.
    Convert(aka implement): The task of translating captured behavior into a circuit, possibly involving simplification

VHDL:
Entity=new object/component
    includes entit declaration(external interface) and architecture body(internal behavior and structure)
Declarations: specifies name and a list of the ports
Ports: input/output. include specified name, direction and type of port
std_logic type defines a bit that can have values 0 or 1

    library IEEE;
    use IEEE.STD_LOGIC_1164.ALL;
    entity DoorOpenDetector is
    port (b,c : in std_logic;
            z : out std_logic);
        end DoorOpenDetector;

    architecture Behavior of DoorOpenDetector is
    begim
        process(b,c) begin
        z <= b and not c;
        end process;
    end Behavior;

'''Big VHDL Code block template'''
entity AND2 is
port(A, B : in bit;
X : out bit);
end AND2;
architecture beh of AND2 is
begin
X <= A AND B;
end beh;
entity XOR2 is
port(A, B : in bit;
X : out bit);
end XOR2;
architecture beh of XOR2 is
begin
X <= A XOR B;
end beh;
entity OR2 is
port(A, B : in bit;
X : out bit);
end OR2;
architecture beh of OR2 is
begin
X <= A OR B;
end beh;
--Entity for a 2 input XOR Gate
--Entity for a half adder

entity halfadder is
port(A, B : in bit;
Sum, CarryOut : out bit);
end halfadder;
architecture structural of halfadder is
component AND2 is -- import AND Gate
port(A, B : in bit;
X : out bit);
end component;
component XOR2 is -- import OR Gate
port(A, B : in bit;
X : out bit);
end component;
--Declare the component for the AND gate
--Declare the component for the XOR gate

begin
u1: XOR2 port map(A, B, Sum);
u2: AND2 port map(A, B, Carryout);
end structural;

entity fulladder is
port(A, B, Cin : in bit;
Sum, CarryOut : out bit);
end fulladder;
architecture structural_2 of fulladder is
component halfadder is
port(A, B : in bit;
Sum, CarryOut : out bit);
end component;
component OR2 is
port(A, B : in bit;
X : out bit);
end component;
signal Q,W,E: bit;
begin
u0: halfadder port map(A, B, Q, W);
u1: halfadder port map(Q, Cin, Sum, E);
u3: OR2 port map(W, E, CarryOut);
end structural_2;

'''END OF VHDL TEST CODE'''

functions = a process
process' sensitivity list: defines inputs and signals whose value ganges cause the process to execute

Bitwise operators
    Operator	Description
    and         Bitwise AND operation
    or          Bitwise OR operation
    not         Bitwise NOT operation
    nand	    Bitwise NAND operation
    nor	        Bitwise NOR operation
    xor	        Bitwise XOR operation
    xnor	    Bitwise XNOR operation

VHDL Keywords
    abs	constant if on	report	type
    access	context	impure	open	restrict	unaffected
    after	cover in or restrict_guarantee	units
    alias	default	inertial	others return until
    all	disconnect	inout	out	rol	use
    and downto is package	ror	variable
    architecture else label	parameter	select	vmode
    array	elsif	library	port	sequence	vprop
    assert end	linkage	postponed	severity	vunit
    assume	entity	literal	procedure	shared	wait
    assume_guarantee	exit	loop	process	signal	when
    attribute	fairness	map	property	sla while
    begin	file	mod	protected	sll with
    block for nand	pure	sra	xnor
    body	force	new	range	srl	xor
    buffer	function	next	record	strong
    bus	generate	nor	register	subtype
    case	generic not reject	then
    component	group	null	release	to
    configuration	guarded	of	rem	transport

VHDL Complex Examples
'''FSM GARAGE DOOR'''
library ieee;
use ieee.std_logic_1164.all;

entity garage_door is
port(A, CLK, RESET: in std_logic;
    Q: out std_logic);
end garage_door;

architecture behav of garage_door is
    -- state definition
    type states is (s0, s1);
    signal state: states;
begin
    process(CLK, RESET)
    begin
        if RESET = '1' then
            state <= s0;
        elsif CLK = '1' and CLK'event then
            case state is
            when s0 =>
                Q <= '0';
                if A = '0' then
                    state <= s0;
                elsif A = '1' then
                    state <= s1;
                end if;
            when s1 =>
                Q <= '1';
                if A = '0' then
                    state <= s1;
                elsif A = '1' then
                    state <= s0;
                end if;
            end case;
        end if;
    end process;
end behav;


"""REGISTER"""
library ieee;
use ieee.std_logic_1164.all;

entity reg is
generic(N: natural := 4);
port(CLK, ENABLE: in std_logic;
    D: in std_logic_vector(N-1 downto 0);
    Q: out std_logic_vector(N-1 downto 0));
end reg;

architecture behav of reg is
begin
    process(CLK)
    begin
        if CLK='1' and CLK'event then
            if ENABLE ='1' then
                Q <= D;
            end if;
        end if;
    end process;
end behav;

"""SHIFT REGISTER"""
library ieee;
use ieee.std_logic_1164.all;

entity shift_register is
port(D, CLK: in std_logic;
    Q: out std_logic);
end shift_register;

architecture behav of shift_register is
    signal temp: std_logic_vector(3 downto 0) := (others => '0');
begin
    process(CLK)
    begin
        if CLK = '1' and CLK'event then
            Q <= temp(3);
            temp(3) <= temp(2);
            temp(2) <= temp(1);
            temp(1) <= temp(0);
            temp(0) <= D;
        end if;
    end process;
end behav;

K-maps
2x2 square for 2 variable function
Like a punnent square to show the relation between the variables

3 variable K-maps:
dont count in binary for last two rows, it goes 11 then 10
because adjacent boxes need to vary in only 1 variable

a\bc 00      01      11     10
0    a'b'c'  a'b'c   a'bc   a'bc'
1    ab'c'   ab'c    abc    abc'

if the the K-map looks like
a\bc 00     01      11      10
0
1    1      1

the two 1's differ between the variabe c' and c,
therefore this can be simplified to just ab
abc'+abc->ab(c'+c)->ab

only powers of 2 can be circled, 1, 2, 4, 8, 16...
multiple circle cancellations
minterms can be circled twice but there is no need for circles over
    minterms that are all already covered
draw largest circles possible
do not leave any minterm uncircled
you can wrap around the edges

a\bc 00     01      11      10
0    1      1
1           1

a'b' + b'c
b'(a'+c)

for 3 variable k-maps
if there is a circle of 4, one of the variables must be true alone
a\bc 00     01      11      10
0          
1    1      1       1       1
simplifies to a

a\bc 00     01      11      10
0                   1       1
1                   1       1
simplifies to b

a\bc 00     01      11      10
0           1       1        
1           1       1        
simplifies to c

4 varialbe minterms
ab\cd 00    01      11      10
00
01
11
10

same rules apply 
corners are still adjacent

Muxes
Multiplexors/Multiplexers
A combinational circuit that passes one of multiple data inouts through a single output
allows 1 input to be passed through based on a selected input

4x1 MUX
4 data iputs
1 output
2 selected inputs

selected inputs = log base 2 (data inputs)
4 ->2
8 -> 3
Truth table:
S1 S0 I3 I2 I1 I0   Y
000000

lengthy^

s1 s0   y
0  0    i0
0  1    i1
1  0    i2
1  1    i3

produces SOP form

this allows us to implement mux into a circuit
3bit 2x1 mux
takes 3 input bits
a1a2a3 and b1b2b3
all a0 bits are in respective i0
same with b bits
1 selected input
uses three 2x1 mux for each digit of the input
shares same selected input

Decoders
a combinational circuit that inputs a N to one of 2^N outputs

2x4 decoder, 2 to 4, converts two inputs to a 1 on exaclty one of 4 outputs
i1 i0   y3 y2 y1 y0
0  0    0  0  0  1
0  1    0  0  1  0
1  0    0  1  0  0
1  1    1  0  0  0

y0 = i1'i0'
y1 = i1'i0
y2 = i1i0'
y3 = i1i0

There is only one 1 in each of the 4 outputs
Expands how 2 bits are displayed

Decoders always leave 1 signal out
so how do you turn it off?
enable input (e)
and e with the i1 and i0 for each y
makes it so e needs to be 1
e = 0; all outputs = 0

Encoder
converts 1 of N inputs to a binary value, using log2(N) outputs
4x2 encoder
d3 d2 d1 d0     e1 e0
0  0  0  1      0  0
0  0  1  0      0  1
0  1  0  0      1  0
1  0  0  0      1  1

if >2 or 0 puts are 1, there has been an error
priority encoders:
determines which inputs are more special

allows errors of >2 1 bits to have priority
d3 d2 d1 d0     e1 e0
0  0  1  1      0  1
gives d1 priority

d0 d1 d2 d3     e1 e0
0  0  0  1      0  0
0  0  1  0      0  1
0  0  1  1      0  1
0  1  0  0      1  0
0  1  0  1      1  0
0  1  1  0      1  0
0  1  1  1      1  0
1  0  0  0      1  1
ETC

Off set: when output should be 0
On set: when output should be 1
Dont Care: when input for this ouput space is not defined (not expected, impossible, not logical)
    Desginer cares whether 1 or 0 is selected

Dont care example
    pressing E and R at the same time: designer decide output
dont cares should be whatever can make the circuit more simple
A B 0 1
0   0 1
1   1 DK
if DK is 0 then circuit must be AXORB or A'B or AB'
if DK is 1 then circuit can be AORB or A + B

greater inputs and more complex circuits will make simplification much more useful

Sequential Circuits
Circuits with stoerd values:
Circuits that use past values
Can at least store 1 bit

Load Registers/Registers
Memory units that serve sequential circuits

Latches
building blocks of registers

SR latch
stores 1 bit
Set-Reset latch
inputs s and r
Uses 2 NOR Gates
output of first is connected to input of second, 
output of second is connected to input of first

s   1   0   0   0  
r   0   0   1   0
q   1   1   0   0

s   r       q
0   0       previously stored bit
0   1       0 'reset'
1   0       1 'set'
1   1       unknwon 'oscillation'

set 1 and reset 1 cause output to oscilate between 0 and 1
waveform of oscillation
s   0   1   0   0   0   0   0   0   0    
r   0   1   0   0   0   0   0   0   0
q   0   0   0   1   0   1   0   1   0...
                  ^oscillation^

Can really mess up your function
Do not apply s and r at the same time

resolution:

stable state in latches:
when currents dont change any gate outputs so the function output is stable

D latch:
stores 1 bit
d - input bit
e - enables bit storing
q - stored bit output

an SR latch with 2 extra AND gates and an inverter
allows for current to pass through for
make s and r internal values
D latches help stop s1r1 oscillation
force SR latch to not take 11 input, solves issue of oscillation
d   e       s   r
0   0       0   0
0   1       0   1
1   0       0   0
1   1       1   0
              ^No 11 for SR

D latch behavior
e   d       q
0   0       previously stored bit (d is ignored)
0   1       previously stoerd bit (d is ignored)
1   0       0 (d bit is stored)
1   1       1 (d bit is stored)

Clocks:
regular oscillating signal used to control when to store bits
bits are stored on rising edge, instant 0 changes to 1
cycle: time between two rising edges, period
frequency: cycles per second in hertz (Hz) 
rising edge: change from 0 to 1
1 Hz frequency = 1 microsecond period
small trianlge indicates the clock input

D flip flop
latches are level sensitive, only storing when level is high
D flip flops store new bits on a clocks rising edge
Flip flops are edge-triggered

D flip flops can be implemented by cascading two D latches
inverted clock on for e on leading and clock for e on following
q from leading is d for following

3-bit register using 3 flip flops stored on rising clock]
leading, leader = master
following, follwing = slave, servant

Load register behavior
ld  operation
0   maintain
1   load

on clock rising edge, if load is 1, new value from input d1 will be stored

reset button to set load to 1 and all inputs to 0

Multi-function registers
clearing a register
clr     ld      Register Function
0       0       maintain
0       1       load
1       0       clear
1       1       maintain

shift registers
using 4x1 mux paired with D FF, a shifter can shift a binary digit number to the right or left (dividing by 2 or multiplying by 2)

multi-function registers have load, clear, and invert
ld      clr     inv     s1      s0      Register Function
0       0       0       0       0       maintain
0       0       1       0       1       invert bits
0       1       0       1       0       clear
0       1       1       0       0       maintain
1       0       0       1       1       load
1       0       1       0       0       maintain
1       1       0       0       0       maintain
1       1       1       0       0       maintain

Depends on the circuit and circuit designers choices
Load clear and invert:
ld      clr     inv     s1      s0      Register Function
0       0       0       0       0       maintain
0       0       1       0       1       load
0       1       0       1       0       clear
0       1       1       0       0       maintain
1       0       0       1       1       incriment
1       0       1       0       0       maintain
1       1       0       0       0       maintain
1       1       1       0       0       maintain

combinational logic - as inputs change, outputs change immediately
sequentional logic - circuits with memory

Finite State Machines
FSM
input
Initial state
outputs
clock input
states
reoccuring indication

On every clock rising edge state changes from one to another
each state has designated outputs
starts at initial state
reoccuring indication allows for another input when high to decide that the state should not change during the next rising edge
    reoccuring indications can be different inputs, inverted, and unique to each state

Pulse
a' reoccuring over state with output 0
when a allows state to pass to pulse high state with output 1
have a allows pass to state pulse slow with output 0
a allows to go back to pulse high again
returns back to initial state with a'


Toggle

Sequence detector
use reoccuring indications and state change indications to allow for the current state to follow desired path to eventually have output = 1

Transitions coming out of state should never overlap each other
    there should be no input combination should lead to 2 states
    there should be no cases left uncovered
    no transition with 2 states

Making a FSM

ex debouncer:
think of the states:
    WaitRise: initial, s = 0, pass a, repeat a
    Skip: s = 1, pass regardless
    WaitFall: s = 1, repeat a, pass a'

Making hardware for FSM
Controllers
State register is the register in the controller holding FSM present state
3 states = 3 inputs 3 outputs
2 inputs are 2 of the outputs
1 input is data
1 output is real output

Ecode the states
00 01 10
each state gets a unique state number

b is data input
needs 2 registers for 2 circulating outputs
n1, n0 are register inputs
p1, p0 are register outputs
present
Make a truth table for p1, p0, b
    p1  p0  b       n1  n0  y
   '0   0'  0 S1    0   0   0
    0   0   1       0   1   0

   '0   1'  0 S2    1   0   1
    0   1   1       1   0   1

   '1   0'  0 S3    0   0   1
    1   0   1       0   0   1

   '1   1'  0  DK   0   0   0     
    1   1   1  DK   0   0   0
                        ^decide states of outputs for y and n

Write boolean functions for n1, n0 and y
n1 = p0p1'
n0 = p0'p1'b
y = p1p0' + p1'p0

Adders:
    Carry ripple adder
    Incrimenter
        Adds 1 to a number
Subtractors:
    Compliment/Invert negative bit and add 1
     1100
    -1010 = 12-10 = 2
    12-10
     1100
    +0110 = 10010 -> 0010
    Ignore leading 1
    
Comparators:
    Compare digits of two numbers
    outputs which one is greater
    outputs gt, lt, edge
    can be implemented using carry-ripple comparators

Signed numbers in Binary:
    Left most digit, MSB used to signify positive or negative

Complementing Binary numbers:
    110101 invert digits: 001010 incriment: 001011
Pos to Neg: invert, add 1
Neg to Pos: sub 1, invert


Color space converter: RGB to CMYK

Carry-look ahead adders:
for the digit:
    0 + 0 = kill
    0 + 1 = propagate
    1 + 0 = propagate
    1 + 1 = generate
uses carry in determined by generate or propagate with a carry

more complex added but can computer faster
less gate delay


Multipliers:
same as by hand multipliers:
except partial products can only be either 0000000 or the multiplicant
 1001
x1010
-----
    0000
   10010
  000000
+1001000
--------
1011010

Array multipliers
and each digit of the bottom multiplicant with corresponding digits of the top
pp0 + pp1(shift left 1) + pp2(shift left 2) + pp3(shift left 3) +...+ ppn(shift left n)

of you instead of summing each partial product:
    requires 2n-1 bit adder
however, for a 4x4 bit multiplication, you can add the 4 bits vertically
using 2 bit adders, could be cheaper


Tristate buffer/three state buffer
a   | z
0    'Z' (high impedance)
1     b


NxM registre file
N M-bit registers
16x32 register file has 16 registers each 32 bits wide
to avoid having 512 wires
    register file consolidates loads through one 32-bit data input
    tradeoff: only 1 register can load at a time

loading register in registre file is known as WRITE operation
    write port: data input, address input, load enable
    read port: 32-bit data output, 4-bit address input, enable input

W_data
W_add
W_en

R_add
R_en

Can have multple read ports, specified with RA_add and RB_add

"""READ FUNCTION CAN WORK ANYTIME, NOT JUST ON CLOCK CYCLES"""
"""Write function can only write on clock edges"""

"""When R_EN is LOW: R_DATA outputs Z"""
"""If reading from an address that hasn't been written into yet, or is not specified, R_DATA = U, undefined"""

"""If you Write into a row at the same time you read that row, it is the new datat"""


Routing congestion and fanout
routing congestion occurs when too many wires are present in a small area
fanout is the number of gates or transistors controlled by a single output of a circuit
    high fanout can result in insufficient current to controll transistors
problems can be sovled with a file register with 1 read and 1 write port


Multi-function registers:
clearing a register: loading zeroes
control input called "clear" or "clr"
can be implemented with 4x1 muxes

registers with clear and load are called multi-function registers


ALUs
datapath component capable of performing various arithmetic and logical functions like add and subtract and AND.
Arithmetic-logic unit
5 4x1 muxes, 1 for each digit of the 2 2-bit inputs, 1 for adding Cin
connected to a 2-bit adder

W and X are the selection inputs for the muxes but also inputs for the ALU

W   X   |   ALU operation
0   0   |   S = A+B
0   1   |   S = A-B 
1   0   |   S = A AND B
1   1   |   S = A 

Bigger ALUs
Control inputs	    ALU operation   	Mux configuration
v	w	x   	                        A	B	cin
0	0	0   	    S = A + B	    A	B	0
0	0	1   	    S = A - B	    A	B'	1
0	1	0   	    S = A + 1	    A	0	1
0	1	1   	    S = 0	0	    0	0
1	0	0   	    S = A AND B	    AB	0	0
1	0	1   	    S = A OR B	    A OR B	0	0
1	1	0   	    S = A XOR B	    A XOR B	0	0
1	1	1   	    S = NOT A	    A'	0	0


SRAM and DRAM
Ram is called random bc it can be access quickly
    volitile
SRAM - static ram, uses 6 transistors to store each bit value by passing the bit into a loop within those transistors
DRAM - dynamic ram, uses 1 transistor and 1 capacitor to store each bit value, by charging the capacitor

SRAM:
    faster
    100x more expensive
DRAM:
    better for fixed size
    better for bigger storage


Memory size
A memory's size may be specified in various ways.

4096x32: Indicates the number of words, and the bits per word.
131,072 bits: Indicates the total number of bits.
16,384 bytes: Indicates the total number of bytes (a byte is 8 bits).
16 KBytes (or 16 KB): Approximate number of bytes. The K is the metric kilo, for 1,000. Note: This method is common but inaccurate, because 16 Kbytes means 16,000 bytes rather than the actual 16,384 bytes.
128 Kbits (or 128 Kb): Indicates the total number of bits. Again, this method is common but inaccurate.



VERY IMPORTANT LECTURE
RTL
Register Transfer Level
circuit is described in terms of data preparation operations

RTL allow for more complex operations than FSM

RTLs have 2 components
Controller:
    Statelogic with registers
Datapath:
    Computes the actual math

Controller + Datapath = Microprocessors

HLSM:
High Level State Machine
    FSM at a higher level
    HLSM have outputs as functions
        D in bit; T out bit
        T = D+5 or T = D-5
    HLSM can use inequality as transition parameters
        very hard to do with FSMs
        can mix inequalities with boolean logic for transitions
        allows for counting with an index
        allows for variables to be used inside controllers
    Specific HLSM notation for logic

HLSM Writing
Item	        C	        Notes
AND: ab, a*b	a && b	
OR: a + b	    a || b	    The || is made from two vertical bar characters, not from the letter "el" (l) or the letter "ay" (I).
NOT: a'	        !a	        The ! comes before a, rather than after.
Equality	    ==	        a == b compares; true if same.
                            In contrast,    y = a assigns y with a's value.
End of action	y = a;
                x = b;	    In C notation, each action is a "statement" that ends with a semicolon.

FOR FSM: Use boolean logic to describe relation

HLSM and loops:
common for loop behavior
2 states: wait(z = 0, i = 0) and genpulse(z = 1, I = I + 1)
input b
output z
variable I(8)
wait -b> genpulse
genpulse -I<5> genpulse
genpulse -!(I<5)> wait
wait -!b> wait 

RTL datapath capabilities:
data transfers: a = b, I = I+1
data ops: c = a*b, a = a+i, b = a+16
control: while I <5:___, if a ==5:___,...

Instantiate: to introduce an item to a circuit
Instance: each instanciated item

Designing the datapath knowing there will be a controller behind it
decide multi-bit input and output
each data output requires a register
    each register has a register load coming in (T_ld)
draw each state output actions
    Or: simplify the output combinations to minimize the mux size and complexity 
connect data ops with a mux to the register
    each register has a selection bit coming in (T_s)

T_ld and T_s are internal inputs which are the output of the controller
Controller decides when to load and what value the mux should display

for internal variables:
    require an extra internal register in datapath along side the register for output 
    mux going into variables register
        inputs of mux are: default/reset value AND output of variables output
        makes another selection bit needed from controller

Using comparators for inequalities:
    inputs E and 6, E > 6
    sends E_gt_6 or E_lt_6 as an output TO the controller!!
    controller uses that input to determine the selection bit above output register
    E_gt_6 is not used inside datapath! only used in controller

How to make controllers from HLSM:
    copy over states and transitions from HLSM
    change output for each state to be in terms of selection and load bits
        this creates the FSM for the controller
