print("""
██████╗░██████╗░░█████╗░░░░░░██╗███████╗████████╗░█████╗░  ░░███╗░░
██╔══██╗██╔══██╗██╔══██╗░░░░░██║██╔════╝╚══██╔══╝██╔══██╗  ░████║░░
██████╔╝██████╔╝██║░░██║░░░░░██║█████╗░░░░░██║░░░██║░░██║  ██╔██║░░
██╔═══╝░██╔══██╗██║░░██║██╗░░██║██╔══╝░░░░░██║░░░██║░░██║  ╚═╝██║░░
██║░░░░░██║░░██║╚█████╔╝╚█████╔╝███████╗░░░██║░░░╚█████╔╝  ███████╗
╚═╝░░░░░╚═╝░░╚═╝░╚════╝░░╚════╝░╚══════╝░░░╚═╝░░░░╚════╝░  ╚══════╝""")

"""1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar."""
#print("É PAR OU IMPAR")
#numero = int(input("Digite um número qualquer:\n"))
#if numero % 2 == 0:
#    print("É PAR")
#else:
#    print("É IMPAR")



"""2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:

Criança: 0 a 12 anos;
Adolescente: 13 a 18 anos;
Adulto: acima de 18 anos."""

#print("Criança, Adolescente ou Adulto?")
#idade = int(input("Qual sua idade?"))
#
#if idade <= 12:
#    print(f"Criança: {idade} anos")
#elif idade <= 18:
#    print(f"Adolescente: {idade} anos")
#else:
#    print(f"Adulto: {idade} anos")

"""3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você."""
#user = input("Digite seu usuário:\n")
#password = input("Agora digite sua senha:\n")
#
#if user == "Thiago" and password == "123":
#    print(f"Bem vindo {user}!")
#else:
#    print("Mete o pé vagabundo!")

"""4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:
 
Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
Terceiro Quadrante: os valores de x e y devem ser menores que zero;
Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
Caso contrário: o ponto está localizado no eixo ou origem."""

#numX = int(input("Digite a primeira coordenada:\n"))
#numY = int(input("Digite a segunda coordenada:\n"))
#
#if numX > 0 and numY > 0:
#    print("Primeiro Quadrante!!")
#elif numX < 0 and numY > 0:
#    print("Segundo Quadrante!!")
#elif numX < 0 and numY < 0:
#    print("Terceiro Quadrante!!")
#elif numX > 0 and numY < 0:
#    print("Quarto Quadrante!!")
#else:
#    print("Ponto está localizado no eixo ou origem!")