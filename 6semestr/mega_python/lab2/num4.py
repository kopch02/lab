import argparse
import sys

parser = argparse.ArgumentParser()

parser.add_argument("--upper",action="store_true")
parser.add_argument("--lines", type=int, required = False)
parser.add_argument("file_out",type=argparse.FileType('r'))
parser.add_argument("file_in",type=argparse.FileType('w'))

args = parser.parse_args()
if args.lines:
    text = args.file_out.readlines()
    try:
        text = text[:args.lines]
    except:
        text = text
if args.upper:
    text = list(map(lambda x: x.upper(),text))

t = ""

for i in text:
    t += i

args.file_in.write(t)