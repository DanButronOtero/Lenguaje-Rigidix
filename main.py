import  token2 as tk
import numpy as np
import recursivo as rc
import posfijo as pj
import temporales as tmp
import optimizacion as opt
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

tokens=np.array([
        [1,     'inicio',   'indica inicio del programa'],
        [2,     'fin',      'indica el fin'],
        [3,     '{',        'llave que abre'],
        [4,     '}',        ' que cierra'],
        [5,     'num',      'TDato'],
        [5,     'cad',      'TDato'],
        [9,     ';',        'punto y coma'],
        [10,    'imprimir', 'token escritura'],
        [11,    'si',        'condicional'],
        [12,    'mientras',  'ciclo'],
        [13,    ',',        'coma'],
        [14,    '=',        'asignacion'],
        #[15,    ';',        'punto y coma'],
        [16,    '(', 'parentesis que abre'],
        [17,    ')', 'parentesis que cierra'],
        [18,    'leer',     'token lectura'],
        [19,    'llamar', 'llamada a metodo'],
        [20,    '+',    'OpArit'],
        [20,    '-',    'OpArit'],
        [20,    '*',    'OpArit'],
        [20,    '/',    'OpArit'],
        [21,    'sino', 'Else'],
        [22,    '==',  'OpRel'],
        [22,    '>',   'OpRel'],
        [22,    '<',   'OpRel'],
        [23,    'and',   'OpLog'],
        [23,    'or',   'OpLog'],
        #[,'', ''],
        
        #var        6
        #number     7
        #cadena     8
    ])
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
        ')'
    ]
nombre_archivo= './programa.ejem'
arrToken=tk.tokenizar(nombre_archivo,tokens,separadores)

err = tk.findErr(arrToken)

toknum = np.array(arrToken)[:,0]
tokpal = np.array(arrToken)[:,1]
if len(err)== 0:
    for i in arrToken:
        print(bcolors.OKBLUE + str(i[0])+'\t\t'+i[1]+'\t\t'+i[2] + bcolors.ENDC)
    if rc.analizadorGramatica(toknum,tokpal) == True:
        #print(rc.variables) 
        #inter=rc.codigoIntermedio(rc.variables,tokpal)
        inter=tmp.codigoIntermedio(rc.variables,tokpal)
        print('\nTabla de Simbolos')
        print('Tipo  Token  Metodo  Uso')
        for k in rc.varDeclaradas:
            print(k)
        print('\nMETODOS ')
        for k in rc.metodos:
            print(k)
        print('\n\n')
 
        #print(rc.varDec_inter)
        for q in rc.varDec_inter:
            print(q)
        for q in rc.inter:
            print(q)
        opt.optimizar(rc.inter)
        #print(rc.varDec_inter)
else:
    for i in err:
        print(bcolors.FAIL + str(i[0])+'\t\t'+i[1]+'\t\t'+i[2] + bcolors.ENDC)

arrpos = [
'(', 'a', '*', 'b', '+', 'c', '/', 'b', ')', '+', 'a', '*', 'a', '+', '(', 'b', '+', 'c', '/', 'd', ')', '+', 'a']
arpos2=['5','+','2','*','b','+','3',]
pil =pj.posfijo(arrpos)
string = ''
#print(pil)
for i in pil:
    string = string+' '
    string = string + i
#print(string)