from re import S


def showline():
    print('-' * 20)

showline()
print('     Student')
showline()

# Buscar como centralizar palavras

def message(msg):
    print('-' * 20)
    print(msg)
    print('-' * 20)
message('     Book')

def history(msg):
    print('-' * 20)
    print(msg)
    print('-' * 20)
history('     Hitler')

def soma(a, b):
    s = a + b
    print(s)

soma(9, 11)
soma(20, 25)

test1 = int(input('Type a number: '))
test2 = int(input('Type other number: '))

soma(test1, test2)

def test(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de {a} + {b} = {s}')

test(b=5, a=9)

# É possível alterar ordens dos números alternando a sequência de variáveis
# Também é possível acrescentar variáveis na def, mas preciso testar opções durante exercícios

def contador(* num):
    print(num)

contador(8, 0, 7)
contador(7, 6, 3, 0, 5, 9)
contador(4)

# Cria tuplas

def cont(* num):
    for v in num:
        print(v)

cont(8, 0, 7)
cont(7, 6, 3, 0, 5, 9)
cont(4)

# Mostra valor como uma linha reta para baixo com apenas um número por linha

def c(* num):
    for v in num:
        print(f'{v}', end='')

c(8, 0, 7)
c(7, 6, 3, 0, 5, 9)
c(4)

# Mostra os números na ordem inserida

def con(* num):
    tam = len(num)
    print(f'Recebi os valores {num} e foram inseridos ao todo {tam} números')

con(8, 0, 7)
con(7, 6, 3, 0, 5, 9)
con(4)

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [9, 5, 3, 6, 2, 5, 6]
dobra(valores)
print(valores)

def soma(* num):
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')
soma(5, 6)
soma(4, 8, 7)
