import re

def solution(lines: list[str]) -> int:

	gameIDTotal = 0
	gameNum = 1
	for line in lines:
		line = line[line.find(':') + 2:]
		for part in re.split('; |, ', line):
			values = part.split(' ')
			amount, color = int(values[0]), values[1]
			if (amount > 14 and color == 'blue') or (amount > 13 and color == 'green') or (amount > 12 and color == 'red'):
				gameIDTotal -= gameNum
				break

		gameIDTotal += gameNum
		gameNum += 1

	return gameIDTotal

def solution2(lines: list[str]) -> int:

	powerTotal = 0
	for line in lines:
		line = line[line.find(':') + 2:]
		maxes = {'red': 0, 'green': 0, 'blue': 0}
		for part in re.split('; |, ', line):
			values = part.split(' ')
			amount, color = int(values[0]), values[1]
			if amount > maxes[color]:
				maxes[color] = amount

		power = 1
		for m in maxes:
			power *= maxes[m]
		powerTotal += power

	return powerTotal


if __name__=='__main__':
	f = open('inputs/day02.txt', 'r')
	lines = f.read().splitlines()
	example1 = ['Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
				'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
				'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
				'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
				'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green']
	print("Part 1 Example Output:", solution(example1))
	print("Part 1 Problem Output:", solution(lines))
	print("Part 2 Example Output:", solution2(example1))
	print("Part 2 Problem Output:", solution2(lines))
	f.close()