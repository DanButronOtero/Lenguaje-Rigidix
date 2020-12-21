import time
import numpy as np
bloques = []
def optimizar(arr):
    separar(arr)

def separar(arr):
    print('************************')
    blq=[]
    for i in arr:
        if 'goto' in i[3] or ':' in i[2]:
            bloques.append(blq)
            blq = []
            blq.append(i)
        else:
            blq.append(i)
    c = 1
    for i in bloques:
        print('BLOQUE ',c)
        for j in i:
            print(j)
        c+=1
    

def operacion(num1,num2,op):
    if op == '+':
        return str(int(num1)+int(num2))
    elif op == '-':
        return str(int(num1)-int(num2))
    elif op == '*':
        return str(int(num1)*int(num2))
    elif op == '/':
        return str(int(num1)/int(num2))