def evaluate_direction(report):
    report_asc = sorted(report, reverse=True)
    report_desc = sorted(report, reverse=False)

    # Line is not ascending or descending
    if not (report == report_asc or report == report_desc):
        return False
    else:
        return True


def evaluate_duplicity(report):
    no_dup_list = []
    for i in report:
        if i not in no_dup_list:
            no_dup_list.append(i)
    if len(report) == len(no_dup_list):
        return True
    else:
        return False


def evaluate_deltas(report):
    delta_check_flag = True
    for report_section in range(len(report) - 1):
        # Sliding window through the rows
        start_room = int(report[report_section])
        next_room = int(report[report_section + 1])
        print(start_room, next_room)
        room_diff = next_room - start_room

        # If delta greater than limits room is not valid
        if abs(room_diff) > 3 or abs(room_diff) < 1:
            delta_check_flag = False
            break

    return delta_check_flag


safe_counter = 0

with open("input.txt", "r") as report_data:
    for report in report_data.readlines():
        print("------------------- START ------------------")
        report = report.strip().split(" ")

        # Convert to integers
        master_report = [int(i) for i in report]
        print(f"MASTER: {master_report}")

        master_eval = evaluate_direction(master_report)
        # check sorting
        if not master_eval:
            test_direction_outcomes = []
            for i in range(1, len(master_report) + 1):
                test_list = master_report[: i - 1] + master_report[i:]
                print(f"test: {test_list}")
                test_direction_eval = evaluate_direction(test_list)
                print(f"Eval: {test_direction_eval}")
                if test_direction_eval:
                    test_direction_outcomes.append(test_list)

            if not test_direction_outcomes:
                # report has more than one issue
                print("More than one direction change")
                continue
            else:
                new_test_strings = test_direction_outcomes
        else:
            new_test_strings = [master_report]

        print("=========================")
        print("Strings passing the direction test")
        print(new_test_strings)
        print("=========================")

        passing_dup_strings = []
        for i in new_test_strings:
            dup_check = evaluate_duplicity(i)
            if dup_check:
                print(f"{i} passing dup check")
                passing_dup_strings.append(i)
            else:
                if len(i) == len(master_report):
                    for j in range(0, len(i) + 1):
                        test_list = i[:j - 1] + i[j:]
                        dup_check = evaluate_duplicity(test_list)
                        if dup_check:
                            print(f"{test_list} passing dup check")
                            if test_list not in passing_dup_strings:
                                passing_dup_strings.append(test_list)

        if len(passing_dup_strings) == 0:
            print("Not passing duplicates")
            continue
        print("=============")
        print(f"checking deltas on{passing_dup_strings}")

        for i in passing_dup_strings:
            check_flag = evaluate_deltas(i)
            if check_flag:
                safe_counter += 1
                print(f"{i} passing delta check")
                print(f"MASTER: {master_report} SAFE!")
                break
            elif len(i) == len(master_report):
                for j in range(1, len(i) + 1):
                    test_list = i[:j - 1] + i[j:]
                    check_second_flag = evaluate_deltas(test_list)
                    if check_second_flag:
                        print(f"{test_list} passing delta check")
                        safe_counter += 1
                        print(f"MASTER: {master_report} SAFE!")
                        break
                    else:
                        print(test_list, "Not passing delta check")
            else:
                print(i, "Not passing delta check")

        print("------------------------- END --------------------")
print(f"Safe report count: {safe_counter}")
