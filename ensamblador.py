import time as tm
import pyperclip
ensamblador = [
'org 100h ',

'include "emu8086.inc"', 

'DEFINE_PRINT_STRING ',

'DEFINE_PRINT_NUM ',

'DEFINE_PRINT_NUM_UNS',   

'DEFINE_SCAN_NUM ',

 

'.model small ',

'.stack 64 ',

'.data ']
inicio = [
    '.code ',
    'inicio proc far',
        'mov ax,@data', 
        'mov ds,ax',
        ''     
]
def generaEnsamblador(arr):
    variables = []
    mensajes = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if len(arr[i][j])==5:
                arr[i][j]= [arr[i][j][0],arr[i][j][1],arr[i][j][2],arr[i][j][3]]
                print('quintuple')
    
    for i in arr:
        if i[0] != '' and not i[0].isnumeric():
            if i[0] not in variables:
                variables.append(i[0])
        if i[1] != '' and not i[1].isnumeric():
            if i[1] not in variables:
                variables.append(i[1])
        if i[3] != '' and not i[3].isnumeric() and not "'" in i[3] and not 'goto' in i[3]:
            if i[3] not in variables:
                variables.append(i[3])
    for i in arr:
        if  "'" in i[3]:
            mensajes.append(i[3])
    print(variables)
    cont = 1
    for i in mensajes:
        ensamblador.append('msg'+str(cont)+ ' db 10,13,'+i+",'$'")
        cont +=1
    
    
    ensamblador.append('salto'+ ' db 10,13,'+"''"+",'$'")
    for i in variables:
        ensamblador.append(i+'  dw  0')
    for i in inicio:
        ensamblador.append(i)

    cont = 1
    for i in arr:
        if i[2] =='=':
           ensamblador.append('')
           ensamblador.append('mov cx,'+i[0]) 
           ensamblador.append('mov '+i[3]+',cx')
        if i[2] == 'imprimir' :
            if "'" in i[3]:
                ensamblador.append('')
                ensamblador.append('mov ah,09')
                ensamblador.append('lea dx,msg'+str(cont))
                ensamblador.append('int 21h')        
                ensamblador.append('')
                ensamblador.append('mov ah,09')
                ensamblador.append('lea dx,salto')
                ensamblador.append('int 21h') 
                cont+=1
            else:
                ensamblador.append('')
                ensamblador.append('MOV ax,'+i[3])
                ensamblador.append('call PRINT_NUM ')
                ensamblador.append('')
                ensamblador.append('mov ah,09')
                ensamblador.append('lea dx,salto')
                ensamblador.append('int 21h') 
        if i[2]=='leer':
            ensamblador.append('')
            ensamblador.append('call SCAN_NUM')
            ensamblador.append('mov '+i[3]+',cx')
        if ':' in i[2]:
            ensamblador.append('a'+i[2])
        if 'goto' in i[3] and i[2] =='':
            ensamblador.append('')
            ensamblador.append('jmp a'+i[3][5:])
        if i[2] =='>' :
            ensamblador.append('')
            ensamblador.append('mov cx,'+i[0])
            ensamblador.append('cmp cx,'+i[1])
            ensamblador.append('jnle a'+i[3][5:])

        if i[2] =='<' :
            ensamblador.append('')
            ensamblador.append('mov cx,'+i[0])
            ensamblador.append('cmp cx,'+i[1])
            ensamblador.append('jnge a'+i[3][5:])
        if i[2] =='>=' :
            ensamblador.append('')
            ensamblador.append('mov cx,'+i[0])
            ensamblador.append('cmp cx,'+i[1])
            ensamblador.append('jl a'+i[3][5:])

        if i[2] =='<=' :
            ensamblador.append('')
            ensamblador.append('mov cx,'+i[0])
            ensamblador.append('cmp cx,'+i[1])
            ensamblador.append('jle a'+i[3][5:])
        
        if i[2] == '+':
            ensamblador.append('')
            ensamblador.append('mov cx,'+i[0])
            ensamblador.append('add cx,'+i[1])
            ensamblador.append('mov '+i[3]+',cx')
        
        if i[2] == '-':
            ensamblador.append('')
            ensamblador.append('mov cx,'+i[0])
            ensamblador.append('sub cx,'+i[1])
            ensamblador.append('mov '+i[3]+',cx')

        if i[2] == '*':
            ensamblador.append('')
            ensamblador.append('mov ax,'+i[0])
            ensamblador.append('mov bx,'+i[1])
            ensamblador.append('mul bx')
            ensamblador.append('mov '+i[3]+',ax')




        if i[2] == '/':
            ensamblador.append('mov ax,'+i[0])
            ensamblador.append('mov bx,'+i[1])
            ensamblador.append('xor dx,dx')
            ensamblador.append('div bx')
            ensamblador.append('mov cx,ax')
            ensamblador.append('mov '+i[3]+',cx')
            ensamblador.append('')

        


    cadena = ''
    for i in arr:
        cadena = cadena+str(i)+'\n'
    for i in ensamblador:
        cadena = cadena+i+'\n'
        print(i)

    pyperclip.copy(cadena)
    
