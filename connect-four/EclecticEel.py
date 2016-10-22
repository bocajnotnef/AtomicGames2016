#! /usr/bin/env python3
import sys
import argparse
import random

global DebugFile
DebugFile = None


def PrintBanner(location):
    """Prints the banner of our progam to the location"""
    banner = r"""
$$$$$$$$\          $$\                       $$\     $$\
$$  _____|         $$ |                      $$ |    \__|
$$ |      $$$$$$$\ $$ | $$$$$$\   $$$$$$$\ $$$$$$\   $$\  $$$$$$$\
$$$$$\   $$  _____|$$ |$$  __$$\ $$  _____|\_$$  _|  $$ |$$  _____|
$$  __|  $$ /      $$ |$$$$$$$$ |$$ /        $$ |    $$ |$$ /
$$ |     $$ |      $$ |$$   ____|$$ |        $$ |$$\ $$ |$$ |
$$$$$$$$\\$$$$$$$\ $$ |\$$$$$$$\ \$$$$$$$\   \$$$$  |$$ |\$$$$$$$\
\________|\_______|\__| \_______| \_______|   \____/ \__| \_______|
$$$$$$$$\          $$\
$$  _____|         $$ |
$$ |      $$$$$$\  $$ | $$$$$$$\
$$$$$\   $$  __$$\ $$ |$$  _____|
$$  __|  $$$$$$$$ |$$ |\$$$$$$\
$$ |     $$   ____|$$ | \____$$\
$$$$$$$$\\$$$$$$$\ $$ |$$$$$$$  |
\________|\_______|\__|\_______/
\n\n
            _____
     _..--'`     `'-.       BEHOLD! The EclecticEel!
   .'            _   '.     ASCII Art From
                (@)    \    http://www.chris.com/ascii/joan/www.geocities.com/SoHo/7373/aquatic.html
                _.---:-'    Program written by Riley Annis & Jake Fenton
               _\'._ \\     https://github.com/bocajnotnef/AtomicGames2016
    jgs_.--''`` `'-.`' |    for the Atomic Object Atomic Games 2016
     .'             `""`
    /
\n\n
"""
    print(banner, file=location)


def get_args():
    """Build parser and get parsed args from it
    returns parsed args"""
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", "--board", help="JSON string of board state")
    parser.add_argument("-t", "--timetokill", help="Allowed runtime length of program")
    parser.add_argument("-p", "--player", help="Which player we'll be")
    parser.add_argument("--debug", action="store_true",
                        help="Debug Mode")
    return parser.parse_args()


def PrettyPrint(board, location):
    """Print the board in a nice fasion"""
    print("Board state is:", file=location)
    for el in board:
        print("\t{}".format(el), file=location)


def log(string):
    """"Log a string to file, if debugging is enabled"""
    global DebugFile
    if DebugFile is not None:
        print(string, DebugFile)


def main():
    global DebugFile
    args = get_args()
    if args.debug:
        DebugFile = open("debug_eel.txt", "w")
    PrintBanner(sys.stderr)
    board = eval(args.board[1:-1])
    PrettyPrint(board, sys.stderr)
    sys.exit(play_random(board))


def play_random(board):
    return random.choice([x for x in range(len(board[0])) if not board[0][x]])


if __name__ == "__main__":
    main()
