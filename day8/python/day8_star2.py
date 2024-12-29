with open("input.txt", "r") as infile:
    file_data = infile.readlines()

antenna_layout = [list(i.strip()) for i in file_data]

print(antenna_layout)

# Get all antenna families and locations

antenna_familes = {}

for i in range(len(antenna_layout)):
    for j in range(len(antenna_layout[0])):
        cell = antenna_layout[i][j]

        if cell != ".":
            if cell not in antenna_familes.keys():
                antenna_familes[cell] = [(j, i)]
            else:
                antenna_familes[cell].append((j, i))


def grid_printer(grid):
    print("\n".join(["".join(i) for i in grid]))


def count_antinodes(grid):
    dot_count = "".join(["".join(i) for i in grid]).count(".")
    total_area = max_x * max_y
    return total_area - dot_count



def calc_all_pairs(antenna_family):
    if len(antenna_family) <= 1:
        return []

    pairs = [(antenna_family[0], i) for i in antenna_family[1:]]

    return pairs + calc_all_pairs(antenna_family[1:])


def get_coord_of_antinode(antenna_pair, max_x, max_y):
    delta_x = antenna_pair[0][0] - antenna_pair[1][0]
    delta_y = antenna_pair[0][1] - antenna_pair[1][1]

    all_antinodes = []
    counter = 1
    while True:
        valid_nodes = []
        first_flag = True

        second_flag = True

        first_antinode_pos = (antenna_pair[0][0] + (delta_x * counter), antenna_pair[0][1] + (delta_y * counter))
        # first_antinode_pos = (0,0)
        second_antinode_pos = (antenna_pair[1][0] - (delta_x * counter), antenna_pair[1][1] - (delta_y * counter))
        # second_antinode_pos = (0, 0)

        print("first" , first_antinode_pos)
        print("second", second_antinode_pos)

        if first_antinode_pos[0] < max_x and first_antinode_pos[0] >= 0:
            if first_antinode_pos[1] < max_x and first_antinode_pos[1] >= 0:
                valid_nodes.append(first_antinode_pos)
            else:
                first_flag = False
                print("first invalid")
        else:
            first_flag = False
            print("first invalid")

        if second_antinode_pos[0] < max_y and second_antinode_pos[0] >= 0:
            if second_antinode_pos[1] < max_y and second_antinode_pos[1] >= 0:
                valid_nodes.append(second_antinode_pos)
            else:
                second_flag = False
                print("second invalid")
        else:
            second_flag = False
            print("second invalid")

        if not first_flag and not second_flag:
            print("first and 2nd out of bounds")
            break
        else:
            all_antinodes += valid_nodes
        counter += 1


    return all_antinodes

max_x = len(antenna_layout[0])
max_y = len(antenna_layout)

# loop through each antenna family and get the distance between each pair of antennas
for i in antenna_familes.keys():
    if len(antenna_familes[i]) > 1:
        print(f"Calculating antenna family - {i}")
        all_antenna_combos = calc_all_pairs(antenna_familes[i])
        for antenna_pair in all_antenna_combos:
            antinode_coords = get_coord_of_antinode(antenna_pair, max_x, max_y)
            print(antinode_coords)

            for antinode_coord in antinode_coords:
                antinode_col = antinode_coord[0]
                antinode_row = antinode_coord[1]
                if antinode_col < len(antenna_layout[0]) and antinode_col >= 0:
                    if antinode_row < len(antenna_layout) and antinode_row >= 0:
                        antenna_layout[antinode_coord[1]][antinode_coord[0]] = "#"
                        print("-----------------------")
                        grid_printer(antenna_layout)
                        print("-----------------------")

print(f"Answer: {count_antinodes(antenna_layout)}")
