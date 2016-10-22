#! /usr/bin/env python3
import sys
import argparse

global DebugFile
DebugFile = None


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", "--board", help="JSON string of board state")
    parser.add_argument("--debug", action="store_true",
                        help="Debug Mode")
    return parser.parse_args()


def PrettyPrint(board, location):
    print("Board state is:", file=location)
    for el in board:
        print("\t{}".format(el), file=location)


def log(string):
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

if __name__ == "__main__":
    main()
