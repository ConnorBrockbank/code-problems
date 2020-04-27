#Author: Connor Brockbank
#Initial Date: 2020-04-27

import sys

#polygon definitions
tetrahedron = 4
cube = 6
octahedron = 8
dodecahedron = 12
icosahedron = 20

totalSides = 0

for line in sys.stdin:
    #remove newline character
    line = line.rstrip()
    #print(line)

    if line == "Tetrahedron":
        totalSides += tetrahedron
    if line == "Cube":
        totalSides += cube
    if line == "Octahedron":
        totalSides += octahedron
    if line == "Dodecahedron":
        totalSides += dodecahedron
    if line == "Icosahedron":
        totalSides += icosahedron

print (totalSides)
