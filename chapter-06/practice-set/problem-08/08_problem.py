#This is also a correct working code but there is more good way exist 
# i = 0;
# with open("log.txt","r") as f:
#     for line in f:
#         i = i + 1;
#         if("python" in line):
#             print(i)

#Second way is by using the enumerate function which is more good way to do this

with open("log.txt","r") as f:
    for line_number, line in enumerate(f,start=1):
        if("python" in line.lower()):
            print("The word python find at line :",line_number)