# algorithm of Needleman Wunsch for global sequence alignment
# from 	oosd-bioinfo

d = -5 # gap penalty
# two sequences to be compared A, B
# similarity matrix S

# intialization
for i in xrange(len(A)):
  F[i][0] = d*i
  
for j in xrange(len(B)):
  F[0][j] = d*j

# scoring for F
for i in xrange(1, len(A)):
  for j in xrange(1, len(B)):
    Match = F[i-1][j-1] + S[A[i]][B[j]]
    Delete = F[i-1][j] + d
    Insert = F[i][j-1] + d
    F[i][j] = max(Match, Delete, Insert)

# traceback
alignmentA, alignmentB = "", ""
i = len(A) - 1
j = len(B) - 1

while (i>0 and j>0):
  score = F[i][j]
  scorediag = F[i-1][j-1]
  scoreup = F[i][j-1]
  scoreleft = F[i-1][j]
  if (score == scorediag + S[A[i]][B[j]]):
    alignmentA = A[i] + alignmentA
    alignmentB = B[j] + alignmentB
    i-=1
    j-=1
  elif (score==scoreleft + d):
    alignmentA = A[i] + alignmentA
    alignmentB = "-" + alignmentB
    i-=1
  elif (score==scoreup + d):
    alignmentA = "-" + alignmentA
    alignmentB = B[j] + alignmentB
    j-=1
  else:
    pass

while (i>0):
  alignmentA = A[i] + alignmentA
  alignmentB = "-" + alignmentB
  i-=1
while (j>0):
  alignmentA = "-" + alignmentA
  alignmentB = B[j] + alignmentB
  j-=1

