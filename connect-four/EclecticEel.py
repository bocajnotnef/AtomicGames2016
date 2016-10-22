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


def SearchHorizontal()


def SearchAndScore(board, row, el):
    """
    Search in all cardinal directions for pieces, for both players, and determine how badly they
    want to be at (row, col)
    """

    # bound which row we can be in
    row_max = min([row + 3, len(board) - 1])
    row_min = max([row - 3, 0])
    # bound which column we can be in
    col_max = min([col + 3, len(board[0]) - 1])
    col_min = min([col - 3, 0])

    # do each search
    horiz_p1 = SearchHorizontal(board, row, col, col_min, col_max, 1)
    horiz_p2 = SearchHorizontal(board, row, col, col_min, col_max, 2)

    vert_p1 = SearchVertical(board, row, col, row_min, row_max, 1)
    vert_p2 = SearchVertical(board, row, col, row_min, row_max, 2)

    diag_p1 = SearchDiag(board, row, col, row_min, row_max, col_min, col_max, 1)
    diag_p2 = SearchDiag(board, row, col, row_min, row_max, col_min, col_max, 1)


def ScoreEmptyPositions(board):
    """
    Score the empty positions of the board according to who wants to be there the most
    """
    scored_board = [[None] * len(board[0])] * len(board)
    for row in range(len(board)):
        for el in range(len(board[0])):
            if board[row][col] == 0:
                scored_board[row][el] = SearchAndScore(board, row, el)


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
    """Plays a random empty location on the board"""
    return random.choice([x for x in range(len(board[0])) if not board[0][x]])


if __name__ == "__main__":
    main()
