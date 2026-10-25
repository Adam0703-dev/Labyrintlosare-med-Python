# Labyrintlösare med Python

## Overview

This project documents the development of a Python maze solver with a graphical display built using Tkinter. A white square moves through a maze, following a left-hand wall-following rule until it reaches the goal.

The project is divided into versions to document its development, from the first implementation with a fixed maze to a planned version with separate algorithm and maze generation modules.

## Versions

### Version 1 – Original Implementation

The first version contains two Python source files: `main.py` and `grafik.py`.

- Focus: Movement logic and graphical visualisation of a predefined maze.
- Display: A 6 × 6 maze with green walls, black passages, and a white moving square.
- Movement: One step per second, with turns prioritised left, forward, right, then backward.
- [View Version 1](./docs/version-1/)

### Version 2 – Planned

A future version is intended to include all four modules: `main.py`, `grafik.py`, `algoritm.py`, and `random_labyrint_generator.py`.

Version 2 has not been added to this repository yet.

## Project Structure

| Directory | Contents |
| --- | --- |
| [Version 1](./docs/version-1/) | Version notes and instructions for the original implementation. |
| [Version 1 Software](./docs/version-1/software/) | Original `main.py` and `grafik.py` source files. |

## Getting Started

1. Install Python 3 with Tkinter support. No third-party Python packages are required.
2. Clone or download this repository.
3. From the repository root, run:

   ```sh
   python docs/version-1/software/main.py
   ```

   On Windows, `py` can be used instead of `python`.

The animation starts automatically. The square starts at row 0, column 1 and stops at row 5, column 4. Coordinates are zero-based. Close the window to exit.

## Future Development

Planned work includes separating the movement algorithm into its own module, adding random maze generation, and improving boundary handling for different maze layouts. Version 1 preserves the original source files and is designed around the supplied maze.

## Author

Developed by Adam Odeh as a Python programming project, with the goal of exploring maze-solving algorithms, graphical visualisation, and modular program design.
