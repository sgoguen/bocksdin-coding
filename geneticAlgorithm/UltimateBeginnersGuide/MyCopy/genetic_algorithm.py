from random import random
import matplotlib.pyplot as plt
import pymysql
import plotly.express as px


class Product():
  def __init__(self, name, space, price):
    self.name = name
    self.space = space
    self.price = price
# END OF PRODUCT #

class Individual():
  def __init__(self, spaces, prices, space_limit, generation=0):
    self.spaces = spaces
    self.prices = prices
    self.space_limit = space_limit
    self.score_evaluation = 0
    self.used_space = 0
    self.generation = generation
    self.chromosome = []

    for _ in range(len(spaces)):
      if random() < 0.5:
        self.chromosome.append('0')
      else:
        self.chromosome.append('1')

  def fitness(self):
    score = 0
    sum_spaces = 0
    
    for i in range(len(self.chromosome)):
      if self.chromosome[i] == '1':
        score += self.prices[i]
        sum_spaces += self.spaces[i]
    
    if sum_spaces > self.space_limit:
      score = 1

    self.score_evaluation = score
    self.used_space = sum_spaces

  def crossover(self, other_individual):
    cutoff = round(random() * len(self.chromosome))

    child1 = other_individual.chromosome[0:cutoff] + self.chromosome[cutoff:]
    child2 = self.chromosome[0:cutoff] + other_individual.chromosome[cutoff:]

    children = [Individual(self.spaces, self.prices, self.space_limit, self.generation + 1),
                Individual(self.spaces, self.prices, self.space_limit, self.generation + 1)]
    children[0].chromosome = child1
    children[1].chromosome = child2
    
    return children

  def mutation(self, rate=0.01):
    for i in range(len(self.chromosome)):
      if random() < rate:
        if self.chromosome[i] == '0':
          self.chromosome[i] = '1'
        else:
          self.chromosome[i] = '0'
# END OF INDIVIDUAL #

class GeneticAlgorithm():
  def __init__(self, population_size):
    self.population_size = population_size
    self.population = []
    self.generation = 0
    self.best_solution = None
    self.list_of_solutions = []

  def initialize_population(self, spaces, prices, space_limit):
    for _ in range(self.population_size):
      self.population.append(Individual(spaces, prices, space_limit))

    self.best_solution = self.population[0]

  def order_population(self):
    self.population = sorted(self.population, key=lambda individual: individual.score_evaluation, reverse=True)

  def best_individual(self, individual):
    if individual.score_evaluation > self.best_solution.score_evaluation:
      self.best_solution = individual

  def sum_evaluations(self):
    sum = 0

    for individual in self.population:
      sum += individual.score_evaluation

    return sum

  def select_parent(self, sum_evaluation):
    parent = -1
    random_value = random() * sum_evaluation
    
    sum, i = 0, 0
    while i < len(self.population) and sum < random_value:
      sum += self.population[i].score_evaluation
      parent += 1
      i += 1

    return parent

  def visualize_generation(self):
    best = self.population[0]
    print('Generation: ', self.population[0].generation,
          'Total price: ', best.score_evaluation, 'Space: ', best.used_space,
          'Chromosome: ', best.chromosome)

  def solve(self, mutation_probability, number_of_generations, spaces, prices, limit):
    self.initialize_population(spaces, prices, limit)
    
    for individual in self.population:
      individual.fitness()

    self.order_population()
    self.best_solution = self.population[0]
    self.list_of_solutions.append(self.best_solution.score_evaluation)

    for generation in range(number_of_generations):
      sum = self.sum_evaluations()
      
      new_population = []
      for new_individuals in range(0, self.population_size, 2):
        parent1 = self.select_parent(sum)
        parent2 = self.select_parent(sum)
        children = self.population[parent1].crossover(self.population[parent2])
        
        children[0].mutation(mutation_probability)
        children[1].mutation(mutation_probability)

        new_population.append(children[0])
        new_population.append(children[1])

      self.population = list(new_population)
      
      for individual in self.population:
        individual.fitness()

      best = self.population[0]
      self.list_of_solutions.append(best.score_evaluation)
      self.best_individual(best)

    print('**** Best Solution - Generation: ', self.best_solution.generation,
          'Total price: ', self.best_solution.score_evaluation, 'Space: ', self.best_solution.used_space,
          'Chromosome: ', self.best_solution.chromosome)
    return self.best_solution.chromosome
# END OF GENETIC ALGORITHM #


if __name__ == '__main__':
  products_list = []
  connection = pymysql.connect(host='localhost', user='root', passwd='tHl7Ld_4Azl3rEcre1ri', db='products')
  cursor = connection.cursor()
  cursor.execute("""SELECT
                  product_name
                  ,space
                  ,price
                  ,quantity
                FROM products""")

  for product in cursor:
    for i in range(product[3]):
      products_list.append(Product(product[0], product[1], product[2]))

  cursor.close()
  connection.close()

  spaces = []
  prices = []
  names = []
  limit = 10


  for product in products_list:
    spaces.append(product.space)
    prices.append(product.price)
    names.append(product.name)


  mutation_probability = 0.01
  number_of_generations = 1000
  population_size = 200
  ga = GeneticAlgorithm(population_size)

  result = ga.solve(mutation_probability,
                    number_of_generations,
                    spaces,
                    prices,
                    limit)


  # figure = px.line(x = range(0, number_of_generations + 1), y = ga.list_of_solutions, title = 'Genetic Algorithm Results')
  # figure.show()