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
print(opera(3, 4, 4))