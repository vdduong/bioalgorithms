def convert(A,B):
  # converting A, B into n_a, n_b
  return log_2(A+1), log_2(B+1)

# base case A = 1, B= 1 so that n_a = 1, n_b=1: 3 positions
# base case A= 0, B = 0 so that n_a = 0, n_b= 0: 1 positions
# base case A = 1, B= 0 so thqt 2 positions
# base case A = 0, B= 1 so thqt 2 positions

dict_nb_positions = dict()
dict_nb_positions[(0,0)] = 1
dict_nb_positions[(0,1)] = 2
dict_nb_positions[(1,0)] = 2

dict_positions = dict()

# given A, B
n_a, n_b = convert(A,B)

def positions(n_a, n_b):
  if n_a = 0 and n_b = 0:
    nb_positions = 1
    positions[nb_positions] = (0,0)
    return nb_positions, positions
  else:
    min_ab = min(n_a, n_b)
    nb_positions, positions = positions(n_a-1, n_b)
    
