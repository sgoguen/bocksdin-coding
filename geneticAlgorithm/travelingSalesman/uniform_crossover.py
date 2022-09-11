# 5 cities
# genome length of 20 (1 for each connection)
# value (travel_time)
# lowest travel_time containing all 5 cities wins

import random
import numpy as np
from time import time
from tqdm import tqdm


cities = [1, 2, 3, 4, 5]
cost_to_optimize = 'travel_time'


class Path:
  def __init__(self, origin, destination, distance, avg_speed):
    self.origin = origin
    self.destination = destination
    self.distance = distance # in miles
    self.avg_speed = avg_speed # in miles per hour
    self.travel_time = distance / avg_speed
  # END init
# END OF ROUTE CLASS


class Traveler:
  def __init__(self, paths, generation=0):
    self.chromosome = []
    self.distance = 0
    self.time = 0
    self.cost = 0
    self.generation = generation

    for _ in range(len(paths)):
      if random.random() > 0.5:
        self.chromosome.append(1)
      else:
        self.chromosome.append(0)
  # END init

  def crossover(self, other_traveler, paths):
    child1, child2 = [], []
    for i in range(0, len(self.chromosome)):
      if i % 2 == 0:
        child1.append(self.chromosome[i])
        child2.append(other_traveler.chromosome[i])
      else:
        child1.append(other_traveler.chromosome[i])
        child2.append(self.chromosome[i])

    children = [Traveler(paths, self.generation + 1),
                Traveler(paths, self.generation + 1)]
    
    children[0].chromosome = child1
    children[1].chromosome = child2
    
    return children
  # END crossover

  def mutation(self, rate=0.01):
    for i in range(len(self.chromosome)):
      if random.random() < rate:
        if self.chromosome[i] == 0:
          self.chromosome[i] = 1
        else:
          self.chromosome[i] = 0
  # END mutation

  def fitness(self, paths):
    if self.chromosome.count(1) != len(cities):
      self.cost = float('inf')
      return

    cost, distance, time = 0, 0, 0
    origins_visited = []
    destinations_visited = []
    combinations = []

    for i in range(len(self.chromosome)):
      if self.chromosome[i] == 1:
        origins_visited.append(paths[i].origin)
        destinations_visited.append(paths[i].destination)
        combinations.append((paths[i].origin, paths[i].destination))
        cost += getattr(paths[i], cost_to_optimize)
        distance += paths[i].distance
        time += paths[i].travel_time

    self.distance = distance
    self.time = time
      
    for city in cities:
      origin_count = origins_visited.count(city)
      destination_count = destinations_visited.count(city)
      if origin_count != 1 or destination_count != 1:
        self.cost = float('inf')
        return

    self.cost = cost
  # END fitness
# END OF TRAVELER CLASS


class GeneticAlgorithm:
  def __init__(self):
    self.population_size = 0
    self.population = []
    self.generation = 0
    self.best_solution = None
  # END init

  def initialize_population(self, population_size, paths):
    self.population_size = population_size

    for _ in range(self.population_size):
      self.population.append(Traveler(paths))

    self.calculate_fitness(paths)
    self.order_population()

    self.best_solution = self.population[0]
  # END initialize_population

  def calculate_fitness(self, paths):
    for traveler in self.population:
      traveler.fitness(paths)
  # END calculate_fitness

  def order_population(self):
    self.population = sorted(self.population, key=lambda traveler: traveler.cost)
  # END order_population

  def best_traveler(self, traveler):
    if traveler.cost < self.best_solution.cost:
      self.best_solution = traveler
  # END best_traveler

  def sum_costs(self):
    sum = 0

    for traveler in self.population:
      sum += traveler.cost

    return sum
  # END sum_costs

  def select_parent_cutoff(self, sum_cost):
    parent = -1
    random_value = random.random() * sum_cost

    sum, i = 0, 0
    while i < len(self.population) and sum < random_value:
      sum += self.population[i].cost
      parent += 1
      i += 1

    return parent
  # END select_parent_cutoff

  def solve(self, mutation_probability, number_of_generations, population_size, paths):
    self.initialize_population(population_size, paths)

    for _ in tqdm(range(number_of_generations)):
      sum = self.sum_costs()

      new_population = []
      for _ in range(0, self.population_size, 2):
        parents = [self.select_parent_cutoff(sum),
                   self.select_parent_cutoff(sum)]
        children = self.population[parents[0]].crossover(self.population[parents[1]], paths)

        children[0].mutation(mutation_probability)
        children[1].mutation(mutation_probability)

        new_population.append(children[0])
        new_population.append(children[1])

      self.population = list(new_population)
      self.calculate_fitness(paths)
      self.order_population()

      if self.population[0].cost < self.best_solution.cost:
        self.best_solution = self.population[0]

      self.generation += 1

    return self.best_solution
  # END solve
# END OF GENETIC ALGORITHM CLASS


paths = []

paths.append(Path(1, 2, 10, 60)) #^
paths.append(Path(2, 3, 10, 60)) #^
paths.append(Path(3, 4, 10, 60)) #^
paths.append(Path(4, 5, 10, 60)) #^
paths.append(Path(5, 1, 10, 60)) #^
paths.append(Path(1, 5, 10, 60)) #$
paths.append(Path(5, 4, 10, 60)) #$
paths.append(Path(4, 3, 10, 60)) #$
paths.append(Path(3, 2, 10, 60)) #$
paths.append(Path(2, 1, 10, 60)) #$
paths.append(Path(1, 3, 20, 60)) 
paths.append(Path(3, 1, 20, 60)) 
paths.append(Path(1, 4, 20, 60)) 
paths.append(Path(4, 1, 20, 60)) 
paths.append(Path(2, 4, 20, 60)) 
paths.append(Path(4, 2, 20, 60)) 
paths.append(Path(2, 5, 20, 60)) 
paths.append(Path(5, 2, 20, 60)) 
paths.append(Path(3, 5, 20, 60)) 
paths.append(Path(5, 3, 20, 60)) 

mutation_probability = 0.01
number_of_generations = 1000
population_size = 200

times = []
best_result = None
results = []

for _ in range(1000):
  ga = GeneticAlgorithm()
  start = time()
  result = ga.solve(mutation_probability,
                    number_of_generations,
                    population_size,
                    paths)
  end = time()
  times.append(end - start)

  if best_result == None or best_result.cost > result.cost:
    best_result = result

  results.append(result.cost)

            
print(f'\n\n\nBest Result: {best_result.cost}, Avg Result: {np.mean(results)}, in average of {np.mean(times)}, total time of {np.sum(times)}\n\n\n')
