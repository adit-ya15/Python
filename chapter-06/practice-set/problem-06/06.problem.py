with open("log.txt") as f: 
    data = f.read()

if("python" in data):
    print("Your log file conatains the word python")
else:
    print("Your log file not contains the word python")