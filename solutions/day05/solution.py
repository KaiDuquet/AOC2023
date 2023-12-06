import re

def solution(lines: list[str]) -> int:

	seeds = lines[0][len('seeds: '):].split()
	n = len(lines)

	min_location = -1

	for seed in seeds:
		key = int(seed)
		
		it = 3
		while it < n:
			line = lines[it]

			if not line or line[-1] == ':':
				it += 1
				continue
			
			dest, src, r = [int(i) for i in line.split()]
			if key >= src and key < src + r:
				key += dest - src
				while it < n and lines[it]:
					it += 1
			it += 1
		if min_location < 0 or key < min_location:
			min_location = key
	return min_location


def solution2(lines: list[str]) -> int:
	seeds = lines[0][len('seeds: '):].split()
	n = len(lines)

	print([int(s) for s in seeds])
	return 
	min_location = -1

	for seed in seeds:
		key = int(seed)
		
		it = 3
		while it < n:
			line = lines[it]

			if not line or line[-1] == ':':
				it += 1
				continue
			
			dest, src, r = [int(i) for i in line.split()]
			if key >= src and key < src + r:
				key += dest - src
				while it < n and lines[it]:
					it += 1
			it += 1
		if min_location < 0 or key < min_location:
			min_location = key
	return min_location


if __name__=='__main__':
	f = open('inputs/day05.txt', 'r')
	lines = f.read().splitlines()
	example1 = ['seeds: 79 14 55 13',
				'',
				'seed-to-soil map:',
				'50 98 2',
				'52 50 48',
				'',
				'soil-to-fertilizer map:',
				'0 15 37',
				'37 52 2',
				'39 0 15',
				'',
				'fertilizer-to-water map:',
				'49 53 8',
				'0 11 42',
				'42 0 7',
				'57 7 4',
				'',
				'water-to-light map:',
				'88 18 7',
				'18 25 70',
				'',
				'light-to-temperature map:',
				'45 77 23',
				'81 45 19',
				'68 64 13',
				'',
				'temperature-to-humidity map:',
				'0 69 1',
				'1 0 69',
				'',
				'humidity-to-location map:',
				'60 56 37',
				'56 93 4']
	print("Part 1 Example Output:", solution(example1))
	print("Part 1 Problem Output:", solution(lines))
	print("Part 2 Example Output:", solution2(example1))
	print("Part 2 Problem Output:", solution2(lines))
	f.close()