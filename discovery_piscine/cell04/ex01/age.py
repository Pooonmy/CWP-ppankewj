n = input("Please tell me your age: ")
print("You are currently " + n + " years old.")
for i in range (10, 31, 10):
    print("In " + str(i) + " years, you'll be " + str(int(n) + i) + " years old.")