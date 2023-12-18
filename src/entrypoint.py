import sys
import importlib


def run():
    # print(sys.argv)
    if len(sys.argv) == 3:
        year = sys.argv[1]
        day = sys.argv[2]
    else:
        year = input("Which year to run?")
        day = input("Which day to run?")
    main = importlib.import_module(f"src.year_{year}.day_{day}.main")
    main.run()