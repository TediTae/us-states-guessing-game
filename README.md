# U.S. States Guessing Game 🗺️

## Description
This is an interactive game built with Python's Turtle graphics and Pandas, where the goal is to correctly guess all 50 U.S. states.
Each correct guess displays the state name on a blank U.S. map.
The game continues until all states are guessed or the player exits.

## Features
- Graphical interface using Turtle
- Text input dialog for guesses
- Dynamically displays correct guesses on the map
- Saves missing states to a `.csv` file for learning
- Case-insensitive guessing with `.title()` formatting

## How It Works
1. A blank U.S. map is loaded using a `.gif` image.
2. User is prompted to guess a state name.
3. If the guess is correct, the state name is shown on the map.
4. The game ends when all 50 states are guessed or the user types `Exit`.
5. When exited early, the game saves a list of missing states to `states_to_learn.csv`.

## Requirements
- Python 3.x  
- `pandas` library  
- `turtle` (built-in with Python)  
- A `50_states.csv` file containing columns: `state`, `x`, `y`  
- A `blank_states_img.gif` image file

## Installation
1. Clone this repository
2. Make sure you have the following files in the project directory:
   - blank_states_img.gif
   - 50_states.csv
3. Run the Python script:
   - main.py

## Technologies Used
- Python 3
- Turtle Graphics
- Pandas
- CSV File Handling

## License
- This project is open source and available under the MIT License.

## Contact
- tolgayilmaz1377@gmail.com
