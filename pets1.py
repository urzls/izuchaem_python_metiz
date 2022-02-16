#pets.py
"""
def describe_pet(animal_type, pet_name):
	#Выводит информацию о животном.
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")
	
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
"""


def describe_pet(animal_type, pet_name):
	"""Выводит информацию о животном."""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')

