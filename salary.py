R=int(input("Enter the salary:"))
L=int(input("Enter the no.of days of leave taken:"))
if L>=0 and L<=2:
    print("The Salary is:",R)
elif L>2:
    d=R-((L-2)*500)
    print("The final amount deduced from your salary is:",d)
print("THANK YOU")
