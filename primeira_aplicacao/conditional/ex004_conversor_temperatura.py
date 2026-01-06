# def conversor_temperatura():

#     celsius = int(input('Qual a temperatura em Celsius? '))
    # fahrenheit = (celsius * 9/5) + 32
    # print(f'A temperatura em Fahrenheit é de {fahrenheit}ºF')

def getUserInput():
    celsius = float(input('Qual a tempetatura em Celsius? '))
    return celsius

def conversorCparaF(celsius):
   return (celsius * 9/5) + 32

if __name__ == "__main__":
    celsius = getUserInput()
    fahrenheit = conversorCparaF(celsius)
    print(f'A temperatura convertida para ºF é {fahrenheit}')