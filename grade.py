t=int(input("Enter your mark:"))
e=int(input("Enter your mark:"))
m=int(input("Enter your mark:"))
s=int(input("Enter your mark:"))
ss=int(input("Enter your mark:"))
Total=t+e+m+s+ss
Percentage=((Total/500)*100)
print("Your total mark is:",Total)
print("Your Percentage is:",Percentage)
if Percentage>=90:
    print("Grade is 'O'")
elif Percentage>=80:
    print("Grade is 'A+'")
elif Percentage>=70:
    print("Grade is 'A'")
elif Percentage>=60:
    print("Grade is 'B+'")
elif Percentage>=55:
    print("Grade is 'B'")
elif Percentage>=50:
    print("Grade is 'C'")
else:
    print("FAIL")
print("THANK YOU")
