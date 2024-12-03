

all_poss_mults = set()

with open("input.txt", "r") as mul_data:
    data_stream = ""
    for i in mul_data.readlines():
        data_stream += i.strip()

print("------------")
print("Original")
print(data_stream)
print("------------")

start_mul_inst = data_stream.split("mul(")

mul_strings = []
if data_stream[:4] != "mul(":
    data_stream = "mul(".join(start_mul_inst)[len(start_mul_inst[0]):]
    start_mul_inst.pop(0)

print("------------")
print("mul(split")
print(start_mul_inst)

mul_comma_strings = []
for i in start_mul_inst:
    i = i.split(",")[0]
    try:
        _ = int(i)
        mul_comma_strings.append(i)
    except:
        pass
print("------------")
print(", split")
print(mul_comma_strings)
start_mul_inst = "".join(start_mul_inst)

print("------------")
mul_first_digit = []
for i in mul_comma_strings:
    str_build = f"mul({i},"
    print(str_build)
    test_str = data_stream.split(str_build)
    print(test_str)
    if test_str[0] == "":
        test_str.pop(0)

    for j in test_str:
        final_nums = j.split(")")
        for k in final_nums:
            print(k)
            try:
                _ = int(k)
                print(f"{k} = Possible ending")
                all_poss_mults.add(f"{str_build}{k})")
            except:
                pass


print(all_poss_mults)

enabled_string_portions = []
input("-------------------1111111111111111111111111---------------------")
while True:
    flagged_list = data_stream.split("don't()", 1)
    print("-------------------1111111111111111111111111---------------------")
    print("flagged list")
    print(flagged_list)
    print("-------------------1111111111111111111111111---------------------")
    enabled_string_portions.append(flagged_list[0])
    if len(flagged_list) == 1:
        break
    data_stream = "".join(flagged_list[1:])
    print("-------------------1111111111111111111111111---------------------")
    print(data_stream)
    print("-------------------1111111111111111111111111---------------------")
    flagged_list = data_stream.split("do()", 1)
    print("-------------------1111111111111111111111111---------------------")
    print(flagged_list)
    print("-------------------1111111111111111111111111---------------------")
    data_stream = "".join(flagged_list[1:])
    print("-------------------1111111111111111111111111---------------------")
    print(data_stream)
    print("-------------------1111111111111111111111111---------------------")

print("999999999999999999999999999")
for i in enabled_string_portions:
    print(i)
print("999999999999999999999999999")
final_data_stream = "".join(enabled_string_portions)
# Lastsly count all mults
def mult_evaluator(multstring, count):
    first_num = int(multstring.split("(")[1].split(",")[0])
    second_num = int(multstring.split(",")[1].split(")")[0])
    total = first_num * second_num * count
    return total

running_total = 0
for i in all_poss_mults:
    app_count = final_data_stream.count(i)
    print(i, app_count)
    running_total += mult_evaluator(i, app_count)

print(running_total)


# correct - 89798695
