# a simplified schelling segregation model
# from blog.suspended-chord.info

import random

neighborhood = 2 # cells on both sides
happy = 2 

empty = .1
red = .45
blue = .45

numcells = 80
trials = 1000

def create_city(n):
  city = []
  for i in range(n):
    x = random.random()
    if x < empty:
      cell = ' '
    elif x < empty+red:
      cell = '+'
    else:
      cell = '.'
    city.append(cell)
  return city

def print_city(city):
  print ''.join(city)

def iterate(city):
  # choose rqndom cell
  cell = random.randint(0, len(city)-1)
  # determine if happy, if so, do nothing
  if not cell_is_happy(cell, city):
    empties = [x for x in range(len(city)) if city[x] == ' ']
    destination = empties[random.randint(0, len(empties)-1)]
    city[destination] = city[cell]
    city[cell] = ' '

def cell_is_happy(cell, city):
  # cell is on index into city
  type = city[cell]
  count = 0
  for i in xrange(1, neighborhood+1):
    if city[cell-i] == type: count+=1
    if cell+i >= len(city):
      if city[len(city)-cell+i] == type: count+=1
    else:
      if city[cell+i] == type: count+=1
  return count >= happy

def main():
  city = create_city(numcells)
  print_city(city)
  for i in xrange(trials):
    iterate(city)
    print_city(city)
  print 'Done'




