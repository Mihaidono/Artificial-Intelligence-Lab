# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Exercises from https://www.learnpython.org to get accustomed to python


print("Hello, World!")

myList = [1, 2, 3, 4]

print(myList[1], myList[2], myList[0])

for x in myList:
    print(x)

# this will result 7 to the power of 2

squared = 7 ** 2
print(squared)

# puts it 3 times
lotsOfHellos = "hello " * 3
print(lotsOfHellos)

even_numbers = [2, 4, 6, 8]
odd_numbers = [1, 3, 5, 7]
all_numbers = odd_numbers + even_numbers  # concat arrays
print(all_numbers)

print([1, 2, 3] * 3)  # prints the original array 3 times

# This prints out "Hello, John!"
name = "John"
print("Hello, %s!" % name)

# This prints out "John is 23 years old."
name = "John"
age = 23
print("%s is %d years old." % (name, age))

# This prints out: A list: [1, 2, 3]
myList = [1, 2, 3]
print("A list: %s" % myList)

data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."

print(format_string % data)

aString = "Hello world!"
print(aString.index("o"))

aString = "Hello world!"
print(aString.count("l"))  # counts how many 'l's there are

x = 2
print(x == 2)  # prints out True
print(x == 3)  # prints out False
print(x < 3)  # prints out True

name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")

name = "John"
if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")

statement = True
another_statement = False
if statement is True:
    print("The statement was true")
    pass
elif another_statement is True:  # else if
    print("The other statement was true")
    pass
else:
    print("Guess none were true after all")
    pass

x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)  # Prints out True
print(x is y)  # Prints out False

print(not False)  # Prints out True
print((not False) == (False))  # Prints out False

# change this code
number = 16
second_number = False
first_array = [1, 2, 3]
second_array = [1, 2]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

print("")

primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)

# Prints out the numbers 0,1,2,3,4
for x in range(5):
    print(x)

# Prints out 3,4,5
for x in range(3, 6):
    print(x)

# Prints out 3,5,7
for x in range(3, 8, 2):
    print(x)

# Prints out 0,1,2,3,4

count = 0
while count < 5:
    print(count)
    count += 1

# Prints out 0,1,2,3,4

count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

# Prints out only odd numbers -> 1,3,5,7,9
for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)

# Prints out 0,1,2,3,4, and then it prints "count value reached 5"

count = 0
while count < 5:
    print(count)
    count += 1
else:
    print("count value reached %d" % count)

# Prints out 1,2,3,4
for i in range(1, 10):
    if i % 5 == 0:
        break
    print(i)
else:
    print("the loop was broken so it won't print")

numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]

# your code goes here
for number in numbers:
    if number == 237:
        break
    if number % 2 == 1:
        continue
    print(number)


def isPrime(myNumber):
    for iterator in range(2, int(myNumber / 2)):
        if myNumber % iterator == 0:
            return False
    return True


print(*['Is 100 a prime number?', isPrime(100)])
print("Are 100 and 200 prime numbers?", isPrime(100), isPrime(200))
print("Are 100(%s) and 200(%s) prime numbers?" % (isPrime(100), isPrime(200)))

band = 8
name = "Sarah Fer"

print("The band for %(n)s is %(b)s out of 10" % {'n': name, 'b': band})


class MyClass:
    variable = "blah"

    def function(self):
        print("\n   This is a message inside the class.")


myNewObject = MyClass()
myNewObject.function()
print("\nThis is a variable from my class: %s" % myNewObject.variable)


# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00

    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

    def __init__(self, n, k, c, v):
        self.name = n
        self.kind = k
        self.color = c
        self.value = v


# your code goes here
car1 = Vehicle("Fer", "convertible", "red", 60000.00)
car2 = Vehicle("Jump", "van", "blue", 10000.00)
# test code
print(car1.description())
print(car2.description())

print("\n")

phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781

print(phonebook)

# or you can create it like this

phonebook = {"John": 938477566, "Jack": 938377264, "Jill": 947662781}
print(phonebook)

for name, number in phonebook.items():
    print("\nPhone number of %s is %d" % (name, number))

del phonebook["John"]  # or phonebook.pop("John")
print("\n", phonebook)
phonebook["Jake"] = 938273443  # added an entry to the dictionary
print("\n", phonebook)
