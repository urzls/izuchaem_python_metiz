"""
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'q' when you are finished.) "
while True:
	city = input(prompt)
	if city == 'q':
		break
	else:
		print("I'd love to go to " + city.title() + "!")
"""
"""
#counting.py
current_number = 0
while current_number < 10:
	current_number += 1
	if current_number % 2 == 0:
		continue
	print(current_number)
"""

#counting.py
x = 1
while x <= 5:
	print(x)
	x += 1
