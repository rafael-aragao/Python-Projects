def celsius_para_fahrenheit(c):
    return (c * 9/5) + 32

temp = float(input("Digite a temperatura em Celsius: "))
print("Fahrenheit:", celsius_para_fahrenheit(temp))