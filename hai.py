def convert(A,B):
  # converting A, B into n_a, n_b
  return log_2(A+1), log_2(B+1)

# base case A = 1, B= 1 so that n_a = 1, n_b=1: 3 positions
# base case A= 0, B = 0 so that n_a = 0, n_b= 0: 1 positions
# base case A = 1, B= 0 so thqt 2 positions
# base case A = 0, B= 1 so thqt 2 positions

dict_last_positions = dict() # hash table
def last_positions():
  if n_a, n_b == 0, 0:
    dict_last_positions[(0,0)]= (0,0)
  else:
    next_step = min(n_a,n_b)
    for key_step in dict_last_positions:
      last_positions = dict_last_positions[key_step]
      if last_positions[0]+2**next_step <= A:
        last_positions_0 = last_positions[0] + 2**next_step
        del dict_last_positions[key_step] # remove old last positions
        dict_last_positions[]
      elif last_positions[1] + 2**next_step <= B:
        last_positions_1 = last_positions[0] + 2**next_step
