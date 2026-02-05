#One way but not a good way as it reads the whole file in one go 
f = open("poems.txt","r");

data = f.read();

if("twinkle" in data):
    print("File contains the twinkle")
else:
    print("Not contains")  

f.close()  

#So we use other way in which we read the file line by line which is a good practice as if we have very larger files then this method is good

found = False

with open("poems.txt","r") as f:
    for line in f:
        if("Aditya" in line):
            print("File contains the word Aditya")
            found = True
            break

if(not found):
    print("File not contains the word Aditya")
