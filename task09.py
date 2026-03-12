a = float(input("First side of triangle:"))
b = float(input("second side of triangle: "))
c = float(input("third side of triangle: "))
if a== b == c:
    print("equilateral triangle")
elif a==b or a == c or c== b:
    print("Equal side triangle!")
else:
    print("different side triangle!")
