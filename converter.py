#Конвертер температур F <-> C

temp = input("Введите температуру (32с, 100F): ").lower().strip()
degrees = int(temp[:-1])
scale = temp[-1]
result = None

print(temp, degrees, scale)

if scale == "f":
    result = (degrees - 32) / 1.8
    print(f"{degrees}F == {result}C")
else:
    result = degrees * 1.8 +32
    print(f"{degrees}C == {result}F")


