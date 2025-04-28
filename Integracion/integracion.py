
def conversion_binarios(num):             # Se define la funcion conversión_binarios 
    potencia=len(num)-1                   # Calcula la potencia máxima de los términos 
    acum=0                                # acumula la suma de los terminos
    for i in num:                         # mantiene la variable como str para iterar directamente                                    
        try:
            if(int(i)>1):                     # asegura que el usuario ingrese solo 0 o 1.
                print("Por favor, ingresá un número binario válido.") 
                exit() 
            conv=int(i)*(2**potencia)     # se intenta convertir cada caracter a int y se lo multiplica por 2 elevado a la potencia que corresponda al término
            acum+=conv                    # se suma el resultado del término                          
            potencia-=1                   # se ajusta la potencia antes de pasar al próximo término (índice)
        except ValueError:                # evita que el usuario ingrese un caracter que no pueda ser convertido a int
            print("Por favor, ingresá un número binario válido.")    
            exit() 
    print(f"El número binario {num} es igual a {acum} en el sistema decimal") # imprime el resultado de la función
 

def conversion_decimales(num):            # Se define la funcion conversión_decimales
    try:
        num=float(num)                    # se convierte el número ingresado a float previendo la posibilidad de que el usuario ingrese un número decimal
        num = int(num)                    # se convierte el número decimal a int
    except ValueError:                    # evita que el usuario ingrese un caracter que no pueda ser convertido a int
        print("Por favor, ingresá un número entero.")
        exit()                
    if(num==0):                           # debido a que el ciclo while finaliza en 1, se prevé la posibilidad de que el usuario ingrese 0 
       print(f"El número ingresado equivale a 0 en el sistema binario")
    elif num<0:                           # evita que el usuario ingrese un número negativo
        print("Por favor, ingresá un número positivo")
    else:
        resultado=""
        while num>=1:                     # se inicia el ciclo while que divide sucesivamente por 2 el número ingresado por el usuario 
            resto=num%2                   # calcula el resto de cada división 
            resultado=resultado+str(resto) # concatena el resto de cada división a la variable "resultado"       
            num=int(num/2)                 # se divide el numero por 2 para ajustarlo y calcular nuevamente el resto en la proxima vuelta del ciclo 
        resInvertido = resultado[::-1]     # permite invertir la lectura de la variable "resultado"
        print(f"El número ingresado equivale a {resInvertido} en el sistema binario") # imprime el resultado de la función




# ********* Programa principal ***********

print("Ingresá 1 para convertir números binarios a decimales")
print("Ingresá 2 para convertir números decimales a binarios")
opc=input()
if(opc=="1"):
    conversion_binarios(input("Ingresá el número binario que querés convertir: "))

elif(opc=="2"):
    conversion_decimales(input("Ingresá el número entero que te gustaría convertir: "))

else:
    print("Por favor, ingresá una opción válida")

