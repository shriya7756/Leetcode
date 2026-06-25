# Predefined score matrix representing the target's rings
# Each element represents the score for that position on the target
score = [
	[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
	[1, 2, 2, 2, 2, 2, 2, 2, 2, 1],
	[1, 2, 3, 3, 3, 3, 3, 3, 2, 1],
	[1, 2, 3, 4, 4, 4, 4, 3, 2, 1],
	[1, 2, 3, 4, 5, 5, 4, 3, 2, 1],
	[1, 2, 3, 4, 5, 5, 4, 3, 2, 1],
	[1, 2, 3, 4, 4, 4, 4, 3, 2, 1],
	[1, 2, 3, 3, 3, 3, 3, 3, 2, 1],
	[1, 2, 2, 2, 2, 2, 2, 2, 2, 1],
	[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

import sys
input = sys.stdin.read

data = input().split()

# Read number of test cases
t = int(data[0])
index = 1

for _ in range(t):
	# 10x10 grid to store the target for each test case
a = []
	for i in range(10):
		a.append(data[index])
		index += 1

	# Variable to accumulate the total score for the current test case
total_score = 0

	# Loop through each row of the grid
	for i in range(10):
		# Loop through each column of the grid
		for j in range(10):
			# Check if there is an arrow at this position
			if a[i][j] == 'X':
				# Add the score for this position to the total score
				total_score += score[i][j]

	# Output the total score for the current test case
	print(total_score)

# Time Complexity (TC): O(n^2) = O(100)
# Space Complexity (SC): O(10*10) = O(100)
