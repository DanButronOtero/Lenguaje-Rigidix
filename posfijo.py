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
        return 3
    if car==')':
        return 2
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
        else:
            if len(pilaSec)==0:
                if clasificar(i) != 2:
                    pilaSec.append(i)
            else :
                if clasificar(i) ==2:
                    while pilaSec:
                        aux =pilaSec.pop()
                        if clasificar(aux) != 3:
                            pilaPrin.append(aux)
                else:
                    if clasificar(i)<= clasificar(pilaSec[len(pilaSec)-1]) and clasificar(i) !=3:
                        while pilaSec:
                            aux =pilaSec.pop()
                            if clasificar(aux) != 3:
                                pilaPrin.append(aux)
                        pilaSec.append(i)
                    else:
                        pilaSec.append(i)
    while pilaSec:
        aux =pilaSec.pop()
        if clasificar(aux) != 3:
            pilaPrin.append(aux)


    return pilaPrin

