f1 = []
f2 = []
f3 = []
ff = []

def file_reading(file_name):
	data = [file_name + '\n']
	with open(file_name) as f:
		 data += f.readlines()
	return data

f1 = file_reading('1.txt')
f2 = file_reading('2.txt')
f3 = file_reading('3.txt')

ff.append(f1)
ff.append(f2)
ff.append(f3)

new_ff = sorted(ff, key=len)
new_file_string = ''
with open('result.txt', 'w') as res:
	for i in range(len(new_ff)):
		new_ff[i].insert(1, f'{len(new_ff[i]) - 1}\n')
		for j in range(len(new_ff[i])):
			new_file_string += new_ff[i][j]
		new_file_string += '\n'
		# print(new_ff[i])
	res.write(new_file_string)

