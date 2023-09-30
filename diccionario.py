agenda = {}

while True:
    print("Menu de la agenda")
    print("1. Agregar/Cambiar")
    print("2. Buscar")
    print("3. Eliminar")
    print("4. Mostrar items")
    print("5. Salir")
    
    opcion = input("Seleccione una opcion 1,2,3,4,5")
    
    if opcion == "1":
        nombre = input("Ingrese el nombre del compañero")
        telefono = input("Ingrese el numero del telefono")
        
        if nombre in agenda:
            print(f"El telefono actual de {nombre} es: {agenda[nombre]}")
            
            if input ("¿Desea cambiar el telefono? (S/N):").lower() == "s":
                agenda[nombre] = telefono
                print(f"El telefono de {nombre} se ha actualizado")
                
        else:
            agenda[nombre] = telefono
            print(f"{nombre} ha sido agregado a la agenda")
            
    elif opcion == 2:
        cadena = input("Ingrese una cadena de caracteres a buscar")
        print("Resultados de la busqueda")
        for nombre, telefono in agenda.items():
            if nombre.startswith(cadena):
                print(f"{nombre}: {telefono}")
                
    elif opcion == 3:
        nombre = input("Ingrese del compañero a eliminar")
        if nombre in agenda:
            confirmacion = input(f"¿Desea eliminar a {nombre}? (S/N): ").lower()
            if confirmacion == "s":
                del agenda[nombre]
                print(f"{nombre} ha sido eliminada de la agenda")
                
        else:
            print(f"{nombre} no se encuentra en la agenda")
            
    elif opcion == 4:
        print("Contactos de la agenda")
        for nombre, telefono in agenda.items():
            print(f"{nombre}: {telefono}")
            
    elif opcion == 5:
        print("Hasta Luego")
        break
    
    else:
        print("opcion no valida. por favor,seleccione una opcion valida 1,2,3,4,5")
        