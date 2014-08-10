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
def main():
  Natoms = read_Natoms()
  mass = read_atom_mass(Natoms)
  coord = read_atom_coord(Natoms)
  velocity = [ [0.1, 0.2, 0.3] for i in xrange(Natoms)]
  print get_acceleration(coord, mass)

# the output should be
# f atoms?
# 3
# For each atom: mass
# 10
# 20
# 15
# For each atom: x, y, z
# 0 0 0
# 0 0 .3
# .1 .2 -.3
# [[-0.0012143469700354181, -0.0024287378274090443, -2.8852483886704636],
# [0.0003772257075318475, 0.0007544514316476514, 1.4421824477393457],
# [0.00030659703662931176, 0.000613223309409161, 0.0005889954611815185]]

# VERLET algorithm
def main():
  Natoms = read_Natoms()
  mass = [mass_Argon for i in xrange(Natoms)]
  coord = read_atom_coord(Natoms)
  velocity = [ [0.0, 0.0, 0.0] for i in xrange(Natoms)]
  coord, velocity = verlet(Nsteps=1000, Delta_t=0.1, coord, mass, velocity)

# the expected output
# Number of atoms?
# 3
# For each atom: x, y, z
# 0 0 0
# 0 0 .3
# .1 .2 -.3
# 3Step 0 E = 0.396856906955
# Ar 0.000000 0.000000 0.000000
# Ar 0.000000 0.000000 0.300000
# Ar 0.100000 0.200000 -0.300000
# 3
# Step 1 E = 0.371644652669
# Ar -0.000002 -0.000003 -0.003611
# Ar 0.000001 0.000002 0.303610
# Ar 0.100001 0.200001 -0.299999
# [...]
# 3
# Step 998 E = 0.377839040613
# Ar -1.656240 -3.312489 -5.790241
# Ar 0.000898 0.001795 10.642537
# Ar 1.755342 3.510694 -4.852296
# 3
# Step 999 E = 0.377839040613
# Ar -1.657894 -3.315796 -5.796029
# Ar 0.000898 0.001797 10.652901
# Ar 1.756995 3.513999 -4.856872
