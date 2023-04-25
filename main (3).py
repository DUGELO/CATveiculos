def opera(var1, var2, operando):
    
    if operando == 1:
        ope = (var1 + var2)
    elif operando == 2:
        ope = (var1 - var2)
    elif operando == 3:
        ope = (var1 * var2)
    elif operando == 4:
        ope = (var1 / var2)
    else:
        ope = 0
    return ope

def loop():
    opcoes = int(input('''1: Soma
2: Subtração
3: Multiplicação
4: Divisão
0: Sair\n'''))
    if opcoes in [0, 1, 2, 3, 4]:
        if opcoes != 0:
            print(opera(int(input('Valor 1\n')), int(input('Valor 2\n')), opcoes))
            loop()
    else:
        print('Essa opção não existe')
        loop()

loop()