
test_input_list = [199,200,208,210,200,207,240,269,260,263]
puzzle_input_list = [int(x) for x in open("day1_input.txt").readlines()]

input_list = puzzle_input_list

total_p1 = sum([bool(input_list[x] - input_list[x-1]>0) for x in range(1,len(input_list))])
print("Part 1: {}".format(total_p1))


total_p2 = sum([bool(input_list[x] - input_list[x-3]>0) for x in range(3,len(input_list))])

print("Part 2: {}".format(total_p2))
