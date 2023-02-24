#calculadora em python simples

n1, n2 = float(input('qual e o primeiro numerero: ')),float(input('qual e o segundo numero:'))

o1 =  str(input('qual sera o tipo de operaçao: [+, -, *, /] \n'))

if o1 == "+":
    print(n1 + n2)
elif o1 == "-":
    print(n1 - n2)
elif o1 == "*":
    print(n1 * n2)
elif o1 == "/":
    print(n1 / n2)
