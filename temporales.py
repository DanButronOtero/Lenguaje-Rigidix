import  posfijo as pj
import numpy as np
import numpy
operadores=[
    '+',
    '-',
    '*',
    '/',
    '(',
    ')',
    '=',
    '>=',
    '<=',
    '>',
    '<',
    'and',
    'or'
]

def temporalesPosfijo(arr,i):
    temp=[] 
    arr=pj.posfijo(arr)
    print(arr)
    for l in range(0,len(arr)-1):
        if arr[l][0] == 'T' and str.isnumeric(arr[l][1:]):
            arr.pop(l)
    cont =i
    while len(arr)>1:
        i=0
        while (i<len(arr)):
            if str(arr[i]) not in operadores and str(arr[i+1]) not in operadores and str(arr[i+2]) in operadores:
                temp.append([arr[i],arr[i+1],arr[i+2],'T'+str(cont)])
                arr[i]= 'T'+str(cont)
                cont = cont +1
                arr.pop(i+2)
                arr.pop(i+1)
            i=i+1            
    return temp

def codigoIntermedio(var,tokpal):
    cuadruples=[]
    tokpal=tokpal.tolist()
    cont =0
    for i in var:
        if i[0][1]==5 and i[1][1]==6 and i[2][1]==9:
            #print('declaracion simple')
            cuadruples.append([tokpal[i[1][0]],'',tokpal[i[0][0]],''])
        if i[0][1]==5 and i[1][1]==6 and i[2][1]==14 and i[4][1]!=9:
            #print('declaracion asignacion ')
            aux=[]
            aux2=[]
            #print(i[0],'**')
            cuadruples.append([tokpal[i[1][0]],'',tokpal[i[0][0]],''])
            aux2 =type(i)
            for l in range(3,len(i)-1):
                aux.append(tokpal[i[l][0]])
           # print(len(aux))

            aux2=temporalesPosfijo(aux,cont)
            cont =int(aux2[len(aux2)-1][3][1:])+1

            for n in aux2:
                cuadruples.append(n)

            cuadruples.append([aux2[len(aux2)-1][3],'','=',tokpal[i[1][0]]])
            aux2 =[]
            
    return cuadruples


'''arrpos = [
'(', 'a', '*', 'b', '+', 'c', '/', 'b', ')', '+', 'a', '*', 'a', '+', '(', 'b', '+', 'c', '/', 'd', ')', '+', 'a']

arrpos2=['5', '+', 'B']

arrpos3=['A', '>', 'B','and','B','<','C','or','A','<','C','+','1']
arrpos4=['(','a','>','b','or','b','>','c',')','or','(','c','>','d','and','c','>','b',')',')']
cont_temp=0
temp=temporalesPosfijo(arrpos4,cont_temp)

print(temp)

print(pj.posfijo(arrpos4))

for i in temp:
    print(i)'''