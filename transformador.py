# ºC = 0
# ºF = 32

temperatura = float(input("Ingrese la temperatura a convertir: "))
escala = input("Indique la escala ºC o ºF: ").lower()

if escala == "c":
    fahrenheit = (temperatura * 9 / 5) + 32
    print(fahrenheit)
elif escala == "f":
    celsius = (temperatura - 32) * 5 / 9
    print(celsius)
else:
    print("Valor incorrecto, ¿Has puesto correctamente 'C' o 'F'?")