f = open("./data/funny.txt","w")
f.write("I Love Python")
f.close()

# to append to a new line
f = open("./data/funny.txt","a")
f.write("\nI Love JavaScript")
f.write("\nProgramming is so cool ")
f.close()

# read all
f = open("./data/funny.txt","r")
print(f.read())
f.close()

# read line by line
f = open("./data/funny.txt","r")
for line in f:
    print(line)
f.close()

# tokenizing
f = open("./data/funny.txt","r")
for line in f:
    tokens = line.split(' ')
    print(tokens)
f.close()

# counting words
f = open("./data/funny.txt","r")
for line in f:
    line_without_new_line = line[:-1]
    tokens = line.split(' ')
    print(line_without_new_line + ":" + str(len(tokens)))
f.close()

# with keyword
with open("./data/funny.txt","r") as f:
    print(f.read())