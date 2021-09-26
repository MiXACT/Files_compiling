def file_reading(file_name):
	'''Принимает на вход имя файла для чтения;
	возвращает список, каждый эл-т которого - строка файла'''
	data = [file_name + '\n']
	with open(file_name) as f:
		 data += f.readlines()
	return data

files_data = []

#цикл чтения файлов; имена файлов задаются числами через f-строку
for i in range(3):
	files_data.append(file_reading(f'{i + 1}.txt'))

files_data = sorted(files_data, key=len)
new_file = ''

with open('result.txt', 'w') as res:
	for i in range(len(files_data)):
		files_data[i].insert(1, f'{len(files_data[i]) - 1}\n')
		for j in range(len(files_data[i])):
			new_file += files_data[i][j]
		new_file += '\n'
	res.write(new_file)

