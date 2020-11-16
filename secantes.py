tabla = []
punto1=5
punto2=7
#[xi,xi-1,f(xi),f(xi-1),xi+1,error]
#xi+1= xi - (f(xi)(xi-1-xi))/(f(xi-1)-f(xi))
def fx(x):
    #return (pow(x,3))-(8*pow(x,2))+(6*x)+12
    return (pow(x,2)-(3*x)-4)
xs = punto2 - ((fx(punto2)*(punto1-punto2))/(fx(punto1)-fx(punto2)))
err=(round(xs,2)-round(punto2,2))/round(xs,2)*100
tabla.append([1,round(punto2,5),round(punto1,5),round(fx(punto2),5),round(fx(punto1),5),round(xs,5),round(err,5)])
i=2
while abs(err) > 0.00001:
    punto1=punto2
    punto2=xs
    xs = punto2 - ((fx(punto2)*(punto1-punto2))/(fx(punto1)-fx(punto2)))
    err=(xs-punto2)/xs*100
    tabla.append([i,round(punto2,5),round(punto1,5),round(fx(punto2),5),round(fx(punto1),5),round(xs,5),round(err,5)])
    i=i+1
for i in tabla:
    print(i)