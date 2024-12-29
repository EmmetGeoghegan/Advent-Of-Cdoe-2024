

with open("input.txt", "r") as maze_file:
    maze_data = maze_file.readlines()

maze_data = [list(i.strip()) for i in maze_data]
for row_loc in range(len(maze_data)):
    if "^" in maze_data[row_loc]:
        col_loc = maze_data[row_loc].index("^")
        break
print(f"x: {col_loc}, y: {row_loc}")
direction_mode = "U"
rotation_tracker = ["U", "R", "D", "L"]

while True:
    # print("--------------")
    # print("\n".join(["".join(i) for i in maze_data]))
    # print("--------------")
    if direction_mode == "U":
        new_row_loc = row_loc - 1
        new_col_loc = col_loc
    elif direction_mode == "D":
        new_row_loc = row_loc + 1
        new_col_loc = col_loc
    elif direction_mode == "L":
        new_col_loc = col_loc - 1
        new_row_loc = row_loc
    elif direction_mode == "R":
        new_col_loc = col_loc + 1
        new_row_loc = row_loc

    # Test if out of bounds
    if new_col_loc < 0 or new_row_loc < 0 or new_col_loc == len(maze_data[0]) or new_row_loc == len(maze_data):
        print("DONE!")
        maze_data[row_loc][col_loc] = "x"
        final_maze = "\n".join(["".join(i) for i in maze_data])
        print(final_maze)
        print(final_maze.count("X"))

        with open("pathing.txt", "w+") as pathingfile:
            pathingfile.writelines(final_maze)
        break

    new_location = maze_data[new_row_loc][new_col_loc]

    if new_location == "#":
        direction_mode = rotation_tracker[(rotation_tracker.index(direction_mode) + 1) % 4]
    else:
        if maze_data[row_loc][col_loc] == ".":
            maze_data[row_loc][col_loc] = "x"
        col_loc = new_col_loc
        row_loc = new_row_loc


print("Done!")

