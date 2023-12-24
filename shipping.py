weight = 4.8
cost_ground = 0

#Ground Shipping
if weight < 2:
  cost_ground = weight * 1.50 + 20 
elif weight > 2 and weight < 6:
  cost_ground = weight * 3.00 + 20
elif weight > 6 and weight < 10:
  cost_ground = weight * 4.00 + 20
else: 
  cost_ground = weight * 4.75 + 20

print(cost_ground)

cost_premiumground = 125

print( "This is the cost of premium ground shipping", cost_premiumground)
cost_drone = 0 

#Drone Shipping 
if weight < 2: 
  cost_drone = weight * 4.50 + 0 
elif weight > 2 and weight < 6:
  cost_drone = weight * 9.00 + 0
elif weight > 6 and weight < 10: 
  cost_drone = weight * 12.00 + 0
else: 
  cost_drone = weight * 14.25 + 0


print("This is the cost of drone shipping", float(cost_drone))

if cost_ground > cost_premiumground: 
  print("Premium Ground is Cheaper")
elif cost_ground < cost_premiumground: 
  print("Ground Shipping is cheaper")
elif cost_ground > cost_drone: 
  print("Drone shipping is cheaper")
else: 
  print("Ground shipping is cheaper")

  