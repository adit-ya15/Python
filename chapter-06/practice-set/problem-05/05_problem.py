list = []

with open("file.txt","r") as f:
    data = f.read()

data = data.split()

print(data)

for word in data:
    newWord = word.strip(".,!?")
    if(newWord == "####"):
        list.append(newWord)

print(list)