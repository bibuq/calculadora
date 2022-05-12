from logo import logo
print(logo)

def suma(n1,n2):
    return n1 + n2

def resta(n1,n2):
    return n1 - n2

def multiplicacion(n1,n2):
    return n1 * n2

def division(n1,n2):
    return n1 / n2

operador = {
    '+':suma,
    '-':resta,
    '*':multiplicacion,
    '/':division
}

num1 = int(input('primer numero:\n'))
for simbol in operador:
    print(simbol)
operador_simbol = input('selecciona un operador:\n')

num2 = int(input('segundo numero:\n'))

operacion = operador[operador_simbol]
resultado = operacion(num1,num2)
print(f'{num1} {operador_simbol} {num2} = {resultado}')



    
    



