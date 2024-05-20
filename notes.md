importing

from FILE import THING - file being a file in PATH without extention, THING being a variable, function, w/e from that file

if __name__ == "__main__": -makes it not run interactively?

print("{}".format(a)) - sticks the var a in place of the brackets, like printf in c
len() - length of something
dir() - contents of someting in alpha order


lists are very similar to arrays but are growable and can contain w/e different data sets you want

list = [1, 2, "string", 1.234]


git add * test

hjkl wb _$
iaIAoO
f+char ,,,;;; t+char F+ T+
u ctrl+r
vyp

advanced 
df{ - deletes from cursor up to and including squirley brace
dt{ - deletes from cursor up to but not including squirley brace
yf) - copies from cursor up to and including closed paren (copy a whole function name!)
up to and including { hello from squirrley }

class
fields
methods
both are the class attributes
instance variables belong to that instance (self.whatever)
class variables belong to the class (regular variables)
@classmethod
def howmany(cls) - that cls is a decorator that shows it is a class method

-subclasses-
class Schoolmember:
    def __init__(self, name, age)
...

class Teacher(Schoolmember):
    def __init__(self, name, age, salary)
        Schoolmember.__init__(self, name, age)
        ...


//////////////////////////////////////////


with open("myfile.txt") as f:
    for line in f:
        print(line, end="")  ##opens, prints all lines and closes myfile.txt

f = open(filename, mode, encoding)


/////////////
