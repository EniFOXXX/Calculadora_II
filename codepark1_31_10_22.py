# -*- coding: utf-8 -*-
"""CodePark1 - 31/10/22.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GJHD3SZeXZ5m0RdUHnc4kCgirll1AZoN
"""

print("1. Soma")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")
print("0. Sair")

opCorreta = True
while(opCorreta == True):
  print(" Digite a operação:")
  op = int(input())
  if(op == 0):
    print("Programa finalizado!")
    opCorreta = False
    break
  elif(op >= 5 or op < 0):
    print("Esta opção não existe")
  else:
   print(" Digite o primeiro número:")
   n1 = float(input())
  
   print(" Digite o segundo número:")
   n2 = float(input())
   if(n2 == 0):
    print("Resultado: Error!!!")
    
  res = calculadora(op,n1,n2)
   
    
  print("Resultado:",res)

def calculadora(op1,n3,n4):
   if(op1 == 1):

    resul =  n3 + n4


   elif(op1 == 2):

    resul =  n3 - n4


   elif(op1 == 3):

    resul =  n3 * n4


   elif(op1 == 4) and (n4 != 0):

    resul = n3 / n4
   
   else:
     resul = 0
   

   return resul