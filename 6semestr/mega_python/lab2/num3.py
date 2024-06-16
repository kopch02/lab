import argparse
import sys


parser = argparse.ArgumentParser()

parser.add_argument("any_args",nargs="*")

args = parser.parse_args()

if args.any_args:
    for i in args.any_args:
        print(i)
else:
    print("no args")