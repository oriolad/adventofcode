# PUZZLE 1 A # 

# Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input); apparently, something isn't quite adding up.

#Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

# For example, suppose your expense report contained the following:

# 1721
# 979
# 366
# 299
# 675
# 1456
# In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.

# Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you get if you multiply them together?

file = open("input_1.txt")
lines = file.readlines()

lines = list(map(int, lines))
lines.sort()


entry2 = None
for entry1 in lines:
	difference = 2020 - entry1
	if difference in lines:
		entry2 = difference
		break

print("Entry 1 " + str(entry1))
print("Entry 2 " + str(entry2))

answer = entry1 * entry2
print("Part 1a Answer: " + str(answer))

# PART 2 #

# The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from a past vacation. They offer you a second one if you can find three numbers in your expense report that meet the same criteria.

# Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together produces the answer, 241861950.

# In your expense report, what is the product of the three entries that sum to 2020?

for l1 in lines:
	for l2 in lines:
		for l3 in lines:
			if l1 + l2 + l3 == 2020:
				print("found")
				entry1 = l1
				entry2 = l2
				entry3 = l3
				break

print("Entry 1 " + str(entry1))
print("Entry 2 " + str(entry2))
print("Entry 3 " + str(entry3))

answer = entry1 * entry2 * entry3
print("Part 1b Answer: " + str(answer))