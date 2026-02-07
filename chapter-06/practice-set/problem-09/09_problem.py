with open("source.txt","r") as f:
    data1 = f.read()

with open("destination.txt","r") as f:
    data2 = f.read()

if(data1 == data2):
    print("Both the files are identical")
else:
    print("Files are not identical")    