# Road Rage
This is a car game that I have been working on for about one year. It was under development for two years, but I didn't work on it for the majority of the time. This game was written in Python, using the module [Pygame Zero](https://pygame-zero.readthedocs.io).
## Getting started
1. To execute code, you will need to install [Python 3.7.8](https://www.python.org/downloads/release/python-378). It might also work on different versions depending on if they support _Pygame Zero 1.2_.
2. Then, navigate to the directory where the instalation of Python is located from the terminal and execute `pip install pgzero`. This will install the module that will has been used in the project.
3. Now you can download or rather fork the repository. Make sure you put it somewhere where you won't require external permissions to modify. If you're on Windows, that would mean running it as administrator everytime you want to run the game.
4. After that, you may use the Python that has been described to run the file `main.py`.
5. You do not have to do this step, but if you're going to run the game multiple times, you should create a shell/batch script to do it automatically. On Windows, the file extension for a batch script is `.bat` or `.cmd`, on Unix-based operating systems, any extension would work but the widely accepted file extension is `.sh`.
## How to play
While in-game, use A to move left or D to move right. You can alternatively use the arrow keys or the mouse too.

In the top-left corner, a number representing your fuel level will be displayed. You need to drive over the fuel bags to reset it. You'll lose if you let your fuel level run down to zero (I can imagine assumptions about the game being bugged because you randomly lose without crashing into a car although you really just lost on fuel level).

If you score better than you've ever before, the highscore will update. It is stored in hexadecimal under the file `highscore.hex`. Make sure you never delete or otherwise edit the file, as there is no security system preventing an error. It will definetly be introduced in the next update, as it's an easy fix.
## I had to break PEP-8
You may notice how all of the imports aren't on the top of the script, which is against PEP-8 according to rule E402. It actually goes back to a long time ago. I realised that instead of the window spawning in the middle of the screen, the top-left _corner_ spawns in the middle of the screen. I contacted my teacher about this, and he said that it can be fixed by putting a few lines of code at the top of the script. This meant, even above all other imports. I guess that Pygame has some way of calculating for where to put the corner of the window for it to be centered. If you attempt to follow PEP-8, and put all imports at the top, the window will summon oddly to the side again.
