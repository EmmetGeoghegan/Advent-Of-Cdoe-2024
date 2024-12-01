
left_list = []
right_list = []
with open("input.txt", "r") as input_data:
    for line in input_data.readlines():
        left_num, right_num = line.strip("\n").split("   ")
        left_list.append(left_num)
        right_list.append(right_num)

left_list = sorted(left_list)
right_list = sorted(right_list)

# Pre-compute number occurrence counts into a lookup dict
right_lookup_dict = {}

for i in right_list:
    if i in right_lookup_dict:
        right_lookup_dict[i] += 1
    else:
        right_lookup_dict[i] = 1

similarity_score_list = []

for i in left_list:
    if i in right_lookup_dict.keys():
        similarity_score_list.append(int(i) * right_lookup_dict[i])

print(f"Similarity score: {sum(similarity_score_list)}")