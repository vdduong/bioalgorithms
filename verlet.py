# implementation of Verlet algorithm

# lennard-jones potential
def V_lj(r):
  global eps, sigma
  return 4.*eps*((sigma/r)**12 - (sigma/r)**6)

# molecular geometry
# reads from the standard input: the nb of atoms, the atomic masses, the atomic coordinates (x,y,z)
def main():
  Natoms = read_Natoms()
  mass = read_atom_mass(Natoms)
  coord = read_atom_coord(Natoms)
  print mass
  print coord

# the output should be
# Number of atoms?
# 3
# For each atom: mass
# 40
# 10
# 20
# For each atom: x, y, z
# 0 0 0
# 1 2 3
# -1 0 2
# mass = [40.0, 10.0, 20.0]
# coord = [[0.0, 0.0, 0.0], [1.0, 2.0, 3.0], [-1.0, 0.0, 2.0]]

# compute the distance matrix:
def main():
  Natoms = read_Natoms()
  coord = read_atom_coord(Natoms)
  distances = get_distances(coord)
  for d in distances:
    print d

# the output should be
# Number of atoms?
# 3
# For each atom: x, y, z
# 0 0 0
# 1 2 3
# -1 0 2
# [0.0, 3.7416573867739413, 2.23606797749979]
# [3.7416573867739413, 0.0, 3.0]
# [2.23606797749979, 3.0, 0.0]

# potential for multiple atoms
def main():
  Natoms = read_Natoms()
  coord = read_atom_coord(Natoms)
  print V_lj(coord)

# the output should be
# Number of atoms?
# 3
# For each atom: x, y, z
# 0 0 0
# 0 0 .3
# .1 .2 -.3
# 0.396856906955

# total energy
def main():
  Natoms = read_Natoms()
  mass = read_atom_mass(Natoms)
  coord = read_atom_coord(Natoms)
  velocity = [ [0.1, 0.2, 0.3] for i in range(Natoms)]
  print E_tot(coord, mass, velocity)

# the output should be
# Number of atoms?
# 3
# For each atom: mass
# 10
# 20
# 15
# For each atom: x, y, z
# 0 0 0
# 0 0 .3
# .1 .2 -.3
# 3.54685690696

# accleration

