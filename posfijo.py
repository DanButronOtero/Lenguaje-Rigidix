pilaPrin=[]
pilaSec=[]

arr = [
'(', 'a', '*', 'b', '+', 'c', '/', 'b', ')', '+', 'a', '*', 'a', '+', '(', 'b', '+', 'c', '/', 'd', ')', '+', 'a']

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
#print(arr)

def clasificar(car):
    if car=='*':
        return 5
    if car=='/':
        return 5
    if car=='+':
        return 4
    if car=='-':
        return 4
    if car=='(':
        return 8
    if car==')':
        return 7
    if car=='<':
        return 1
    if car=='>':
        return 1
    if car=='==':
        return 1
    if car=='!=':
        return 1
    if car=='<=':
        return 1
    if car=='>=':
        return 1
    if car=='=':
        return 0
    if car=='and':
        return 0
    if car=='or':
        return 0
    else:
        return 10

#principal
def posfijo(arr):
    for i in arr:

        if i not in operadores:
            pilaPrin.append(i)
        elif clasificar(i)==8:#(
            pilaSec.append(i)
        elif clasificar(i)==7:#)

            while pilaSec:
                if pilaSec[len(pilaSec)-1]=='(':
                    pilaSec.pop()
                    break
                else:
                    pilaPrin.append(pilaSec.pop())

        elif len(pilaSec) != 0:
            print(pilaSec)
            if clasificar(i)<= clasificar(pilaSec[len(pilaSec)-1]):
                while clasificar(i)<= clasificar(pilaSec[len(pilaSec)-1]) and clasificar(pilaSec[len(pilaSec)-1]) !=8 and len(pilaSec)-1>0:
                    aux =pilaSec.pop()
                    pilaPrin.append(aux)
                pilaSec.append(i)
            else:
                pilaSec.append(i)
        else:
            pilaSec.append(i)



    while pilaSec:
        aux =pilaSec.pop()
        if clasificar(aux) != 8:
            pilaPrin.append(aux)

    return pilaPrin

    

'''arrpos4=['(','a','>','b','or','b','<','c',')','or','(','c','>','d','and','c','<','b',')']
salida=posfijo(arrpos4)
print(salida)'''


