def Prim_Herm(a):
    b=a+1
    con=0
    for i in range(1,b+1):
        if b%i==0:
            con=con+1
    if con <=2 and a%6 != 0:
        print("el numero efectivamente es primo hermano")
    else:
        print("el numero desafortunadamente no es primo hermano")
        
a=int(input("ingrese un numero"))
Prim_Herm(a)
