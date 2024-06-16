import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('pairs', nargs='+')
parser.add_argument('--sort', action='store_true')
args = parser.parse_args()
kvs = []
for pair in args.pairs:
    k, v = pair.split('=')
    kvs.append(f"Key: {k} Value: {v}")

if args.sort:
    kvs.sort()
print('\n'.join(kvs))