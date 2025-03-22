'''1. Write a program that accepts a string from user. Your program should count and display number of 
vowels in that string.  '''
'''name=input("Enter a string")
print(len(name))
count=0
for i in range(len(name)):
    if(name[i]=="a" or name[i]=="e" or name[i]=="i" or name[i]=="o" or name[i]=="u"):
        count+=1
print(f"The number of vowels in the {name} are {count}")'''

'''2. Write a program that reads a string from keyboard and display: 
* The number of uppercase letters in the string 
upper=0
word=input("Enter a word")
for i in range(len(word)):
    if word[i].isupper():
        upper+=1
print(f"in {word} there are {upper} capital letter")

* The number of lowercase letters in the string 
lower=0
word2=input("Enter a word")
for i in range(len(word2)):
    if word2[i].islower():
        lower+=1
print(f"in {word2} there are {lower} small letter")

* The number of digits in the string
string2=input("Enter a string")
numcount=0
for i in range(len(string2)):
    if(string2[i].isdigit()):
        numcount+=1
print(f"there are {numcount} digits in the word {string2}")
'''
'''* The number of whitespace characters in the string
string4=input("Enter a string")
print(string4.count(" "))'''

'''3. Write a Python program that accepts a string from user. Your program should create and display a 
new string where the first and last characters have been exchanged. 
For example if the user enters the string 'HELLO' then new string would be 'OELLH' 

string1=input("Enter a string")
first=string1[0]
last=string1[-1]
middle=string1[1:-1]
word=last+middle+first
print(f"the string {string1} after exchanging becomes {word}")'''

'''4. Write a Python program that accepts a string from user. Your program should create a new string in 
reverse of first string and display it.
string3=input("Enter a string")
rev_String3=string3[-1: :-1]
print(rev_String3)'''

'''5. Write a Python program that accepts a string from user. Your program should create a new string by 
shifting one position to left.

word=input("Enter a string")
firstpart=word[0]
middlepart=word[1:-1]
last=word[-1]
new_Word=middlepart+last+firstpart
print(new_Word)'''

'''6 Write a program that asks the user to input his name and print its initials. Assuming that the user 
always types first name, middle name and last name and does not include any unnecessary spaces. 
For example, if the user enters Ajay Kumar Garg the program should display A. K. G. 
Note:Don't use split() method '''
'''name=input("Enter your full name ")
print(name)
first=name[0]
middle=name.find(" ")
last=name.rfind(" ")
print(f"{first}.{name[middle+1]}.{name[last+1]}")'''

'''7. A palindrome is a string that reads the same backward as forward. For example, the words dad, 
madam and radar are all palindromes. Write a programs that determines whether the string is a 
palindrome. 
Note: do not use reverse() method  '''

'''str1=input("Enter a string")
rev_str=str1[-1::-1]
print(rev_str)
if(str1==rev_str):
    print("the string is palindrome")
else:
    print("The string is not a palindrome")'''

'''8. Write a program that display following output: 
SHIFT 
HIFTS 
IFTSH 
FTSHI 
TSHIF 
SHIFT '''

'''str2=input("Enter a string")
print(str2)
for i in range(len(str2)+1):
    print(str2[i:]+str2[:i])'''

'''9. Write a program in python that accepts a string to setup a passwords. Your entered password must 
meet the following requirements: 
The password must be at least eight characters long. 
It must contain at least one uppercase letter. 
It must contain at least one lowercase letter. 
It must contain at least one numeric digit. 
Your program should should perform this validation.  '''

'''password=input("Enter the password for verification")

issmall=False
isbig=False
isnum=False
valid_length = len(password) >= 8
for word in password:
    if(word.islower()):
        issmall=True
    if(word.isupper()):
        isbig=True
    if(word.isdigit()):
        isnum=True
if(isnum and isbig and issmall):
    print("The password is valid")
else:
    print("password is not valid")
        
'''
