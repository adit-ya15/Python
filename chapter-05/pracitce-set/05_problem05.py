list = ["Aditya","Anshika","Harshit","Ved","Akanksha","ka"]

def rem_and_strip(list,word):
    n = []
    for item in list:
        if not(item == word):
            n.append(item.strip("ka"))
    
    return n

print(rem_and_strip(list,"ka"))