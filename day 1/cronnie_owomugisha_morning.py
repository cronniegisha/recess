#control flow
#if clause
#if condition 1:
#print("true")
 
#input
#age=int(input())
#if age<18:
 #   print("you are underage")
#elif age>=18 and age<65:
 #   print("you are an adult")
#else:
 #   print("you are a senior citizen")

#have a variable
#age=45
#if age<18:
 #   print("you are underage")
#elif age>=18 and age<65:
 #   print("you are an adult")
#else:
  #  print("you are a senior citizen")

#loops
#cars=["Tesla","Jeep","Ford","Toyota","BMW",]
#for car in cars:
  #  print(car)

#fruits=["grapes","apples","kiwi","mango","oranges",]
#for fruit in fruits:
 #   print(fruit)    

#fruits=["grapes","apples","kiwi","mango","oranges",]
#fruits_count=0
#while fruits_count< len(fruits):
 #   print(fruits_count)
  #  fruits_count+=1

#x=0
#while x<10 and x>2:
 #   print(x)
  #  if x==8:
   #     break
   # x+=1

#break and continue statements
#break terminates a loop
#for number in range(1,8):
 #   if number==4:
  #      break
   # print(number)

#continue skips the number
#for number in range(1,8):
 #   if number==4:
  #      continue
   # print(number)

#exception handling
#try:
#   age=int(input())
#except Exception:
 #   print("Interger needed")
#else:
 #   print(age)
#finally:
 #   print("you are most welcome")
    

mentally={
   10:"Its all smiles and sunshine.",
   9:"You are doing well.",
   8:"Keep pushing!",
   7:"Almost there!",
   6:"We will get there. ",
   5:"Have you had enough rest?",
   4:"What's going on?",
   3:"Are you feeding?",
    2:"Do you want to talk?",
}
mental_status=input("How do you rate today?")

if mental_status in mentally:
    print(mentally[mental_status])
else :
    print("let me connect you to our helpline")