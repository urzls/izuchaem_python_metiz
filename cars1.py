cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())


requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
	print("Hold the anchovies!")

#Проверка на вхоэжение
requested_toppings = ['mushrooms', 'onions', 'pineapple']
'mushrooms' in requested_toppings

#banned_users.py
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
	print(user.title() + ", you can post a response if you wish.")

age = 19
if age >= 18:
	print("You are old enough to vote!")
	print("Have you registered to vote yet?")

age = 17
if age >= 18:
	print("You are old enough to vote!")
	print("Have you registered to vote yet?")
else:
	print("Sorry, you are too young to vote.")
	print("Please register to vote as soon as you turn 18!")

