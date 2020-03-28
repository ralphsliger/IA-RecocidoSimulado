import random
import string, math
from math import e

# Ralph Sliger - Andres Castañeda 
# Etapa 0 Extraccion de datos

# Traemos la matriz del set de datos
def distancesFromCoords():

	f = open('dan42.tsp')
	ciudades = 42
	data = [line.replace("\n","").split(" ")[1:] for line in f.readlines()[6:(ciudades+6)]]
	coords =  list(map(lambda x: [float(x[0]),float(x[1])], data))
	distances = []

	for i in range(len(coords)):
		row = []
		for j in range(len(coords)):
			distancia = math.sqrt( ((coords[i][0]-coords[j][0])**2) + ((coords[i][1]-coords[j][1])**2) )
			distancia = round(distancia, 2)
			row.append(distancia)
		distances.append(row)
	return distances

dis = distancesFromCoords()

# Obtenemos la matriz de distancias
distancias = []
for i in range( len(dis) ):
	for j in range( len(dis[i]) ):
		if ( i<j):	
			distancias.append(dis[i][j])


# Etapa 1 Crecion del mapa

# Tamaño de nuestro vector de ciudades
tam = len(dis)

# Instaciamos todos los valores
ciudades = []
crucesCiudades = []
distanciaCiudades = distancias

# Creamos todos los cruces posibles y sus respectivas distancias
for i in range( tam ):
	ciudades.append(i)
	for j in range( tam ):
		cruce = {i,j}
		if cruce not in crucesCiudades:
			if cruce != {i}:
				crucesCiudades.append( {i,j} )
				#distanciaCiudades.append( int(input("\nCual es la distancia entre : "+ str({i,j}) )) )
				#distanciaCiudades.append( random.randrange(10, 100))


# print("\nEl listado de Ciudades es\n")
# print( ciudades )


print("\nSe hacen un total de "+ str(len(distancias)) + " cruces")

print("\nEl listado de cruces es\n")
print( crucesCiudades )

print("\nEl listado de distancias es\n")
print( distanciaCiudades )

input("\nPresione enter para comenzar la busqueda de la mejor ruta")

print("\nEspere mientras se calcula la mejor distancia ... \n")




# Etapa 2 Procesamiento de los datos

# Variables de iteracion
temperatura = 2						# Temperatura 
alfa = 0.85							# Valor que se enfria la temperatura en cada iteracion
nAleatorio = 0						# N que se genera de probabilidad
pro = 0								# La probabilidad de bolztman

ruta = []
rutaOptima = []

rutaDistancia = 0
rutaDistanciaTemp = 0

terminado = False					# Si ya encontro la mejor ruta o no
ronda = 0							# Ronda actual
items = []							#Lista de todas las posciciones de las ciudades que se pueden cambiar, esta lista no se modifica, es una plantilla

#Creamos la  lista de las ciudades que se pueden intercambiar entr ellas
for i in range(1,tam):
	items.append(i)

# Creamos la primera ruta en el orden basico
for i in range(len(ciudades)):
	ruta.append(ciudades[i])

ruta.append(ciudades[0])


while not terminado:

	rutaDistanciaTemp = 0

	# Aqui se calculan las distancia de este recorrido
	for ciudad in range( len(ruta) - 1 ):
		
		c1 = ruta[ciudad]; c2 = ruta[ciudad+1]
	
		# Determinamos el peso de ese cruce y lo sumamos al siguiente
		posCruce = crucesCiudades.index({c1,c2})
		rutaDistanciaTemp = rutaDistanciaTemp + distanciaCiudades[posCruce]

	# Hacemos la evaluacion si no es la primera ronda
	if( ronda < 1): rutaDistancia = rutaDistanciaTemp; next

	# Evaluamos el valor de la nueva poscicion perturbada
	# Si el valor de la distancia es menor aceptamos y bajamos la temperatura
	if( rutaDistancia > rutaDistanciaTemp ):
		
		# Aceptamos la nueva solucion
		rutaDistancia = rutaDistanciaTemp
		rutaOptima = []
		for i in range(len(ruta)):
			rutaOptima.append(ruta[i])

		# Bajamos la temperatura
		temperatura = temperatura - alfa

	else:

		# Se calcula la probabilidad de Boltzman
		pro = e**(-(abs(rutaDistancia-rutaDistanciaTemp))/temperatura)
		# Se genera un numero aleatorio entre 0 y 1
		nAleatorio = random.random()

		#print("Bolz es " + str(pro) +" y nran es "+str(nAleatorio))
		if( pro > nAleatorio):

			# Aceptamos la nueva solucion
			rutaDistancia = rutaDistanciaTemp
			rutaOptima = []
			for i in range(len(ruta)):
				rutaOptima.append(ruta[i])

			# Bajamos la temperatura
			temperatura = temperatura - alfa
		

	#print ("\nLa ronda es " +str(ronda))
	#print ("La temperatura actual es " +str(temperatura))

	#print ("\nLa distancia actual es " +str(rutaDistanciaTemp))
	#print (ruta)

	# Si aun no ha terminado repetimos el proceso
	if( temperatura < 0.005 ):
		terminado = True
		break

	# Cambiamos posciciones de dos puntos
	itemsTemp = []
	for i in range(1,tam): itemsTemp.append(i)
	cc1 = random.choice(itemsTemp); itemsTemp.remove(cc1)
	cc2 = random.choice(itemsTemp)

	# Intercambaimos las posciciones
	a = ruta[cc1]; ruta[cc1] = ruta[cc2]; ruta[cc2] = a

	ronda = ronda + 1
	#input("\nSiguiente ronda")

		
# Etapa 3 Brindamos los resultados
print("\nPasaron "+ str(ronda) +" rondas")
print("\nLa distancia final es "+ str(rutaDistancia))
print("\nLa ruta mas optima es\n")
print (rutaOptima)

# print("\nEl listado de Ciudades es\n")
# print( ciudades )

# print("\nEl listado de cruces es\n")
# print( crucesCiudades )

# print("\nEl listado de distancias es\n")
# print( distanciaCiudades )



