
#inheritance
# class Dog(Animal):

"""
class Animal:
    def __init__(self, name):
        self.name = name


    def eat(self):
        print(f"{self.name} is eating..." )

class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking...woofff" )


class Cat(Animal):
    def purrs(self):
        print(f"{self.name} is purring...purrrrr" )

#creating objects
animal = Animal("animal")
dog=Dog("sparky")   
cat=Cat("kitty")

#invoking methods
animal.eat()
dog.bark()
cat.purrs()

#demonstrating inheritance exercise

class Shape():
    def __init__(self, area, perimeter):
        self.area = area
        self.perimeter = perimeter

class circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        self.area = 3.14 * radius ** 2
        self.perimeter = 2 * 3.14 * radius

class rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = self.width * self.height
        self.perimeter = self.width + self.height

CIRCLE=circle(4)
RECTANGLE=rectangle(10,20)

print(CIRCLE.area)  
print(CIRCLE.perimeter)
print(RECTANGLE.area)
print(RECTANGLE.perimeter)


#multiple inheritance

class Animal:
    def __init__(self, name):
        self.name = name


    def eat(self):
        print(f"{self.name} is eating..." )

class Flyable:
    def fly(self):
        print(f"{self.name} is flying..." )

class Bird(Animal, Flyable):
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def display_info(self):
        print(f"{self.name} is a {self.species}" )
        print(f"{self.name} is eating..." )
        print(f"{self.name} is flying..." )

#creating objects
bird = Bird("duck", "bird")

#invoking methods
bird.eat()
bird.fly()
bird.display_info()


#method overriding
class Animal:
    def make_sounds(self):
        print("making loud sounds...")

class Dog(Animal):
    def make_sounds(self):
        print("barking...")

class Cat(Animal):
    def make_sounds(self):
        print("purring...")

class Goat(Animal):
    def make_sounds(self):
        print("bleating...")

#creating objects

cat = Cat("kitty")
goat = Goat("Gulugulu")

#invoking methods
cat.make_sounds()
goat.make_sounds()



#polymorphism

class Shape:
    def __init__(self, area, perimeter):
        pass

class Rectangle (Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = self.width * self.height
        self.perimeter = self.width + self.height

class Circle (Shape):
    def __init__(self, radius):
        self.radius = radius
        self.area = 3.14 * radius ** 2
        self.perimeter = 2 * 3.14 * radius

#creating objects
rectangle = Rectangle(5,7)
circle = Circle(8)

#calculate and display areas
print("area of rectangle:", rectangle.area) 
print("area of circle:", circle.area)



# abstraction
#abstraction exercise

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

    def perimeter(self):
        return 2 * 3.14 * self.radius

r = Rectangle(5, 10)
print("Area of rectangle:", r.area())
print("Perimeter of rectangle:", r.perimeter())

c = Circle(5)
print("Area of circle:", c.area())
print("Perimeter of circle:", c.perimeter())

"""

#assignment 
from tkinter import *

class ReceiptPrinter:
    def __init__(self, master):
        self.master = master
        master.title("Cronnie Owomugisha Receipt Printer")

        self.label = Label(master, text="Enter your receipt information below:")
        self.label.pack()

        self.name_label = Label(master, text="Name:")
        self.name_label.pack()

        self.name_entry = Entry(master)
        self.name_entry.pack()

        self.item_label = Label(master, text="Item:")
        self.item_label.pack()

        self.item_entry = Entry(master)
        self.item_entry.pack()

        self.price_label = Label(master, text="Price:")
        self.price_label.pack()

        self.price_entry = Entry(master)
        self.price_entry.pack()


        self.submit_button = Button(master, text="Submit", command=self.print_receipt)
        self.submit_button.pack()

    def print_receipt(self):
        name = self.name_entry.get()
        item = self.item_entry.get()
        price = self.price_entry.get()

        if not name or not price:
            print("Please enter details.")
            return

        receipt = f"Name: {name}\nPrice: {price}\nItem: {item}"

        print(receipt)

        self.name_entry.delete(0, END)
        self.item_entry.delete(0, END)
        self.price_entry.delete(0, END)


root = Tk()
my_gui = ReceiptPrinter(root)
root.mainloop()






