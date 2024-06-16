import argparse

parser = argparse.ArgumentParser()
parser.add_argument('file')
parser.add_argument('--count', action='store_true')
parser.add_argument('--num', action='store_true')
parser.add_argument('--sort', action='store_true')
args = parser.parse_args()

lines = []
try:
    with open(args.file, 'r') as f:
        lines = f.readlines()
except FileNotFoundError:
    print('ERROR')

if args.sort:
    lines.sort()
if args.num:
    for i in range(len(lines)):
        lines[i] = str(i) + " " + lines[i]
if args.count:
    lines.append(f"rows count: {len(lines)}")

print(''.join(lines))