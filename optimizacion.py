import time
import numpy as np
bloques = []



def optimizar(arr):
    separar(arr)
    imprimir()
    for i in range(0,len(bloques)):
        for j in range(0,len(bloques[i])):
            #operaciones
            bloques[i]=optBlq(bloques[i])
    
    aux = eliminarVarNoUso(bloques)
    arr = []
    
    
    separar(arr)
    c = 0
    b =0
    print('7777777777777777777777777777777777777777')
    for i in bloques:
        print('BLOQUE ',b)
        for k in i:
            print(k)
            if len(k) ==5:
                c+=1
        b+=1
    print(c,'***********************************************************++')
    


        



   
def eliminarVarNoUso(blq):
    variables  = []
    for i in blq:
        for j in i:
            if  'goto' not in j[3] and j[3] != '' and "'" not in j[3]:
                if j[3] not in variables:
                    variables.append(j[3])
                if j[3] in variables:
                    print('variable encontrada')
    print(variables)
    for i in range(len(variables)):
        variables[i]= [variables[i],0]
    vars = np.array(variables)[:,0]
    for i in blq:
        for j in i:
            if j[0]  in vars:
                indice =np.where(vars ==j[0])[0][0]
                #print(j[0],indice)
                variables[indice][1]= variables[indice][1]+1
            if j[1]  in vars:
                indice =np.where(vars ==j[1])[0][0]
                print(j[1],indice)
                variables[indice][1]= variables[indice][1]+1
            if (j[2] == 'imprimir' or j[2] == 'leer') and j[3]  in vars:
                indice =np.where(vars ==j[3])[0][0]
                variables[indice][1]= variables[indice][1]+1

    eliminar = []
    for i in variables:
        if i[1] == 0:
            eliminar.append(i[0])
    print(eliminar)
    
    print('*************')
    for i in range(len(blq)):
        for j in range(len(blq[i])-1,-1,-1):
            
            #print(i,j,blq[i][j])
            if blq[i][j][3] in eliminar:
                print(blq[i][j])
                blq[i] =np.delete(blq[i],j,0)
        print(blq[i])

    for i in blq:
        for j in i:
            print(j)

    #print(np.delete(bloques[0],0,0))
    return blq
    


def imprimir():
    c = 1
    for i in bloques:
        print('BLOQUE ',c)
        for j in i:
            print(j)
        c+=1


def optBlq(bloque):
    print('OPTIMIZACION')
    for j in range(len(bloque)):
        if bloque[j][2] in ['+','-','*','/'] and (bloque[j][0].isnumeric() and bloque[j][1].isnumeric()):
            bloque[j] = [operacion(bloque[j][0],bloque[j][1],bloque[j][2]),'','=',bloque[j][3]]
            bloque=eliminarNoUso(bloque,bloque[j])
        #multiplicacion * 1
        if bloque[j][2]=='*' and bloque[j][1] == '1':
            bloque[j] = [bloque[j][0],'','=',bloque[j][3]]
            bloque=propagar(bloque,j)
        if bloque[j][2]=='*' and bloque[j][0] == '1':
            bloque[j] = [bloque[j][1],'','=',bloque[j][3]]
            bloque=propagar(bloque,j)
        if bloque[j][2]=='*' and bloque[j][1] == '0':
            bloque[j] = ['0','','=',bloque[j][3]]
            bloque=propagar(bloque,j)
        if bloque[j][2]=='*' and bloque[j][0] == '0':
            bloque[j] = ['0','','=',bloque[j][3]]
            bloque=propagar(bloque,j)
        
            
    return bloque

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

    for i in bloques:
        for j in i:
            if j[2] in ['+','-','*','/'] and (j[0].isnumeric() and j[1].isnumeric()):
                j = [operacion(j[0],j[1],j[2]),'','=',j[3]]

    


    
def eliminarNoUso(bloque,variable):
    bloque = np.array(bloque)
    variable = np.array(variable)

    inicio = np.where( variable in bloque)[0]

    for i in range(inicio[0],len(bloque)):
        if (bloque[i][0]== variable[3] or bloque[i][1]== variable[3] ) and bloque[i][3] !=  variable[3]:
            if bloque[i][0]== variable[3]:
                bloque[i][0] = variable[0]

            if bloque[i][1]== variable[3]:
                bloque[i][1] = variable[0]
    #print('++++++++++++++++++++')
    #print(bloque)
    #print('++++++++++++++++++++')
    bloque =bloque.tolist()
    return bloque
    
def propagar(bloque,variable):
    var = bloque[variable][3]
    valor = bloque[variable][0]
    for j in range(variable,len(bloque)):
        if bloque[j][0] == var:
            bloque[j][0] = valor
        if bloque[j][1] == var:
            bloque[j][1] = valor
    return bloque

def operacion(num1,num2,op):
    if op == '+':
        return str(int(num1)+int(num2))
    elif op == '-':
        return str(int(num1)-int(num2))
    elif op == '*':
        return str(int(num1)*int(num2))
    elif op == '/':
        return str(int(num1)/int(num2))

