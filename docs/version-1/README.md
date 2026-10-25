# Version 1 – Original Implementation

## Overview

This is the first version of the maze solver. It combines a predefined maze and movement logic in `main.py` with a Tkinter display in `grafik.py`.

The two source files are preserved as supplied, without changes to their code.

## Software

| File | Purpose |
| --- | --- |
| [main.py](./software/main.py) | Defines the maze, start and goal, movement priorities, and timed updates. |
| [grafik.py](./software/grafik.py) | Draws the maze and updates the moving square's position. |

## Running

Use Python 3 with Tkinter support. From the repository root:

```sh
python docs/version-1/software/main.py
```

No external packages or hardware are required. The animation begins automatically and updates every 1,000 milliseconds.

## Behaviour

- The maze is represented by a 6 × 6 list: `1` is a wall and `0` is a passage.
- Each cell is 100 × 100 pixels, producing a 600 × 600 pixel canvas.
- Walls are green, passages are black, and the moving square is white.
- The start is `(0, 1)`, the goal is `(5, 4)`, and the initial direction is down.
- At each step, the solver prefers left, forward, right, and finally backward relative to its current direction.
- Updates stop when the goal is reached; the window remains open until closed.

## Limitations and Next Version

The movement logic and display are tailored to the supplied maze. Neighbour indexing does not fully check maze boundaries, and there is no general handling for unsolvable mazes or repeated states.

The planned Version 2 will include separate `algoritm.py` and `random_labyrint_generator.py` modules alongside `main.py` and `grafik.py`. These additional modules are not part of Version 1.

[Back to project overview](../../README.md)
