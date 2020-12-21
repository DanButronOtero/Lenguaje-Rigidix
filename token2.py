#libreria que genera el tokenizado de un texto
import numpy as np
abcd=list('ABCDEFGHIJKLMNOPQRSTUVXYZ'.upper())
def tokenizar(nombre_archivo,tokens,separadores):
    text = np.loadtxt(nombre_archivo,dtype='str',delimiter='\t')
    pila = []
    aux = ''
    pila = []
    arrToken = []
    #push = append
    #pop = pop
    fCad = False
    cadStr=''
    for i in text:
        aux = i
        auxstr=''
        for j in range(0,len(aux)):
            if fCad == False:
                if aux[j] in separadores :
                    pila.append(auxstr)
                    auxstr=''
                    pila.append(aux[j])
                else:
                    auxstr= auxstr + aux[j]
                    if j == len(aux)-1:
                        pila.append(auxstr)

    #print(pila)
    tokensaux = tokens[:,1].tolist()
    tokensauxnum = tokens[:,0]
    #print(pila)
    fCad = False
    cadStr = "'"
    for i in pila:
        if fCad == False:
            if i == "'":
                fCad=True
                cadStr = i
            elif i not in tokensaux and i != ' ':
                if i!= '':
                    if i[0] in abcd and i.isdigit() == False:
                        arrToken.append([6,i,'Var'])
                    elif i.isdigit():
                        arrToken.append([7,i,'number'])
                    else:
                        arrToken.append([-1,'ERROR',"Error token "+i])
            else:
                if i != ' ':
                    #print(tokens[tokensaux.index(i)])
                    arrToken.append(tokens[tokensaux.index(i)])
        else:
            if i[len(i)-1] == "'":
                cadStr = cadStr + i
                arrToken.append([8,cadStr,'cadena'])
                cadStr = "'"
                fCad = False
            else:
                cadStr = cadStr + i
    '''for i in arrToken:
        print(i)
    '''
    return arrToken

def findErr(arr):
    err = []
    for i in arr:
        if i[0] == -1:
            err.append(i)
    return err