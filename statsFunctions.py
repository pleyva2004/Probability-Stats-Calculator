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


#def range(nums):
#      return (max(nums)-min(nums))


def stem_leaf_plot():
      branches = []
      nums = [6,5,3,4,12,34,23,46,56,77,65,67]
      n = len(nums)
      for number in nums:
            if int(number/10) == 0:
                
                  if not len(branches):
                        branches.append(branch(0,number))
                        
                  else:
                  #search
                        for b in branches:
                              if b.getStem() == 0:
                                   
                                    b.append(number)
                                   # b.sort()
                                   

            if int(number/10) < 10 and int(number/10) != 0:
                  
                  found = False
                  n = len(branches)
                  for i in range(len(branches)):
                        if branches[i].getStem() == int(number/10):
                              branches[i].append(number%10)
                             # branches[i].sort()
                              found = True
                  
                  if not found:
                        newBranch = branch(int(number/10),number%10)
                        branches.append(newBranch)
                        #print(branches[-1].toString())

      for b in branches:
            print(b.toString())             
                        
                  



class branch:
      leafs = ""
   
      
      def __init__(self, stem, leaf):
            self.stem = stem
           # print(self.stem)
           
            self.leafs += str(leaf) + " "
           # print(self.leafs)

      def append(self, leaf):
            self.leafs += str(leaf) + " "
      
      def getStem(self):
            return self.stem
      
      def getLeafs(self):
            return self.leafs

      def toString(self):
            myStr = "" + str(self.stem) + "  :  " + self.leafs
            return myStr
      
      #def sort(self):
            self.leafs.sort()

         
stem_leaf_plot()








      
