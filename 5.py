suma1=0
suma2=0
N= str(input("Ingrese letra:"))
for D in (N):
    if D=="a" or D=="e" or D=="i" or D=="o" or D=="u" or D=="A" or D=="E" or D=="I" or D=="O" or D=="U":
        suma1 += 1
        print("vocal")
    else:
        suma2 += 1
        print("consonante")
suma= suma2+suma1
print("El numero de letras es",suma)