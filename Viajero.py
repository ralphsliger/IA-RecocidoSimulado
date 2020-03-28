import random

# Etapa 1 Crecion del mapa

# Tamaño de nuestro vector de ciudades
tam = 5

# Tenemos las ciudades, el codigo de cada ciudad es su codigo en el indice del vector
ciudadesNombres = ["Cartagena","Barranquilla","Santa Marta","Medellin","Maicao","Pereira","Valledupar","Sincelejo","Leticia","Turbaco"]

# Instaciamos todos los valores
ciudades = []
crucesCiudades = []
distanciaCiudades = []

# Creamos todos los cruces posibles y sus respectivas distancias
for i in range( tam ):
	ciudades.append(i)
	for j in range( tam ):
		cruce = {i,j}
		if cruce not in crucesCiudades:
			if cruce != {i}:
				crucesCiudades.append( {i,j} )
				distanciaCiudades.append( random.randrange(1,20) )

print("\nEl listado de Ciudades es\n")
print( ciudades )

print("\nEl listado de cruces es\n")
print( crucesCiudades )

print("\nEl listado de distancias es\n")
print( distanciaCiudades )

input("\nPresione enter para comenzar la busqueda de la mejor ruta")




# Etapa 2 Procesamiento de los datos

# Variables de iteracion
# temperatura = tam * 10
# alfa = 0.9
# nAleatorio = random.random()

ruta = []
rutaOptima = []

rutaDistancia = 0
rutaDistanciaTemp = 0

terminado = False			# Si ya encontro la mejor ruta o no
ronda = 0					# Ronda actual
items = []					#Lista de todas las posciciones de las ciudades que se pueden cambiar, esta lista no se modifica, es una plantilla

#Creamos la  lista de las ciudades que se pueden intercambiar entr ellas
for i in range(1,tam):
	items.append(i)

# Creamos la primera ruta en el orden basico
ruta = ciudades
ruta.append(ciudades[0])


while not terminado:

	rutaDistanciaTemp = 0

	print("\nEl recorrido que se hara es")
	print( ruta )

	for ciudad in range( len(ruta) - 1 ):
		
		c1 = ruta[ciudad]
		c2 = ruta[ciudad+1]
		
		# Determinamos el peso de ese cruce y lo sumamos al siguiente
		posCruce = crucesCiudades.index({c1,c2})
		rutaDistanciaTemp = rutaDistanciaTemp + distanciaCiudades[posCruce]
		print( str(c1) + " "+ str(c2)+" "+str(distanciaCiudades[posCruce]) )

	if( ronda < 1): rutaDistancia = rutaDistanciaTemp; next

	# Hacemos la evaluacion si no es la primera ronda
	itemsTemp = []
	for i in range(1,tam): itemsTemp.append(i)

	cc1 = random.choice(itemsTemp); itemsTemp.remove(cc1)
	cc2 = random.choice(itemsTemp)

	print("\nSe cambiara la poscicion "+ str(cc1) + " por la poscicion "+str(cc2))

	a = ruta[cc1]
	ruta[cc1] = ruta[cc2]
	ruta[cc2] = a


	ronda = ronda + 1

	if( rutaDistancia > rutaDistanciaTemp ): rutaDistancia = rutaDistanciaTemp
	print ("Esta distancia es " +str(rutaDistanciaTemp))
	print ("La distancia actual es " +str(rutaDistancia))
	print ("La ronda es " +str(ronda))
	input("\nSiguiente ronda")

		

# Etapa 3 Brindamos los resultados

print("\nLa distancia final es")
print( rutaDistancia )


