
left_list = []
right_list = []
with open("input.txt", "r") as input_data:
    for line in input_data.readlines():
        left_num, right_num = line.strip("\n").split("   ")
        left_list.append(left_num)
        right_list.append(right_num)

left_list = sorted(left_list)
right_list = sorted(right_list)

total_distance = []
for left, right in zip(left_list, right_list):
    total_distance.append(abs(int(right) - int(left)))

print(f"Total Distance: {sum(total_distance)}")


