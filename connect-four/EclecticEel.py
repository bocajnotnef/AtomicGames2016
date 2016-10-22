#! /usr/bin/env python3
import sys
import argparse
import random

global DebugFile
DebugFile = None


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
    board = eval(args.board[1:-1])
    PrettyPrint(board, sys.stderr)


def play_random(board):
    random.choice([x for x in board[0] if x])
    

if __name__ == "__main__":
    main()
