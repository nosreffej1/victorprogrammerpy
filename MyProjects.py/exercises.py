# Faça um programa que tenha a função chamada area(),
# que receba as dimensoes de um terreno retangular(larg e comprimento
# e mostre a área do terreno 

# Faça um programa que tenha uma funcao chamada escreva() 
# que receba um texto qualquer como parâmetro e mostre
# uma mensagem com tamanho adaptãvel

# Faça um programa que tenha uma função chamada contador()
# que receba três parâmetros: início, fim e passo e realize a contagem
# Seu programatem que realizar três  contagens através da função criada:
# a) De 1 até 10, de 1 em 1
# b) De 10 até 0, de 2 em 2
# c) Uma contagem personalizada

# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros
# com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual é o maior

# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteio()
# e somapar(). A primeira função vai sortear 5 números e vai colocálos dentro da lista 
# e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior

from time import sleep


def detalhe():
    print('-' * 35)

def maior(numero, numero_2):
    if numero > numero_2:
        detalhe()
        print(f'{numero} é o maior.')
        detalhe()
    elif numero_2 > numero:
        detalhe()
        print(f'{numero_2} é o maior.')
        detalhe()
    else:
        detalhe()
        print('Os dois valores são iguais.')
        detalhe()
    

while True:
    print('-=' * 20)
    print('Comparador de números \nIremos mostrar o maior número informado')
    print('-=' * 20)
    numero = int(input('Digite um número: '))
    sleep(0.5)
    numero_2 = int(input('Informe outro número: '))
    pergunta = str(input('Certo, anotamos o número informado!\nDeseja continuar? '))[0]
    if pergunta == 's':
        continue
    else:
        break
    
maior(numero, numero_2)

from time import sleep

cont = 0

def contador(* num):
        if ini <= fim:
            while True:
                sleep(0.3)
                tot = ini - passos
                print(tot)


choice_user = str(input('Você deseja ver a operação trabalhando de 1 até 10, de 1 em 1? '))[0]
if choice_user in 's':
    while cont < 10:
        sleep(1)
        print(1 + cont)
        cont += 1
elif choice_user not in 's':
    choice_user = str(input('Você deseja ver a operação trabalhando de 10 até 0, de 2 em 2? '))[0]
    if choice_user in 's':
        print(10)
        sleep(1)
        print(8)
        sleep(1)
        print(6)
        sleep(1)
        print(4)
        sleep(1)
        print(2)
        sleep(1)
        print(0) 
    elif choice_user not in 's':
        choice_user = str(input('Deseja personalizar uma operação de ascendência ou decadência? '))[0]
        if choice_user in 's':
            ini = int(input('Informe o número de início: '))
            fim = int(input('Informe até qual número o programa irá trabalhar: '))
            passos = int(input('Quantos passos do início até o fim? '))
            print('Muito bem, estamos processando os dados informados...')
            contador(ini, fim, passos)
def escreva(msg):
    print('-' * 30)
    len(msg)
    print(msg)
    print('-' * len(msg)) 

msg = str(input('Escreva seu Título: '))

escreva(msg)

def detalhe_grafico():
    print('-=' * 16)

def area(a, b):
    detalhe_grafico
    total = a * b
    print(f'A área de um terreno com a largura {a} e o comprimento {b} é de {total}')
    detalhe_grafico

detalhe_grafico()
print('Informe apenas números INTEIROS')
detalhe_grafico()

larg = int(input('Informe a LARGURA do terreno: '))
comp = int(input('Informe o COMPRIMENTO do terreno: '))

a = larg
b = comp

area(a, b)
