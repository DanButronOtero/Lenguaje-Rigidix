import numpy as np
import pdb
from time import sleep
import temporales

variables = []
global varDec_inter
varDec_inter = []
inter = []
inter_metodo = []
varDeclaradas = []
varInsert = []
metodos = [['principal', False, 0, 1]]
cont_temporales = 0


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    # var        6
    # number     7
    # cadena     8
    # def (arr,i,arr2):


operadores = [
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

separadores = [
    '{',
    '}',
    ' ',
    ',',
    ';',
    '.',
    "'",
    ';',
    '=',
    '+',
    '-',
    '*',
    '/',
    '(',
    ')',
    '=='
]


# CONDICIONALES CODIGO INTERMEDIO
# Metodo recursivo que termina hasta llegar a una condicion terminal como son 
# todas las que no sean AND y OR
def condIntermedio(arr, eV, eF):
    global cont_temp
    global cont_etiqueta
    if arr[len(arr) - 1][2] == 'and':
        andIntermedio(arr, eV, eF)
    elif arr[len(arr) - 1][2] == 'or':
        orIntermedio(arr, eV, eF)
    else:
        insertarinter([arr[len(arr) - 1][0], arr[len(arr) - 1][1], arr[len(arr) - 1][2], 'goto ' + str(eV)])
        insertarinter(['', '', '', 'goto ' + str(eF)])


# And Codigo Intermedio
def andIntermedio(arr, eV, eF):
    global cont_etiqueta
    rizq = arr[len(arr) - 1][0]
    rder = arr[len(arr) - 1][1]
    E1v = cont_etiqueta
    cont_etiqueta = cont_etiqueta + 10
    E1f = eF
    E2v = eV
    E2f = eF
    arrbusqueda = np.array(arr)[:, 3]
    iizq = np.where(arrbusqueda == rizq)[0][0]
    ider = np.where(arrbusqueda == rder)[0][0]
    condIntermedio(arr[:iizq + 1], E1v, E1f)
    insertarinter(['', '', str(E1v) + ':', ''])
    condIntermedio(arr[:ider + 1], E2v, E2f)


# OR codigo Intermedio
def orIntermedio(arr, eV, eF):
    global cont_etiqueta
    E1v = eV
    E1f = cont_etiqueta
    cont_etiqueta = cont_etiqueta + 10
    E2v = eV
    E2f = eF
    rizq = arr[len(arr) - 1][0]
    rder = arr[len(arr) - 1][1]
    arrbusqueda = np.array(arr)[:, 3]
    iizq = np.where(arrbusqueda == rizq)[0][0]
    ider = np.where(arrbusqueda == rder)[0][0]
    condIntermedio(arr[:iizq + 1], E1v, E1f)
    insertarinter(['', '', str(E1f) + ':', ''])
    condIntermedio(arr[:ider + 1], E2v, E2f)


# insercion codigo intermedio
# depende de el nivel actual de el codigo
def insertarinter(arr):
    global inter_metodo
    if metActual() == 0:
        inter.append(arr)
    else:
        inter_metodo.append(arr)


# incrementa el uso del metodo
def metodo_incrementar(met):
    for i in metodos:
        if i[0] == met:
            i[3] = i[3] + 1


# Declaracion global de las variables inciales
def funcglobal():
    global cont_temp
    global cont_etiqueta
    cont_temp = 0
    cont_etiqueta = 10


# Verificacion metodos no utilizados
def metodoNoUtilizado():
    for i in metodos:
        if i[3] == 0:
            return True
    return False


# validaacion si el metodo existe
def metodoDeclarado(var):
    for i in metodos:
        if i[0] == var:
            return True
    return False


# Devuelve el tipo de una variable
def varsTipoMetodo(metodo):
    i_param = 0
    if metodoDeclarado(metodo):
        for i in metodos:
            print(i)
            #sleep(2)
            if i[0] == metodo:
                num_par = i[2]
                break
            i_param = i_param + 1

        tipos = []
        for i in varDeclaradas:
            if len(tipos) == num_par:
                break
            if i[2] == i_param:
                tipos.append(i[0])
        return tipos
    else:
        return False


# metodo que valida que una varible no este declarada para poder insertarla en la tabla
# de variables
def notInVarDec(var, mact):
    for i in varDeclaradas:
        if i[1] == var and i[2] == mact:
            return False
    return True


'''def VarDec(var,mact):
    for i in varDeclaradas:
        if i[1]==1
    return False'''


# regresa el tipo de una variable
def vartipo(var):
    mact = metActual()
    for i in varDeclaradas:
        if i[1] == var and (i[2] == mact or i[2] == 0):
            return i[0]
    return None


def buscarVar(var):
    mact = metActual()
    for i in varDeclaradas:
        if i[1] == var and (i[2] == mact or i[2] == 0):
            return True
    return False


# regresa la posicion de una variable
def traerVar(var):
    mact = metActual()
    for i in varDeclaradas:
        if i[1] == var and (i[2] == mact or i[2] == 0):
            return i
    return False


# incrementa el uso de una variable para la validacion de
# variables utilizadas
def varIncremetaUso(var):
    mact = metActual()
    for i in varDeclaradas[::-1]:
        if i[1] == var and (i[2] == mact or i[2] == 0):
            varDeclaradas[varDeclaradas.index(i)] = [i[0], i[1], i[2], i[3] + 1]
            break


# devuelve el metodo actual en el ue se encuentre siendo el 0 el metodo principal
def metActual():
    for i in range(len(metodos) - 1, -1, -1):
        if metodos[i][1] == False:
            return i


# aqui empiezan metodos gramatica
def senR1p(arr, i, arr2):
    print(bcolors.WARNING + "senR1p" + bcolors.ENDC)
    if arr[i] in [18, 10, 6, 11, 12, 19]:  # leer,imprimir,leer,si,mients,var
        i = senR1(arr, i, arr2)
        return i
    else:
        return i


def senR1(arr, i, arr2):
    print(bcolors.WARNING + "senR1" + bcolors.ENDC)
    if arr[i] in [18, 10, 6, 11, 12, 19]:  # leer,imprimir,leer,si,mients,var
        i = sentencia(arr, i, arr2)
        i = senR1p(arr, i, arr2)
        return i
    else:
        return 'a'


# sentencia while
def senRep(arr, i, arr2):
    global cont_temp
    print(bcolors.WARNING + "senRep" + bcolors.ENDC)
    global cont_etiqueta
    # generacion etiquetas
    eI = cont_etiqueta
    cont_etiqueta = cont_etiqueta + 10
    eV = cont_etiqueta
    cont_etiqueta = cont_etiqueta + 10
    eF = cont_etiqueta
    cont_etiqueta = cont_etiqueta + 10
    # fin generacion etiqueta
    if arr[i] == 12 and arr[i + 1] == 16:  # mientras (
        i = i + 2
        aux_cond = i
        i = condicion(arr, i, arr2)
        arrAux = []
        arrAux2 = []
        # generacion codigo intermedio
        insertarinter(['', '', str(eI) + ':', '', 'Incio Ciclo'])
        for p in range(aux_cond, i):
            arrAux2.append(arr2[p])
            if arr2[p] not in separadores and arr[p] == 6:
                arrAux.append(arr2[p])
        if arr[i] == 17 and arr[i + 1] == 3:  # ) {
            i = i + 2
            # Codigo intermedio
            if len(arrAux2) == 3:
                # generacion de etiquetas
                insertarinter([arrAux2[0], arrAux2[2], arrAux2[1], 'goto ' + str(eV)])
                # print([arrAux2[0],arrAux2[2],arrAux2[1],str(eV)])
                insertarinter(['', '', '', 'goto ' + str(eF)])
                insertarinter(['', '', str(eV) + ':', ''])
                varIncremetaUso(arrAux2[0])
                varIncremetaUso(arrAux2[2])
            else:
                auxVariables = np.array(varDeclaradas)[:, 1]
                for l in arrAux2:
                    if l in auxVariables:
                        varIncremetaUso(l)
                arr_temp = temporales.temporalesPosfijo(arrAux2, cont_temp)
                band = False
                for k in arr_temp:
                    if k[2] in ['+', '-', '*', '/']:
                        inter.append(k)
                        band = True
                if band == True:
                    cont_temp = int(arr_temp[len(arr_temp) - 1][3][1:]) + 1
                condIntermedio(arr_temp, eV, eF)
                insertarinter(['', '', str(eV) + ':', ''])

            for p in range(aux_cond, i):
                if arr[p] == 7:  # num
                    arrAux.append("num")

                if arr[p] == 8:  # num
                    arrAux.append("cad")

            # fin codigo intermedio
            i = senR1(arr, i, arr2)
            if arr[i] == 4:  # }
                i = i + 1
                insertarinter(['', '', '', 'goto ' + str(eI)])
                insertarinter(['', '', str(eF) + ':', '', 'Fin Ciclo'])
                return i
            else:
                return 'a'
        else:
            return 'a'
    else:
        return 'a'


def expresion(arr, i, arr2):
    print(bcolors.WARNING + "expresion" + bcolors.ENDC)
    if arr[i] in [6, 7, 8]:  # var num cad
        i = i + 1
        return i
    else:
        return 'a'


def con1(arr, i, arr2):
    print(bcolors.WARNING + "con1" + bcolors.ENDC)
    if arr[i] == 23:  # OpLog
        i = i + 1
        i = condicion(arr, i, arr2)
        i = con1(arr, i, arr2)
        return i
    else:
        return i


def condicion(arr, i, arr2):
    print(bcolors.WARNING + "condicion" + bcolors.ENDC)
    if arr[i] in [6, 7, 8]:  # var num cad
        i = EXP(arr, i, arr2)
        if arr[i] == 22:  # OpRel
            i = i + 1
            i = EXP(arr, i, arr2)
            i = con1(arr, i, arr2)

            return i
        else:
            return 'a'
    else:
        return 'a'


def senC2(arr, i, arr2):
    print(bcolors.WARNING + "senC2" + bcolors.ENDC)
    if arr[i] == 21 and arr[i + 1] == 3:  # sino {
        i = i + 2
        i = senC1(arr, i, arr2)
        if arr[i] == 4:  # }
            i = i + 1
            return i
        else:
            return 'a'
    else:
        return i


def senC1(arr, i, arr2):
    print(bcolors.WARNING + "senC1" + bcolors.ENDC)
    if arr[i] in [18, 10, 6, 11, 12, 19]:  # leer,imprimir,leer,si,mients,var
        i = sentencia(arr, i, arr2)
        i = senC1(arr, i, arr2)
        return i
    else:
        return i


# sentencia if
def senCond(arr, i, arr2):
    global cont_etiqueta
    global cont_temp
    # generacion etiquetas
    eV = cont_etiqueta
    cont_etiqueta = cont_etiqueta + 10
    eF = cont_etiqueta
    cont_etiqueta = cont_etiqueta + 10
    eS = cont_etiqueta
    cont_etiqueta = cont_etiqueta + 10
    # print(cont_etiqueta)
    # sleep(1)
    print(bcolors.WARNING + "senCond" + bcolors.ENDC)
    if arr[i] == 11 and arr[i + 1] == 16:  # si (
        i = i + 2
        aux_cond = i
        arrAux = []
        arrAux2 = []
        # validacion tipos condicion si
        i = condicion(arr, i, arr2)
        for p in range(aux_cond, i):
            arrAux2.append(arr2[p])
            if arr2[p] not in separadores and arr[p] == 6:
                arrAux.append(arr2[p])
        # print(arrAux2)
        if len(arrAux2) == 3:
            # generacion de intermedio
            insertarinter([arrAux2[0], arrAux2[2], arrAux2[1], 'goto ' + str(eV), 'Inicio Condicion'])
            # print([arrAux2[0],arrAux2[2],arrAux2[1],str(eV)])
            insertarinter(['', '', '', 'goto ' + str(eF)])
            insertarinter(['', '', str(eV) + ':', ''])
        else:
            auxVariables = np.array(varDeclaradas)[:, 1]
            for l in arrAux2:
                if l in auxVariables:
                    varIncremetaUso(l)
            # 1
            arr_temp = temporales.temporalesPosfijo(arrAux2, cont_temp)
            band = False
            for k in arr_temp:
                if k[2] in ['+', '-', '*', '/']:
                    inter.append(k)
                    band = True
            if band == True:
                cont_temp = int(arr_temp[len(arr_temp) - 1][3][1:]) + 1
                condIntermedio(arr_temp, eV, eF)
                insertarinter(['', '', str(eV) + ':', ''])
            # 2

        for p in range(0, len(arrAux)):
            if vartipo(arrAux[p]) != None:
                arrAux[p] = vartipo(arrAux[p])
            else:
                print("variable no declarada")
                i = 'a'

        for p in range(aux_cond, i):
            if arr[p] == 7:  # num
                arrAux.append("num")

            if arr[p] == 8:  # num
                arrAux.append("cad")
        if len(list(set(arrAux))) != 1:
            print("Error Tipos No Compatibles")
            i = 'a'
        # print(list(set(arrAux)))
        # print(arrAux)
        if arr[i] == 17 and arr[i + 1] == 3:  # ) {
            i = i + 2
            i = senC1(arr, i, arr2)
            if arr[i] == 4:  # }
                i = i + 1
                insertarinter(['', '', '', 'goto ' + str(eS)])
                insertarinter(['', '', str(eF) + ':', ''])
                i = senC2(arr, i, arr2)
                insertarinter(['', '', str(eS) + ':', '', 'Fin Condicion'])
                # sleep(5)
                return i
            else:
                return 'a'
        else:
            return 'a'
    else:
        return 'a'


def Ep(arr, i, arr2):
    print(bcolors.WARNING + "Ep" + bcolors.ENDC)
    if arr[i] == 20:
        i = OArit(arr, i, arr2)
        i = EXP(arr, i, arr2)
        return i
    else:
        return i


def EXP(arr, i, arr2):
    print(bcolors.WARNING + "EXP" + bcolors.ENDC)
    if arr[i] == 16:  # (
        i = i + 1
        i = EXP(arr, i, arr2)
        if arr[i] == 17:  # )
            i = i + 1
            i = Ep(arr, i, arr2)
            return i
        else:
            return 'a'
    elif arr[i] == 6:  # var
        i = i + 1
        i = Ep(arr, i, arr2)
        return i
    elif arr[i] == 7:  # num
        i = i + 1
        i = Ep(arr, i, arr2)
        return i
    elif arr[i] == 8:  # cad
        i = i + 1
        i = Ep(arr, i, arr2)
        return i
    else:
        return 'a'


def asignacion(arr, i, arr2):
    print(bcolors.WARNING + "asignacion" + bcolors.ENDC)
    global cont_temp
    var_actual = arr2[i]
    valor_actual = arr2[i + 2]
    if arr[i] == 6 and arr[i + 1] == 14:  # var =
        mact = metActual()
        arrasig = []
        pos_inicio = i + 2
        pos_fin = i
        operacion = []
        arr_temp = []
        # comprobacion var declarada y tipos compatibles
        if vartipo(arr2[i]) == 'num':
            p = i + 2
            while arr2[p] != ';':
                if arr2[p] not in separadores:
                    arrasig.append(p)
                p = p + 1
            pos_fin = p
            for p in arrasig:
                if arr[p] == 6:
                    varIncremetaUso(arr2[p])
            for p in arrasig:
                if arr[p] == 6 and vartipo(arr2[p]) != 'num':
                    if vartipo(arr2[p]) == None:
                        print("Variable ", arr2[p], " no declarada")
                    else:
                        print('Error Tipos no compatibles', arr2[p])
                    i = 'a'
                if arr[p] == 8:
                    print('Error Cadena no compatible con  var Numerica')
                    i = 'a'

            # temporales asignacion
            if pos_fin - pos_inicio > 1:
                for k in range(pos_inicio, pos_fin):
                    operacion.append(arr2[k])
                arr_temp = temporales.temporalesPosfijo(operacion, cont_temp)
                cont_temp = int(arr_temp[len(arr_temp) - 1][3][1:]) + 1

                for k in arr_temp:
                    inter.append(k)
                inter.append([arr_temp[len(arr_temp) - 1][3], '', '=', var_actual])
            else:
                inter.append([valor_actual, '', '=', var_actual])

        else:
            p = i + 2
            while arr2[p] != ';':
                if arr2[p] not in separadores:
                    arrasig.append(p)
                p = p + 1
            for p in arrasig:
                if arr[p] == 6 and vartipo(arr2[p]) != 'cad':
                    if vartipo(arr2[p]) == None:
                        print("Variable ", arr2[p], " no declarada")
                    else:
                        print('Error Tipos no compatibles', arr2[p])
                    i = 'a'
                if arr[p] == 7:
                    print('Error numero no compatible con  var tipo Cadena')
                    i = 'a'
        # print(arrasig)
        # print(arr2[i],buscarVar(arr2[i]),vartipo(arr2[i]))
        if notInVarDec(arr2[i], mact):
            print(arr2[i], 'error var no declarada')
        i = i + 2
        # sin esto acepta suma de cadenas y agregando 8 en el siguiente if
        '''if arr[i]== 8:#cadena
            i= i+1
            if arr[i]==9:#;
                i=i+1
                return i
        el'''
        if arr[i] in [16, 6, 7, 8]:  # ( | var | num | cad
            i = EXP(arr, i, arr2)
            if arr[i] == 9:  # ;
                i = i + 1
                return i
        else:
            return 'a'

    else:
        return 'a'


def OArit(arr, i, arr2):
    print(bcolors.WARNING + "OArit" + bcolors.ENDC)
    if arr[i] == 20:  # ORAIT + - * /
        i = i + 1
        return i
    else:
        return 'a'


def lectura(arr, i, arr2):
    print(bcolors.WARNING + "lectura" + bcolors.ENDC)
    if arr[i] == 18:  # leer
        i = i + 1
        if arr[i] == 6 and vartipo(arr2[i]) != None:
            varIncremetaUso(arr2[i])
            insertarinter(['', '', 'leer', arr2[i]])
            i = i + 1
        else:
            print("Variable ", arr2[i], " no declarada o tipo de dato incorrecto")
            i = 'a'

        # i=expresion(arr,i,arr2)

        if arr[i] == 9:  # ;
            i = i + 1
            return i
        else:
            return 'a'
    else:
        return 'a'


'''def llmet2(arr,i,arr2):
    print(bcolors.WARNING + "llmet2" + bcolors.ENDC)
    if arr[i]==6:#var
        i=i+1
        i=llmet2(arr,i,arr2)
        return i
    else:
        return i


def llmet(arr,i,arr2):
    print(bcolors.WARNING + "llmet" + bcolors.ENDC)
    if arr[i]==6 and arr[i+1]==16:# var (
        i=i+2
        i=llmet2(arr,i,arr2)
        if arr[i]==17 and arr[i+1]==9:# ) ;
            i=i+2
            return i
        else:
            return 'a'
    else:
        return 'a'
        
        '''


def param2(arr, i, arr2):
    print(bcolors.WARNING + "param2" + bcolors.ENDC)
    if arr[i] == 13:  # ,
        i = i + 1
        i = param(arr, i, arr2)
        return i
    else:
        return i


def param(arr, i, arr2):
    print(bcolors.WARNING + "param" + bcolors.ENDC)
    if arr[i] == 6:  # var
        i = i + 1
        i = param2(arr, i, arr2)
        return i
    else:
        return 'a'


def llamar(arr, i, arr2):
    print(bcolors.WARNING + "llamar" + bcolors.ENDC)
    if arr[i] == 19 and arr[i + 1] == 6 and arr[i + 2] == 16:  # llamar Var (
        met = False                         #bandera para insertar en el metodo
        for j in inter_metodo:
            print(j[2][-1])
            if met:
                if j[2][-1]==':':
                    met = False
                else:
                    insertarinter(j)
            if j[2]== str(arr2[i + 1])+':':
                met = True
                print(j)
                #sleep(2)


        var = arr2[i + 1]
        metodo_incrementar(var)
        i = i + 3
        ini_param = i
        i = param(arr, i, arr2)
        fin_param = i
        tipos_reales = []
        for q in range(ini_param, fin_param):
            if arr[q] == 6:
                tipos_reales.append(vartipo(arr2[q]))

        tipos_esperados = varsTipoMetodo(var)
        if tipos_esperados == False:
            print('Metodo ', var, 'no Declarado')
            i = 'a'
        else:
            if len(tipos_reales) != len(tipos_esperados):
                print('numero de parametros incorrecto en metodo ', var)
                i = 'a'
            elif tipos_reales != tipos_esperados:
                print('tipos de parametros incorrectos en metodo ', var)
                i = 'a'

        if arr[i] == 17 and arr[i + 1] == 9:  # ) ;
            i = i + 2
            return i
    else:
        return 'a'


def sentencia(arr, i, arr2):
    print(bcolors.WARNING + "sentencia" + bcolors.ENDC)
    if arr[i] == 18:  # leer
        i = lectura(arr, i, arr2)
        return i
    elif arr[i] == 10:  # imprimir
        i = escritura(arr, i, arr2)
        return i
    elif arr[i] == 6 and arr[i + 1] == 14:  # var =
        # cadena=
        i = asignacion(arr, i, arr2)
        return i
    elif arr[i] == 11:  # si
        i = senCond(arr, i, arr2)
        return i
    elif arr[i] == 12:  # mientras
        i = senRep(arr, i, arr2)
        return i
    elif arr[i] == 19:  # llamar
        i = llamar(arr, i, arr2)
        return i
    else:

        return 'a'


def esc1(arr, i, arr2):
    print(bcolors.WARNING + "esc1" + bcolors.ENDC)
    if arr[i] in [6, 8] and arr2[i + 1] not in operadores:  # cadena | Var
        if arr[i] == 6 and vartipo(arr2[i]) == None:
            print("Variable ", arr2[i], " no declarada")
            i = 'a'
        elif arr[i] == 6 and vartipo(arr2[i]) != None:
            varIncremetaUso(arr2[i])
        i = i + 1
        return i
    else:
        i = EXP(arr, i, arr2)

        # print(arr2[i])
        # sleep(1)
        return i


def escritura(arr, i, arr2):
    global cont_temp
    print(bcolors.WARNING + "escritura" + bcolors.ENDC)
    if arr[i] == 10:  # imprimir
        i = i + 1
        pos_inicio = i
        # insertarinter(['','','imprimir',arr2[i]])
        i = esc1(arr, i, arr2)
        pos_fin = i
        if arr[pos_inicio] == 9:
            insertarinter(['', '', 'imprimir', arr2[i]])
        else:
            operacion = []
            for k in range(pos_inicio, pos_fin):
                operacion.append(arr2[k])

            if arr[pos_inicio] == 8:
                insertarinter(['', '', 'imprimir', arr2[i - 1]])
            else:
                if len(operacion) == 1:

                    insertarinter(['', '', 'imprimir', arr2[i - 1]])
                else:
                    arr_temp = temporales.temporalesPosfijo(operacion, cont_temp)
                    cont_temp = int(arr_temp[len(arr_temp) - 1][3][1:]) + 1
                    for k in arr_temp:
                        insertarinter(k)
                    insertarinter(['', '', 'imprimir', arr_temp[len(arr_temp) - 1][3]])

        if arr[i] == 9:  # ;
            i = i + 1
            return i
        else:
            return 'a'
    else:
        return 'a'


def metodo(arr, i, arr2):
    print(bcolors.WARNING + "metodo" + bcolors.ENDC)
    if arr[i] == 6 and arr[i + 1] == 16:  # var (
        if metodoDeclarado(arr2[i]):
            print('Metodo ' + arr2[i] + ' repetido')
            i = 'a'
        else:
            metodos.append([arr2[i], False, 0, 0])
        insertarinter(['', '', arr2[i] + ':', ''])
        i = i + 2
        if arr[i] == 5:
            i = decmet(arr, i, arr2)
        if arr[i] == 17 and arr[i + 1] == 3:  # ) {
            i = i + 2
            if arr[i] == 5:
                i = ini1met(arr, i, arr2)

            i = ini2met(arr, i, arr2)
            if arr[i] == 4:  # }
                i = i + 1
                metodos[len(metodos) - 1][1] = True
                return i
            else:
                return 'a'
        else:
            return 'a'


def dec2(arr, i, arr2):
    print(bcolors.WARNING + "dec2" + bcolors.ENDC)

    if arr[i] == 6 and arr[i + 1] == 14:  # var =
        i = asignacion(arr, i, arr2)
        if True:  # arr[i]==9:# ;

            # i=i+1
            return i
        else:
            return 'a'
    if arr[i] == 6 and arr[i + 1] == 9:  # var ;
        i = i + 2
        return i
    else:
        return 'a'


def decmet2(arr, i, arr2):
    print(bcolors.WARNING + "decmet2" + bcolors.ENDC)
    if arr[i] == 13:  # ,
        i = i + 1
        i = decmet(arr, i, arr2)
        return i
    else:
        return i


def decmet(arr, i, arr2):
    print(bcolors.WARNING + "decmet" + bcolors.ENDC)
    if arr[i] == 5 and arr[i + 1] == 6:  # Tdato Var
        mact = metActual()
        metodos[mact] = [metodos[mact][0], metodos[mact][1], metodos[mact][2] + 1, metodos[mact][3]]
        # print(mact)
        # print(arr2[i+1])
        # print(notInVarDec(arr2[i+1],mact))
        if notInVarDec(arr2[i + 1], mact):
            varDeclaradas.append([arr2[i], arr2[i + 1], mact, 0])
        else:
            print('ERROR var ', arr2[i + 1], 'repetida')
            i = -1
        i = i + 2
        i = decmet2(arr, i, arr2)
        return i
    else:
        return 'a'


def declaracion(arr, i, arr2):
    global cont_temp
    print(bcolors.WARNING + "declaracion" + bcolors.ENDC)
    if arr[i] == 5:  # tdato
        mact = metActual()
        # print(mact)
        # print(arr2[i+1])
        # print(notInVarDec(arr2[i+1],mact))
        if notInVarDec(arr2[i + 1], mact):
            varDeclaradas.append([arr2[i], arr2[i + 1], mact, 0])
        else:
            print('ERROR var ', arr2[i + 1], 'repetida')
            i = 'a'

        i = i + 1
        # print(arr2[i])
        varDec_inter.append(['', '', arr2[i - 1], arr2[i], ''])
        # sleep(1)
        auxInicio = i + 1
        i = dec2(arr, i, arr2)
        auxFin = i

        temp = []
        if auxFin - auxInicio > 1:
            # print('Decalracion compleja')
            if (auxFin - 1) - (auxInicio + 1) > 1:
                for cont in range(auxInicio + 1, auxFin - 1):
                    temp.append([cont, arr[cont]])
                variables.append(temp)
                # print(temp)
                aux_cad = []
                for cont in temp:
                    aux_cad.append(arr2[cont[0]])
                # print(aux_cad)
                arr_temp = temporales.temporalesPosfijo(aux_cad, cont_temp)
                cont_temp = int(arr_temp[len(arr_temp) - 1][3][1:]) + 1
                '''if len(arr_temp)>1:
                    for j in arr_temp:
                        inter.append(j)
                    inter.append([arr_temp[len(arr_temp)-1][3],'','=',var_actual])'''

        # sleep(1)

        return i
    elif arr[i] == 6 and arr[i + 1] == 16:  # var (
        i = metodo(arr, i, arr2)
        # if arr[i]==9:#;
        aux = i
        # bug
        '''for cont in range(auxInicio,auxFin):
            temp.append([cont,arr[cont]])
        variables.append(temp)'''
        i = aux
        return i
    return 'a'


def ini2p(arr, i, arr2):
    print(bcolors.WARNING + "ini2p" + bcolors.ENDC)
    if arr[i] in [18, 10, 6, 11, 12, 19]:  # leer,imprimir
        i = ini2(arr, i, arr2)
        return i
    else:
        return i


def ini2(arr, i, arr2):
    print(bcolors.WARNING + "ini2" + bcolors.ENDC)
    if arr[i] in [18, 10, 6, 11, 12, 19]:  # leer,imprimir,leer,si,mients,var
        i = sentencia(arr, i, arr2)
        i = ini2p(arr, i, arr2)
        return i

    return 'a'


def ini2metp(arr, i, arr2):
    print(bcolors.WARNING + "ini2p" + bcolors.ENDC)
    if arr[i] in [18, 10, 6, 11, 12, 19]:  # leer,imprimir
        i = ini2(arr, i, arr2)
        return i
    else:
        return i


def ini2met(arr, i, arr2):
    print(bcolors.WARNING + "ini2" + bcolors.ENDC)
    if arr[i] in [18, 10, 6, 11, 12, 19]:  # leer,imprimir,leer,si,mients,var
        i = sentencia(arr, i, arr2)
        i = ini2p(arr, i, arr2)
        return i

    return 'a'


def ini1p(arr, i, arr2):
    print(bcolors.WARNING + "ini1p" + bcolors.ENDC)
    if arr[i] in [5, 6]:
        i = ini1(arr, i, arr2)
        return i
    else:
        return i


def ini1(arr, i, arr2):
    print(bcolors.WARNING + "ini1" + bcolors.ENDC)
    if arr[i] in [5, 6]:  # tDato Var
        i = declaracion(arr, i, arr2)
        i = ini1p(arr, i, arr2)

        return i
    return 'a'


def ini1metp(arr, i, arr2):
    print(bcolors.WARNING + "ini1p" + bcolors.ENDC)
    if arr[i] in [5, 6]:
        i = ini1(arr, i, arr2)
        return i
    else:
        return i


def ini1met(arr, i, arr2):
    print(bcolors.WARNING + "ini1" + bcolors.ENDC)
    if arr[i] in [5, 6]:  # tDato Var
        i = declaracion(arr, i, arr2)
        i = ini1p(arr, i, arr2)

        return i
    return 'a'


# produccion inicio
def inicio(arr, i, arr2):
    print(bcolors.WARNING + "inicio" + bcolors.ENDC)
    try:
        funcglobal()
        if arr[i] == 1 and arr[i + 1] == 3 and len(arr) >= 4:  # inicio {
            i = i + 2
            i = ini1(arr, i, arr2)
            i = ini2(arr, i, arr2)
            if arr[i] == 4 and arr[i + 1] == 2:  # }    fin
                varT = np.transpose(np.array(varDeclaradas))
                metUso = []
                for k in metodos:
                    metUso.append(k[2])
                # validacion variables  y metodos no utilizadas
                if '0' in np.ndarray.tolist(varT)[3]:
                    print(bcolors.FAIL + "ERROR Variables No UTILIZADAS" + bcolors.ENDC)
                    return False
                else:
                    if metodoNoUtilizado():
                        print('metodo no utilizado')
                        return False
                    else:
                        print(bcolors.OKGREEN + 'Correcto!' + bcolors.ENDC)
                        for p in inter_metodo:
                            inter.append(p)

                        return True
            else:
                print(bcolors.FAIL + "Error 1" + bcolors.ENDC)
                return False
        else:
            print(bcolors.FAIL + "Error 2" + bcolors.ENDC)
            return False
    except:
        print(bcolors.FAIL + "Error 3" + bcolors.ENDC)
        return False


# el metodo corre todo el codigo intermedio
def codigoIntermedio(var, tokpal):
    cuadruples = []
    for i in var:
        if i[0][1] == 5 and i[1][1] == 6 and i[2][1] == 9:
            # print('declaracion simple')
            cuadruples.append([tokpal[i[1][0]], '', tokpal[i[0][0]], ''])
        if i[0][1] == 5 and i[1][1] == 6 and i[2][1] == 14 and i[4][1] == 9:
            # print('declaracion asignacion simple')
            cuadruples.append([tokpal[i[1][0]], '', tokpal[i[0][0]], ''])
            cuadruples.append([tokpal[i[1][0]], '', '=', tokpal[i[3][0]]])
    return cuadruples


def analizadorGramatica(arr, arr3):
    arr2 = []
    for i in arr:
        arr2.append(int(i))
    # la linea comntada imprime el arreglo de num
    # print(arr2)
    return inicio(arr2, 0, arr3)
