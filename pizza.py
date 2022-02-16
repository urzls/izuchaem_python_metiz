# Сохранение информации о заказанной пицце.
pizza = {
	'crust': 'thick',
	'toppings': ['mushrooms', 'extra cheese'],
}

# Описание заказа.
print(
	"You ordered a " + pizza['crust'] + 
	"-crust pizza " + 
	"with the following toppings:"
)
for topping in pizza['toppings']:
	print("\t" + topping)

print("\n====================\n")

#favorite_languages.py
favorite_languages = {
	'jen': ['python', 'ruby'],
	'sarah': ['c'],
	'edward': ['ruby', 'go'],
	'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages.items():
	print("\n" + name.title() + "'s favorite languages are:")
	for language in languages:
		print("\t" + language.title())

