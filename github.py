# #A simple banking system
a=float(input("Initial Balance: "))
print("1.Deposit")
print("2.Withdraw")
print("3.Display")
b=int(input("Choose from above options:"))
if b==1:
    x=float(input("How much you want to deposit:"))
    print("Your total balance becomes:" ,a+x)
elif b==2:
    y=float(input("How much you want to withdraw: "))
    print("Your total balance becomes:" ,a-y)
elif b==3:
    print(a)