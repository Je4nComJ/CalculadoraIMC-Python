def calculadora_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

peso = float(input ("Digite seu peso (KG):"))
altura = float(input("Digite sua altura (METROS):"))

imc = calculadora_imc(peso, altura)

print("Seu IMC é {:.1f}".format(imc))

if imc <= 18.5:
 print("Você está ABAIXO do peso ideal!")

elif imc >= 18.6 and imc <= 24.9:
 print("Você está na faixa de peso ideal, parabéns!")

elif imc >= 25.0 and imc <= 29.9:
 print("Atenção! Você está em sobrepeso.") 

elif imc >= 30.0 and imc <= 34.9:
  print("Você está em obesidade GRAU I, preste bastante atenção!")

elif imc >= 35.0 and imc <= 39.9:
  print("Você está em obesidade GRAU II, cuidado!")

elif imc >= 40.0:
  print("Tenha bastante cuidado! Você está em OBESIDADE MÓRBIDA!")