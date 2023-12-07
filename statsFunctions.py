#sum = lambda a,b: a + b


# This is adding up all the values and diving by number of values
def Mean(nums):
      sum = 0
      n = len(nums)
      for number in nums:
            sum += number # adding of the values
      return sum/n # returns the total / num of values


# This will add up the quantity (x - Mean(x))^2 for all values of x and dividve by the number of values minus 1
def Variance(nums):
      sum = 0
      n = len(nums)
      quantity = lambda x, mean: (x  - mean)**2 # The quantity of (x - Mean(x))^2
      sampleMean = Mean(nums) # The sample mean calculated
      for number in nums:
            sum += quantity(number,sampleMean) # adding up all the quantities
      return sum/(n-1) # returns the sum / num of values - 1

def Range(nums):
      return (max(nums)-min(nums))


def pupolation_Variance(nums):
      sum = 0
      n = len(nums)
      quantity = lambda x, mean: (x  - mean)**2 # The quantity of (x - Mean(x))^2
      populationMean = Mean(nums) # The sample mean calculated
      for number in nums:
            sum += quantity(number,populationMean) # adding up all the quantities
      return sum/(n) # returns the sum / num of values - 1


# This will take the squre root of Variance
def Standard_Dev(nums):
      return Variance(nums)**0.5


def population_Standard_Dev(nums):
      return pupolation_Variance(nums)**0.5

def stem_leaf_plot(nums):
      branches = []
      n = len(nums)
      for number in nums:
            if int(number/10) == 0:
                  found = False
            
                  for b in branches:
                        if b[0] == 0:
                        #if there is a stem that = 0 
                             
                             #then add 1s place digit
                              b[1].append(number)
                              b[1].sort()
                              found = True
                
                  if not found:
                  #if there is no stem that = 0 

                        #then make a new branch with stem = 0 and 1s digit and add to list
                        newBranch = (0,[number])
                        branches.append(newBranch) 
                        
                                   
            if int(number/10) < 10 and int(number/10) != 0:
                  found = False

     
                  
                  for b in branches:
                        if b[0] == int(number/10):
                        #if there is a stem = the 10s place digit 

                              #then add the 1s place digit     
                              b[1].append(number%10)
                              b[1].sort()
                              found = True
                  
                  if not found:
                  #if there is no stem that = the 10s place digit 

                        #then make a new branch with that stem and 1s place digit & + to list
                        newBranch = (int(number/10),[number%10])
                        branches.append(newBranch)
     

            if int(number/10) >= 10 and int(number/100) != 0 :
                  found = False

                  for b in branches:
                        if b[0] == int(number/10):
                        #if there is a stem = the 10s place digit 

                              #then add the 1s place digit     
                              b[1].append(number%10)
                              b[1].sort()
                              found = True
                  
                  if not found:
                  #if there is no stem that = the 10s place digit 

                        #then make a new branch with that stem and 1s place digit & + to list
                        newBranch = (int(number/10),[number%10])
                        branches.append(newBranch)
      
      branches.sort()
      start = "Stem                  Leafs"
      stringBranches = [start,]
      for b in branches:
            if b[0] < 10:     
                  string = "" + str(b[0]) + "       :      " + str(b[1]) + "     " # add frequency --- str(len(b[1]))
                  stringBranches.append(string)
            elif b[0] >= 10 and b[0] < 100:
                  string = "" + str(b[0]) + "      :      " + str(b[1]) + "     " # add frequency --- str(len(b[1]))
                  stringBranches.append(string)
      
      #for strB in stringBranches:
      #      print(strB)

      return stringBranches





      
