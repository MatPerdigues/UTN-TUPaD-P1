import time


def busqueda_ciclos(lista1,lista2):
    start=time.time()
    repetidos=[]
    for i in lista1:
        for x in lista2:
            if i == x:
                repetidos.append(i)
    end=time.time()
    return (end-start)*1000



def busqueda_in(lista1,lista2):
    start=time.time()
    repetidos=[]
    for z in lista1:
        if z in lista2:
            repetidos.append(z)
    end=time.time()
    return (end-start)*1000





def busqueda_set(lista1, lista2):
    start=time.time()
    set2 = set(lista2)  
    repetidos = []
    for z in lista1:   
        if z in set2: 
            repetidos.append(z)
    end=time.time()
    return (end-start)*1000




def funcion_principal():
    while True:
        print("**************************************************")
        print("Seleccioná un algoritmo para medir su eficiencia: ")
        print()
        print("[1] busqueda_ciclos")
        print("[2] busqueda_in")
        print("[3] busqueda_set")
        print("[4] Salir del Programa")
        opc=input()
        if opc == "1":
            print("*************")
            print("Procesando...")
            print("*************")
            for n in [100,200,400,800,1600,3200,6400,12800,25600]:
                print(busqueda_ciclos(list(range(n)),list(range(n))))
   
        elif opc == "2":
            print("*************")
            print("Procesando...")
            print("*************")
            for n in [100,200,400,800,1600,3200,6400,12800,25600]:
                print(busqueda_in(list(range(n)),list(range(n))))

        elif opc == "3":
            print("*************")
            print("Procesando...")
            print("*************")
            for n in [100,200,400,800,1600,3200,6400,12800,25600]:
                print(busqueda_set(list(range(n)),list(range(n))))

        elif opc == "4":
            print("Adios!!")
            break

        else:
            print("Por favor ingresá una opción válida.")
            continue      
               

funcion_principal()