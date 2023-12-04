import re

# And now probably my best solution so far LMAO

def solution(lines: list[str]) -> int:
	total = 0

	for line in lines:
		line = line[line.find(':') + 2:].split(' | ')
		winning_nums = {n for n in line[0].split()}
		nums = {n for n in line[1].split()}

		diff = len(winning_nums) - len(winning_nums - nums)
		if diff > 0:
			total += 2 ** (diff - 1)
	return total

def solution2(lines: list[str]) -> int:

	card_infos = dict()
	card_count = 1
	for line in lines:
		line = line[line.find(':') + 2:].split(' | ')
		winning_nums = {n for n in line[0].split()}
		nums = {n for n in line[1].split()}

		card_infos[card_count] = [1, len(winning_nums) - len(winning_nums - nums)]
		card_count += 1

	total_card_count = 0
	for card_num, info in card_infos.items():
		copies = info[0]
		wins = info[1]
		for i in range(1, wins + 1):
			if card_num + i < card_count:
				card_infos[card_num + i][0] += copies
		total_card_count += copies

	return total_card_count


if __name__=='__main__':
	f = open('inputs/day04.txt', 'r')
	lines = f.read().splitlines()
	example1 = ['Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53',
				'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19',
				'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1',
				'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83',
				'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36',
				'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11']
	print("Part 1 Example Output:", solution(example1))
	print("Part 1 Problem Output:", solution(lines))
	print("Part 2 Example Output:", solution2(example1))
	print("Part 2 Problem Output:", solution2(lines))
	f.close()