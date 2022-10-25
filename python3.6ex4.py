cars=100
space_in_a_car=4.0 #omiting .0 has no effect on the program. It still runs
drivers=30
passengers=90
cars_not_driven=cars-drivers
cars_driven=drivers
carpool_capacity=cars_driven*space_in_a_car
average_passengers_per_car=passengers/cars_driven
print("There are",cars,"cars available")
print("There are only",drivers,"drivers available")
#When it is a print statement you space out. When it's not..don't
print("There will be",cars_not_driven,"empty cars today.")
      #let's see if we can go on with the print statements without the word print but with a sequence of prints preceding
print("We can transport",carpool_capacity,"people today.")
      #Well,that didn't work.
print("We have",passengers,"to carpool today")
print("We need to put about",average_passengers_per_car,"in each car")
#I'll keep my comments as reminder notes
