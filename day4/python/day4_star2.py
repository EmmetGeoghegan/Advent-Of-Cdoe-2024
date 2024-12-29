with open("fuck.txt") as wordsearch:
    wordsearch_data = wordsearch.readlines()

wordsearch_data = [i.strip() for i in wordsearch_data]

# Use 3x3 sliding window through the array

number_horizontal_steps = len(wordsearch_data[0]) - 2
number_vertical_steps = len(wordsearch_data) - 2


def test_for_mas(test_cell):
    # Test for A in center
    if test_cell[1][1] != "A":
        return False

    # Test that the corners are M or X
    mas_set_1 = sorted([test_cell[0][0], test_cell[2][2]])
    mas_set_2 = sorted([test_cell[0][2], test_cell[2][0]])
    if mas_set_1 != ["M", "S"]:
        return False
    if mas_set_2 != ["M", "S"]:
        return False

    return True


xmascount = 0
for i in range(0, number_horizontal_steps):
    for j in range(0, number_vertical_steps):
        selected_rows = wordsearch_data[j:j + 3]
        selected_cells = [col[i:i + 3] for col in selected_rows]
        result = test_for_mas(selected_cells)
        for k in selected_cells:
            print(k)
        if result:
            xmascount += 1
        print(f"STEP DOWN {j + 1}")
    print(f"STEP RIGHT {i + 1}")

print(xmascount)

# 1892 too high
# 1800 too high
