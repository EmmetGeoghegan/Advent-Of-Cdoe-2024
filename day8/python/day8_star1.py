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
    return "".join(["".join(i) for i in grid]).count("#")
def calc_all_pairs(antenna_family):
    if len(antenna_family) <= 1:
        return []

    pairs = [(antenna_family[0], i) for i in antenna_family[1:]]

    return pairs + calc_all_pairs(antenna_family[1:])


def get_coord_of_antinode(antenna_pair):
    delta_x = antenna_pair[0][0] - antenna_pair[1][0]
    delta_y = antenna_pair[0][1] - antenna_pair[1][1]

    first_antinode_pos = (antenna_pair[0][0] + delta_x, antenna_pair[0][1] + delta_y)
    # first_antinode_pos = (0,0)
    second_antinode_pos = (antenna_pair[1][0] - delta_x, antenna_pair[1][1] - delta_y)
    # second_antinode_pos = (0, 0)

    return [first_antinode_pos, second_antinode_pos]


# loop through each antenna family and get the distance between each pair of antennas
for i in antenna_familes.keys():
    if len(antenna_familes[i]) > 1:
        print(f"Calculating antenna family - {i}")
        all_antenna_combos = calc_all_pairs(antenna_familes[i])
        for antenna_pair in all_antenna_combos:
            antinode_coords = get_coord_of_antinode(antenna_pair)
            print(antinode_coords)

            for antinode_coord in antinode_coords:
                antenna_layout[antinode_coord[1]][antinode_coord[0]] = "#"
                print("-----------------------")
                grid_printer(antenna_layout)
                print("-----------------------")

print(f"Answer: {count_antinodes(antenna_layout)}")