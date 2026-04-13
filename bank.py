rl=float(input("Enter the initial amount"))
opt=int(input("Enter your mode of transaction 1.DEPOSIT 2.WITHDRAWAL"))
if opt==1:
    a=float(input("Enter amount to deposit"))
    if a>=1000:
        rl=rl+a
    else:
        rl=rl+0
elif opt==2:
    b=float(input("Enter amount to withdrawal"))
    if rl<=1000 and b>rl:
        print("Invalid")
    else:
        rl=rl-b
else:
    print("Invalid option")
print("updated balance:",rl)
print("THANK YOU")
