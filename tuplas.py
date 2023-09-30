import random

opciones = ("piedra","papel","tijera")

cantidad_turnos = int(input("Ingrese la cantidad de turnos que desea jugar"))

puntaje_maquina = 0
puntaje_usuario = 0

for turno in range(cantidad_turnos):
    print(f"Turno {turno + 1}:")
    
    eleccion_maquina = random.choice(opciones)
    
    eleccion_usuario = input("Ingrese su eleccion(piedra,papel,tijera): ").lower()
    
   
    print("Usted eligio: {eleccion_usuario}")
    print("La maquina eigio: {eleccion_maquina}")
    
    if eleccion_usuario == eleccion_maquina:
        print("En este turno la partida queda en empate")
        
    elif (eleccion_usuario == "piedra" and eleccion_maquina == "tijera") or \
          (eleccion_usuario == "papel" and eleccion_maquina == "piedra") or \
          (eleccion_usuario == "tijera" and eleccion_maquina == "papel"):
              print("Usted gana este turno")
              puntaje_usuario += 1
              
    else:
        print("La maquinagana este turno")
        puntaje_maquina += 1
        
print("Puntaje final")
print("Puntaje de usuario: {puntaje_usuario}")
print("Puntaje maquina: {puntaje_maquina}")

if puntaje_usuario > puntaje_maquina:
    print("El usuario gana el juego")
elif puntaje_maquina > puntaje_usuario:
    print("L maquina gana el juego")
else:
    print("El juego termina en empate")