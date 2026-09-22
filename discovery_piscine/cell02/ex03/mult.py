a = int(input(""))
b = int(input(""))

c = a * b
print(a, "x", b, "=", c)

if c < 0:
    print("The result is negative.")
elif c > 0:
    print("The result is positive.")
else:
    print("The result is both positive and negative.")