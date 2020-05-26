
def cost_of_ground(weight):
  cost = 0
  if(weight >=0):
      if (weight <=2):
        cost = 20 + (weight*1.50)
        return cost
      elif(weight > 2 and weight <=6):
        cost = 20 + (weight*3.00)
        return cost
      elif(weight > 6 and weight <=10):
        cost = 20 + (weight*4.00)
        return cost
      else:
        cost = 20 + (weight*4.75)
        return cost 
  else:
    return print("Invalid Weight") 
#print(cost_of_ground(8.4))

cost_of_premium_ground = 125.00

def cost_of_drone(weight):
  cost = 0 
  if(weight >=0):
      if (weight <=2):
        cost = (weight*4.50)
        return cost
      elif(weight > 2 and weight <=6):
        cost = (weight*9.00)
        return cost
      elif(weight > 6 and weight <=10):
        cost = (weight*12.00)
        return cost
      else:
        cost = (weight*14.25)
        return cost 
  else:
    return print("Invalid Weight") 
#print(cost_of_drone(1.5))

def cheapest_option(weight):
  min_price=(min(cost_of_premium_ground,cost_of_drone(weight),cost_of_ground(weight)))
  
  if (min_price == cost_of_premium_ground):
    return print("The cheapest shipping method is Premimum Ground and the cost is "+str(cost_of_premium_ground))
  elif (min_price == cost_of_ground(weight)):
    return print("The cheapest shipping method is Ground Shipping and the cost is "+str(cost_of_ground(weight)))
  elif (min_price == cost_of_drone(weight)):
    return print("The cheapest shipping method is Drone Shipping and the cost is "+str(cost_of_drone(weight)))


cheapest_option(41.5)