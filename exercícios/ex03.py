def achatar(lista):
    resultado = []

    for elemento in lista:
        if type(elemento) == list:
            resultado = resultado + achatar(elemento)
        else:
            resultado = resultado + [elemento]

    return resultado

def achatar2(lista):
    return [ x for elemento in lista for x in (achatar2(elemento) if type(elemento) == list else [elemento])]
        
