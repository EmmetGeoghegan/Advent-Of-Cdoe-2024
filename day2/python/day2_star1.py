

safe_counter = 0

with open("input.txt", "r") as report_data:
    for report in report_data.readlines():
        report = report.strip().split(" ")

        # Convert to integers
        report = [int(i) for i in report]
        # check sorting
        report_asc = sorted(report, reverse=True)
        report_desc = sorted(report, reverse=False)

        # Line is not ascending or descending
        if not (report == report_asc or report == report_desc):
            continue

        # Line has duplicates
        if len(set(report)) != len(report):
            continue

        check_flag = True

        for i in range(len(report)-1):
            # Sliding window through the rows
            start_room = int(report[i])
            next_room = int(report[i+1])
            room_diff = next_room - start_room

            # If delta greater than limits room is not valid
            if abs(room_diff) > 3 or abs(room_diff) < 1:
                check_flag = False
                break

        # If all sliding windows pass the deltas are good so the report passes
        if check_flag:
            safe_counter += 1

print(f"Safe report count: {safe_counter}")







