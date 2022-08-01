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
import numpy as np


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

  def two_point_crossover(self, other_individual):
    cutoff_one = round(random() * len(self.chromosome))
    cutoff_two = cutoff_one

    while cutoff_two == cutoff_one:
      cutoff_two = round(random() * len(self.chromosome))

    cutoffs = sorted([cutoff_one, cutoff_two])
    children_chromosomes = [self.chromosome[0:cutoffs[0]] + other_individual.chromosome[cutoffs[0]:cutoffs[1]] + self.chromosome[cutoffs[1]:],
                            other_individual.chromosome[0:cutoffs[0]] + self.chromosome[cutoffs[0]:cutoffs[1]] + other_individual.chromosome[cutoffs[1]:]]

    children = [Individual(self.items, children_chromosomes[0], self.generation+1),
                Individual(self.items, children_chromosomes[1], self.generation+1)]

    return children
  # END two_point_crossover method

  def uniform_crossover(self, other_individual):
    child_chromosomes = [[], []]
    for i in range(len(self.chromosome)):
      if i % 2 == 0:
        child_chromosomes[0].append(self.chromosome[i])
        child_chromosomes[1].append(other_individual.chromosome[i])
      else:
        child_chromosomes[1].append(self.chromosome[i])
        child_chromosomes[0].append(other_individual.chromosome[i])

    children = [Individual(self.items, child_chromosomes[0], self.generation+1),
                Individual(self.items, child_chromosomes[1], self.generation+1)]

    return children
  # END uniform_crossover_method

  def sinusoidal_motion_crossover(self, other_individual):
    child_chromosomes = [[], []]
    for i in range(len(self.chromosome)):
      if len(child_chromosomes[0]) < len(self.chromosome):
        child_chromosomes[0].append(self.chromosome[i])
      else:
        child_chromosomes[1].append(self.chromosome[i])

      if len(child_chromosomes[0]) < len(self.chromosome):
        child_chromosomes[0].append(other_individual.chromosome[i])
      else:
        child_chromosomes[1].append(other_individual.chromosome[i])

    children = [Individual(self.items, child_chromosomes[0], self.generation+1),
                Individual(self.items, child_chromosomes[1], self.generation+1)]

    return children
  # END sinusoidal_motion_crossover

  def mutation(self, rate=0.01):
    for i in range(len(self.chromosome)):
      if random() < rate:
        if self.chromosome[i] == 0:
          self.chromosome[i] = 1
        else:
          self.chromosome[i] = 0
  # END mutation method
# END Individual class

class GeneticAlgorithm:
  def __init__(self):
    self.population_size = 0
    self.population = []
    self.generation = 0
    self.best_solution = None
  # END init method

  def initialize_population(self, population_size, items):
    self.population_size = population_size
    self.items = items

    for _ in range(self.population_size):
      self.population.append(Individual(self.items))

    self.calculate_fitness()
    self.order_population()

    self.best_solution = self.population[0]
  # END initialize_population method

  def calculate_fitness(self):
    for individual in self.population:
      individual.fitness(self.weight_limit)
  # END calculate_fitness method

  def order_population(self):
    self.population = sorted(self.population, key=lambda individual: individual.value)
  # END order_population method

  def select_best_individual(self):
    if self.population[0].value > self.best_solution.value:
      self.best_solution = self.population[0]
  # END select_best_individual method

  def sum_values(self):
    sum = 0

    for individual in self.population:
      sum += individual.value

    return sum
  # END sum_values method

  def select_parent(self, sum_value):
    index = -1
    random_value = random() * sum_value

    sum, i = 0, 0
    while i < len(self.population) and sum < random_value:
      sum += self.population[i].value
      index += 1
      i += 1

    return index
  # END select_parent method

  def visualize_generation(self):
    best = self.best_solution
    print('Generation: ', self.generation,
          '- Total Value: ', best.value,
          '- Total Weight: ', best.weight,
          '- Chromosome: ', best.chromosome)
  # END visualize_generation method

  def solve(self, mutation_probability, number_of_generations, population_size, weight_limit, items, recombination='single_point_crossover'):
    self.weight_limit = weight_limit
    self.initialize_population(population_size, items)

    for _ in range(number_of_generations):
      sum = self.sum_values()

      new_population = []
      for _ in range(0, self.population_size, 2):
        parents = [self.select_parent(sum),
                   self.select_parent(sum)]

        children = getattr(self.population[parents[0]], recombination, lambda f: print('Recombination function not found!'))(self.population[parents[1]])

        children[0].mutation(mutation_probability)
        children[1].mutation(mutation_probability)

        new_population.append(children[0])
        new_population.append(children[1])

      self.population = new_population
      self.calculate_fitness()
      self.order_population()
      self.select_best_individual()

      self.generation += 1
    #   self.visualize_generation()

    # print('\n**** Best Solution ****',
    #       '\nGeneration: ', self.best_solution.generation,
    #       '\nTotal Value: ', self.best_solution.value,
    #       '\nTotal Weight: ', self.best_solution.weight,
    #       '\nChromosome: ', self.best_solution.chromosome)

    # print('**** Items Packed ****')
    # for i in range(len(self.best_solution.chromosome)):
    #   if self.best_solution.chromosome[i] == 1:
    #     print(items[i].name)

    return self.best_solution
  # END solve method
# END GeneticAlgorithm class

items = []

items.append( Item('Bottle of Water', 0.680389, 15) )
items.append( Item('Snacks', 0.136078, 8) )
items.append( Item('Hat', 0.453592, 10) )
items.append( Item('Sunglasses', 0.3175147, 10) )
items.append( Item('Camera', 0.907185, 9) )
items.append( Item('Umbrella', 1.36078, 2) )
items.append( Item('Laptop', 1.13398, 5) )

mutation_probability = 0.01
number_of_generations = 1000
population_size = 20
weight_limit = 2.5

# ga = GeneticAlgorithm()

# result = ga.solve(mutation_probability,
#                   number_of_generations,
#                   population_size,
#                   weight_limit,
#                   items)

def solve_many(mutation_probability, number_of_generations, population_size, weight_limit, items, number_of_iterations):
  recombinations = ['single_point_crossover',
                    'two_point_crossover',
                    'uniform_crossover',
                    'sinusoidal_motion_crossover']

  for recombination in recombinations:
    results = []
    for _ in range(number_of_iterations):
      ga = GeneticAlgorithm()
      results.append(ga.solve(mutation_probability, number_of_generations, population_size, weight_limit, items, recombination))

    results_values = [i.value for i in results]
    results_weights = [i.weight for i in results]
    print('\nRecombination Method: ', recombination,
          '\nBest Value: ', np.max(results_values),
          '\nWorst Value: ', np.min(results_values),
          '\nAverage Value: ', np.mean(results_values),
          '\nBest Weight: ', np.max(results_weights),
          '\nWorst Weight: ', np.min(results_weights),
          '\nAverage Weight: ', np.mean(results_weights),
          '\nAverage Generations: ', np.mean([i.generation for i in results]))


solve_many(mutation_probability,
           number_of_generations,
           population_size,
           weight_limit,
           items,
           20)