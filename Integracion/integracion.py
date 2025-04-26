print("Ingresá 1 para convertir números binarios a decimales")
print("Ingresá 2 para convertir números decimales a binarios")
opc=input()
if(opc=="1"):
    num=input("Ingresá el número binario que querés convertir: ")
    potencia=len(num)-1
    acum=0
    binario=True
    for i in num:
        if(int(i)>1):
            print("Por favor, ingresá un número binario válido.")
            binario=False
            break
        else:
            conv=int(i)*(2**potencia)
            acum+=conv
            potencia-=1        
    if binario: print(f"El número binario {num} es igual a {acum} en el sistema decimal")
 
elif(opc=="2"):
    num=int(input("Ingresá el número entero decimal que te gustaría convertir: "))
    resultado=""
    while num>=1:
        resto=num%2        
        resultado=resultado+str(resto)        
        num=int(num/2)    
    resInvertido = resultado[::-1]
    print(f"El número ingresado equivale a {resInvertido} en el sistema binario")

else:
    print("Por favor, ingresá una opción válida")