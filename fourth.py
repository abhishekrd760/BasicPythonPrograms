a = int(input("Enter a number for countdown"))
if(a<0):
    print("you gave negative i/p , It is processed as Positive")
    a = -1 *a

while a>0:
    print(a)
    a-=1