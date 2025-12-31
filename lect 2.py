"""Strings & functions"""
name=str(input("Enter your name :"))
fat_name=str(input("Enter your father name :"))
print("Hello! ", name)
print(fat_name, "is your father name.")
print("Your information successfully stored!!!...")
# Strin concatenation
print(name + " " + fat_name)
# F string
name=input("Enter your name :")
age=int(input("Enter your age :"))
print(f"Welcome in the class {name}./n Your age is {age}")
# Indexing
name="Sara Khan"
print(len(name))
str1="Artificial Intelligence"
print(str1[22])
# Slicing
print(str1[0:22])
print(str1[0:])
print(str1[:23])
print(str1[0:len(str1)])
print(str1[-5:-1])
# Strings functions
str2="My name is Ayehsa My bestfriend is Aisha"
str2.endswith("Aisha.")
str2.capitalize()
str2.upper()
str2.find("Aisha")
str2.replace("Aisha","Ayesha")
str2.count("Ayesha")
str3="Data-Science-13"
str3.isalpha()
str2.isalpha()
print(str2.split())
"""Write a programs(WAPs)"""
# WAP to input user’s first name & print its length.
name=str(input("Enter your first name :"))
print(len(name))
# WAP to find the occurrence of ‘$’in a String.
comment="Welcome to the $ world"
print(comment.find("$"))
"""CONDITIONAL STATEMENTS"""
# Check for vote through ages.
age=int(input("Enter your age :"))
if (age>=18 and age<=60):
    print("Yes! You can vote.")
else:
    print("No! You cannot vote.")
# Grade Checker
per=int(input("Enter your percentage :"))
if(per>=80):
    print("You have score A+ grade.")
elif(per>=70):
    print("You have score A grade.")
elif(per>=60):
    print("You have score B grade.")
elif(per>=50):
    print("You have score C grade.")
elif(per>=40):
    print("You have score D grade.")
else:
    print("You're Failed.")
"""Nested If Structure"""
# WAP to check if the age oif the player is greater than 18 and less than 40.
#  If age is greater than 18 then check if he is fit to play cricket or not. 
# if he is fit then include him in national team otherwise not.
age=int(input("Enter your age :"))
fit=input("Are you healthy fit to play cricket Yes or No?")
nationality=input("Enter your nationality.")
if(age>=18 and age<=60):
    if(fit=="Yes"):
        if(nationality=="Pakistani."):
            print("Congragulations! You are now a part of the team.")
        else:
            print("Sorry! You are not Egligible.")
    else:
        print("Sorry! You are not Egligible.")
else:
    print("Sorry! You are not Egligible.")
name=input("Enter your name : ")
if(len(name)==6):
  print("Your name is of acccurate length ")
else:
  print("Your name is has more or less characters than expected ")
"""LIST"""
marks=[98,89,87,85,78,64,58]
print(type(marks))
# Indexing In List
marks=[98,89,87,85,78,64,58]
print(marks)
print("Old Marks were :", marks[3])
marks[3]=90
print("New Marks are :", marks[3])
Student1=["Sheikhsahab",786535,"karachi",99.9]
Student2=["Sheikhzaadi",786535,"Karachi",99.9]
print(Student1[0])
print(len(Student2))
# List Slicing
print(Student1[0:4])
print(Student2[-4:-2])
print(Student2[0:3])
print(Student2[-1::-2])
# LIST METHODS
list1=[1,2,3,4,5,7,8,10,11,13,14,15,16,17,19]
print(list1)
list1.append(6)
list1.append(9)
list1.append(12)
list1.append(18)
list1.append(20)
print(list1)
list1.sort()
print(list1)
list1.sort(reverse=True)
print(list1)
list2=["Areeba","Alisha","Anum","Noor"]
list2.sort()
print(list2)
list2.sort(reverse=True)
print(list2)
list2.sort(reverse=False)
print(list2)
list3=[1,7,8,9,4]
list3.sort(reverse=True)
print(list3)
list3.reverse()
print(list3)
list3.insert(1,2)
list3.insert(2,3)
list3.insert(4,5)
list3.insert(5,6)
list3.insert(9,10)
print(list3)
list4=[3,6,9,12,15]
list4.remove(3)
list4.remove(12)
print(list4)
list4.pop()
### WAP to ask the user to enter names of their 3 favorite movies & store them in a list.
# My teacher method!
movies=[]
movies.append(input("Enter your fav movie name :"))
movies.append(input("Enter your fav movie name :"))
movies.append(input("Enter your fav movie name :"))
print("Your entered fav movies are :", movies)
# My method!
movie1=input("Enter your fav movie name :")
movie2=input("Enter your fav movie name :")
movie3=input("Enter your fav movie name :")
list_of_movies=[movie1, movie2, movie3]
print("Your Entered fav movies are", list_of_movies)
### WAP to check if a list contains a palindrome of elements. (Hint: use copy( ) method).
list1=[1,2,3,4,5,6,7,8]
print(list1)
list2=list1.copy()
list2.reverse()
print(list2)
if list1==list2:
    print("Palindrome!")
else:
    print("Not a palindrome!")
list3=["m","a","d","a","m"]
print(list3)
list4=list3.copy()
list4.reverse()
print(list4)
if list3==list4:
    print("Palindrome!")
else:
    print("Not a palindrome!")
