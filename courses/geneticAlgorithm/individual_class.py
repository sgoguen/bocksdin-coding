# Backpack
# We can carry 2.5kg
# Maximize the weight limit utilized
# Maximizing the value of the items

# - Items
#   - Bottle of water
#     - Weight: 0.680389 kg
#     - Value:  15
#   - Snacks
#     - Weight: 0.136078 kg
#     - Value:  8
#   - Hat
#     - Weight: 0.453592 kg
#     - Value:  10
#   - Sunglasses
#     - Weight: 0.3175147 kg
#     - Value:  10
#   - Camera
#     - Weight: 0.907185 kg
#     - Value:  9
#   - Umbrella
#     - Weight: 1.36078 kg
#     - Value:  2
#   - Laptop
#     - Weight: 1.13398 kg
#     - Value: 5
# total weight of items - 4.9895187 kg


# - [0, 1, 1, 0, 0, 1, 0]
# - Snacks, hat, umbrella
# - 1.95045 kg
# - 20
# - [1, 1, 0, 1, 0, 0, 1]
# - bottle of water, snacks, sunglasses, and laptop
# - 2.2679617 kg
# - 38

from random import random


class Item:
  def __init__(self, name, weight, value):
    self.name = name
    self.weight = weight
    self.value = value
  # END init method
# END Item class

class Individual:
  def __init__(self, items, chromosome=[], generation=0):
    self.items = items
    self.chromosome = chromosome
    self.generation = generation
    self.value = float('-inf')
    self.weight = 0

    if len(chromosome) == 0:
      for _ in range(len(items)):
        if random() > 0.5:
          self.chromosome.append(1)
        else:
          self.chromosome.append(0)
  # END init method

  def fitness(self, weight_limit):
    weight, value = 0, 0

    for i in range(len(self.chromosome)):
      if self.chromosome[i] == 1:
        weight += self.items[i].weight
        value += self.items[i].value

        if weight > weight_limit:
          self.value = float('-inf')
          return

    self.value = value
    self.weight = weight
  # END fitness method

  def single_point_crossover(self, other_individual):
    cutoff = round(random() * len(self.chromosome))

    child_chromosomes = [other_individual.chromosome[0:cutoff] + self.chromosome[cutoff:],
                         self.chromosome[0:cutoff] + other_individual.chromosome[cutoff:]]

    children = [Individual(self.items, child_chromosomes[0], self.generation+1),
                Individual(self.items, child_chromosomes[1], self.generation+1)]

    return children
  # END single_point_crossover method

  def mutation(self, rate=0.01):
    for i in range(len(self.chromosome)):
      if random() < rate:
        if self.chromosome[i] == 0:
          self.chromosome[i] = 1
        else:
          self.chromosome[i] = 0
  # END mutation method
# END Individual class

items = []

items.append( Item('Bottle of Water', 0.680389, 15) )
items.append( Item('Snacks', 0.136078, 8) )
items.append( Item('Hat', 0.453592, 10) )
items.append( Item('Sunglasses', 0.3175147, 10) )
items.append( Item('Camera', 0.907185, 9) )
items.append( Item('Umbrella', 1.36078, 2) )
items.append( Item('Laptop', 1.13398, 5) )