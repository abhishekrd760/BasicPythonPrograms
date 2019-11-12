file1 = open('myfile.txt','r')
lines = 0
words = 0
characters = 0

for line   in file1:
    wordlist = line.split()
    print(wordlist)
    lines = lines+1
    words = words + len(wordlist)
    characters = characters + len(line)

print("Number of Words is : ", words)
print("Number of lines are: ", lines)
print("Number of Characters are : ", characters)
