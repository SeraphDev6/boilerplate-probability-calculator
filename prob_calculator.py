import copy
import random


class Hat:
  def __init__(self,**kwargs):
    #create the contains variable
    self.contents=[]
    #loop through the arguments and add them to selcontenains
    for key, value in kwargs.items():
      for i in range(value):
        self.contents.append(key)
  #Pick a ball any ball
  def draw(self,number_of_balls):
    #Handle too many balls
    if number_of_balls>=len(self.contents):
      return self.contents
    output=[]
    for i in range(number_of_balls):
      #remove a ball from contents and add it to output
      output.append(self.contents.pop(random.randint(0,len(self.contents)-1)))
    return output
    


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  #run the experiment num_experiment times
  num_of_successes=0
  for i in range(num_experiments):
    #make a copy of hat
    new_hat=copy.deepcopy(hat)
    #get the results of the draw
    results=new_hat.draw(num_balls_drawn)
    #test to see if results is missing any of the expected balls
    contains=True
    for item in expected_balls.keys():
      for j in range(expected_balls.get(item)):
        if results.count(item)>0:
          results.remove(item)
        else:
          contains=False
          break 
    #increment successes if result contains all of the expected balls
    if contains:
      num_of_successes+=1
  #probability is successful / total
  probability=num_of_successes/num_experiments
  return probability 


