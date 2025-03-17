'''1) A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
Ask user for their salary and year of service and print the net bonus amount.
    
salary = float(input("Enter your salary: "))
years_of_service = int(input("Enter your years of service: "))

if years_of_service > 5:
    bonus = salary * 0.05 
    print("Congratulations! Your bonus amount is:", bonus)
else:
    print("Sorry, you are not eligible for a bonus.")'''

''''
'2) Write a program to check whether a person is eligible for voting or not. (accept age from user) if age is greater than 17 eligible otherwise not eligible
age = 14
if age >= 18:
    print("Your are eligible for vote")
else:
    print("Your are not eligible for vote")'''


'''3) Write a program to check whether a number entered by user is even or odd.

add_number = int(input("Add a number"))

if add_number  % 2 == 0:
    print ("your number is even ")
else:
    print ("Your number is odd")'''

'''
4) Write a program to check whether a number is divisible by 7 or not.
Show Answer
add_number = int(input("Add a number"))

if add_number  % 7 == 0:
    print ("your number can be divisible by 7 ")
else:
    print ("Your number can't be divisible by 7")'''

'''
5) Write a program to display 
"Hello" if a number entered by user is a multiple of five , otherwise print "Bye".
add_number = int(input("Add a number"))

if add_number  % 5 == 0:
    print ("hello! ")
else:
    print ("Bye Bye! ")
'''

'''
6) Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria :
     Unit                                                     Price  
uptp 100 units                                             no charge
Next 200 units                                              Rs 5 per unit
After 200 units                                             Rs 10 per unit
(For example if input unit is 350 than total bill amount is Rs.3500
(For example if input unit is 97 than total bill amount is Rs.0
(For example if input unit is 150 than total bill amount is Rs.750


units = int(input("Add your Units "))

if units <=100:
    print("there will be no charge for such a unit")
elif units <=200:
    bill =  units * 5
    print ("Your bill whould be ", bill)
elif units >200:
    bill = units * 10
    print ("Your bill whoulc be ", bill)
else:
    print("the amount is incorrect")
'''

'''
9) Take values of length and breadth of a rectangle from user and print if it is square or rectangle.
length = int(input("Enter length"))
breadth = int(input("Enter breadth"))

if length == breadth:
    print("It is a Square")
else:
    print("It is a Rectangle")

    10) Take two int values from user and print greatest among them.
    
x = int(input("Enter first number"))
y = int(input("Enter second number"))

if x > y:
    print(x, "is greater.")
elif y > x:
    print(y, "is greater.")
else:
    print("Both numbers are equal.")

    
11) A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
Ask user for quantity
Suppose, one unit will cost 100.
Judge and print total cost for user.
quantity = int(input("Enter the quantity of items you want to purchase: "))
unit_price = 100
total_cost = quantity * unit_price

if total_cost > 1000:
    total_cost -= total_cost * 0.10

print("Total cost after discount (if applicable): Rs.", total_cost)


12) A school has following rules for grading system:

a. Below 25 - F

b. 25 to 45 - E

c. 45 to 50 - D

d. 50 to 60 - C

e. 60 to 80 - B

f. Above 80 - A

Ask user to enter marks and print the corresponding grade.

marks = int(input("Enter your marks: "))

if marks < 25:
    grade = "F"
elif marks < 45:
    grade = "E"
elif marks < 50:
    grade = "D"
elif marks < 60:
    grade = "C"
elif marks < 80:
    grade = "B"
else:
    grade = "A"

print("Your grade is:", grade)

14)A student will not be allowed to sit in exam if his/her attendence is less than 75%.

Take following input from user

- Number of classes held

- Number of classes attended.

And print

- percentage of class attended

- Is student is allowed to sit in exam or not.
classes_held = int(input("Enter the number of classes held: "))
classes_attended = int(input("Enter the number of classes attended: "))

attendance_percentage = (classes_attended / classes_held) * 100

print("Attendance Percentage:", attendance_percentage, "%")

if attendance_percentage >= 75:
    print("Student is allowed to sit in the exam.")
else:
    print("Student is NOT allowed to sit in the exam.")

    15) Modify the above question to allow student to sit if he/she has medical cause. Ask user if he/she has medical cause or not ( 'Y' or 'N' ) and print accordingly.
    classes_held = int(input("Enter the number of classes held: "))
classes_attended = int(input("Enter the number of classes attended: "))

attendance_percentage = (classes_attended / classes_held) * 100

print("Attendance Percentage:", attendance_percentage, "%")

if attendance_percentage >= 75:
    print("Student is allowed to sit in the exam.")
else:
    medical_cause = input("Do you have a medical cause? (Y/N): ").strip().upper()
    if medical_cause == 'Y':
        print("Student is allowed to sit in the exam due to medical cause.")
    else:
        print("Student is NOT allowed to sit in the exam.")


'''
'''16) Write a program to check if a year is leap year or not.

If a year is divisible by 4 then it is leap year but if the year is century year like 2000, 1900, 2100 then it must be divisible by 400.'''

'''year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")'
    '''

'''17) Ask user to enter age, gender ( M or F ), marital status ( Y or N ) and then using following rules print their place of service.

if employee is female, then she will work only in urban areas.

if employee is a male and age is in between 20 to 40 then he may work in anywhere

if employee is male and age is in between 40 t0 60 then he will work in urban areas only.

And any other input of age should print "ERROR"'''

'''age = int(input("Enter age: "))
gender = input("Enter gender (M/F): ").upper()
marital_status = input("Enter marital status (Y/N): ").upper()

if gender == 'F':  
    print("She will work only in urban areas.")
elif gender == 'M':
    if 20 <= age <= 40:
        print("He may work anywhere.")
    elif 40 <= age <= 60:
        print("He will work only in urban areas.")
    else:
        print("ERROR")
else:
    print("ERROR")'''
