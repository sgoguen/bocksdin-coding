cities = []


# UNNECESSARY COPYING OF ARRAY
def fitness(self):
  # DO SOMETHING
  self.paths
  self.cities



# EFFICIENT REFERENCE OF ARRAY
def fitness(self, paths, cities):
  # DO SOMETHING
  pass




# MORE EXPENSIVE FUNCTION
def fitness(self, paths):
  # EXPENSIVE CALCULATION
  pass


# LESS EXPENSIVE FUNCTION
def fitness(self, paths):
  if self.chromosome.count(1) != len(cities):
    self.cost = float('inf')
    return
  
  # EXPENSIVE CALCULATION




