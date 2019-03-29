def Num_Prim(a):
    cont=0
    for i in range(1,a+1):
        if a%i==0:
            cont=cont+1
        
    if cont>2:
        print("numero no es primo")
    else:
        print("numero es primo")

a=int(input("ingrese numero"))
Num_Prim(a)

