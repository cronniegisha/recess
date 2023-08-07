
"""
regular expressions
generators
decorators
context manager
multithreading and multiprocessing

"""
#regular expressions
"""
summary
\d: matches any digit(0-9)
\w: matches any alphanumeric character
\s: matches any whitespace character
.: matches any character except a newline character
^: matches the beginning of a string
*: matches zero or more characters
+: matches one or more characters
?: matches zero or one characters
{n}: matches exactly n characters   
{n,}: matches at least n characters
{n,m}: matches between n and m characters
[]: matches any character within the brackets
[^]: matches any character not within the brackets
^: matches the start of the line
$: matches the end of the line

#matching and searching
#regex re.match(), regex.search(), regex.findall(), regex.find

#example1
import re
text ="Hi there, my name is Cronnie and I am in year 2 ."

match=re.search(r"^\w+$", text)
if match:
    print("match: ",match.group)

matches=re.findall(r"^\d", text)
print("matches: ",matches)

#example2

def validate_email(email):
    pattern= r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return True
    else:
        return False
    
email1 ="cronniegisha@gmail.com"
email2 ="cronnie.gisha@gmail.com"

print(validate_email(email1))
print(validate_email(email2))



#generators and iterators
#"yield" generator 
#iterator '__iter__' "__next__" iterator

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
for i in range(1,10):
    print(factorial(i))
"""

#using the iterator
def squares():
    for i in range(10):
            yield i**2

#create an iterator object

squares_iterator=squares()

for i in range(6):
      print(next(squares_iterator))

# Decorators @my_decorator
# Decorators in python allow you to modify the behaviour of functions or classes without 
#directly changing their source code 
"""
def my_decorator(func):
    def inner():
        print("This is a decorator")
        func()
    return inner()

@my_decorator
def outer_decorator(func):
    print("This is an outer decorator")

outer_decorator()    
"""
# context manager 
# Is an objesct that defines a temporary context for a block of code
# example 1
# demonstrating a context manager to open a file and return a context instance
"""
def open_file(filename):
    
   file = open(filename, 'r')
   def __enter__():
       return file
   
   def __exit__(self, exc_type, exc_val, exc_tb):
       file.close()
       return __enter__ .__exit__

with open_file("my_file.txt") as f:
    contents = f.read()
"""    
# example 2, context manager using time series
"""
import time

class Timer:
    def __enter__(self):
      self.start_time = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        end_time = time.time()
        execution_time = execution_time
        print("Execution time:", execution_time)

# with example usage
with Timer():
    # measure execution time
    time.sleep(1)      
"""
# Multithreading and multi-multiplexing
# techeniques that can be used to improve performance of a python program

# Multithreading is a technique where multiple threads are created within a single process
# Multiplexing is a technique where multiple threads 

# example of multithreading
"""
import threading

def task(name):
    print (f"Running task {name}")

#create multiple threads
threads =[]
for i in range(10):
    t = threading.Thread(target=task, args=(f"Thread {i}",))
    threads.append(t)
    t.start()

# wait for all thraed to finish

for t in threads:
    t.join()
"""
# Example 4: demonstrate for multiprocessing
"""
import multiprocessing

def process_task(name):
    print (f"Processing task {name}")

# create a pool of processes
pool =multiprocessing.Pool(processes=5)

# submit the multiple task to the pool
for i in range (6):
    pool.apply_async(process_task, args=(f"Process {i}",))

# close the pool and wait for the processes to finish
pool.close()
pool.join()

# Example 5: use of multithreading and multiprocessing
import threading
import multiprocessing

def task(name):
    print (f"Running task {name} thread {threading.current_thread().name}with process (multiprocessing.current_process().name)")

# craete multiple thraeds
threads =[]
for i in range(10):
    t = threading.Thread(target=task, args=(f"Thread {i}",))
    threads.append(t)
    t.start()

# wait for all threads to finish
for t in threads:
    t.join()

# Assignment 
# 1a) Show a context manager for file handling that automatically opens and closes a file

class File():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
         
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    #The __enter__ method opens the test.txt file in write mode(setup operation) and returns a file object to variable f.
     
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()
    #The __exit__ method closes the test.txt file(teardown operation).

# loading a file
with File('test.txt', 'w') as f:
    f.write('Test')
 
print(f.closed)

# b) Show a context manager for managing a database connection
import sqlite3

class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()

#The '_enter' method creates a new connection to the database and returns it, while the 'exit_' method closes the connection. 

with DatabaseConnection('my_database.db') as conn:
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM my_table')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# I use the `with` statement to create a new instance of the `DatabaseConnection` class, which automatically opens and closes the database connection.

"""
# c) Show a multithreading and multiprocessing  that allows us to run the function for different amounts of time.

import threading
import multiprocessing
import time

def my_function(seconds):
    print(f'Starting function for {seconds} seconds')
    time.sleep(seconds)
    print(f'Function finished after {seconds} seconds')

# Multi-threading
threads = []
for i in range(1, 6):
    t = threading.Thread(target=my_function, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

# Multi-processing
processes = []
for i in range(1, 6):
    p = multiprocessing.Process(target=my_function, args=(i,))
    processes.append(p)
    p.start()

for p in processes:
    p.join()


