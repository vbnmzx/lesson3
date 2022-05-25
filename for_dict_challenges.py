# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
	{'first_name': 'Вася'},
	{'first_name': 'Петя'},
	{'first_name': 'Маша'},
	{'first_name': 'Маша'},
	{'first_name': 'Петя'},
]
# ???
peoples = {}
for student in students:
	if student.get('first_name') not in peoples:
		peoples[student.get('first_name')] = 1
	else:
		peoples[student.get('first_name')] += 1
for people in peoples:
	print(f'{people}: {peoples[people]}')
# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
	{'first_name': 'Вася'},
	{'first_name': 'Петя'},
	{'first_name': 'Маша'},
	{'first_name': 'Маша'},
	{'first_name': 'Оля'},
]
# ???
peoples = {}
for student in students:
	if student.get('first_name') not in peoples:
		peoples[student.get('first_name')] = 1
	else:
		peoples[student.get('first_name')] += 1
most_pop = 0
name = ''
for people in peoples:
	if peoples[people] > most_pop:
		name = people
		most_pop = peoples[people]
print(f'Самое частое имя среди учеников: {name}')

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
	[  # это – первый класс
		{'first_name': 'Вася'},
		{'first_name': 'Вася'},
	],
	[  # это – второй класс
		{'first_name': 'Маша'},
		{'first_name': 'Маша'},
		{'first_name': 'Оля'},
	], [  # это – третий класс
		{'first_name': 'Женя'},
		{'first_name': 'Петя'},
		{'first_name': 'Женя'},
		{'first_name': 'Саша'},
	],
]
# ???
i = 0
for students in school_students:
	peoples = {}
	for student in students:
		if student.get('first_name') not in peoples:
			peoples[student.get('first_name')] = 1
		else:
			peoples[student.get('first_name')] += 1
	most_pop = 0
	name = ''
	for people in peoples:
		if peoples[people] > most_pop:
			name = people
			most_pop = peoples[people]
	i += 1
	print(f'Самое частое имя в классе {i}: {name}')

# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
	{'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
	{'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
	{'class': '2б', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
	'Олег': True,
	'Маша': False,
	'Оля': False,
	'Миша': True,
	'Даша': False,
}
# ???
for a in range(len(school)):
	male = 0
	female = 0
	for student in school[a]['students']:
		if is_male[student['first_name']]:
			male += 1
		else:
			female += 1
	print(f'Класс {school[a]["class"]}: девочки {female}, мальчики {male}')
# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
	{'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
	{'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
	'Маша': False,
	'Оля': False,
	'Олег': True,
	'Миша': True,
}
# ???
male = {'class': '', 'male': 0}
female = {'class': '', 'female' : 0}
for a in range(len(school)):
	male1 = 0
	female1 = 0
	for student in school[a]['students']:
		if is_male[student['first_name']]:
			male1 += 1
		else:
			female1 += 1
	if male1 > female1 and male1 > male['male']:
		male['class'] = school[a]['class']
		male['male'] = male1
	elif female1 > male1 and female1 > female['female']:
		female['class'] = school[a]['class']
		female['female'] = female1
print(f'Больше всего мальчиков в классе {male["class"]}')
print(f'Больше всего девочек в классе {female["class"]}')