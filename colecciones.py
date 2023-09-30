num_conductores = int(input("ingrese numero de conductores"))

nombreConductor = []
diaSemana = ["Lunes", "Martes", "Miercoles", "jueves","viernes","sabado"]
recaudo = []
totalRecaudo = []
porcentajeRecaudo = []


for i in range(num_conductores):
    nombre = input(f"ingrese el nombre del condctor {i  + 1}: ")
    nombreConductor.append(nombre)
    
    recaudo_conductor = []
    for dia in diaSemana:
        recaudo_dia = float(input(f"ingrese el recaudo de {dia} para {nombre}:"))
        recaudo_conductor.append(recaudo_dia)
        
    recaudo.append(recaudo_conductor)
    
for recaudo_conductor in recaudo:
    total = sum(recaudo_conductor)
    totalRecaudo.append(total)
    

print("Resumen de recaudos por conductor")
for i in range(num_conductores):
    print(f"Conductor: {nombreConductor[i]}")
    for j in range(len(diaSemana)):
        print(f"{diaSemana[j]}: ${recaudo[i][j]}")
    print(f"Total recaudado: ${totalRecaudo[i]}")
    

    
            
