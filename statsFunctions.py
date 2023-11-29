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
      quantity = lambda x, sampleMean: (x  - sampleMean)**2 # The quantity of (x - Mean(x))^2
      sampleMean = Mean(nums) # The sample mean calculated
      for number in nums:
            sum += quantity(number,sampleMean) # adding up all the quantities
      return sum/(n-1) # returns the sum / num of values - 1
            
# This will take the squre root of Variance
def Standard_Dev(nums):
      return Variance(nums)**0.5