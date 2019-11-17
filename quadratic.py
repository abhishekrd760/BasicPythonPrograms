import cmath
a = float(input("Enter the value of a in quadratic equation"))
b =float(input("Enter the value of b in quadratic equation"))
c = float(input("Enter the value of c in quadratic equation"))
x1 = (-b + cmath.sqrt((b**2)-(4*a*c)))/(2*a)
x2 = (-b - cmath.sqrt((b**2)-(4*a*c)))/(2*a)
d = (b**2)-(4*a*c)

print("The two roots of the quadratic equation are : ",x1,x2)
if d<0:
    print("The roots are complex")
else:
    print("The roots are not complex")