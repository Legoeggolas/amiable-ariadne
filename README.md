# amiable-ariadne

A simple Python program that generates and solves 2D mazes created by the Daedalus Maze Generator.

Inspired by Computerphile's Maze Solving video, available [here](https://www.youtube.com/watch?v=rop0W4QDOUI)

Unlike their project, mine generates the mazes at runtime and displays both the pathfinder exploring the maze
as well as the path being drawn from the end to the start.

# Technologies

This project was created with the help of:

- Python 3.8.7

with the following packages:

- Numpy 1.21.2
- PyDaedalus 0.1.5
- PyGame 2.0.1
- Pillow 8.3.2

Formatting was imposed using yapf with the following configuration:

```
[style]
based_on_style = google
spaces_before_comment = 2
indent_width: 4
split_before_logical_operator = true
column_limit = 100
```

# Setup

Simply install all the dependencies listed above, clone this git to your local computer, and run:

```
python main.py
```

# Usage

```
Enter the size of the maze (small/medium/large): medium
Enter the type of maze you want: braid eller
Enter the algorithm you wish to use: tourist
```

The first thing the script requires you to enter is the required size of the maze.
This can be either of the three strings

- small : Ranges from 199x199 to 335x173
- medium : Ranges from 337x175 to 501x261
- large : Ranges from 503x263 to 751x395

The next choice corresponds to the algorithm used to generate the maze.
PyDaedalus provides about 19 such algorithms, and 18 of them can be used.
Any of these can be used by entering their specific keys.
These, with their corresponding descriptions from PyDaedalus documentation, are:

- perfect : Creates a Perfect maze, aka a maze with only one entrance and exit, using the Hunt and Kill algorithm.
- braid : Creates a Braid maze, aka a maze without any dead ends, by adding walls
- braid tilt : Creates a Braid maze, seeded by a Tilt Maze template
- spiral : Forms a maze composed of interlocking spirals. Hazardous to the eye
- diagonal : A maze created with a diagonal bias, where many of the walls look like stairs
- recursive : Creates a Perfect Maze using a Recursive Backtracking Algorithm. Only carves passages
- prim : Creates a Perfect maze using a modified version of Prim's Algorithm.
- tree : Creates a Perfect maze using the Growing Tree Algorithm.
- forest : Creates a Perfect maze using a Growing Forest Algorithm.
- aldous : Creates a Perfect maze using the Aldous-Broder Algorithm. Is unbiased
- wilson : Creates a Perfect maze in the bitmap using Wilson's Algorithm. Is unbiased, and 5x faster than Aldous
- eller : Creates a Perfect maze using Eller's Algorithm. Fastest of them all
- braid eller : Creates a Braid maze using Eller's Algorithm
- division : Creates a Perfect maze using Recursive Division. Only adds walls
- binary : Creates a Perfect maze using the Binary Tree Algorithm
- sidewinder : Creates a Perfect maze using the Sidewinder Algorithm
- unicursal : Creates a Unicursal maze, aka a maze without any junctions

Lastly, one needs to enter the algorithm to be used to find a path through the maze.
The ones currently present are:

- bfs: Standard Breadth First Search
- dfs: Standard Depth First Search
- tourist: A pathfinder that randomly decides the next node to search from the neighbours of the current node
  and backtracks if all viable nodes have been exhausted

When all three of these have been specified, the maze is solved in real time, the progress visible in a PyGame window.

# Additional Notes

Installing PyDaedalus on newer systems can be quite a pain, since the project is old and hasn't been updated in ages.
Even I had a lot of troubles building it, which required some tinkering with Visual Studio Build Tools and the setup.py
which unfortunately I did not have the foresight to document.

I have only tested this on a Windows system as of now, and if you have a Mac or a Linux installation, it might simply
work without a hitch.

If such is the case, do let me know the specifications under which you managed to install PyDaedalus.
