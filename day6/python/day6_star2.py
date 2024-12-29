from tqdm import tqdm

with open("pathing.txt", "r") as maze_file:
    maze_data = maze_file.readlines()

maze_data = [list(i.strip()) for i in maze_data]

for row_loc in range(len(maze_data)):
    if "^" in maze_data[row_loc]:
        col_loc = maze_data[row_loc].index("^")
        break

print(f"x: {col_loc}, y: {row_loc}")


def maze_printer(maze):
    print("\n".join(["".join(i) for i in maze]))


def eval_maze(maze, row_loc, col_loc):
    rotation_tracker = ["U", "R", "D", "L"]
    direction_mode = "U"
    location_tracker = {}

    # maze_printer(maze)

    while True:

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
        if new_col_loc < 0 or new_row_loc < 0 or new_col_loc == len(maze[0]) or new_row_loc == len(maze):
            print("maze escaped")
            return False

        new_location = maze[new_row_loc][new_col_loc]

        if new_location == "#":
            direction_mode = rotation_tracker[(rotation_tracker.index(direction_mode) + 1) % 4]
        else:
            col_loc = new_col_loc
            row_loc = new_row_loc

            loc_key = (col_loc, row_loc)
            if loc_key in location_tracker.keys():
                if location_tracker[loc_key] == direction_mode:
                    print("We are in a loop")
                    return True

            location_tracker[loc_key] = direction_mode
            # print(location_tracker)
        # print("new location")

valid_loops = 0
for xloc in tqdm(range(len(maze_data))):
    for yloc in tqdm(range(len(maze_data[0]))):
        if maze_data[xloc][yloc] == "x":
            print(f"X found - {xloc}, {yloc}")


            test_maze = [i.copy() for i in maze_data]
            test_maze[xloc][yloc] = "#"

            # Evaluate the maze
            location_eval = eval_maze(test_maze, row_loc, col_loc)
            if location_eval:
                valid_loops += 1

print(valid_loops)




