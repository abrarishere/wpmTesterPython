# Typing Test Game

This is a simple typing test game implemented using Python's `curses` library. The goal of the game is to type a given text as quickly and accurately as possible, and the game calculates your words per minute (WPM) as you type.

## Features

- Displays a random line of text for the user to type.
- Calculates and displays the user's WPM in real-time.
- Provides visual feedback for correct and incorrect characters typed.
- Allows the user to restart the test or exit the game upon completion.

## Requirements

- Python 3.x
- `curses` module (usually included with Python standard library)

## Installation

1. Clone this repository:
   ```sh
   git clone https://github.com/abrarishere/wpmTesterPython.git
   cd wpmTesterPython
   ```

2. Ensure you have a `text.txt` file in the same directory. This file should contain lines of text that the game will randomly select for the typing test.

## Usage

Run the game using the following command:

```sh
python main.py 
```

## How to Play

1. **Start Screen**: When you run the game, you'll see a welcome screen. Press any key to start the game.
2. **Typing Test**:
    - A line of text will be displayed at the top of the screen.
    - Your current WPM will be shown below the text.
    - As you type, correct characters will be displayed in green and incorrect characters in red.
3. **Completion**:
    - Once you complete the text, a message will appear indicating that you've finished.
    - Press any key to restart the test or `ESC` to quit the game.

## Code Overview

### Functions

- `start_screen(stdscr)`: Displays the welcome screen.
- `display_text(stdscr, target, user, wpm)`: Displays the target text, user's current input, and WPM.
- `load_text()`: Loads a random line of text from `text.txt`.
- `wpm_test(stdscr)`: Main logic for the typing test, including handling user input and calculating WPM.
- `main(stdscr)`: Initializes color pairs, starts the welcome screen, and handles restarting or exiting the game.

### Key Bindings

- Any key: Start the game from the welcome screen.
- `ESC`: Exit the game during the test or after completing the test.
- `Backspace`: Delete the last character typed.

## Example `text.txt` File

Here is an example of what your `text.txt` file might look like:

```
The quick brown fox jumps over the lazy dog.
A journey of a thousand miles begins with a single step.
To be or not to be, that is the question.
All that glitters is not gold.
```

Ensure each line of text is on a new line in the file.

## Contributing

Feel free to open issues or submit pull requests if you have suggestions or improvements!

---

Enjoy improving your typing skills with this fun and interactive typing test game!
