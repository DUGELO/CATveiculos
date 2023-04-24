qtdRodas = 4
pesoBruto = 3000
qtdPessoas = 5 

if qtdRodas == 2 or qtdRodas == 3:
    print('Categoria A')
elif qtdRodas == 4 and pesoBruto <= 3500 and qtdPessoas <= 8:
    print('Categoria B')
elif qtdRodas >= 4 and 3500 <= pesoBruto <= 6000:
    print('Categoria C')
elif qtdRodas >= 4 and qtdPessoas > 8:
    print('Categoria D')
elif qtdRodas >= 4 and pesoBruto > 6000:
    print('Categoria E')