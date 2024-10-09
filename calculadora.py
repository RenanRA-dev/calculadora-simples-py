print('Instruções de uso:')
print()
print('- Digite o primeiro valor e aperte enter.')
print('- Digite o operador matemático e aperte enter:')
print('-- + para adição')
print('-- - para subtração')
print('-- * para multiplicação')
print('-- / para divisão')
print('-- ^ para potenciar')
print('-- /^ para fatoração')
print('- Digite o segundo valor e aperte enter.')
print()

valor1 = float(input())
operador = input()
valor2 = float(input())
print()

if operador == '+':
    print(valor1 + valor2)

elif operador == '-':
    print(valor1 - valor2)

elif operador == '*':
    print(valor1 * valor2)

elif operador == '/':
    print(valor1 / valor2)

elif operador == '^':
    print(pow(valor1,valor2))

elif operador == '/^':
    print(pow(valor1,1/valor2))

else:
    print('Valores e/ou operador desconhecidos. Por favor tente novamente.')