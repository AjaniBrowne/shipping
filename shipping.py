weight = 41.5
premium_ground_shipping = 125.00

#ground shipping

if weight <= 2:
  cost_ground = weight * 1.5 + 20
elif (weight >= 2) or (weight == 6):
  cost_ground = weight * 3.0 + 20
elif (weight >= 6) or (weight <= 10):
  cost_ground = weight * 4.0 + 20
elif weight > 10:
  cost_ground = weight * 4.75 + 20
else:
  print("enter in weight")  

print("Ground Shipping $", cost_ground)

print("Ground Shipping Premium $", premium_ground_shipping)

#Drone shipping

if weight <= 2:
  cost_drone = weight * 4.50
elif (weight >= 2) or (weight == 6):  
  cost_drone = weight * 9.0
elif (weight >= 6)  or (weight <= 10):
  cost_drone = weight * 12.0
elif weight > 10:
  cost_drone = weight * 14.25
else:
  print("enter in weight")

print("Drone Shipping $", cost_drone)  
