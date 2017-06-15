cars = 100
spaceInCar = 4.0
drivers = 30
passangers = 90
carsNotDriven = cars-drivers
carsDriven = drivers
carpoolCapacity = carsDriven * spaceInCar
avgPassangersPerCar = passangers / carsDriven

print ("There are", cars, "cars available.")
print ("There are only", drivers, "drivers available.")
print ("There will be", carsNotDriven, "empty cars today.")
print ("We can transport", carpoolCapacity, "people today.")
print ("We have", passangers, "to carpool today.")
print ("We need to put about", avgPassangersPerCar, "in each car.")