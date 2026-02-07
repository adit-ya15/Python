a = int(input("Enter a number : "))
b = int(input("Enter second number : "))

try:
    ans = a/b
    print(ans)
except ZeroDivisionError as e:
    print("Infinite")

except Exception as e: 
    print("Please enter a valid number",e)