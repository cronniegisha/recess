#arithmetric operators

#addition
y=50+67
#print(y)

#subtraction
z=50-7
#print(z)

#division
b=50/7
#print(b)

#multiplication
t=50*67
#print(t)

#divide
c=50//7
#print(c)

#modulus
a=50%7
#print(a)

#exponention
f=5**2
#print(f)

#comparison operators
k= -50
j= -500
"""
#greater than
if k>j:
    print("k is greater than j")
else:
    print(k>j)

#less than
if k<j:
    print("k is less than j")
else:
    print(k<j)

#greater than or equal to
if k>=j:
    print("k is greater than or equals to j")
else:
    print(k>=j)

#less than or equal to
if k<=j:
    print("k is less than or equals to j")
else:
    print(k<=j)  

#equals to  
if k==j:
    print("k is equal to j")
else:
    print(k==j)




#logical operators
a=True
b=False

#logical AND
print(a and b)

#logical OR
print(a or b)

#logical NOT
print(not b)
print(not a)


#assignment operators

r=4
print(r)
#add and assign
r+=4
print(r)

#subtract and assign
r-=2
print(r)

#multiply and assign
#add and assign
r*=10
print(r)


#membership operators
shoes=['Adidas','Nike','jordans','balenciaga']

print('Nike' in shoes)
print('pumps' in shoes)
print('Adidas' in shoes)


#identity operators
x=7.0
y=7.00
print(x is y)
print(x is not y)
print(x == y)
print(x != y)

#bitwise operators
a=20
b=1

#bitwise AND operator
result_and= a & b
print(result_and)

#bitwise OR operator
result_or= a | b
print(result_or)

#bitwise XOR operator
result_xor= a ^ b
print(result_xor)

#bitwise NOT operator
result_not= ~a 
print(result_not)

#bitwise lift shift operator
result_left_shift= a << 2
print(result_left_shift)

#bitwise right shift operator
result_right_shift= b>> 2
print(result_right_shift)

"""
#assignment

from tkinter import *

# globally declare the expression variable
expression = ""

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def equalpress():
	total = str(eval(expression))

	equation.set(total)
	expression = ""

def clear():
	global expression
	expression = ""
	equation.set("")

if __name__ == "__main__":
	gui = Tk()
	gui.configure(background="black")
	gui.title("Cronnie_Owomugisha_Calculator")
	gui.geometry("400x350")
	equation = StringVar()
	expression_field = Entry(gui, textvariable=equation)
	expression_field.grid(columnspan=4, ipadx=90)
	
	button1 = Button(gui, text=' 1 ', fg='black', bg='grey',
					command=lambda: press(1), height=3, width=4)
	button1.grid(row=2, column=0)

	button2 = Button(gui, text=' 2 ', fg='black', bg='grey',
					command=lambda: press(2), height=3, width=4)
	button2.grid(row=2, column=1)

	button3 = Button(gui, text=' 3 ', fg='black', bg='grey',
					command=lambda: press(3), height=3, width=4)
	button3.grid(row=2, column=2)

	button4 = Button(gui, text=' 4 ', fg='black', bg='grey',
					command=lambda: press(4), height=3, width=4)
	button4.grid(row=3, column=0)

	button5 = Button(gui, text=' 5 ', fg='black', bg='grey',
					command=lambda: press(5), height=3, width=4)
	button5.grid(row=3, column=1)

	button6 = Button(gui, text=' 6 ', fg='black', bg='grey',
					command=lambda: press(6), height=3, width=4)
	button6.grid(row=3, column=2)

	button7 = Button(gui, text=' 7 ', fg='black', bg='grey',
					command=lambda: press(7), height=3, width=4)
	button7.grid(row=4, column=0)

	button8 = Button(gui, text=' 8 ', fg='black', bg='grey',
					command=lambda: press(8), height=3, width=4)
	button8.grid(row=4, column=1)

	button9 = Button(gui, text=' 9 ', fg='black', bg='grey',
					command=lambda: press(9), height=3, width=4)
	button9.grid(row=4, column=2)

	button0 = Button(gui, text=' 0 ', fg='black', bg='grey',
					command=lambda: press(0), height=3, width=4)
	button0.grid(row=5, column=0)

	plus = Button(gui, text=' + ', fg='black', bg='grey',
				command=lambda: press("+"), height=2, width=4)
	plus.grid(row=2, column=3)

	minus = Button(gui, text=' - ', fg='black', bg='grey',
				command=lambda: press("-"), height=2, width=4)
	minus.grid(row=3, column=3)

	multiply = Button(gui, text=' * ', fg='black', bg='grey',
					command=lambda: press("*"), height=2, width=4)
	multiply.grid(row=4, column=3)

	divide = Button(gui, text=' / ', fg='black', bg='grey',
					command=lambda: press("/"), height=2, width=4)
	divide.grid(row=5, column=3)

	equal = Button(gui, text=' = ', fg='black', bg='grey',
				command=equalpress, height=2, width=4)
	equal.grid(row=5, column=2)

	gui.mainloop()
