#mountain_poll.py
responses = {}

# Установка флага продолжения опроса.
polling_active = True

while polling_active:
	# Запрос имени и ответа пользователя.
	name = input("\nWhat is your name? ")
	response = input("Which mountain would you like to climb someday? ")
	
	# Ответ сохраняется в словаре:
	responses[name] = response
	
	# Проверка продолжения опроса.
	repeat = input("Would you like to let another person respond? (y/ n) ")
	if repeat == 'n':
		polling_active = False
		
# Опрос завершен, вывести результаты.
print("\n--- Poll Results ---")
for name, response in responses.items():
	print(name + " would like to climb " + response + ".")

