from os import system
from random import choice, randint

from daedalus import Maze
from numpy import array
from PIL import Image

from maze.solve import MazeSolver
from util.inpututils import take_input


# Select the algorithm used to generate the maze
# Pretty sure a better looking way exists, but it just works
def maze_interface(maze: Maze):
    maze_dispatch = {
        "perfect": 0,
        "braid": 1,
        "braid tilt": 2,
        "spiral": 3,
        "diagonal": 4,
        "recursive": 5,
        "prim": 6,
        "tree": 7,
        "forest": 8,
        "aldous": 9,
        "wilson": 10,
        "eller": 11,
        "braid eller": 12,
        "division": 13,
        "binary": 14,
        "sidewinder": 15,
        "unicursal": 16
    }

    choice = take_input(str,
                        msg="Enter the type of maze you want: ",
                        scope=[key for key in maze_dispatch.keys()].append("random"))

    if choice == "random":
        choice = randint(0, 16)
    else:
        choice = maze_dispatch[choice]

    if choice == 0:
        if randint(0, 1) == 0:
            maze.create_perfect()
        else:
            maze.create_perfect2()
    elif choice == 1:
        maze.create_braid()
    elif choice == 2:
        maze.create_braid_tilt()
    elif choice == 3:
        maze.create_spiral()
    elif choice == 4:
        maze.create_diagonal()
    elif choice == 5:
        maze.create_recursive()
    elif choice == 6:
        if randint(0, 1) == 0:
            maze.create_prim()
        else:
            maze.create_prim2()
    elif choice == 7:
        maze.create_tree()
    elif choice == 8:
        maze.create_forest(0)
    elif choice == 9:
        maze.create_aldous_broder()
    elif choice == 10:
        maze.create_wilson()
    elif choice == 11:
        maze.create_eller()
    elif choice == 12:
        maze.create_braid_eller()
    elif choice == 13:
        maze.create_division()
    elif choice == 14:
        maze.create_binary()
    elif choice == 15:
        maze.create_sidewinder()
    elif choice == 16:
        maze.create_unicursal()


# The driver code
def main() -> None:
    while True:
        m_size = take_input(str,
                            msg="Enter the size of the maze (small/medium/large): ",
                            scope=["small", "medium", "large"])

        maze_size = tuple()

        if m_size == "small":
            maze_size = (choice(range(119, 337, 2)), choice(range(119, 175, 2)))
        elif m_size == "medium":
            maze_size = (choice(range(337, 503, 2)), choice(range(175, 263, 2)))
        else:
            maze_size = (choice(range(503, 753, 2)), choice(range(263, 393, 2)))

        maze = Maze(maze_size[0], maze_size[1])
        maze_interface(maze)

        maze.save_bitmap("test.bmp")

        # Flip walls to black
        a = array(Image.open("test.bmp"))
        img = Image.fromarray(~a)

        # Convert the image to RGB
        img = img.convert('RGB')

        # Make the maze less hurtful to look at
        # You haven't known pain until you have seen a B/W Spiral
        img_data = img.load()
        for i in range(0, maze_size[0]):
            for j in range(0, maze_size[1]):
                if img_data[i, j] == (0, 0, 0):
                    img_data[i, j] = (68, 1, 36)
                else:
                    img_data[i, j] = (26, 230, 164)

        solver = MazeSolver(img, list(maze)[:])
        solver.render(maze_size, rate=10000)

        check = take_input(str, "Would you like to render another maze? (y/n): ", scope=["y", "n"])

        if check == "n":
            break

        system("cls")


if __name__ == "__main__":
    main()
