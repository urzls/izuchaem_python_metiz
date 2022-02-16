requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
	print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
	("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
	print("Adding extra cheese.")
	
print("\nFinished making your pizza!\n")


#toppings.py
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
	print("Adding " + requested_topping + ".")
	
print("\nFinished making your pizza!\n")


for requested_topping in requested_toppings:
	if requested_topping == 'green peppers':
		print("Sorry, we are out of green peppers right now.")
	else:
		print("Adding " + requested_topping + ".")
		
print("\nFinished making your pizza!\n")



requested_toppings = []
if requested_toppings:
	for requested_topping in requested_toppings:
		print("Adding " + requested_topping + ".")
		print("\nFinished making your pizza!\n")
	else:
		print("Are you sure you want a plain pizza?\n")


available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print("Adding " + requested_topping + ".")
	else:
		print("Sorry, we don't have " + requested_topping + ".")

print("\nFinished making your pizza!\n")


