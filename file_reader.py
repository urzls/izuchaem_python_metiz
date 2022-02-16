"""
with open('pi_digits.txt') as file_object:
	contents = file_object.read()
	print(contents)
"""

#with open('text_files\имя_файла.txt') as file_object:
#Если файл находится в другом каталоге, например text_files


#Абсолютные пути В Windows выглядят так:
#file_path = 'C:\Users\ehmatthes\other_files\text_files\имя_файла.txt'
#with open(file_path) as file_object:


# Цикл for
"""
filename = 'pi_digits.txt'
with open(filename) as file_object:
	for line in file_object:
		print(line.rstrip())
"""

filename = 'pi_digits.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

for line in lines:
	print(line.rstrip())
