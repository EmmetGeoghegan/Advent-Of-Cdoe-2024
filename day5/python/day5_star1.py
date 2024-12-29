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

good_updates = []
for update in updates:
    update = update.strip().split(",")
    if update == [""]:
        continue
    ok_flag = True
    for page_num in update:
        if page_num in page_rules_dict.keys():
            for criteria in page_rules_dict[page_num]:
                if criteria in update:
                    if update.index(page_num) > update.index(criteria):
                        ok_flag = False

    if ok_flag:
        good_updates.append(update)
        print(update)
print(len(good_updates))
result = 0
for i in good_updates:
    result += int(i[len(i) // 2])

print(result)


