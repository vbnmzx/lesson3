"""
with open('text.txt', 'a', encoding='utf-8') as f:
	f.write("Привет, мир!")
with open('text.txt', 'r', encoding='utf-8') as f:
	for line in f:
		line = line.upper()
		line = line.replace('\n', '')
		print(line)
"""
file_str = ''
with open('referat.txt', 'r', encoding='utf-8') as f:
	for line in f:
		file_str += line
print(len(file_str))
print(len(file_str.split()))
with open('referat2.txt', 'w', encoding='utf-8') as f:
	f.write(file_str.replace('.', '!'))
