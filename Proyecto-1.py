import random


class Graph:
    def __init__(self):
        # dictionary containing keys that map to the corresponding vertex object
        self.vertices = {}

    def add_vertex(self, key):
        """Add a vertex with the given key to the graph."""
        vertex = Vertex(key)
        self.vertices[key] = vertex

    def get_vertex(self, key):
        """Return vertex object with the corresponding key."""
        return self.vertices[key]

    def __contains__(self, key):
        return key in self.vertices

    def add_edge(self, src_key, dest_key, weight=1):
        """Add edge from src_key to dest_key with given weight."""
        self.vertices[src_key].add_neighbour(self.vertices[dest_key], weight)

    def does_edge_exist(self, src_key, dest_key):
        """Return True if there is an edge from src_key to dest_key."""
        return self.vertices[src_key].does_it_point_to(self.vertices[dest_key])

    def __len__(self):
        return len(self.vertices)

    def __iter__(self):
        return iter(self.vertices.values())


class Vertex:
    def __init__(self, key):
        self.key = key
        self.points_to = {}

    def get_key(self):
        """Return key corresponding to this vertex object."""
        return self.key

    def add_neighbour(self, dest, weight):
        """Make this vertex point to dest with given edge weight."""
        self.points_to[dest] = weight

    def get_neighbours(self):
        """Return all vertices pointed to by this vertex."""
        return self.points_to.keys()

    def get_weight(self, dest):
        """Get weight of edge from this vertex to dest."""
        return self.points_to[dest]

    def set_weight(self, dest, weight):
        """Set weight of edge from this vertex to dest."""
        self.points_to[dest] = weight

    def does_it_point_to(self, dest):
        """Return True if this vertex points to dest."""
        return dest in self.points_to


def create3D(dimension, ratio, numeroCubos):
    environment = [[[0 for k in range(dimension)] for j in range(dimension)] for i in range(dimension)]
    for p in range(numeroCubos):
        x1 = random.randrange(dimension)
        y1 = random.randrange(dimension)
        z1 = random.randrange(dimension)
        b = checkPoint(x1, y1, z1, ratio, dimension)
        while b == 0:
            x1 = random.randrange(dimension)
            y1 = random.randrange(dimension)
            z1 = random.randrange(dimension)
            b = checkPoint(x1, y1, z1, ratio, dimension)
        print("En Append " + str(p))
        print(str(x1) + "," + str(y1) + "," + str(z1))
        fillCube(environment, x1, y1, z1, ratio)
        listaX.append(x1)
        listaY.append(y1)
        listaZ.append(z1)
    return environment


listaX = []
listaY = []
listaZ = []


def checkPoint(x4, y4, z4, ratio, dimension):
    o = 3
    factor = -2
    while o > 0:
        o -= 1
        factor += 1
        r1 = x4 + (factor * ratio)
        r2 = y4 + (factor * ratio)
        r3 = z4 + (factor * ratio)
        if r1 < 0:
            return 0
        if r1 >= dimension:
            return 0
        if r2 < 0:
            return 0
        if r2 >= dimension:
            return 0
        if r3 < 0:
            return 0
        if r3 >= dimension:
            return 0
        if len(listaX) > 0 & len(listaY) > 0 & len(listaZ) > 0:
            for k in zip(listaX, listaY, listaZ):
                print("did you enter??")
                if x4 == k[0] & y4 == k[1] & z4 == k[2]:
                    return 0
                maxX = k[0] + ratio
                maxY = k[1] + ratio
                maxZ = k[2] + ratio
                minX = k[0] - ratio
                minY = k[1] - ratio
                minZ = k[2] - ratio
                a = (r1 >= minX) & (r1 <= maxX)
                b = (r2 >= minY) & (r2 <= maxY)
                c = (r3 >= minZ) & (r3 <= maxZ)
                if a:
                    if b:
                        if c:
                            return 0

    return 1


def fillCube(environment, x, y, z, ratio):
    for i in range(x-ratio, x+ratio+1):
        for j in range(y-ratio, y+ratio+1):
            for k in range(z-ratio, z+ratio+1):
                environment[i][j][k] = 1


def checkSpace(dimension, ratio, numeroCubos):
    volumenP = (1+(2*ratio))**3
    volumenG = dimension**3
    temp = int(volumenG/volumenP)
    if numeroCubos > temp:
        return 0
    return 1


def fillGraph(entorno1,dimension,graph,lis=[]):
    for i in range(dimension):
        for j in range(dimension):
            for k in range(dimension):
                if entorno1[i][j][k] == 0:
                    if isinstance(graph, Graph):
                        vertice = (i, j, k)
                        graph.add_vertex(vertice)
                        lis.append(vertice)


def checkPoint2(vertice, dimension, entorno1):
    if vertice[0] < 0 | vertice[0] > dimension:
        return 0
    if vertice[1] < 0 | vertice[1] > dimension:
        return 0
    if vertice[2] < 0 | vertice[2] > dimension:
        return 0
    if entorno1[vertice[0]][vertice[1]][vertice[2]] == 1:
        return 0
    return 1


def connectGraph(entorno1,dimension,graph,lis=[]):
    if isinstance(graph,Graph):
        for vertice in lis:
            for i in range(vertice[0] - 1, vertice[0] + 2):
                for j in range(vertice[1] - 1, vertice[1] + 2):
                    for k in range(vertice[2] - 1, vertice[2] + 2):
                        if vertice != (i, j, k):
                            if checkPoint2(vertice, dimension, entorno1) == 1:
                                origin = vertice
                                destiny = (i, j, k)
                                weight = 1
                                graph.add_vertex(origin,destiny,weight)
                                graph.add_vertex(destiny, origin, weight)



'''
dimen = int(input("Ingrese la dimension del entorno: "))
radio = int(input("Ingrese el radio del cubo: "))
numCubes = int(input("Ingrese el numero de cubos: "))

while (checkSpace(dimen, radio, numCubes) == 0) | (dimen <= 0):
    print("Valores ingresados no validos")
    dimen = int(input("Ingrese la dimension del entorno: "))
    radio = int(input("Ingrese el radio del cubo: "))
    numCubes = int(input("Ingrese el numero de cubos: "))
'''
entorno = create3D(100, 3, 100)
g = Graph()
listaq = []
fillGraph(entorno, 100, g,listaq)
connectGraph(entorno,100,g,listaq)


