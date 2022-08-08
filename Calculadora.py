from ast import If

def ValidarEntradas(numero1, numero2, operacao):
    if operacao not in "+-*/":
        return False
    if operacao == "/":
        if numero2 == 0:    
            return False
    if not numero1.isnumeric():
        return False
    if not numero2.isnumeric():
        return False            
    return True
    

def calcular(numero1, numero2, operacao):
    valido = ValidarEntradas(numero1, numero2, operacao)
    if not valido:
        return None
    numero1 = float(numero1)
    numero2 = float(numero2)    

    if operacao == "+":
       return numero1 + numero2  
    elif operacao == "-":
       return numero1 - numero2        
    elif operacao == "/":
        return numero1 / numero2
    else:
        return numero1 * numero2

while True:
    print("Informe o primeiro valor: ")
    valor1 = input()
    print("Informe o  segundo valor: ")
    valor2 = input()
    print("Informe a operação (Para soma +, Para subtação -, para divisão /, para multiplicação *): ")
    FormaDeOperacao = (input())

    resultado = calcular(valor1, valor2, FormaDeOperacao)
    if resultado == None:
        print("Os valores são invalidos")
    else:
        print("O resultado da operação foi:", resultado)
    print("Deseja continuar? S/N")
    continua = input()
    if (continua.lower() != 's'):
        break    