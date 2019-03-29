def pot(a,b):
    x=a**b
    print(x)
    return(x)

for i in range(0,2):
    a=int(input("ingrese la base"))
    b=int(input("ingrese el exponente"))
    if i==0:
        V1=pot(a,b)
    else:
        V2=pot(a,b)

if V1>V2:
    print("la primera potencia ingresada es mayor")
else:
    print("la segunda potencia que ingreso es mayor")
