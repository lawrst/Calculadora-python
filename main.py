from operacoes import operacoes

print("calculadora")

operacao = operacoes()

op = int(input("""digite 1 para realizar uma soma de 2 numeros\n
           digite 2 para realizar uma subtração de 2 numeros\n
           digite 3 para realizar uma multiplicação de 2 numeros\n
           digite 4 para realizar a divisão de 2 numeros: \n"""))
if (op == 1):
    num1 = int(input("digite o primeiro numero para calcular: "))
    num2 = int(input("digite o primeiro numero para calcular: "))
    operacao = operacoes()
    resultado = operacoes.soma(num1, num2)
    print("resultado da soma: ", resultado)
    
if (op == 2):
    num1 = int(input("digite o primeiro numero para calcular: "))
    num2 = int(input("digite o primeiro numero para calcular: "))
    operacao = operacoes()
    resultado = operacoes.sub(num1, num2)
    print("resultado da ssubtação: ", resultado)
    
if (op == 3):
    pass#metodo da multiplicação
if (op == 4):
    pass#metodo da divisão

