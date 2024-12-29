with open("input.txt", "r") as inputtext:
    input_data = "".join(inputtext.readlines())

page_rules, updates = input_data.split("\n\n")


page_rules_dict = {}
for i in page_rules.split("\n"):
    key, value = i.strip().split("|")
    if key in page_rules_dict.keys():
        page_rules_dict[key].append(value)
    else:
        page_rules_dict[key] = [value]




updates = updates.split("\n")

# good_updates = []
# for update in updates:
#     update = update.strip().split(",")
#     if update == [""]:
#         continue
#     ok_flag = True
#     for page_num in update:
#         if page_num in page_rules_dict.keys():
#             for criteria in page_rules_dict[page_num]:
#                 if criteria in update:
#                     if update.index(page_num) > update.index(criteria):
#                         ok_flag = False
#
#     if ok_flag:
#         good_updates.append(update)
#         print(update)

bad_rules = []
for update in updates:
    update = update.strip().split(",")
    print(update)
    if update == [""]:
        continue
    search_flag = True

    for page_num in update:
        if search_flag:
            if page_num in page_rules_dict.keys() and search_flag == True:
                for criteria in page_rules_dict[page_num]:
                    if criteria in update:
                        if update.index(page_num) > update.index(criteria):
                            print("Update added to bad list")
                            bad_rules.append(update)
                            search_flag = False
                            print(update)
                            break
        else:
            continue
print(len(updates))
print(len(bad_rules))

def check_ok(ordering, rules):
    for i in ordering:
        if i in rules.keys():
            for criteria in page_rules_dict[i]:
                # print(f"{i} - RuleS: {page_rules_dict[i]}")
                if criteria in ordering:
                    key_page_index = ordering.index(i)
                    value_page_index = ordering.index(criteria)
                    if key_page_index > value_page_index:
                        # print("issue found")
                        # print(f"{i} after {criteria}")
                        new_list = fix_list(ordering, key_page_index, value_page_index)
                        return new_list
    print("No issues found!")
    return ordering

def fix_list(ordering, index1, index2):
    output_list = ordering.copy()

    output_list[index1] = ordering[index2]
    output_list[index2] = ordering[index1]

    # print(output_list)
    # print(ordering)
    return output_list


fixed_lists = []

for i in bad_rules:
    print(f"Fixing {i}")
    while True:
        # print(f"checking again - {i}")
        new_list = check_ok(i, page_rules_dict)
        if new_list == i:
            fixed_lists.append(i)
            print("LIST FIXED")
            print(new_list)
            break
        else:
            # print("List not fixed")
            i = new_list

# print(fixed_lists)

result = 0
for i in fixed_lists:
    result += int(i[len(i) // 2])

print(result)


# 9070 too high



