import re

# Probably my worst solution so far but gg wtv

def solution(m: list[str]) -> int:
	total = 0
	i = 0

	len_m = len(m)
	n = len(m[0])

	for i in range(len_m):
		for j in range(n):

			c = m[i][j]
			if c == '.' or c.isdigit():
				continue

			else: #if c in "*@#$%=+/-&!^":
				# Check behind symbol
				if j - 1 >= 0:
					root = j
					INT = ''
					while m[i][j - 1].isdigit():
						INT = m[i][j - 1] + INT
						if j - 2 >= 0:
							j -= 1
						else:
							break
					if INT:
						print(INT)
						total += int(INT)
					j = root
				#Check after symbol
				if j + 1 < n:
					root = j
					INT = ''
					while m[i][j + 1].isdigit():
						INT = INT + m[i][j + 1]
						if j + 2 < n:
							j += 1
						else:
							break
					if INT:
						print(INT)
						total += int(INT)
					j = root
				#Check all above symbol
				if i - 1 >= 0:
					root = j
					INT = ''
					if j - 1 >= 0:
						while m[i - 1][j - 1].isdigit():
							INT = m[i - 1][j - 1] + INT
							if j - 2 >= 0:
								j -= 1
							else:
								break
					j = root
					if not m[i - 1][j].isdigit():
						if INT:
							print(INT)
							total += int(INT)
							INT = ''
						j += 1
					if j < n:
						while m[i - 1][j].isdigit():
							INT = INT + m[i - 1][j]
							if j + 2 < n:
								j += 1
							else:
								break
					if INT:
						print(INT)
						total += int(INT)
					j = root
				if i + 1 < len_m:
					root = j
					INT = ''
					if j - 1 >= 0:
						while m[i + 1][j - 1].isdigit():
							INT = m[i + 1][j - 1] + INT
							if j - 1 >= 0:
								j -= 1
							else:
								break
					j = root
					if not m[i + 1][j].isdigit():
						if INT:
							print(INT)
							total += int(INT)
							INT = ''
						j += 1
					if j < n:
						while m[i + 1][j].isdigit():
							INT = INT + m[i + 1][j]
							if j + 1 < n:
								j += 1
							else:
								break
					if INT:
						print(INT)
						total += int(INT)
					j = root

	return total

def solution2(m: list[str]) -> int:
	total = 0
	i = 0

	len_m = len(m)
	n = len(m[0])

	for i in range(len_m):
		for j in range(n):

			c = m[i][j]
			if c == '.' or c.isdigit():
				continue

			elif c == '*':
				saved_int = []
				# Check behind symbol
				if j - 1 >= 0:
					root = j
					INT = ''
					while m[i][j - 1].isdigit():
						INT = m[i][j - 1] + INT
						if j - 2 >= 0:
							j -= 1
						else:
							break
					if INT:
						saved_int.append(int(INT))
					j = root
				#Check after symbol
				if j + 1 < n:
					root = j
					INT = ''
					while m[i][j + 1].isdigit():
						INT = INT + m[i][j + 1]
						if j + 2 < n:
							j += 1
						else:
							break
					if INT:
						saved_int.append(int(INT))
					j = root
				#Check all above symbol
				if i - 1 >= 0:
					root = j
					INT = ''
					if j - 1 >= 0:
						while m[i - 1][j - 1].isdigit():
							INT = m[i - 1][j - 1] + INT
							if j - 2 >= 0:
								j -= 1
							else:
								break
					j = root
					if not m[i - 1][j].isdigit():
						if INT:
							saved_int.append(int(INT))
							INT = ''
						j += 1
					if j < n:
						while m[i - 1][j].isdigit():
							INT = INT + m[i - 1][j]
							if j + 2 < n:
								j += 1
							else:
								break
					if INT:
						saved_int.append(int(INT))
					j = root
				if i + 1 < len_m:
					root = j
					INT = ''
					if j - 1 >= 0:
						while m[i + 1][j - 1].isdigit():
							INT = m[i + 1][j - 1] + INT
							if j - 1 >= 0:
								j -= 1
							else:
								break
					j = root
					if not m[i + 1][j].isdigit():
						if INT:
							saved_int.append(int(INT))
							INT = ''
						j += 1
					if j < n:
						while m[i + 1][j].isdigit():
							INT = INT + m[i + 1][j]
							if j + 1 < n:
								j += 1
							else:
								break
					if INT:
						saved_int.append(int(INT))
					j = root

				if len(saved_int) == 2:
					total += saved_int[0] * saved_int[1]
	return total


if __name__=='__main__':
	f = open('inputs/day03.txt', 'r')
	lines = f.read().splitlines()
	example1 = ['467..114..',
				'...*......',
				'..35..633.',
				'......#...',
				'617*......',
				'.....+.58.',
				'..592.....',
				'......755.',
				'...$.*....',
				'.664.598..']
	print("Part 1 Example Output:", solution(example1))
	print("Part 1 Problem Output:", solution(lines))
	print("Part 2 Example Output:", solution2(example1))
	print("Part 2 Problem Output:", solution2(lines))
	f.close()