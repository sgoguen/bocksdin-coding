import numpy as np
import random
from deap import base, creator, algorithms, tools
import six
import sys
sys.modules['sklearn.externals.six'] = six
import mlrose

people = [('Lisbon', 'LIS'),
          ('Madrid', 'MAD'),
          ('Paris', 'CDG'),
          ('Dublin', 'DUB'),
          ('Brussels', 'BRU'),
          ('London', 'LHR')]

destination = 'FCO'

flights = {('BRU', 'FCO'): ['15:44', '18:55', 382]}

flights = {}
for row in open('flights.txt'):
  origin, destination, departure, arrival, price = row[:-1].split(',')

  flights.setdefault((origin, destination), [])
  flights[(origin, destination)].append((departure, arrival, int(price)))


def fitness_function(deap=False):
  def func(schedule):
    flight_id = -1
    total_price = 0
    for i in range(0, 6):
      origin = people[i][1]
      flight_id += 1
      going = flights[(origin, destination)][schedule[flight_id]]
      total_price += going[2]
      flight_id += 1
      returning = flights[(destination, origin)][schedule[flight_id]]
      total_price += returning[2]

    return (total_price, ) if deap else total_price

  return func


toolbox = base.Toolbox()
creator.create('FitnessMin', base.Fitness, weights=(-1.0,))
creator.create('Individual', list, fitness=creator.FitnessMin)
toolbox.register('attr_int', random.randint, a=0, b=9)
toolbox.register('individual', tools.initRepeat, creator.Individual, toolbox.attr_int, n=12)
toolbox.register('population', tools.initRepeat, list, toolbox.individual)
toolbox.register('evaluate', fitness_function(deap=True))
toolbox.register('mate', tools.cxOnePoint)
toolbox.register('mutate', tools.mutFlipBit, indpb=0.01)
toolbox.register('select', tools.selTournament, tournsize=3)
population = toolbox.population(n=500)
crossover_probability = 0.7
mutation_probability = 0.3
number_of_generations = 100

statistics = tools.Statistics(key=lambda individual: individual.fitness.values)
statistics.register('max', np.max)
statistics.register('min', np.min)
statistics.register('mean', np.mean)
statistics.register('std', np.std)

population, info = algorithms.eaSimple(population, toolbox, crossover_probability, mutation_probability, number_of_generations, statistics)

best_solution = tools.selBest(population, 1)
for individual in best_solution:
  print(individual)
  print(individual.fitness)


fitness = mlrose.CustomFitness(fitness_function(deap=False))
problem = mlrose.DiscreteOpt(length=12, fitness_fn=fitness, maximize=False, max_val=10)

best_solution, best_fitness = mlrose.genetic_alg(problem, pop_size=500, mutation_prob=0.3)
print(best_solution)
print(best_fitness)