import numpy as np
import random
from deap import base, creator, algorithms, tools


class Product():
  def __init__(self, name, space, price):
    self.name = name
    self.space = space
    self.price = price
# END OF PRODUCT #


products_list = []
spaces = []
prices = []
names = []
limit = 3


mutation_probability = 0.01
number_of_generations = 100
population_size = 200


products_list.append(Product('Refrigerator A', 0.751, 999.90))
products_list.append(Product('Cell phone', 0.00000899, 2199.12))
products_list.append(Product('TV 55', 0.400, 4346.99))
products_list.append(Product("TV 50' ", 0.290, 3999.90))
products_list.append(Product("TV 42' ", 0.200, 2999.00))
products_list.append(Product("Notebook A", 0.00350, 2499.90))
products_list.append(Product("Ventilator", 0.496, 199.90))
products_list.append(Product("Microwave A", 0.0424, 308.66))
products_list.append(Product("Microwave B", 0.0544, 429.90))
products_list.append(Product("Microwave C", 0.0319, 299.29))
products_list.append(Product("Refrigerator B", 0.635, 849.00))
products_list.append(Product("Refrigerator C", 0.870, 1199.89))
products_list.append(Product("Notebook B", 0.498, 1999.90))
products_list.append(Product("Notebook C", 0.527, 3999.00))


for product in products_list:
  spaces.append(product.space)
  prices.append(product.price)
  names.append(product.name)


def fitness(solution):
  cost = 0
  sum_space = 0

  for i in range(len(solution)):
    if solution[i] == 1:
      cost += prices[i]
      sum_space += spaces[i]

  if sum_space > limit:
    cost = 1

  return cost,


toolbox = base.Toolbox()
creator.create('FitnessMax', base.Fitness, weights=(1.0,))
creator.create('Individual', list, fitness=creator.FitnessMax)

toolbox.register('attr_bool', random.randint, 0, 1)
toolbox.register('individual', tools.initRepeat, creator.Individual, toolbox.attr_bool, n=14)
toolbox.register('population', tools.initRepeat, list, toolbox.individual)
toolbox.register('evaluate', fitness)
toolbox.register('mate', tools.cxOnePoint)
toolbox.register('mutate', tools.mutFlipBit, indpb=0.01)
toolbox.register('select', tools.selRoulette)


population = toolbox.population(n = population_size)
crossover_probability = 1.0

statistics = tools.Statistics(key=lambda individual: individual.fitness.values)
statistics.register('max', np.max)
statistics.register('min', np.min)

populations, info = algorithms.eaSimple(population, toolbox, crossover_probability, mutation_probability, number_of_generations, statistics)

best_solutions = tools.selBest(population, k=3)
for individual in best_solutions:
  print(individual)
  print(individual.fitness)