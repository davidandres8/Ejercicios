a=-1
b= -2
c= 3
while a<0 or b<0 or c<0:
    a= float(input("Valor a:"))
    b= float(input("Valor b:"))
    c= float(input("Valor c:"))
if a<b and b<c:
    print(a,b,c)
elif b<a and a<c:
    print(b,a,c)
elif c<a and a<b:
    print(c,a,b)