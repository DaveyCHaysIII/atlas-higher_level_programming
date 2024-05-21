# Mid-aged Mutable Python Objects!
### or "Python Objects and their types"
by Davey Hays

## Assignment and References: what's in a name?
***
In python, everything, even ints, floats and chars (called primitives in other languages) are capital O Python Objects, each with their own ```type()```. In C, types have to be very strictly defined before creating a space in memory just snug enough to fit your data, then the data fills the memory space, like so:

```c
int d = 4;
int *ptr = &d;

printf("Value: %d\n", num);                            // 4
printf("Address: %p\n", (void *)&num);                 // Memory Address, 0x7ffdf43d92a8
printf("Size in memory: %lu bytes\n", sizeof(num));    // 4 bytes
```

The focus was specifically around the type, the memory address, and the allocated space in memory- essentially the focus was on the bucket, not on the sand. Python, and other Object Oriented Languages, focus on what's filling the bucket, and the bucket's name, size, shape, color etc almost as an afterthought

```python
d = 4
type(d)        ## returns integer
id(d)          ## returns 140654486853568, and if you convert that to hex...
hex(id(d))     ## returns 0x7F957E7C8640, or the location in memory of d!
d.__sizeof__() ## returns ...24?! ints are huge now!
d.__class__()  ## retruns <class 'int'>

```
As an Object, d has a type, an id, methods, all sorts of things built in to the Object. While all Objects have attributes like this, not all Objects are created equal. 

## Mutable vs Immutable
***

There are two broad categories of Objects in Python, *mutable* and *immutable*. 

| Mutable    | Immutable   |
| ---------- | ---------   |
| Dictionary | Numbers     |
| List       | Strings     |
| Set        | Tuples      |
| Byte Array | Frozen Set  |
|            | Byte        |

*mutable* objects behave just like they sound, through methods or through reassignment they're infinitely changeable, able to add or subtract elements or update elements entirely without so much as a peep from the python interpreter.

```python
my_list = [1, 2, 3, 4, 5]
my_list[0] = 4
print(my_list)  ##returns [4, 2, 3, 4, 5]

```
Immutable Objects, however, cannot be changed once assigned. Strings, numbers, tuples- all immutable once created. 

```python
my_string = 'string'
my_string[0] = 'd'   ##this will result in an error
```
Saying that immutable objects are simply unchangable values however is unfortunately an oversimplification of Immutability - immutable Objects are even stored differently in memory!

## Memory? I thought python was high level!
***
Remember that handy ```id()``` function from before? If you call it on a mutable Object, the id remains the same no matter how many times you mutate it, that id is still the same Object. Not so with Immutable Objects - python will create an entire new object instead. Any time you pass a mutable into a function the mutable will change, while when you pass an immutable to a function a new Object will be created. 

```python
## Mutable Data Types & ID
my_list = [1, 2, 3, 4, 5]
id_one = id(my_list)          ## returns 0x7F957E7B6676
my_list[0] = 4
id_two = id(my_list)          ## returns 0x7F957E7B6676
id_one == id_two              ## returns True

## Immutable Data Types & ID
my_string = "string"
id_one = id(my_string)        ## returns 0x7F957E7C8640
my_string = "strang"
id_two = id(my_string)        ## returns 0x7F957E7C8980
id_one == id_two              ## returns False
```
Python uses a method called "interning" as a method of storing values like integers and commonly used strings to a quickly addressable space in memory, a handy little optimization. Another example of memory optimization with Immutable objects is called integer preallocation- see that's a fancy pants $5 term for saving all the most commonly used integers to an extremely fast place in memory, represented by the constants NSMALLPOSINTS and NSMALLNEGINTS, collectively representing the values -6 through 256. In terms of speed, addressing the integer 256 blows addressing the integer 257 out of the water!

## I heard about a weird exception...
***
Its true, *frozen sets* and *tuples*, while immutable, can contain mutable data (ex. a tuple containing two lists, which are mutable). This works as intended, and was totally intentional. Intentionally. 

## Assignment, Reference, Alias - what's in a name...
***
It turns out that names don't really matter much in python. There's nothing stopping me from calling an Object by the name ```my_object```, and then claiming ```your_object=my_object```. Neither name changes the fact that they are both representations of the uniquely id'd Object in question. In fact, giving an Object another name in such a way is known as an Alias, like a nickname for the Object. Nothing actually changes with the data by doing this. 

## Any other weird things I should know about the topic?
***
So glad you asked! Did you know that instead of the familiar C terms "pass by reference" and "pass by value" its more accurate to say python "passes by assignment" or "call by Object"? Its a whole new way of thinking about data! Yippee!



