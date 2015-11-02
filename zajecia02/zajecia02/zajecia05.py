#Czytanie plików, funkcja open():

def readfoofilev1():
    f = open("foo.txt") # Returns a file object
    line = f.readline() # Invokes readline() method on file
    while line:
        print(line,end='') 
        line = f.readline()
    f.close()

#readfoofilev1();
#python pozwala na iterowanie po opiektach w p?tli:
def readfoofilev2(name):
    for line in open(name):
        #print(line, end='')
        print(line)

#readfoofilev2("foo.txt");

#Aby zapisa? co? do pliku mo?emy sko?ysta? z nasepuj?cej konstrukcji:
def pisaniedopliku():
    #f = open("out","a") # Open file for writing (appending)
    f = open("out","w") # Open file for overwriting
    year = 1901
    while year <= 2015:
        print("%3d " % (year),file=f)
        f.write("%3d\n" % year)
        year += 1
    f.close()
#pisaniedopliku()

#Przy okazji: formatowanie stringów: 
#https://docs.python.org/2/library/stdtypes.html#string-formatting-operations
# np: print("%3d %0.2f" % (year,principal))

#Stringi a la listy:
def stringialalisty():
    a = "Hello World"
    b = a[4]
    c = a[:5]
    d = a[6:]
    e = a[3:8]
    print(' a: ', a, ';\n b: ', b, ';\n c: ', c,' ;\n d: ', d,' ;\n e: ', e)

#stringialalisty()

# List vs. tuple vs. set vs. dictionaty
def listvsrest():
    names = [ "Dave", "Mark", "Ann", "Phil" ]
    stock = ('GOOG', 100, 490.10)
    s = set([3,5,9,10])
    stock = {
        "name" : "GOOG",
        "shares" : 100,
        "price" : 490.10
    } #mo?na pisa? w wielu liniach

#List - by?o w zesz?ym tygodniu:
def odwolaniadoelementu():
    names = [ "Dave", "Mark", "Ann", "Phil" ]
    print(names[1:2])
    a = [1,"Dave",3.14, ["Mark", 7, 9, [100,101]], 10]
    print( a[1], '\n', a[3][2] , '\n', a[3][3][1])
#odwolaniadoelementu()

#Korzystanie z argumentów do skryptu:
import sys
print(sys.argv[0], sys.argv[1])

#samodzielne ?wiczenie: wygeneruj tabelk? w excelu z liczbami od 1 do 1000.
#przekopuj j? do pliku tekstowego i i potem wczytaj do do lisry 
#w pythonie. napisz funkcj?
#znajduj?c? najwi?ksz? liczb?, sum? cyfr i ?redni? liczb.
#nazw? pliku podaj jako argument do skryptu i przeka? do funkcji
#wskazówka: # Convert all of the input values from strings to floats
#fvalues = [float(line) for line in lines]

#tuple
'''
To create simple data structures, you can pack a collection of values together into a sin-
gle object using a tuple.You create a tuple by enclosing a group of values in parentheses
like this:
stock = ('GOOG', 100, 490.10)
address = ('www.python.org', 80)
person = (first_name, last_name, phone)
Python often recognizes that a tuple is intended even if the parentheses are missing:
stock = 'GOOG', 100, 490.10
address = 'www.python.org',80
person = first_name, last_name, phone
For completeness, 0- and 1-element tuples can be defined, but have special syntax:
a = () # 0-tuple (empty tuple)
b = (item,) # 1-tuple (note the trailing comma)
c = item, # 1-tuple (note the trailing comma)
The values in a tuple can be extracted by numerical index just like a list. However, it is
more common to unpack tuples into a set of variables like this:
name, shares, price = stock
host, port = address
first_name, last_name, phone = person
Although tuples support most of the same operations as lists (such as indexing, slicing,
and concatenation), the contents of a tuple cannot be modified after creation (that is,
you cannot replace, delete, or append new elements to an existing tuple).This reflects
the fact that a tuple is best viewed as a single object consisting of several parts, not as a
collection of distinct objects to which you might insert or remove items.
Because there is so much overlap between tuples and lists, some programmers are
inclined to ignore tuples altogether and simply use lists because they seem to be more
flexible.Although this works, it wastes memory if your program is going to create a
large number of small lists (that is, each containing fewer than a dozen items).This is
because lists slightly overallocate memory to optimize the performance of operations
that add new items. Because tuples are immutable, they use a more compact representa-
tion where there is no extra space.
'''
#Przyk?ad:
'''
# File containing lines of the form " name , shares , price "
filename = "portfolio.csv"
portfolio = []
for line in open(filename):
    fields = line.split(",") # Split each line into a list
    name = fields[0] # Extract and convert individual fields
    shares = int(fields[1])
    price = float(fields[2])
    stock = (name,shares,price) # Create a tuple (name, shares, price)
    portfolio.append(stock) # Append to list of records
'''
#cwiczenie:Zgadnij co zwróci print(portfolio[0]). Utwórz plik 
#"portfolio.csv" z dwiema linijkami w podanym formacie i 
#zobacz czy odpowiedzia?a(e)s dobrze.
#zbior czyli set:


#A set is used to contain an unordered collection of objects.To create a set, use the
#set() function and supply a sequence of items such as follows:
#s = set([3,5,9,10]) # Create a set of numbers
#t = set("Hello") # Create a set of unique characters
#Unlike lists and tuples, sets are unordered and cannot be indexed by numbers.
##Moreover, the elements of a set are never duplicated. For example, if you inspect the
#value of  t from the preceding code, you get the following:
#>>> t
#set(['H', 'e', 'l', 'o'])
#Sets support a standard collection of operations, including union, intersection, differ-
#ence, and symmetric difference. Here’s an example:
#a = t | s # Union of t and s
#b = t & s # Intersection of t and s
#c = t – s # Set difference (items in t, but not in s)
#d = t ^ s # Symmetric difference (items in t or s, but not both)
#New items can be added to a set using  add() or update() :
#t.add('x') # Add a single item
#s.update([10,37,42]) # Adds multiple items to s
#An item can be removed using  remove() :
#t.remove('H')

#Slowniki
#A dictionary is an associative array or hash table that contains objects indexed by keys.
#You create a dictionary by enclosing the values in curly braces ( { } ), like this:
#stock = {
#"name" : "GOOG",
#"shares" : 100,
#"price" : 490.10
#}
#To access members of a dictionary, use the key-indexing operator as follows:
#name = stock["name"]
#value = stock["shares"] * shares["price"]
#Inserting or modifying objects works like this:
#stock["shares"] = 75
#stock["date"] = "June 7, 2007"
#Although strings are the most common type of key, you can use many other Python
#objects, including numbers and tuples. Some objects, including lists and dictionaries,
#cannot be used as keys because their contents can change.
#A dictionary is a useful way to define an object that consists of named fields as
#shown previously. However, dictionaries are also used as a container for performing fast
#lookups on unordered data. For example, here’s a dictionary of stock prices:
#prices = {
#"GOOG" : 490.10,
#"AAPL" : 123.50,
#"IBM" : 91.50,
#"MSFT" : 52.13
#}
#An empty dictionary is created in one of two ways:
#prices = {} # An empty dict
#prices = dict() # An empty dict
#Dictionary membership is tested with the  in operator, as in the following example:
#if "SCOX" in prices:
#p = prices["SCOX"]
#else:
#p = 0.0
#This particular sequence of steps can also be performed more compactly as follows:
#p = prices.get("SCOX",0.0)
#To obtain a list of dictionary keys, convert a dictionary to a list:
#syms = list(prices) # syms = ["AAPL", "MSFT", "IBM", "GOOG"]
#Use the  del statement to remove an element of a dictionary:
#del prices["MSFT"]
#Dictionaries are probably the most finely tuned data type in the Python interpreter. So,
#if you are merely trying to store and work with data in your program, you are almost
#always better off using a dictionary than trying to come up with some kind of custom
#data structure on your own


#s?owo kluczowe yield:
#Instead of returning a single value, a function can generate an entire sequence of results
#if it uses the  yield statement. For example:
def countdown(n):
    print("Counting down!")
    while n > 0:
        yield n # Generate a value (n)
        n -= 1

#c = countdown(5)
#print(c.__next__())
#print(c.__next__())
#print(c.__next__())
#print(c.__next__())
#print(c.__next__())


http://stackoverflow.com/questions/354883/how-do-you-return-multiple-values-in-python