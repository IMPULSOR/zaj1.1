print("Podaj współrzędne pierwszego wektora: ")
x1 = float(input("Podaj x: "))
y1 = float(input("Podaj y: "))
z1 = float(input("Podaj z: "))
print("Podaj współrzędne drugiego wektora: ")
x2 = float(input("Podaj x: "))
y2 = float(input("Podaj y: "))
z2 = float(input("Podaj z: "))

print("W1 = [{}, {}, {}]".format(x1, y1, z1))
print("W2 = [{}, {}, {}]".format(x2, y2, z2))

wynik = x1*x2 + y1*y2 + z1*z2
print("W1 * W2 = {}".format(wynik))
