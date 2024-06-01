import curses
import random
import time
from curses import KEY_BACKSPACE, color_pair, wrapper


def start_screen(stdscr):
    stdscr.clear()
    stdscr.refresh()
    stdscr.addstr(0, 0, "Welcome to the Typing Test")
    stdscr.addstr(1, 0, "Press any key to start")
    stdscr.getch()


def display_text(stdscr, target, user, wpm=0):
    stdscr.addstr(target)
    stdscr.addstr(1, 0, f'WPM: {wpm}')
    for i ,char in enumerate(user):
        correct_char = target[i]
        color = color_pair(2)
        if char != correct_char:
            color = color_pair(1)
        stdscr.addstr(0, i , char, color)

def load_text():
    with open('text.txt', 'r') as f:
        lines = f.readlines()
        return random.choice(lines).strip()


def wpm_test(stdscr):
    target_content = load_text() 
    user_text = []
    time_started = time.time()
    stdscr.nodelay(True)

    while True:
        time_elapsed = max(time.time() - time_started, 1)
        wpm = round(( len(user_text) / ( time_elapsed / 60 )) / 5 )
        stdscr.clear()
        display_text(stdscr, target_content, user_text,wpm)
        stdscr.refresh

        if ''.join(user_text) == target_content:
            stdscr.nodelay(False)
            break

        try:
            key = stdscr.getkey()
        except:
            continue

        if ord(key) == 27:
            break
        if key in ('KEY_BACKSPACE', '\b', '\x7F'):
            if len(user_text) > 0:
                user_text.pop()
        elif len(user_text) < len(target_content):
            user_text.append(key)



def main(stdscr):
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screen(stdscr)
    while True:
        wpm_test(stdscr)
        stdscr.addstr(2, 0, 'You have completed the text! Press any key to restart it (ESC to quit).')
        key = stdscr.getkey()

        if ord(key) == 27:
            break

wrapper(main)
