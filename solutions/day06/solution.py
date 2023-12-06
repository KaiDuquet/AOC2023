import math

def solution(lines: list[str]) -> int:
    total = 1
    for pair in zip(lines[0].split()[1:], lines[1].split()[1:]):
        t, r = int(pair[0]), int(pair[1])
        det = math.sqrt(t ** 2 - 4 * r)
        total *= (math.ceil((t + det) / 2) - math.floor((t - det) / 2) - 1)
    return total

def solution2(lines: list[str]) -> int:
    t = int(''.join(lines[0].split()[1:]))
    r = int(''.join(lines[1].split()[1:]))
    det = math.sqrt(t ** 2 - 4 * r)
    return math.ceil((t + det) / 2) - math.floor((t - det) / 2) - 1


if __name__=='__main__':
	f = open('../../inputs/day06.txt', 'r')
	lines = f.read().splitlines()
	example1 = ['Time:      7  15   30',
                'Distance:  9  40  200']
	print("Part 1 Example Output:", solution(example1))
	print("Part 1 Problem Output:", solution(lines))
	print("Part 2 Example Output:", solution2(example1))
	print("Part 2 Problem Output:", solution2(lines))
	f.close()