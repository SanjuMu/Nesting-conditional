med = input("Do you have a medical cause Y or N: ")

atten= int(input("Enter the attendance of the student:"))


if med == 'Y':
    print("You are allowed to write the exam!!")

else:
     if atten>=75:
        print("You are allowed to write the exam!!")

     else:
        print("You are NOT allowed to write the exam!!")

