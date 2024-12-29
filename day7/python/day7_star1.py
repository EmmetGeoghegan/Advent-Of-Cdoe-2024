class OperatorTree:
    possible_tracker = []
    answer = 0
    def __init__(self, target, start_value, remaining_values, operator, input_index):
        print("-------------------")
        self.target = target
        self.children = []
        self.curr_sum = start_value
        self.index = index

        # print(f"Target: {self.target}")
        # print(f"curr_sum: {self.curr_sum}")
        # print(f"Remaining values: {remaining_values}")
        # print(f"opreation mode: {operator}")
        # print(f"index: {self.index}")


        if self.curr_sum > self.target:
            print("Not possible!!")
        else:
            print(f"remaining - {remaining_values}")
            if not remaining_values:
                print(f"Tree expanded - {self.target}")
                print("debug time")
                if self.target == self.curr_sum:
                    print("Its possible!")
                    if self.index not in OperatorTree.possible_tracker:
                        OperatorTree.possible_tracker.append(self.index)
                        OperatorTree.answer += self.target
            else:
                if operator is not None:
                    nextval = remaining_values.pop(0)
                    print(nextval, operator)
                    if operator == "+":
                        self.curr_sum = start_value + nextval
                    else:
                        self.curr_sum = start_value * nextval
                    print(f"new value: {self.curr_sum}")

                self.children.append(OperatorTree(self.target, self.curr_sum, remaining_values.copy(), "+", self.index))
                self.children.append(OperatorTree(self.target, self.curr_sum, remaining_values.copy(), "*", self.index))
        print("-------------------")


with open("input.txt") as input_data:
    input_data = input_data.readlines()

for index, i in enumerate(input_data):
    i = i.strip("\n")
    goal_value = int(i.split(":")[0])
    values = [int(j) for j in i.split(": ")[1].split(" ")]
    start_val = values.pop(0)

    test_tree = OperatorTree(target=goal_value, start_value=start_val, remaining_values=values, operator=None, input_index=index)
    print("debug")
print(OperatorTree.possible_tracker)
print(len(OperatorTree.possible_tracker))


print(OperatorTree.answer)
# 286 too low