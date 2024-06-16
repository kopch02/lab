import sys

def main(args):
    res = dict()
    sort_flag = False
    while args:
        arg = args.pop(0)
        if "=" in arg:
            e = arg.split("=")
            res[e[0]] = e[1]
        elif arg == "--sort":
            sort_flag = True
    if sort_flag:
        res = sorted(res.items())
    else:
        res = list(res.items())
    return res

res = main(sys.argv[1:])
while res:
    elem = res.pop(0)
    print(f"Key: {elem[0]} Value: {elem[1]}")