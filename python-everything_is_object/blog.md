## "Mid-aged Mutable Python Objects"
# or "Data Mutability and Identity in Python and how it differs from C"
***

Python lumps data types into two big groups: Primitives and Objects. Depending on the primitive and depending on the object, they may be mutable or immutable. Plus there's shenanagins when it comes to their equivilency and their identity! Hopefully by the end of this blog post you'll have a better understanding of how Python handles its data under the hood. 

# Variables in C
***

Variables used to be simple, their names were pretty window dressing for a memory address, a convenient little box perfectly and lovingly shaped to hold your data. 

```c
int d = 0;
char school[] = "school";
school[d] = 'a';
printf(school); //returns "achool"

//notice the char array "school" is mutable, able to change
```

However, python does not live in this idyllic, simple world- no it delves into the deep dark forests of object-oriented programming.

```py
d = 0
b = "school"
b[d] = 'a' ##this gives an error

##strings are immutable in python
```

# Python and Objects
***

Everything in Python that isn't a primitive is an Object, and the Object is what the language is oriented towards. In this unnatural malignation of the natural computing order names are just names, and those names are assigned to Objects, rather than values being assigned to names. The names are almost effemeral, just a representation of what we're currently calling an Object. It's trivial to change the name of an Object, and doing so merely changes its *alias*

```py
a = [1. 2. 3]
b = a 
print(b) ##returns 1, 2, 3
print(a == b) ##returns True
print(a is b) ##returns True
```

Where once names were decorators for physical spaces in memory, now they're just affectations, mere shadows of the Objects themselves. 

# Python Objects and Identity
***

In the previous example, both `a` and `b` were identical, as in, their identities were the same. "Oh" I hear you say, "so Python must be passing by reference, like it does in C". And, deep under the hood, you'd be correct! However, Python wasn't content with one layer of abstraction here, so conflating identity in python with reference in C will quickly get you into trouble. Identity is the pythonic way of thinking of the true representation of an Object, represented by the function `id()`. 

```py
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b) ##returns True
##these two are EQUIVILENT

print(a is b) ##returns False
##these two are NOT the same OBJECT

print(id(a) == id(b)) ##returns False
```
>[!info] writing `a is b` is the same as wriing id(a) == id(b)

If you ran the `id()` function on both of those, you'd get two very different numbers. Even though they are the same, functionally equivilent, they are two distinct Objects, and any changes to one have no bearing on any changes to the other. With very few exceptions, two declared Objects are distinct from each other. 

Finally, let's talk about mutability.

# Python Mutability
***

For something to be *mutable* it needs to be able to *mutate*. The past is *immutable*, as it cannot change, but the future is in an ever mutating state. It's fancy pants rich mcgee talk for "able to change". Strings are an immutable data type, as are ints and floats, as are Tuples `(a, b)`. Its best practice, for obvious reasons, to not pass mutable data types into your functions, as none of that data could now be considered internally safe.

```py
a = [1, 2, 3, 4]
print(id(a)) ##returns a number, ex. 5
func(a) ##does something to a
print(id(a)) ##returns a new number, ex. 6
real_func(a) ##that a and the original a are no longer the same

##this could lead to unexpected behaviors!
```

For more information about data safety, please refer to the official python docs


>Davey Hays is currently a student at Atlas Coding School of Tulsa, OK.

