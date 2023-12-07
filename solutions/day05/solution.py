from bisect import bisect

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
	seeds = [(int(seeds[i]), int(seeds[i + 1])) for i in range(0, len(seeds), 2)]

	def find_min(keys, elem):
		index = bisect(keys, elem) - 1
		if keys[index] == elem:
			index += 1
		return index
			
	level = 0
	maps = dict()
	sorted_keys = dict()
	for line in lines[3:]:

		if not line:
			continue
		if line[-1] == ':':
			level += 1
			continue

		if level not in maps:
			maps[level] = dict()
			if level > 0 and sorted_keys[level - 1]:
				sorted_keys[level - 1].sort()
			sorted_keys[level] = list()

		dest, src, r = [int(i) for i in line.split()]
		maps[level][src] = (r, dest - src)
		sorted_keys[level].append(src)

	min_location = -1
	for seed in seeds:
		level = 0
		range_queue = [(seed[0], seed[0] + seed[1] - 1)]

		while len(range_queue):
			ranges_in_level = len(range_queue)
			for _ in range(ranges_in_level, 0, -1):
				pair = range_queue.pop(0)

				min_index = find_min(sorted_keys[level], pair[0])
				max_index = find_min(sorted_keys[level], pair[1])

				for idx in range(min_index, max_index + 1):
					if idx == -1:
						new_b = pair[1] if idx == max_index else sorted_keys[level][idx + 1] - 1
						range_queue.append((pair[0], new_b))
						continue
					params = maps[level][sorted_keys[level][idx]]
					if idx > min_index or pair[0] < sorted_keys[level][idx] + params[0]:
						new_a = sorted_keys[level][idx] + params[1] if idx > min_index else pair[0] + params[1]
						if idx < max_index:
							new_b = sorted_keys[level][idx + 1] - 1 + params[1]
						else:
							new_b = pair[1] + params[1]
					else:
						new_a, new_b = pair
					range_queue.append((new_a, new_b))
			if level == 6:
				break
			level += 1
		
		local_min = min([r[0] for r in range_queue])
		if min_location < 0 or local_min < min_location:
			min_location = local_min
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