# author: Christopher Schayer, Wilson Zhu
# the logger functionality

from neat.population import Population
from neat.reporting import BaseReporter
from neat.math_util import mean
from neat.six_util import itervalues, iterkeys
import csv 
class logger(BaseReporter):
  def __init__(self):
    self.generation = None

     
    
  def start_generation(self, generation):
    self.generation = generation
  
  def end_generation(self, config, population, species_set):
    pass
    
  def post_evaluate(self, config, population, species, best_genome):
    
    fitnesses = [c.fitness for c in itervalues(population)]
    fit_mean = mean(fitnesses)  
    species_ids = list(iterkeys(species.species))
    for i in species_ids:
      s = species.species[i]
     

      with open("data.csv", "a") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        line=(str(self.generation), str(i), str(s.fitness), str(fit_mean))
        writer.writerow(line)
      
  def complete_extinction(self):
    print('All species extinct.')
    
  def found_solution(self, config, generation, best):
    print('\nBest individual in generation {0} meets fitness threshold - complexity: {1!r}'.format(self.generation, best.size()))
    
  def species_stagnant(self, sid, species):
    print("\nSpecies {0} with {1} members is stagnated: removing it".format(sid, len(species.members)))

  def info(self, msg):
    pass
