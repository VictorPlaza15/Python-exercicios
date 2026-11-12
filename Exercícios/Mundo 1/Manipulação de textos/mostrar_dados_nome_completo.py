"Programa que leia o nome completo de uma pessoa e mostre"

nome = input("Digite seu nome: ")
M_nome =  nome.upper()
m_nome = nome.lower()
qtde_letras = len(nome) - nome.count(' ')
first_name = nome.split()
print(M_nome,'/', m_nome, '/', qtde_letras,'/', first_name[0])
