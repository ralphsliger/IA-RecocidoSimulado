import string, math

# Traemos la matriz del set de datos
def distancesFromCoords():

	f = open('dan6.tsp')
	data = [line.replace("\n","").split(" ")[1:] for line in f.readlines()[6:(6+6)]]
	coords =  list(map(lambda x: [float(x[0]),float(x[1])], data))
	distances = []

	print(coords)
	for i in range(len(coords)):
		row = []
		for j in range(len(coords)):
			distancia = math.sqrt( ((coords[i][0]-coords[j][0])**2) + ((coords[i][1]-coords[j][1])**2) )
			row.append(distancia)
		distances.append(row)
	return distances

dis = distancesFromCoords()

# Obtenemos la matriz de distancias
distancias = []
for i in range( 6 ):
	for j in range( len(dis[i]) ):
		if ( i<j):	
			distancias.append(dis[i][j])

print(len(distancias))
print( distancias)