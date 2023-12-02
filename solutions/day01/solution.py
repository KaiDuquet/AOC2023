def solution(lines: list[str]) -> int:
	total = 0
	for line in lines:
		first_digit = None
		last_digit = None
		for c in line:
			if c.isdigit():
				if first_digit is None:
					first_digit = c
				last_digit = c
		if last_digit:
			first_digit += last_digit
		total += int(first_digit)
	return total

def solution2(lines: list[str]) -> int:

	num_map = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}

	trie = dict()
	for word in num_map:
		curr = trie
		for letter in word:
			curr = curr.setdefault(letter, {})
		curr['_'] = '_'
	
	curr_trie = trie
	curr_word = ''
	first_digit = None
	last_digit = None

	def set_digit(c):
		nonlocal first_digit, last_digit
		if first_digit is None:
			first_digit = c
		last_digit = c

	def reset_trie():
		nonlocal curr_trie, curr_word
		curr_trie = trie
		curr_word = ''

	def advance_trie(c):
		nonlocal curr_trie, curr_word
		curr_word += c
		curr_trie = curr_trie[c]

	total = 0
	for line in lines:
		i = 0
		ref = None
		while i < len(line):
			c = line[i]

			if c.isdigit():
				set_digit(c)
				reset_trie()
			
			elif c in curr_trie:
				if ref is None:
					ref = i
				advance_trie(c)

				if '_' in curr_trie:
					set_digit(num_map[curr_word])
					reset_trie()
			else:
				if curr_word and ref is not None:
					if i == len(line) - 1:
						break
					i = ref + 1
					reset_trie()
					ref = None
					continue

			if curr_word == '' and c in curr_trie:
				advance_trie(c)
			i += 1
		
		total += int(first_digit + last_digit)

		reset_trie()
		first_digit = None
		last_digit = None

	return total


if __name__=='__main__':
	f = open('inputs/day01.txt', 'r')
	lines = f.read().splitlines()
	print("Part 1 Example Output:", solution(['1abc2', 'pqr3stu8vwx', 'a1b2c3d4e5f', 'treb7uchet']))
	print("Part 1 Problem Output:", solution(lines))
	print("Part 2 Example Output:", solution2(['two1nine', 'eightwothree', 'abcone2threexyz', 'xtwone3four', '4nineeightseven2', 'zoneight234', '7pqrstsixteen']))
	print("Part 2 Problem Output:", solution2(lines))
	f.close()