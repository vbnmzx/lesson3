# Вывести последнюю букву в слове
word = 'Архангельск'
# ???
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
# ???
print(word.lower().count('а'))

# Вывести количество гласных букв в слове
word = 'Архангельск'
# ???
glas = 'аеёиоуэюя'
i = 0
for a in word.lower():
	if a in glas:
		i += 1
print(i)

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
# ???
print(len(sentence.split()))

# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
# ???
for word in sentence.split():
	print(word[0])

# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
# ???
chars = 0
for word in sentence.split():
	chars += len(word)
print(chars // len(sentence.split()))
