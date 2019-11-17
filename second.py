binary = input("enter binary numbers separated binary numbers").split(',')
decimal=[]
for i in range(len(binary)):
    decimal.append(int(binary[i],2))

for n in range(len(decimal)):
   if decimal[n]%5 == 0:
        print(binary[n],",")