mais13 = 0
while True:
    idade = int(input('Insira a idade: '))
    altura = float(input('Qual altura?: '))
    if altura == 0:
        break
    if idade >= 13 and altura < 150:
        mais13 += 1
print('O número de alunos é: ',mais13)