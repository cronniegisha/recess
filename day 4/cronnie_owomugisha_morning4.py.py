#classes
#abstraction
#inher

"""'
#object 
class Person:
    def _init_(self, name, age,course):
        self.name=name
        self.age= age
        self.course= course
        
    def greet(self):
        print("hello, my name is", self.name)
        print("i am ",self.age," years old")
        print("i am studying ", self.course)

# Person object
my_person=Person("Cronnie",22,"BSSE")
my_person1=Person("Christbell",26,"BBA")

#invoke 

my_person.greet()


# Exercise
# calculate employee bonuses (0.15) of salary


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def bonus(self):
        return self.salary * 0.15


e1 = Employee("Cronnie", 150000)
e2 = Employee("Lynn", 230000)

print(e2.name + "your bonus is:" + e2.bonus)
print(e1.name + "your bonus is:" + e1.bonus)

# encapsulation
# Main goals of encapsulation are

#1. To hide the implementation details of an object from other objects.
#2. To protect the object from changes 
#3.To protect the object from external changes
#4.Code oragnization and modularity



# Example 4 : bank account
class BankAccount(object):
    def _init_(self, account_number, balance):
        self.account_number = (
            account_number  # Encapsulates the account number attribute
        )
        self.balance = balance  # Encapsulates the balance attribute

    def deposit(self, amount):
        self.balance += amount  # encapsulates the deposit amount attribute

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("withdraw amount", amount, "balance:", self.balance)
        else:
            print("insufficient balance")

    def get_balance(self):
        return self.balance


# Bank Object
my_account = BankAccount("0037890678923", 1000)

# accessing accounts
my_account.get_balance()
my_account.deposit(500)
my_account.get_balance()
my_account.withdraw(500)
my_account.get_balance()


# exercise 5:Covert temperature (37 c) from celsius to fahrenheit


class Temperature:
    def __init__(self, celsius):
        self.__celsius = celsius

    def get_celsius(self):
        return self.__celsius

    def set_celsius(self, celsius):
        self.__celsius = celsius

    def get_fahrenheit(self):
        return (self.__celsius * 9/5) + 32

temp = Temperature(37)
print(f"{temp.get_celsius()}°C is equal to {temp.get_fahrenheit()}°F")

"""




# Assignment1:  Show encapsulation with employee information to give a
# pay increamentation (Salary with employee information to new_salary)e.g from 850000 to 1000000

class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def get_name(self):
        return self.__name

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

    def increment_salary(self):
        self.__salary += (self.__salary * 50) / 100

emp1 = Employee("Salima", 50000)
emp2= Employee("Treyz", 1000000   )
print(emp1.get_name())
print("Salary:", emp1.get_salary(), end=" -> ")
emp1.increment_salary()
print(emp1.get_salary())

print("*********************************************************************************************")
print(emp2.get_name())
print("Salary:", emp2.get_salary(), end=" -> ")
emp2.increment_salary()
print(emp2.get_salary())
