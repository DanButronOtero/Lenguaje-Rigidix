import time
import numpy as np
import time as tm

bloques = []


def optimizar(arr):
    separar(arr)
    imprimir()
    for i in range(0, len(bloques)):
        for j in range(0, len(bloques[i])):
            # operaciones
            bloques[i] = optBlq(bloques[i])
    # print('###################')
    # print(bloques)
    # print('###################')
    propagarGlb(bloques)
    eliminarVarNoUso(bloques)
    propagarGlb(bloques)
    for i in range(0, len(bloques)):
        for j in range(0, len(bloques[i])):
            # operaciones
            bloques[i] = optBlq2(bloques[i])
    #eliminarVarNoUso(bloques)
    propagarGlb(bloques)
    eliminarVarNoUso(bloques)
    # print('###################')
    # for i in bloques:
    #     for j in i:
    #         print(j)
    # print('###################')
    arr = []
    separar(arr)
    c = 0
    b = 0
    for i in bloques:
        # print('BLOQUE ',b)
        for k in i:
            # print(k)
            if len(k) == 5:
                c += 1
        b += 1
    propagarGlogal(bloques)
    cambioSigno(bloques)
    print(c, '***********************************************************++')
    imprimir()
    eliminarquintuple(bloques)
    eliminarEtiquetasSeguidas(bloques)
    saltoInecesario(bloques)
    # condVerdadero(bloques)
    # en desarrollo problemas con la identidficacion de condiociones anidadas
    # si qiere activarlo sin tener ciclos anidados descomente el metodo de arriba
    imprimir()
def bloquesUsoVar(blq,var):
    cont =0
    arr=[]
    for i in blq:
        for j in i:
            if j[3]==var:
                if cont not in arr:
                    arr.append(cont)
        cont+=1
    return cont
    

def propagarGlb(blq):
    cont = 0
    var =   []
    val =   []

              
    for i in blq:
        for j in i:
            if len(j)==5:
                print(j[4])
                if 'Inicio' in j[4]:
                    cont+=1
                else:
                    cont-=1
            if cont ==0:
                if j[2] == '=':
                    if j[3] in var:
                        index = var.index(j[3])
                        val[index] = j[0]
                        
                    else:
                        val.append(j[0])
                        var.append(j[3])
                        print(j[0],'    ',j[3])
                        #if j[0] in var:
                        #    print('Bingo  ',j[0],'    ',j[3])
                if j[0] in var:
                    index = var.index(j[0])
                    print(j[0],'+++++++++++++',val[index])
                    #tm.sleep(2)
                    j[0] =  val[index]

                if j[1] in var:
                    index = var.index(j[1])
                    print(j[1],'+++++++++++++',val[index])
                    #tm.sleep(2)
                    j[1] =  val[index]

            else:
                if j[2] == '=' and j[3]in var:
                   index = var.index(j[3])
                   print(index)
                   val.pop(index)
                   var.pop(index)
        
        #tm.sleep(2)
    print(var)
    print(val)
    #tm.sleep(10)
            

    
            

            

    
def saltoInecesario(blq):
    arrElim = []
    for i in range(len(blq)):
        for j in range(len(blq[i])):
            if 'goto' in blq[i][j][3]:
                varGoto = blq[i][j][3][5:]
                if i<len(blq)-1:
                  if varGoto+':' in blq[i+1][j][2]:
                    print('************')
                    print(blq[i])
                    print(blq[i+1])
                    tm.sleep(2)
                    arrElim.append(i)
                    print('************')
                    tm.sleep(6)
    for i in range(len(arrElim)-1,-1,-1):
        print(arrElim[i])
        print(blq[arrElim[i]])
        tm.sleep(2)
        blq.pop( arrElim[i] )

def eliminarquintuple(blq):
    for i in range(len(blq)):
        for j in range(len(blq[i])):
            if len(blq[i][j])==5:
                blq[i][j]= [blq[i][j][0],blq[i][j][1],blq[i][j][2],blq[i][j][3]]
                print('quintuple')
def sustituyeGoto(blq,eO,eC):
    for i in range(len(blq)):
        for j in range(len(blq[i])):
            if blq[i][j][3][5:] == eO:
                print(blq[i][j][3])
                blq[i][j][3] = 'goto '+eC
                print(blq[i][j][3])
def eliminarEtiquetasSeguidas(blq):
    arrElim =[]
    for i in range(len(blq)):
        for j in range(len(blq[i])):
            if j == len(blq[i])-1:
                if ':' in blq[i][j][2]:
                    if i<len(blq)-1:
                        if ':' in blq[i+1][0][2]:
                            print(blq[i][j][2][:len(blq[i][j][2])-1])
                            sustituyeGoto(blq, blq[i][j][2][:len(blq[i][j][2])-1], blq[i+1][j][2][:len(blq[i+1][j][2])-1])
                            arrElim.append(i)
                            print(blq[i])
                            tm.sleep(2)

    for i in range(len(arrElim)-1,-1,-1):
        print(arrElim[i])
        print(blq[arrElim[i]])
        tm.sleep(2)
        blq.pop( arrElim[i] )

def condVerdadero(blq):
    c = 0

    for i in blq:
        h = 0
        for j in i:
            if str.isnumeric(j[0]) and str.isnumeric(j[1]) and j[2] in ['>', '<', '>=', '<=', '==', '!=']:
                print(j)
                print(j[2])
                print(validar(j))
                if validar(j) == False:
                    print(j)
                    etiqueta = j[3][5:] + ":"
                    bloques.pop(c + 2)
                    bloques.pop(c + 1)
                    bloques.pop(c)
                    # print('***********',bloques[c][h],'****')
                    # bloques[c][h]=['','','',j[3],j[4]]
                    eliminarEtiqueta(bloques, etiqueta)
                    print('Verdadero')
                else:
                    etiqueta = j[3][5:] + ":"
                    bloques.pop(c)
                    eliminarBlqEtiqueta(bloques, etiqueta)
                    print('Falso')
            h += 1
        c += 1


def eliminarEtiqueta(blq, etiqueta):
    c = 0
    d = 0
    for i in blq:
        for j in i:
            if j[2] == etiqueta:
                print(j)
                blq[c] = np.delete(blq[c], 0, 0)
                break
            d += 1
        c += 1


def eliminarBlqEtiqueta(blq, etiqueta):
    print(etiqueta)
    c = 0
    for i in blq:
        for j in i:
            if j[2] == etiqueta:
                print(j)
                blq.pop(c)
                break
        c += 1


def validar(intermedio):
    if intermedio[2] == '>':
        return int(intermedio[0]) > int(intermedio[1])
    if intermedio[2] == '<':
        return int(intermedio[0]) < int(intermedio[1])
    if intermedio[2] == '>=':
        return int(intermedio[0]) >= int(intermedio[1])
    if intermedio[2] == '<=':
        print(int(intermedio[0]), '<=', int(intermedio[1]))
        return int(intermedio[0]) <= int(intermedio[1])
    if intermedio[2] == '==':
        return int(intermedio[0]) == int(intermedio[1])
    if intermedio[2] == '!=':
        return int(intermedio[0]) != int(intermedio[1])


def cambioSigno(blq):
    blqEliminar = []
    for i in range(len(blq)):
        for j in range(len(blq[i])):
            if blq[i][j][2] in ['>', '<', '>=', '<=', '==', '!=']:
                # print(blq[i][j],'*********')
                if blq[i][j][2] == '>':
                    blq[i][j][2] = '<='
                    blq[i][j][3] = 'goto ' + str(int(blq[i][j][3][5:]) + 10)
                    blqEliminar.append(i + 1)
                    blq[i + 2] = np.delete(blq[i + 2], 0, 0)
                elif blq[i][j][2] == '<':
                    blq[i][j][2] = '>='
                    blq[i][j][3] = 'goto ' + str(int(blq[i][j][3][5:]) + 10)
                    blqEliminar.append(i + 1)
                    blq[i + 2] = np.delete(blq[i + 2], 0, 0)
                elif blq[i][j][2] == '>=':
                    blq[i][j][2] = '<'
                    blq[i][j][3] = 'goto ' + str(int(blq[i][j][3][5:]) + 10)
                    blqEliminar.append(i + 1)
                    blq[i + 2] = np.delete(blq[i + 2], 0, 0)
                elif blq[i][j][2] == '<=':
                    blq[i][j][2] = '>'
                    blq[i][j][3] = 'goto ' + str(int(blq[i][j][3][5:]) + 10)
                    blqEliminar.append(i + 1)
                    blq[i + 2] = np.delete(blq[i + 2], 0, 0)
                elif blq[i][j][2] == '==':
                    blq[i][j][2] = '!='
                    blq[i][j][3] = 'goto ' + str(int(blq[i][j][3][5:]) + 10)
                    blqEliminar.append(i + 1)
                    blq[i + 2] = np.delete(blq[i + 2], 0, 0)
                elif blq[i][j][2] == '!=':
                    blq[i][j][2] = '=='
                    blq[i][j][3] = 'goto ' + str(int(blq[i][j][3][5:]) + 10)
                    blqEliminar.append(i + 1)
                    blq[i + 2] = np.delete(blq[i + 2], 0, 0)
    # blq[i] = np.delete(blq[i], j, 0)
    for i in range(len(blqEliminar) - 1, -1, -1):
        print(blq[blqEliminar[i]])
        tm.sleep(2)
        bloques.pop(blqEliminar[i])


def propagarGlogal(blq):
    variables = []
    for i in blq:
        for j in i:
            if 'goto' not in j[3] and j[3] != '' and "'" not in j[3]:
                if j[3] not in variables:
                    variables.append(j[3])
    intermedio = []
    for i in blq:
        for j in i:
            intermedio.append(j)

    c = 0
    for i in intermedio:
        if len(i) == 5:
            break
        if ('goto ' not in i[3] and 'goto ' not in i[3] and 'imprimir' not in i[2]) and (i[3] != '') and (
                "'" not in i[3]) and (i[1] == ''):
            # print('***************',i,'  ',c)
            var = i[3]
            valor = i[0]
            for j in range(c, len(intermedio)):
                if len(intermedio[j]) == 5:
                    break
                if (intermedio[j][0] == var and intermedio[j][3] != var):
                    intermedio[j][0] = valor

                if (intermedio[j][1] == var and intermedio[j][3] != var):
                    intermedio[j][1] = valor

        c += 1
    # for i in intermedio:
    #     print(i)

    # print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')


def eliminarVarNoUso(blq):
    variables = []
    for i in blq:
        for j in i:
            if 'goto' not in j[3] and j[3] != '' and "'" not in j[3]:
                if j[3] not in variables:
                    variables.append(j[3])

    # print(variables)
    for i in range(len(variables)):
        variables[i] = [variables[i], 0]
    vars = np.array(variables)[:, 0]
    for i in blq:
        for j in i:
            if j[0] in vars:
                indice = np.where(vars == j[0])[0][0]
                # print(j[0],indice)
                variables[indice][1] = variables[indice][1] + 1
            if j[1] in vars:
                indice = np.where(vars == j[1])[0][0]
                # print(j[1],indice)
                variables[indice][1] = variables[indice][1] + 1
            if (j[2] == 'imprimir' or j[2] == 'leer') and j[3] in vars:
                indice = np.where(vars == j[3])[0][0]
                variables[indice][1] = variables[indice][1] + 1

    eliminar = []
    for i in variables:
        if i[1] == 0:
            eliminar.append(i[0])
    # print(eliminar)

    # print('*************')
    for i in range(len(blq)):
        for j in range(len(blq[i]) - 1, -1, -1):

            # print(i,j,blq[i][j])
            if blq[i][j][3] in eliminar:
                # print(blq[i][j])
                blq[i] = np.delete(blq[i], j, 0)
        # print(blq[i])

    # for i in blq:
    #     for j in i:
    #         print(j)

    # print(np.delete(bloques[0],0,0))


def imprimir():
    c = 1
    for i in bloques:
        print('BLOQUE ', c)
        for j in i:
            print(j)
        c += 1


def optBlq(bloque):
    # print('OPTIMIZACION')
    for j in range(len(bloque)):
        if bloque[j][2] in ['+', '-', '*', '/'] and (bloque[j][0].isnumeric() and bloque[j][1].isnumeric()):
            bloque[j] = [operacion(bloque[j][0], bloque[j][1], bloque[j][2]), '', '=', bloque[j][3]]
            bloque = eliminarNoUso(bloque, bloque[j])
        # multiplicacion * 1
        if bloque[j][2] == '*' and bloque[j][1] == '1':
            bloque[j] = [bloque[j][0], '', '=', bloque[j][3]]
            bloque = propagar(bloque, j)
        if bloque[j][2] == '*' and bloque[j][0] == '1':
            bloque[j] = [bloque[j][1], '', '=', bloque[j][3]]
            bloque = propagar(bloque, j)
        if bloque[j][2] == '*' and bloque[j][1] == '0':
            bloque[j] = ['0', '', '=', bloque[j][3]]
            bloque = propagar(bloque, j)
        if bloque[j][2] == '/' and bloque[j][0] == '0':
            bloque[j] = ['0', '', '=', bloque[j][3]]
            bloque = propagar(bloque, j)
        if bloque[j][2] == '+' and bloque[j][0] == '0':
            bloque[j] = [bloque[j][1], '', '=', bloque[j][3]]
            bloque = propagar(bloque, j)
        if bloque[j][2] == '+' and bloque[j][1] == '0':
            bloque[j] = [bloque[j][0], '', '=', bloque[j][3]]
            bloque = propagar(bloque, j)
        if bloque[j][2] == '*' and bloque[j][0] == '0':
            bloque[j] = ['0', '', '=', bloque[j][3]]
            bloque = propagar(bloque, j)

    return bloque

def optBlq2(bloque):
    # print('OPTIMIZACION')
    for j in range(len(bloque)):
        if bloque[j][2] in ['+', '-', '*', '/'] and (bloque[j][0].isnumeric() and bloque[j][1].isnumeric()):
            bloque[j] = [operacion(bloque[j][0], bloque[j][1], bloque[j][2]), '', '=', bloque[j][3]]
            #bloque = eliminarNoUso(bloque, bloque[j])
        # multiplicacion * 1
        if bloque[j][2] == '*' and bloque[j][1] == '1':
            bloque[j] = [bloque[j][0], '', '=', bloque[j][3]]
            bloque = propagar(bloque, j)
        if bloque[j][2] == '*' and bloque[j][0] == '1':
            bloque[j] = [bloque[j][1], '', '=', bloque[j][3]]
            bloque = propagar(bloque, j)
        if bloque[j][2] == '*' and bloque[j][1] == '0':
            bloque[j] = ['0', '', '=', bloque[j][3]]
            bloque = propagar(bloque, j)
        if bloque[j][2] == '*' and bloque[j][0] == '0':
            bloque[j] = ['0', '', '=', bloque[j][3]]
            bloque = propagar(bloque, j)

    return bloque

def separar(arr):
    # print('************************')
    blq = []
    for i in arr:
        if 'goto' in i[3] or ':' in i[2]:
            bloques.append(blq)
            blq = []
            blq.append(i)
        else:
            blq.append(i)

    for i in bloques:
        for j in i:
            if j[2] in ['+', '-', '*', '/'] and (j[0].isnumeric() and j[1].isnumeric()):
                j = [operacion(j[0], j[1], j[2]), '', '=', j[3]]


def eliminarNoUso(bloque, variable):
    bloque = np.array(bloque)
    variable = np.array(variable)

    inicio = np.where(variable in bloque)[0]

    for i in range(inicio[0], len(bloque)):
        if (bloque[i][0] == variable[3] or bloque[i][1] == variable[3]) and bloque[i][3] != variable[3]:
            if bloque[i][0] == variable[3]:
                bloque[i][0] = variable[0]

            if bloque[i][1] == variable[3]:
                bloque[i][1] = variable[0]
    # print('++++++++++++++++++++')
    # print(bloque)
    # print('++++++++++++++++++++')
    bloque = bloque.tolist()
    return bloque


def propagar(bloque, variable):
    var = bloque[variable][3]
    valor = bloque[variable][0]
    for j in range(variable, len(bloque)):
        if bloque[j][0] == var:
            bloque[j][0] = valor
        if bloque[j][1] == var:
            bloque[j][1] = valor
    return bloque


def operacion(num1, num2, op):
    if op == '+':
        return str(int(num1) + int(num2))
    elif op == '-':
        return str(int(num1) - int(num2))
    elif op == '*':
        return str(int(num1) * int(num2))
    elif op == '/':
        return str(int(num1) / int(num2))
