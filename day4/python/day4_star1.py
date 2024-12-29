with open("input.txt", "r") as wordsearch_fie:
    wordsearch_lines = [i.strip() for i in wordsearch_fie.readlines()]

xmas_count = 0

# Lets do forwards and backwards search
for hline in wordsearch_lines:
    xmas_count += hline.count("XMAS")
    xmas_count += hline.count("SAMX")

print(xmas_count)

# Lets do up and down
for vline in zip(*wordsearch_lines):
    vline_string = "".join(vline)
    print(vline_string)
    xmas_count += vline_string.count("XMAS")
    xmas_count += vline_string.count("SAMX")
    print(xmas_count)

print(xmas_count)

def calc_list_splits(iteration, wordsearch_row_count, wordsearch_row_length):
    if iteration <= wordsearch_row_length:
        start_split = 0
    else:
        start_split = iteration - wordsearch_row_length

    if iteration < wordsearch_row_length:
        end_split = iteration
    else:
        end_split = wordsearch_row_count

    return start_split, end_split


def calc_row_valid_char_fowards(row, row_index, loop_index):
    row_char_selected = loop_index - row_index - 1
    return row[row_char_selected]


def calc_row_valid_char_backwards(row, row_index, loop_index):
    row_char_selected = loop_index - row_index - 1
    row_char_selected = row_char_selected * -1
    row_char_selected -= 1
    return row[row_char_selected]


wordsearch_row_count = len(wordsearch_lines)
wordsearch_row_length = len(wordsearch_lines[0])

diag_line_count = wordsearch_row_count + wordsearch_row_length

# diagonal top left across
for i in range(1, diag_line_count):
    print("------------------------")
    start_split, end_split = calc_list_splits(i, wordsearch_row_count, wordsearch_row_length)
    # print("start,end:", start_split, end_split)
    # print(f"loop index {i}")

    active_lines = wordsearch_lines[start_split:end_split]
    # print(active_lines)

    forward_diag_letters = []
    backward_diag_letters = []
    for index, row in zip(range(start_split, end_split), active_lines):
        # print(index, row)
        valid_diag_letter_forwards = calc_row_valid_char_fowards(row, row_index=index, loop_index=i)
        valid_diag_letter_backwards = calc_row_valid_char_backwards(row, row_index=index, loop_index=i)
        # print(f"Letter chosen = {valid_diag_letter_forwards}")
        # print(f"Letter chosen = {valid_diag_letter_backwards}")
        forward_diag_letters.append(valid_diag_letter_forwards)
        backward_diag_letters.append(valid_diag_letter_backwards)

    diag_letters_forwards = "".join(forward_diag_letters)
    diag_letters_backwards = "".join(backward_diag_letters)

    xmas_count += diag_letters_forwards.count("XMAS")
    print(xmas_count)
    xmas_count += diag_letters_forwards.count("SAMX")
    print(xmas_count)

    xmas_count += diag_letters_backwards.count("XMAS")
    print(xmas_count)
    xmas_count += diag_letters_backwards.count("SAMX")
    print(xmas_count)
    print("------------------------")

print(xmas_count)