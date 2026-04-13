rl=int(input("Enter the number:"))
sm=1
if rl<0:
    print("Factorial does not exists for -ve numbers")
else:
    for i in range(1,rl+1):
        sm=sm*i
print("Factorial of the given number is:",sm)
