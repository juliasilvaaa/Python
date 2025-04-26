# Calculadora IMC

# Variavel com valores entre 13 e 30
# Se o valor for menor que 18.5 , informar que IMC está baixo
# Se o valor for maior que 24.9 informar que IMC está alto
# Caso contrário, informar que IMC está médio


# Perguntando qual o IMC ou Variavél para guardar o valor imc = 13

print(" ------ Calculadora IMC -------- \n")

imc = int (input("Qual seu IMC? "))

if imc < 18.5:
    print("Seu IMC está baixo")
elif imc > 24.9:
    print("Seu IMC está alto")
else:
    print("Seu IMC está médio")

# Calculando IMC através do peso e altura 

print(" ------ Calculadora IMC -------- \n")

peso = int(input("Qual seu peso?"))
altura = float(input("Qual sua altura?"))


imc_calculo = peso / altura * altura

if imc_calculo < 18.5:
    print("Magreza")
elif imc_calculo > 40:
    print("Obesidade Grave")
else:
    print("Normal")

