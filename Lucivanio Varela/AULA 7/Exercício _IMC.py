# EXERCÍCIO IMC

# como o exercicio anterior foi escrito :

# peso = float(input("digite o seu peso (kg): "))
# altura = float(input("digite a sua altura em  (m): "))
# imc = peso/(altura**2)
# print("seu IMC É", imc)

# # Como forma de estrutura de decisão
# if( imc < 17):
#     print ("estou muito abaixo do peso!")
# elif( imc>=17 and imc <= 18.5):    
#     print("estou abaixo do peso!")
# elif(imc >18.5 and imc <=25):
#     print("estou com o peso dentro do normal!")
# elif(imc>25 and imc <=30):
#     print("estou acima do peso!")
# else:
#     print("estou muito acima do peso!")


# Adaptar o problema para utilizar funções, principalmente os trechos de código dentro das estruturas de repetição.



def calculo_de_imc(peso, altura):
  return peso/altura**2

def mostar_imc(imc):
  if(imc <= 17):
    print("estou muito abaixo do peso!")
  elif(imc >= 17 and imc <= 18.5):
    print("estou abaixo do peso!" )
  elif(imc > 18.5 and imc <= 25):
    print("estou com o peso dentro do normal!")
  elif(imc >25 and imc <= 30):
    print("estou acima do peso!")
  else:
    print("estou muito acima do peso!")
  
peso = float(input("Digite o seu peso (kg):"))
altura = float(input("Digite a sua altura em (m): "))
imc = calculo_de_imc(peso, altura)

print('o seu IMC É: ', imc)
mostar_imc(imc)