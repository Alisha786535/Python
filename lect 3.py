"""TUPLE"""
tuple1=(1,2,3,4)
print(type(tuple1))
# If we do not enter a comma so pyhton understand it as integer value.
tuple1=(1)
print(tuple1)
print(type(tuple1))
# do define as a tuple we need to add comma.
# (Becz sometimes we need to work on future 
# but at the time we have only one attribute.)
tuple1=(1,)
print(tuple1)
print(type(tuple1))
tup1=(1,2,3,4)
print(tup1)
print(type(tup1))
# If we try to access a number in a tuple like this, it doesn't works.
# tup1[1]=5
# we should use tuple.index() method!
tup2=(1,2,3,4,5)
result=tup2.index(5)
print(result)
print(type(tup2))
# we can also access a name or string data by .index() method.
tup3=("Alisha","Areeba","Anum","Noor","Areeba")
final=tup3.index("Noor")
print(final)
# By indexing we can access only the data which comes first but...
# To count a number of same data we should use tuple.count() method.
final=tup3.count("Areeba")
print(final)
# Write a program:
# (i) to count the number of students with the “A” grade
#  in the following tuple. [”C”, “D”, “A”, “A”, “B”, “B”, “A”]
tup4=("C","D","A","A","B","B","A")
tup4.count("A")
# (ii) store the above values in a list & sort them from “A” to “D”
list1=["C","D","A","A","B","B","A"]
list1.sort()
print(list1)
""""DICTIONARY"""
# Make a dictionary.
student1={"Name"    :   "Alisha",
          "Class"   :   "Twelve",
          "English" :   "80",
          "Mathematics" :   "90",
          "Urdu"    :   "69",
          "Grade" :   "A"}
print(type(student1))
print(student1)
# To access any data stored in a dictionary by keyword.
print(student1["Name"])
# To change and any parameters by their keywords stored in a dictionary.
student1["Name"]="Anum"
student1["Class"]="Ten"
print(student1)
student2={"Name"    :   "Alisha",
          "Class"   :   "Twelve",
          "Marks"   :{"English" :   "80",
                      "Mathematics" :   "90",
                      "Urdu"    :   "69"},
          "Grade" :   "A"}
print(type(student2))
print(student2)
student3={"name":"Sara",
          "age":30,
          "city":"Karachi",
          "marks":[78,98.5,87,93,76],
          "grade":("A","A1","B")
          }
print(type(student3))
print(student3)
student4={"name":"Sara",
          "age":30,
          "city":"Karachi",
          "marks":{"chem":78,"physics":98.5,"maths":87}
          }
print(type(student4))
print(student4)
student4["age"]=20
print(student4)
print(student4["marks"]["chem"])
student1.keys()
student2.keys()
student3.keys()
student4.keys()
student1.values()
student2.values()
student3.values()
student4.values()
student4.items()
student3.get('city')
student1.update({"per":86.5})
print(student1)
courses={
    "c1":"python",
    "c2":"java",
    "c3":"C++"
}
student1.update(courses)
print(student1)
skills={
    "s1"    :   "Freelancing",
    "s2"    :   "Sales",
    "s3"    :   "WordPress"
}
student3.update(skills)
print(student3)
### WAP to store following word meanings in a python dictionary:
# 1.   table : “a piece of furniture”,“list of facts & figures”
# 2.   cat : “a small animal”.
Vocabs={"table" :   ["a piece of furniture","list of facts & figures"],
        "cat"   :   "a small animal"
        }
print(Vocabs)
### WAP to enter marks of 3 subjects from the user and store them in a dictionary.
#  Start with an empty dictionary & add one by one.
#  Use subject name as key & marks as value.
subjects={}
sub1=input("Enter First Subject :")
marks1=input("Enter {sub1} marks :")
subjects.update({sub1:marks1})
sub2=input("Enter second  Subject :")
marks2=input("Enter {sub2} marks :")
subjects.update({sub2:marks2})
sub3=input("Enter Third Subject :")
marks3=input("Enter {sub3} marks :")
subjects.update({sub3:marks3})
print(subjects)
"""SETS"""
set1={1,2,3,4,5,6,3,5,4}
print(set1)
print(type(set1))
# To initialize an empty set
set2=set()
print(set2)
print(type(set2))
"""SET METHODS"""
set1
set1.add(9)
set1
set1.remove(6)
set1
set1.remove(2)
set1
set1.clear()
set1
set2={"Alisha","Areeba","Noor","Anum"}
set2
print(type(set2))
set2.pop()
set2
set3={1,3,4,6,7,8,}
set4={2,4,6,7,9}
resultant=set3.union(set4)
resultant
result=set3.intersection(set4)
print(result)
### You are given a list of subjects for students.
#  Assume one classroom is required for 1 subject.
#  How many classrooms are needed by all students.
# “python”, “java”, “C++”, “python”, “java”, “java”, “python”, “java”, “C++”, “C”
classes={"python", "java", "C++", "python", "java", "java", "python", "java", "C++", "C"}
print(classes)
print(len(classes))
### Figure out a way to store 9 & 9.0 as separate values in the set

# (You can take help of built-in data types)
set5={9,'9.0'}
print(set5)
"""LOOPS"""
# WHILE LOOPS
print("Sara")
print("Sara")
print("Sara")
print("Sara")
print("Sara")
print("Sara")
count=1
while count<=5:
    print(count,". Sara")
    count+=1
print("loop ended!")
count=5
while count>=1:
    print(count,".Sara")
    count-=1
print("Loop ended")
password=input("Enter password:  ")
while(password!="hello"):
  password=input("Enter password:  ")
print("Access granted!!!")
# Q1: Print numbers from 1 to 100.
count=1
while count<=100:
   print(count)
   count+=1
print("loop ended")
# Q2: Print numbers from 100 to 1.
count=100
while count>=1:
   print(count)
   count-=1
print("loop complete")
# Q3: Print the multiplication table of a number n.
n=int(input("Enter Number of Table :"))
c=1
while c<=10:
   print(c*n)
   c+=1
print("This is the table of/n",n," Now Enter any other number of which the table you want")
# Q4: Print the elements of the following list using a loop: [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
num=[1, 4, 9, 16, 25, 36, 49, 64, 81,100]
i=0
while i<len(num):
  print(num[i])
  i+=1
# Q5: Search for a number x in this tuple using loop: [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
## Break
tup=(1, 4, 9, 16, 25, 36, 49, 25, 64, 81,100,25)
x=81
i=0
while i<len(tup):
  if(tup[i]==x):
    print(f"{x} found at index {i}")
    break
  else:
    print("finding....")
  i+=1
#   Continue
i=1
while i<=10:
  if i%3==0:
    i+=1
    continue
  print(i)
  i+=1
i=1
while i<=15:
  if i%2==0:
    i+=1
    continue
  print(i)
  i+=1
