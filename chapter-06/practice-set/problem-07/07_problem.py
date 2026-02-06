with open("source.txt") as f:
    data = f.read()

with open("destination.txt","w") as f:
    f.write(data)