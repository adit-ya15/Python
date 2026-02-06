with open("file.txt","r") as f:
    data = f.read()
    

if("donkey" in data):
    data = data.replace("donkey","####")
    

with open("file.txt","w") as f:
    f.write(data)
    
