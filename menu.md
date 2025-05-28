

#code of menu


print("\t\tWelcome to our restaurant")
print("1. PIZZA : ₹ 99 ")
print("2. BURGER : ₹ 39 ")
print("3. NOODLES : ₹ 79 ")
print("4. COLD COFFEE : ₹ 49 ")
print("5. OREO SHAKE : ₹ 69 ")
x=0
n=int(input("how many product you want:"))
for i in range(1,n+1):
    z=int(input("Enter Sr no."))
    if z==1:
        x+=99
    elif z==2:
        x+=39
    elif z==3:
        x+=79
    elif z==4:
        x+=49
    elif z==5:
        x+=69
    else:
        print("Enter no. from menu only")
print(f"Total: ₹{x}")        
