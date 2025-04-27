print("Ingresá 1 para convertir números binarios a decimales")
print("Ingresá 2 para convertir números decimales a binarios")
opc=input()
if(opc=="1"):
    num=input("Ingresá el número binario que querés convertir: ")
    potencia=len(num)-1
    acum=0
    for i in num:
        try:
            conv=int(i)*(2**potencia)
            acum+=conv
            potencia-=1
        except ValueError:
            print("Por favor, ingresá un número binario válido.")    
            exit() 
    print(f"El número binario {num} es igual a {acum} en el sistema decimal")
 
elif(opc=="2"):
    try:
        num=float(input("Ingresá el número entero que te gustaría convertir: "))
        num = int(num)
    except ValueError:
        print("Por favor, ingresá un número entero.")
        exit()
                
    if(num==0):
       print(f"El número ingresado equivale a 0 en el sistema binario")
    elif num<0: 
        print("Por favor, ingresá un número positivo")
    else:
        resultado=""
        while num>=1:
            resto=num%2        
            resultado=resultado+str(resto)        
            num=int(num/2)    
        resInvertido = resultado[::-1]
        print(f"El número ingresado equivale a {resInvertido} en el sistema binario")

else:
    print("Por favor, ingresá una opción válida")